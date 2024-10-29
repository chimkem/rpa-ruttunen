import discord
from discord import app_commands

async def search_kide(interaction: discord.Interaction):
    embed = discord.Embed(
            title="Kide.App",
            description="**Tapahtuman nimi**",
            color=discord.Color.dark_purple()
        )
    # Add photos
    embed.set_thumbnail(url="https://play-lh.googleusercontent.com/f_CZ_ZEoAH38iz8WozWC3HkElLPaS3G-0jcDi0NktnsJOklduGpueIwnCjS08aiZeGQ")
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fkide.app%2Fcontent%2Fimages%2Fthemes%2Fkide%2Fapplication%2Fdefault.jpg&f=1&nofb=1&ipt=e956d2044b4a18a1a0e3897c3bfaad6e05e37a692b2fd3add132e3cf2eb2f466&ipo=images")

    # Add text to the embed
    embed.add_field(name="", value = (
            "Milloin:\n"
            "12.12.2023\n\n"
            "Missä:\n"
            "Helsinki, Rautatientori\n\n"
            "Lipunmyynti:\n"
            "`✅ Auki / ⛔ Kiinni`\n"
            "[Lisätiedot ja liput](https://discordpy.readthedocs.io/)"
        ), inline=False)
    # Set footer and current time as the timestamp
    embed.set_footer(text="Robotti Ruttunen")
    embed.timestamp = discord.utils.utcnow()
    
    await interaction.followup.send(embed=embed)
