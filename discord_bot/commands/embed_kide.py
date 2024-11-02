import discord

async def log_kide(interaction: discord.Interaction, haku:str,):
    print(f"Kide search used!")
    embed = discord.Embed(
            title="Kide.App - LOG",
            description="",
            color=discord.Color.dark_purple()
        )
    embed.add_field(name="", value = (
            "**Haku toteutettu seuraavilla kriteereillä:**\n"
            f"Tapahtuman tyyppi: {haku}\n"
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

async def embed_kide(interaction,
                     array_for_events,
                     haku
                    ):
    if array_for_events == 0:
        embed = discord.Embed(
                title="Kide.App",
                description=f"**Ei hakutuloksia, aika opiskella!**\n> Annettu hakusana:\n> ➥ `{haku}`",
                color=discord.Color.dark_purple()
            )
        embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngmart.com%2Ffiles%2F23%2FSad-Cowboy-Emoji-PNG-Image.png&f=1&nofb=1&ipt=5e0e9bb9d91dab37f64ce9cff4dde0a6e721a9087e2b106ebd6948072a4605d6&ipo=images")
        await interaction.followup.send(embed=embed)

    else:
        embed = discord.Embed(
                title="Kide.App",
                description=f"**Hakutuloksesi**",
                color=discord.Color.dark_purple()
            )
        # Add photos
        embed.set_thumbnail(url="https://play-lh.googleusercontent.com/f_CZ_ZEoAH38iz8WozWC3HkElLPaS3G-0jcDi0NktnsJOklduGpueIwnCjS08aiZeGQ")
        embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fkide.app%2Fcontent%2Fimages%2Fthemes%2Fkide%2Fapplication%2Fdefault.jpg&f=1&nofb=1&ipt=e956d2044b4a18a1a0e3897c3bfaad6e05e37a692b2fd3add132e3cf2eb2f466&ipo=images")

        for event in array_for_events:
            kidename = event["event_name"]
            kidelocation = event["event_location"]
            kideprice = event["event_price"]

            # Add text to the embed
            embed.add_field(name=f"**{kidename}**", value = (
                "> Milloin ja missä:\n"
                f"> ➥ `{kidelocation}`\n"
                "> Lipunmyynti:\n"
                f"> ➥ `{kideprice}`\n\n"
            ), inline=False)
        embed.add_field(name="", value= (
            f"[Checkkaa kaikki tapahtumat täältä!](https://kide.app/search?searchText={haku})"
        ), inline=False)
        # Set footer and current time as the timestamp
        embed.set_footer(text="Robotti Ruttunen")
        embed.timestamp = discord.utils.utcnow()
        
        await interaction.followup.send(embed=embed)