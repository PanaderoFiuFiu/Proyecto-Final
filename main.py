import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def dato(ctx):
    datos = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCii7UGk0Z7p16-OQHUUGGrmblNPUZSfgwwXGbJN9XCA&s", "https://cdn.slidesharecdn.com/ss_thumbnails/consejosparareciclar-100606145815-phpapp01-thumbnail.jpg?width=640&height=640&fit=bounds", "https://www.economiadehoy.es/fotos/8/consejosparareducirelconsumodeplsticoennuestrodaada..jpg"]
    dat = random.choice(datos)
    await ctx.send(f"Este es un dato acerca del calentamiento global: {dat}")

@bot.command()
async def consejo(ctx, count_heh = 5):
    await ctx.send("" * count_heh)

bot.run("MTIzMjM2NDk2NTIyNzEzNTA2Ng.GxUU9P.o6APp3781IqbL6eCsVjgAywaFeOIs_4NZso0b0")