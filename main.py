import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("naber müdür") or message.content.startswith("naber bilader"):
        await message.channel.send("iyi abi")
    else:
        await message.channel.send(message.content)

client.run("MTE5NTA1OTMyMzMxMTc2NzYyMw.GbuQtl.NXoni8r2B6qh718tWBnYmwbJ8wwkcsmlM6TiU0")
