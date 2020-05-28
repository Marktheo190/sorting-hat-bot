import discord
import random

client = discord.Client()

houses = ["Girl you have done it again. I see you slitherin' like a snake into all dat drama. So why don't you **SlytherinDisPussy**", "Wow you're sooo brave and loud and slutty. Better be **GryffinWhore**", "Damn you so wise like pennywise. You can walk yo smart ass right into **RavenLikeitRaw**", "You are definitely a freak who is also just and loyal and all dat jazz. I think you'll fit right into **HuffNPuffDisAss**", "Oh hey Peter! Wait, you're not Peter... Another RAT for **GryffinWhore**", "Oh look, another bird brain for **RavenLikeitRaw**", "Ugh, if you're gonna badger me about your sorting, I guess you're **HuffNPuffDisAss**", "Ssssssalutationsssss sssssslut, welcome to **SlytherinDisPussy**"]

@client.event
async def on_ready():
    print("Ready to be sorted?")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!sort"):
        house = random.choice(houses)
        await message.channel.send("%s, huh? %s!" % (message.author, house))

client.run("")