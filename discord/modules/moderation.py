import os
import json
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ui import Button, View


class Moderation(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @app_commands.command(name='mute',
                          description="[Moderation] | Mutes the person on the server, temporarily or forever.")
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
            await member.send(f'You were muted on "{interaction.guild.name}" for {time[1] + time[2]} for reason: {reason}.')
            await asyncio.sleep(tm)
            await member.remove_roles(MutedRole)
        else:
            await member.add_roles(MutedRole, reason=reason)
            await member.send(f'You were muted on "{interaction.guild.name}" for eternity for reason: {reason}.')


async def setup(client):
    await client.add_cog(Moderation(client))
