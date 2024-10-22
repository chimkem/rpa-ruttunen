import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
# from commands.kide import kideresult
from commands.slashes import test, moikkaa

# Load env variables from .env since we want them to be secret
load_dotenv()
TOKEN = os.getenv('TOKEN')
SERVERID = int(os.getenv('SERVERID'))

# Intents for the bot so it can, for example, see the messages
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync the command tree
    print(f"{bot.user.name} has connected to {SERVERID}")

@bot.event
# React to a specific message
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot.user:
        return

    # If user sends the message to the server, the bot will answer
    if message.content == "botbot":
        await message.reply("🐔Häpi Winks🍗")

def register_command(name: str, description: str, func):
    @bot.tree.command(name=name, description=description)
    async def command(interaction: discord.Interaction):
        # Call the provided function
        await func(interaction)
    return command

# V -- SLASH COMMAND LIST -- V

# Register the commands
register_command("moikka", "Moikkaa bottia", moikkaa)
register_command("test", "Test the bot", test)

bot.run(TOKEN)