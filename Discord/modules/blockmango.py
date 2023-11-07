import os
import json
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ui import Button, View


class BlockmanGO(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @app_commands.command(name='bghelp', description='[BlockmanGO] | List of commands for an experimental module.')
    async def bghelp(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)


async def setup(client):
    await client.add_cog(BlockmanGO(client))