import os
import json
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ui import Button, View


class Other(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @app_commands.command(name='ping', description='[Other] | Check response speed')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(f"Hello!\nSent this message in {round(self.client.latency, 1)}s")

    @app_commands.command(name='clear', description='[Other] | Purge messages in the chat for a certain amount.')
    async def clear(self, interaction: discord.Interaction, amount: int, before: str = None, after: str = None,
                   around: str = None, oldest: bool = None, reason: str = None):
        await interaction.response.defer(ephemeral=True)
        await interaction.channel.purge(limit=amount, before=before, after=after, around=around,
                                        oldest_first=oldest, reason=reason)
        await interaction.followup.send(f'Deleted {amount} messages from this channel!')

    @app_commands.command(name='uwu', description='[Other] | Why are you like this?')
    async def uwu(self, interaction: discord.Interaction):
        await interaction.channel.send('UwU')


async def setup(client):
    await client.add_cog(Other(client))
