import asyncio, os, json, discord, queue
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ui import Button, View
import yt_dlp as youtube_dl

youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
}
ffmpeg_options = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=1):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.duration = data.get('duration')
        self.url = data.get('url')
        self.author = data.get('channel')
        self.views = data.get('view_count')
        self.like = data.get('like_count')
        self.comment = data.get('comment_count')

        if self.like is None:
            self.like = 'N/A'
        if self.comment is None:
            self.comment = 'N/A'

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(executable=f"{os.path.dirname(__file__)}/ffmpeg/bin/ffmpeg.exe", source=filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        self.song_queue = queue.Queue()

    def handle_song_finished(self, error, voice_client, interaction):
        if not self.song_queue.empty():
            next_song_info = self.song_queue.get()
            url = next_song_info['url']
            asyncio.run_coroutine_threadsafe(self.play_next_song(url, voice_client, interaction), self.client.loop)

    async def play_next_song(self, url, voice_chn, interaction):
        try:
            player = await YTDLSource.from_url(url, loop=self.client.loop, stream=True)

            song_info = {
                'url': url,
                'title': player.title,
                'author': player.author
            }
            self.song_queue.put(song_info)

            voice_chn.play(player, after=lambda e: self.handle_song_finished(e, voice_chn, interaction))
            await interaction.channel.send(
                f"Now playing: {player.title} by {player.author}.\nLength: ~{round(player.duration / 60)} min. \n 👍 {player.like} 💬 {player.comment} 👁 {player.views}")
        except Exception as e:
            if str(e) == "Not connected to voice.":
                pass
            else:
                await interaction.channel.send(f"Error attempting to play. Please try again later.")
                print(f"Player sent an error traceback: {e}")

    @app_commands.command(name='youtube', description='[Music] | Plays a youtube video in the URL provided.')
    async def youtube(self, interaction: discord.Interaction, url: str):
        await interaction.response.defer()
        voices = interaction.client.voice_clients
        voice_chn = None
        for voice in voices:
            if voice.channel == interaction.user.voice.channel:
                voice_chn = voice
                break
        if interaction.user.voice is None:
            await interaction.followup.send("You aren't in voice channel...")
        elif voice_chn is not None:
            if voice_chn.is_playing():
                await interaction.followup.send('Added to the song queue.')
                self.song_queue.put(url)
            else:
                await self.play_next_song(url, voice_chn, interaction)
        else:
            vc = interaction.user.voice.channel
            voice_chn = await vc.connect()
            await self.play_next_song(url, voice_chn, interaction)
            await interaction.followup.send('New player session has started.')

    @app_commands.command(name='queue', description='[Music] | Shows the current queue of songs.')
    async def queue(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        voices = interaction.client.voice_clients
        voice_chn = next((voice for voice in voices if voice.channel == interaction.user.voice.channel), None)

        if not voice_chn:
            await interaction.followup.send("You aren't in a voice channel...")
            return

        current_queue = list(self.song_queue.queue)
        if not current_queue:
            await interaction.followup.send("The queue is currently empty.")
            return

        queue_list = "\n".join(
            f"{index + 1}. {song['title']} by {song['author']}" for index, song in enumerate(current_queue))
        await interaction.followup.send(f"Current queue:\n\n{queue_list}")

    @app_commands.command(name='volume', description='[Music] | Regulates the sound to a percent (default is 100%).')
    async def volume(self, interaction: discord.Interaction, percent: int):
        await interaction.response.defer(ephemeral=True)
        voices = interaction.client.voice_clients
        for voice in voices:
            if voice.channel == interaction.user.voice.channel:
                voice_chn = voice
                break
        if interaction.user.voice is None:
            await interaction.followup.send("You aren't in voice channel...")
        else:
            voice_chn.source.volume = percent / 100
            await interaction.followup.send(f"Player volume is now set to {percent}")

    @app_commands.command(name='disconnect', description='[Music] | Disconnect bot from the channel.')
    async def disconnect(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.guild.voice_client.disconnect()
        await interaction.followup.send("Disconnected from the voice channel.")

async def setup(client):
    await client.add_cog(Music(client))