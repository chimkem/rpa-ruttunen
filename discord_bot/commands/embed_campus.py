import discord

async def embed_campus(
        interaction: discord.Interaction, 
        courses_info,
        color: discord.Color
        ):
    print(f"Campus search used!")
    embed = discord.Embed(
            title="CampusOnline",
            color=color
        )

    # Add small image
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.savonia.fi%2Fapp%2Fuploads%2F2020%2F11%2Fcampusonline-logo.jpg&f=1&nofb=1&ipt=0283fb533a5c9c0b4e6a5f1092b6edb2536b97d8aaf3f2279026916a20e23cfe&ipo=images")
    
    for course in courses_info:
        course_institution = course["institution"]
        course_points = course["points"]
        course_name = course["name"]
        course_date = course["date"]
        course_language = course["language"]
        course_level = course["level"]
        course_enrollment = course["enrollment_period"]
    
        # Add text to the embed
        embed.add_field(name=f"{course_name} - {course_date}", value = (
            "https://discordpy.readthedocs.io/\n\n"
            "Opintojakson kieli:\n" 
            f"{course_language}\n\n"
            "Korkeakoulu:\n"
            f"{course_institution}\n\n"
            "Opintopisteet:\n"
            f"{course_points} OP\n\n"
            "Taso:\n"
            f"{course_level}\n\n"
            "Ilmoittautuminen:\n"
            f"{course_enrollment}\n"
            "[Ilmoittaudu kurssille](https://discordpy.readthedocs.io/)"
        ), inline=False)

    # Set footer and current time as the timestamp
    embed.set_footer(text="Robotti Ruttunen")
    embed.timestamp = discord.utils.utcnow()

    # Send 
    await interaction.followup.send(embed=embed)

async def log_campus(
        interaction: discord.Interaction, 
        lukukausi: str,
        kieli: str, 
        taso: str, 
        ala: str,
        color: discord.Color
        ):
    print(f"Selected semester color: {color}")
    embed = discord.Embed(
            title="CampusOnline - LOG",
            color=color
        )
    embed.add_field(name="", value = (
            "**Haku toteutettu seuraavilla kriteereillä:**\n"
            f"Opintojakson kieli: {kieli}\n"
            f"Ala: {ala}\n"
            f"Lukukausi: {lukukausi}\n"
            f"Taso: {taso}\n\n"
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
    