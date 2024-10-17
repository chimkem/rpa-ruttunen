import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load env variables from .env since we want them to be secret
load_dotenv()
TOKEN = os.getenv('TOKEN')
SERVERID = int(os.getenv('SERVERID'))

# Intents for the bot so it can, for example, see the messages
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
# Start the bot, print output
async def on_ready():
    # Convert SERVERID to int
    guild = discord.Object(id=int(SERVERID))
    # Sync commands to our server to see updates faster
    await bot.tree.sync(guild=guild)
    # Print output
    print(f'Started {bot.user}, under the name {bot.user.name}')

@bot.event
# React to a specific message
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot.user:
        return

    # If user sends the message to the server, the bot will answer
    if message.content == "botbot":
        await message.reply("🐔Häpi Winks🍗")

# Slash command to test the bot
@bot.tree.command(name="ping", description="test the bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Jep, toimii!")

bot.run(TOKEN)