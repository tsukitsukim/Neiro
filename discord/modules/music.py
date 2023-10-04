import os
import json
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ui import Button, View


class Music(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @app_commands.command(name='youtube', description='[Music] | Does nothing yet.')
    async def youtube(self):
        pass


async def setup(client):
    await client.add_cog(Music(client))