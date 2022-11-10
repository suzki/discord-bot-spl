import discord

TOKEN=''
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'buki':
        await message.channel.send('なんでやねん')
        return
    else:
        await message.channel.send(message.content)
        return
    if client.user in message.mentions:
        await reply(message)
        return

async def reply(message):
    reply = f'{message.author.mention} 呼んだ?'
    await message.channel.send(reply)


client.run(TOKEN)