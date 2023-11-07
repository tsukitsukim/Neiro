import os, json, discord, re, asyncio
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ui import Button, View


class Moderation(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @app_commands.command(name='mute', description="[Moderation] | Mutes the person on the server, temporarily or forever.")
    async def mute(self, interaction: discord.Interaction, member: discord.Member, time: str = None, reason: str = None):
        await interaction.response.defer(ephemeral=True)

        MutedRole = discord.utils.get(interaction.guild.roles, name="NeiroMuted")
        if not MutedRole:
            MutedRole = await interaction.guild.create_role(name="NeiroMuted", color=discord.Color.dark_gray())
            for channel in interaction.guild.channels:
                await channel.set_permissions(MutedRole, speak=False, send_messages=False)

        if time is not None:
            time = re.split('(\d+)', time)
            tm = 0
            if time[2] == "s".lower():
                tm = int(time[1])
            if time[2] == "m".lower():
                tm = int(time[1]) * 60
            if time[2] == "h".lower():
                tm = int(time[1]) * (60 ** 2)
            if time[2] == "d".lower():
                tm = int(time[1]) * (60 ** 3)

            await member.add_roles(MutedRole, reason=reason)
            await interaction.followup.send(f"You have muted {member} for {time[1] + time[2]} for reason: {reason}.")
            await member.send(f'You were muted on "{interaction.guild.name}" for {time[1] + time[2]} for reason: {reason}.')
            await asyncio.sleep(tm)
            await member.remove_roles(MutedRole)
        else:
            await member.add_roles(MutedRole, reason=reason)
            await interaction.followup.send(f"You have muted {member} for eternity for reason: {reason}.")
            await member.send(f'You were muted on "{interaction.guild.name}" for eternity for reason: {reason}.')

    @app_commands.command(name='unmute', description="[Moderation] | Unmutes the person on the server.")
    async def unmute(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.defer(ephemeral=True)
        MutedRole = discord.utils.get(interaction.guild.roles, name="NeiroMuted")
        await member.remove_roles(MutedRole)
        await interaction.followup.send(f'You have unmuted {member}.')

    @app_commands.command(name='ban', description="[Moderation] | Blocks the person from the server.")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, time: str = None, reason: str = None):
        await interaction.response.defer(ephemeral=True)

        if time is not None:
            timeban = re.split('(\d+)', time)
            tb = 0
            if timeban[2] == "s".lower():
                tb = int(timeban[1])
            if timeban[2] == "m".lower():
                tb = int(timeban[1]) * 60
            if timeban[2] == "h".lower():
                tb = int(timeban[1]) * (60 ** 2)
            if timeban[2] == "d".lower():
                tb = int(timeban[1]) * (60 ** 3)

            await member.ban(reason=reason)
            await interaction.followup.send(f"You have banned {member} for {time[1] + time[2]} for reason: {reason}.")
            await member.send(f'You were banned from "{interaction.guild.name}" for {time[1] + time[2]} for reason: {reason}.')
            await asyncio.sleep(tb)
            await member.unban(reason=reason)
        else:
            await member.ban(reason=reason)
            await interaction.followup.send(f"You have banned {member} for eternity for reason: {reason}.")
            try:
                await member.send(f'You were banned from "{interaction.guild.name}" for eternity for reason: {reason}.')
            except:
                pass
    @app_commands.command(name='unban', description="[Moderation] | Unblocks the person on the server.")
    async def unban(self, interaction: discord.Interaction, member: discord.User):
        await interaction.response.defer(ephemeral=True)

        BanList = await interaction.guild.fetch_ban(member)
        while BanList:
            if member not in BanList:
                await interaction.followup.send(f"User {member} was not found")
            else:
                await interaction.guild.unban(member)
                await interaction.followup.send(f'You have unbanned {member}.')
                invitation = await interaction.guild.text_channels[0].create_invite()
                try:
                    await member.send(f'You were unbanned on the server "{invitation.guild.name}"! You can log in any moment now: {invitation}')
                except:
                    pass

    @app_commands.command(name='kick', description='[Moderation] | Kicks the person from the server.')
    async def kick(self, interaction: discord.Interaction, member: discord.User, reason: str = None):
        await interaction.response.defer(ephemeral=True)
        invitation = await interaction.guild.text_channels[0].create_invite()
        await member.send(f'You had been kicked from "{interaction.guild.name}" for reason {reason}. But you can always return here: {invitation}')
        await interaction.guild.kick(member, reason=reason)
        await interaction.followup.send(f"{member} has been kicked from the server for reason {reason}.")
async def setup(client):
    await client.add_cog(Moderation(client))
