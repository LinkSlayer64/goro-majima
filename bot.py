import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import os
import asyncio
import random

bot = commands.Bot(command_prefix='/', description='Kiryu\'s best buddy?')
key = os.getenv('DISCORD_KEY')

@bot.event
async def on_ready():
	game = discord.Game("Tracking down Kiryu-Chan")
	await bot.change_presence(status=discord.Status.idle, activity=game)
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
	
@bot.command()
async def displeased(ctx):
	"""Ganondorf disapproves"""
	await ctx.send("https://i.imgur.com/nxIFd44.gif")
	
@bot.command()
async def smile(ctx):
	"""Who can resist that smile"""
	await ctx.send("https://i.imgur.com/c3UV8TF.gif")
	
@bot.command()
async def unacceptable(ctx):
	"""(voice enabled) UNACCEPTABLE"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
		print("opus found biotch")
	#await ctx.author.voice.channel.connect()
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		
		return await ctx.send("You're not in voice Kiryu-chan!")
	print("we've acquired the voice channel")
	vclient = await vchannel.connect()
	print("we acquired the vclient")
	#await bot.join_voice_channel(vchannel)
	#source = discord.PCMAudio(open("./UNACCEPTABLE.opus"))
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("unacceptable.ogg"))
	print("we've opened the PCMAudio, maybe?")
	vclient.play(source)
	print("we've played it?")
	#if vclient.is_playing
	#await vclient.disconnect()
	#print("we disconnected from it")

@bot.command()
async def goodnight(ctx):
	"""(voice) see ya"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
		print("opus loaded biotch")
	#await ctx.author.voice.channel.connect()
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		
		return await ctx.send("You're not in voice Kiryu-chan!")
	print("we've acquired the voice channel")
	vclient = await vchannel.connect()
	print("we acquired the vclient")
	#await bot.join_voice_channel(vchannel)
	#source = discord.PCMAudio(open("./UNACCEPTABLE.opus"))
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("gameoveryeah.ogg"))
	print("we've opened the PCMAudio, maybe?")
	vclient.play(source)
	print("we've played it?")
	
	
@bot.command()
async def cursed(ctx):
	"""(voice) this command is cursed!"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
		print("opus loaded biotch")
	#await ctx.author.voice.channel.connect()
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		
		return await ctx.send("You're not in voice Kiryu-chan!")
	print("we've acquired the voice channel")
	vclient = await vchannel.connect()
	print("we acquired the vclient")
	#await bot.join_voice_channel(vchannel)
	#source = discord.PCMAudio(open("./UNACCEPTABLE.opus"))
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("friezalaugh.ogg"))
	print("we've opened the PCMAudio, maybe?")
	vclient.play(source)
	print("we've played it?")
	
	
@bot.command()
async def ohmygod(ctx):
	"""(voice) OH MY GOGD"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
		print("opus loaded biotch")
	#await ctx.author.voice.channel.connect()
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		
		return await ctx.send("You're not in voice Kiryu-chan!")
	print("we've acquired the voice channel")
	vclient = await vchannel.connect()
	print("we acquired the vclient")
	#await bot.join_voice_channel(vchannel)
	#source = discord.PCMAudio(open("./UNACCEPTABLE.opus"))
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("ohmygod.ogg"))
	print("we've opened the PCMAudio, maybe?")
	vclient.play(source)
	print("we've played it?")
	
@bot.command()
async def yes(ctx):
	"""(voice) For you, the day Bison graced your village was the most important day of your life."""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
		print("opus loaded biotch")
	#await ctx.author.voice.channel.connect()
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		
		return await ctx.send("You're not in voice Kiryu-chan!")
	print("we've acquired the voice channel")
	vclient = await vchannel.connect()
	print("we acquired the vclient")
	#await bot.join_voice_channel(vchannel)
	#source = discord.PCMAudio(open("./UNACCEPTABLE.opus"))
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("bisonyesonce.ogg"))
	print("we've opened the PCMAudio, maybe?")
	vclient.play(source)
	print("we've played it?")
	
