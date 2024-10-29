import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from commands.slashes import test, moikkaa
from commands.search_campus import search_campus
from commands.search_kide import search_kide
# - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    - INTENTS AND VARIABLES -
""" 
# Load variables from .env since we want these to be secret
load_dotenv()
TOKEN = os.getenv('TOKEN')
SERVERID = int(os.getenv('SERVERID'))
JID = int(os.getenv('JID'))

# Intents for the bot so it can, for example, see the messages
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="/", intents=intents)
        
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to {SERVERID}")


"""
    - SYNC FUNCTION -
""" 
@bot.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot.user:
        return

    # Only one user can use sync command
    if message.content == "sync":
        if message.author.id == JID:
            await bot.tree.sync()
            print("Sync Used!")
            await message.reply("◕‿↼ Synkissä!")
        else:
            await message.reply("Tottelen vaan tyttöjä 🙄")
            print("Sync Tried!")
    else:
        return

"""
    - SEARCH FUNCTION -
"""
@bot.tree.command(name='hae', description='Hae kursseja ja tapahtumia')
@app_commands.choices(
    choice=[
        app_commands.Choice(name="Campus", value="campus"),
        app_commands.Choice(name="Kide", value="kide"),
    ]
)
async def hae(interaction: discord.Interaction, choice: app_commands.Choice[str]):
    # Let the bot think
    await interaction.response.defer()

    if choice.value == "campus":
        await search_campus(interaction)
    elif choice.value == "kide":
        await search_kide(interaction)

"""
    - OTHER SLASH COMMANDS -
    (Mostly for test purposes)
"""
def answer_command(name: str, description: str, func):
    @bot.tree.command(name=name, description=description)
    async def command(interaction: discord.Interaction):
        # Call the function based on the given command
        await func(interaction)
    return command

# Register the commands
answer_command("moikka", "Moikkaa bottia", moikkaa)
answer_command("test", "Test the bot", test)

bot.run(TOKEN)