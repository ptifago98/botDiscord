import discord
import time
import os
import logging
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
from keep_alive import keep_alive

# Start keep-alive server
keep_alive()


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.command(help="Affiche le temps restant avant le début de la saison 1 de WoW Midnight.")
async def midnight(ctx):
    season_start = datetime(2026, 3, 18, 7, 0, 0)
    now = datetime.now()
    remaining = season_start - now
    if remaining.total_seconds() <= 0:
        await ctx.send(f"La saison 1 à commencée {ctx.author.mention}!")

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    await ctx.send(f"Tu es bien impatient! Voilà le temps qu'il te reste à attendre : {days} jours {hours} heures et {minutes} minutes {ctx.author.mention}")

@bot.command(help="Te salue poliment")
async def salut(ctx):
    await ctx.send(f"Tu m’as pris pour ton pote ? Je ne donne que le timer, moi ! Fais-toi de vrais amis. {ctx.author.mention}")
    
@bot.command(help="Affiche la liste des commandes disponibles")
async def commands(ctx):
    embed = discord.Embed(
        title="Bot Commands",
        description="List of available commands",
        color=discord.Color.blue()
    )

    for command in bot.commands:
        embed.add_field(name=f"!{command.name}", value=command.help or "No description", inline=False)

    await ctx.send(embed=embed)

bot.run(token)

