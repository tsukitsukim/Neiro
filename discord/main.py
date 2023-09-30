import os
import json
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ui import Button, View

client = commands.Bot(command_prefix='n.', help_command=None, intents=discord.Intents.all())


@client.event
async def on_ready():
    for module in os.listdir('discord/modules'):
        if module.endswith('.py') and not module == 'main.py':
            await client.load_extension(f'modules.{module[:-3]}')
            print(f'"{module}" loaded up.')
    
    await client.tree.sync()
    print("Neiro is up and running.")

if __name__ == '__main__':
    client.run('MTAxODIwNDI3Njg1NTY3NzA2MQ.GNHDVQ.Ms1wsVbFvdKpjS2CVOBFvj_IeE04WqgmmJvyp4')