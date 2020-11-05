import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} 에 로그인하였습니다!')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
      await message.channel.send('pong!')

client.run('NzczODc5NDc5NTE2MTM1NDI1.X6PpbQ.rom-Xar3zANYt1ysPAdxWIm5OCM')