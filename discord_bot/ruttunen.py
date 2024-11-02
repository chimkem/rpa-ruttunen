import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from commands.slashes import test, moikkaa
from commands.embed_campus import log_campus, embed_campus
from commands.embed_kide import log_kide, embed_kide
from automation.kide import seach_from_kide_app#, embed_kide
from automation.campus import search_from_campusonline
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

# Color options
orange = discord.Color.orange()
yellow = discord.Color.yellow()
green = discord.Color.green()
blue = discord.Color.blue()
        
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
        #if message.author.id == JID:
        await bot.tree.sync()
        print("Sync Used!")
        await message.reply("◕‿↼ Synkissä!")
        """else:
            await message.reply("Tottelen vaan tyttöjä 🙄")
            print("Sync Tried!")"""
    else:
        return

"""
    - KIDE SEARCH FUNCTION -
"""
@bot.tree.command(name='haku_kide', description='Hae tapahtumia')
@app_commands.describe(
    haku='Hae kaikkia Suomen opiskelijatapahtumia nimellä // Esim. Approt',
    )

async def haku_kide(
    interaction: discord.Interaction, 
    haku: str,
):
    # Let the bot think
    await interaction.response.defer()

    if haku: 
        # VV uncomment when automation returns the values VV
        kide_automation_results = seach_from_kide_app(haku)
        await embed_kide(interaction, kide_automation_results, haku)
        #print(kide_automation_results)
        #await embed_kide(interaction, kide_automation_results)
        await log_kide(interaction, haku)
    else:
        await interaction.followup.send("Ilmoita tapahtuman tyyppi, kiitos. // Esim. Approt")

"""
    - CAMPUSONLINE SEARCH FUNCTION -
"""
@bot.tree.command(name='haku_campus', description='Hae kursseja')
@app_commands.describe(
    lukukausi='Valitse lukukausi',
    kieli='Valitse opintojakson kieli',
    taso='Valitse opintojakson taso',
    ala='Valitse ala',
    )

@app_commands.choices(
    lukukausi=[
        app_commands.Choice(name="Kevät", value="spring"),
        app_commands.Choice(name="Kesä", value="summer"),
        app_commands.Choice(name="Syksy", value="fall"),
        app_commands.Choice(name="Non-Stop", value="continous"),
    ],
    kieli=[
        app_commands.Choice(name="Suomi", value="finnish"),
        app_commands.Choice(name="Ruotsi", value="swedish"),
        app_commands.Choice(name="Englanti", value="english"),
        app_commands.Choice(name="Muu", value="other"),
    ],
    taso=[
        app_commands.Choice(name="AMK", value="amk"),
        app_commands.Choice(name="YAMK", value="yamk"),
    ],
    ala=[
        app_commands.Choice(name="Kaikille soveltuva", value="kaikki"),
        app_commands.Choice(name="Humanistinen ja kasvatusala", value="humanistinen"),
        app_commands.Choice(name="Kielet ja kulttuurienvälinen viestintä", value="kielet"),
        app_commands.Choice(name="Kulttuuriala", value="kulttuuri"),
        app_commands.Choice(name="Luonnontieteiden ala", value="luonnontiede"),
        app_commands.Choice(name="Luonnonvara- ja ympäristöala", value="ymparistoala"),
        app_commands.Choice(name="Matkailu-, ravitsemis- ja liikunta-ala", value="matkailu"),
        app_commands.Choice(name="Sosiaali-, terveys- ja liikunta-ala", value="sote"),
        app_commands.Choice(name="Tekniikan ja liikenteenala", value="tekniikka"),
        app_commands.Choice(name="Yhteiskuntatieteiden, liiketalouden ja hallinnon ala", value="yhteiskunta"),
        app_commands.Choice(name="Yrittäjyys", value="yrittajyys"),
    ],
)
async def haku_campus(interaction: discord.Interaction, 
                 lukukausi: app_commands.Choice[str] = None,
                 kieli: app_commands.Choice[str] = None,
                 taso: app_commands.Choice[str] = None,
                 ala: app_commands.Choice[str] = None,
):
    # Let the bot think
    await interaction.response.defer()

    if lukukausi and kieli and taso and ala:

        # Change the color for the embed based on the value
        if lukukausi.value == "spring":
            color = yellow 
        elif lukukausi.value == "summer":
            color = green
        elif lukukausi.value == "nonstop":
            color = blue
        else: 
            color = orange
        
        campus_search_results = search_from_campusonline(lukukausi, kieli, taso, ala)
        print(campus_search_results)

        #await embed_campus(interaction, campus_search_results, color)
        await log_campus(interaction, 
                           lukukausi.value, 
                           kieli.value, 
                           taso.value, 
                           ala.value,
                           color)
    else:
        await interaction.followup.send("Annathan jokaiseen kohtaan hakusanan, kiitos!")

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