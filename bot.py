import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/', description='Kiryu\'s best buddy?')
key = os.getenv('DISCORD_KEY')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print('made by LS64 in the least efficient way possible.')
	
@bot.command()
async def greet(ctx):
	await ctx.send("Kiryu-chan!")
	
@bot.command()
async def mayo(ctx):
	await ctx.send("https://i.imgur.com/ENfyFcQ.gif")
	
@bot.command()
async def sausage(ctx):
	"""Daddy would you like some sauasage."""
	await ctx.send("https://i.imgur.com/xxdRjoc.gif")

print(key)
bot.run(key)