@bot.command()
async def yesyes(ctx):
	"""(voice) But for me, it was Tuesday."""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
		print("opus loaded biotch")
	#await ctx.author.voice.channel.connect()
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		
		return await ctx.send("You're not in voice Kiryu-chan!")
	print("we've acquired the voice channel")
	vclient = await vchannel.connect()
	print("we acquired the vclient")
	#await bot.join_voice_channel(vchannel)
	#source = discord.PCMAudio(open("./UNACCEPTABLE.opus"))
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("bisonyes.ogg"))
	print("we've opened the PCMAudio, maybe?")
	vclient.play(source)
	print("we've played it?")
	
@bot.command()
async def sickness(ctx):
	"""(voice) Get down with it"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
		print("opus loaded biotch")
	#await ctx.author.voice.channel.connect()
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		
		return await ctx.send("You're not in voice Kiryu-chan!")
	print("we've acquired the voice channel")
	vclient = await vchannel.connect()
	print("we acquired the vclient")
	#await bot.join_voice_channel(vchannel)
	#source = discord.PCMAudio(open("./UNACCEPTABLE.opus"))
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("sickness.ogg"))
	print("we've opened the PCMAudio, maybe?")
	vclient.play(source)
	print("we've played it?")
	
@bot.command()
async def mahinapea(ctx):
	"""(voice) MAHINAAAAA PEEEEEA"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
		print("opus loaded biotch")
	#await ctx.author.voice.channel.connect()
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		
		return await ctx.send("You're not in voice Kiryu-chan!")
	print("we've acquired the voice channel")
	vclient = await vchannel.connect()
	print("we acquired the vclient")
	#await bot.join_voice_channel(vchannel)
	#source = discord.PCMAudio(open("./UNACCEPTABLE.opus"))
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("mahinapea.ogg"))
	print("we've opened the PCMAudio, maybe?")
	vclient.play(source)
	print("we've played it?")
	
@bot.command()
async def no(ctx):
	"""(voice) Sure was nice of the princess to invite us over for a picnic, eh Luigi?"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
		print("opus loaded biotch")
	#await ctx.author.voice.channel.connect()
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		
		return await ctx.send("You're not in voice Kiryu-chan!")
	print("we've acquired the voice channel")
	vclient = await vchannel.connect()
	print("we acquired the vclient")
	#await bot.join_voice_channel(vchannel)
	#source = discord.PCMAudio(open("./UNACCEPTABLE.opus"))
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("mariono.ogg"))
	print("we've opened the PCMAudio, maybe?")
	vclient.play(source)
	print("we've played it?")
	
	
@bot.command()
async def hotel(ctx):
	"""(voice) I hope she made lots of spaghetti!"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("mariohotel.ogg"))
	vclient.play(source)
	
	
@bot.command()
async def crusher(ctx):
	"""(voice) Bison Bucks"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("psychocrusher.ogg"))
	vclient.play(source)
	
	
@bot.command()
async def gpeople(ctx):
	"""(voice) What is it that we fight for?"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("gpeople.ogg"))
	vclient.play(source)
	
@bot.command()
async def glight(ctx):
	"""(voice) POWER TO THE EARTH"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("glightitup.ogg"))
	vclient.play(source)

@hotel.after_invoke
@crusher.after_invoke
@glight.after_invoke
@gpeople.after_invoke
@no.after_invoke
@mahinapea.after_invoke
@yes.after_invoke
@yesyes.after_invoke
@sickness.after_invoke	
@cursed.after_invoke
@ohmygod.after_invoke	
@goodnight.after_invoke
@unacceptable.after_invoke
async def disconnect_voice(ctx):
	while ctx.voice_client.is_playing():
		await asyncio.sleep(0.1)
	await ctx.voice_client.disconnect()

	
@bot.command()
async def karin(ctx):
	"""Laugh like an Ojou-sama"""
	choices = [
	'https://i.imgur.com/xZcazrq.gif',
	'https://i.imgur.com/yWc2FJJ.gif',
	'https://i.imgur.com/PzhPIDZ.gif'
	]
	await ctx.send('OOOH HO HO HO\n' + random.choice(choices))

@bot.command()
async def antagonizeLTG(ctx):
	"""bots shouldn't listen to other bots, but oh well lol"""
	await ctx.send("!banned")

	
print(key)
bot.run(key)