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
    
    @app_commands.command(name='ping', description='**[Other]** | Check response speed')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(f"Hello!\nSent this message in {round(app_commands.latency, 1)}")


async def setup(client):
    await client.add_cog(Other(client))
    print("Loaded: other.py")