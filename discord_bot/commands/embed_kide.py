import discord

async def log_kide(interaction: discord.Interaction, 
                   haku:str,
                   paikkakunta:str
                   ):
    print(f"Kide search used!")
    embed = discord.Embed(
            title="Kide.App - LOG",
            description="",
            color=discord.Color.dark_purple()
        )
    embed.add_field(name="", value = (
            "**Haku toteutettu seuraavilla kriteereillä:**\n"
            f"Tapahtuman tyyppi: {haku}\n"
            f"Paikkakunta: {paikkakunta}"
        ), inline=False)
    
    user = interaction.user
    embed.add_field(name="Haun tehnyt käyttäjä: ", value=user.mention, inline=False)

    # Set footer and current time as the timestamp
    embed.set_footer(text="Robotti Ruttunen")
    embed.timestamp = discord.utils.utcnow()
    
    channel = interaction.guild.get_channel(1298710722007531590)
    if channel:
        await channel.send(embed=embed)
    else:
        print("Log channel not found.")

async def embed_kide(interaction: discord.Interaction, 
                     haku:str,
                     paikkakunta:str
                    ):
    embed = discord.Embed(
            title="Kide.App",
            description=f"**{haku}**",
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
            f"{paikkakunta} \n\n"
            "Lipunmyynti:\n"
            "`✅ Auki / ⛔ Kiinni`\n"
            "[Lisätiedot ja liput](https://discordpy.readthedocs.io/)"
        ), inline=False)
    # Set footer and current time as the timestamp
    embed.set_footer(text="Robotti Ruttunen")
    embed.timestamp = discord.utils.utcnow()
    
    await interaction.followup.send(embed=embed)