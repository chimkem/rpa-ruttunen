import discord
from discord import app_commands

async def search_campus(interaction: discord.Interaction):
    embed = discord.Embed(
            title="CampusOnline",
            color=discord.Color.orange(),
        )

    # Add small image
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.savonia.fi%2Fapp%2Fuploads%2F2020%2F11%2Fcampusonline-logo.jpg&f=1&nofb=1&ipt=0283fb533a5c9c0b4e6a5f1092b6edb2536b97d8aaf3f2279026916a20e23cfe&ipo=images")

    # Add text to the embed
    embed.add_field(name="Tähän kurssin nimi", value = (
            "https://discordpy.readthedocs.io/\n\n"
            "Opintojakson kieli:\n" 
            "Suomi\n\n"
            "Korkeakoulu:\n"
            "Laurea\n\n"
            "Opintopisteet:\n"
            "16 OP\n\n"
            "Taso:\n"
            "AMK\n\n"
            "Ilmoittautuminen:\n"
            "12.12.2022 - 14.05.2024\n"
            "[Ilmoittaudu kurssille](https://discordpy.readthedocs.io/)"
        ), inline=False)

    # Set footer and current time as the timestamp
    embed.set_footer(text="Robotti Ruttunen")
    embed.timestamp = discord.utils.utcnow()
    await interaction.followup.send(embed=embed)
