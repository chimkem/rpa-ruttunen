import discord

async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f"Robotti Ruttunen oli robotti peltinen, tehty tynnyristä ja kahdesta ämpäristä.")

async def moikkaa(interaction: discord.Interaction):
    await interaction.response.send_message("Moro!")
