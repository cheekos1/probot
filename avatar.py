import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import webserver

# Load environment variables from a .env file
load_dotenv()

# Get token from environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup with "p" as the prefix
bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")

@bot.command(name="p", help="Send avatar of self or mentioned user.")
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author

    avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
    embed = discord.Embed(title=f"{user.display_name}'s Avatar", color=discord.Color.blue())
    embed.set_image(url=avatar_url)
    await ctx.send(embed=embed)

# Run your bot
webserver.keepalive
bot.run(TOKEN)


