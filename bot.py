import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/', description='Kiryu\'s best buddy?')
key = os.getenv('DISCORD_KEY')

@bot.event
async def on_ready():
	game = discord.game("Tracking down Kiryu-Chan")
	bot.change_presence(status=discord.Status.idle, activity=game)
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print('made by LS64 in the least efficient way possible.')
	
@bot.command()
async def greet(ctx):
	"""A greeting from Goro-san"""
	await ctx.send("Kiryu-chan!")
	
@bot.command()
async def mayo(ctx):
	"""omnomnomnom"""
	await ctx.send("https://i.imgur.com/ENfyFcQ.gif")
	
@bot.command()
async def sausage(ctx):
	"""Daddy would you like some sauasage."""
	await ctx.send("https://i.imgur.com/xxdRjoc.gif")
	
@bot.command()
async def trytobreak(ctx):
	"""attempt to force the bot to react to its own message."""
	await ctx.send("/greet")

print(key)
bot.run(key)