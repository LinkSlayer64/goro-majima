import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import os
import asyncio
import random

bot = commands.Bot(command_prefix='/', description='Kiryu\'s best buddy?')
key = os.getenv('DISCORD_KEY')
#todo - put a handler in voice commands for if we are already a part of a VC
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
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("sickness_quiet.ogg"))
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
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("glightitup_lowered.ogg"))
	vclient.play(source)
	
	
@bot.command()
async def nut(ctx):
	"""(voice) Nut (1993) not the 2016 remake"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("nut.ogg"))
	vclient.play(source)
	
@bot.command()
async def nut2(ctx):
	"""(voice) Nut 2: Hell on Earth"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("nut2.ogg"))
	vclient.play(source)
	
@bot.command()
async def finalnut(ctx):
	"""(voice) Nut Eternal"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("finalnut.ogg"))
	vclient.play(source)

@bot.command()
async def dododo(ctx):
	"""(voice) What's the song?"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("darude_dododo.ogg"))
	vclient.play(source)
	
@bot.command()
async def likethat(ctx):
	"""(voice) YOU LIKE THAT?"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("likethat.ogg"))
	vclient.play(source)
	
@bot.command()
async def soulfist(ctx):
	"""(voice) SOUL FI-SOUL FI-SOUL FI-SOUL FI-SOUL FI-SOUL FI-SOUL FI-SOUL FI-SOUL FI-SOUL FI-SOUL FIST"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("soulfist.ogg"))
	vclient.play(source)
	
@bot.command()
async def reference(ctx):
	"""(voice) Everything is a JoJo's reference"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("reference.ogg"))
	vclient.play(source)

@bot.command()
async def doit(ctx):
	"""(voice)*lightsaber noises*"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("doit.ogg"))
	vclient.play(source)
	
@bot.command()
async def jordan(ctx):
	"""(voice) I'm bad at baseball"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("jordan.ogg"))
	vclient.play(source)
	
@bot.command()
async def imjordan(ctx):
	"""(voice) Space Jam was an enjoyable movie"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("imjordan.ogg"))
	vclient.play(source)
	
@bot.command()
async def stopit(ctx):
	"""(voice) JUST DON'T"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("stopit.ogg"))
	vclient.play(source)
	
@bot.command()
async def gethelp(ctx):
	"""(voice) SEEK ASSISTANCE"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("gethelp.ogg"))
	vclient.play(source)
	
@bot.command()
async def bees(ctx):
	"""(voice) FACE/OFF"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("bees.ogg"))
	vclient.play(source)
	
@bot.command()
async def owen(ctx):
	"""(voice) Wow"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("owen.ogg"))
	vclient.play(source)
	
@bot.command()
async def uwu(ctx):
	"""(voice) OWO"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("uwu.ogg"))
	vclient.play(source)
	
@bot.command()
async def glorious(ctx):
	"""(voice) For only they can perceive reality"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("glorious.ogg"))
	vclient.play(source)
	
@bot.command()
async def ducks(ctx):
	"""(voice) Such magnificento creatures"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("ducks.ogg"))
	vclient.play(source)
	
@bot.command()
async def mahinapeaa(ctx):
	"""(voice) Echoes make everything better"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("mahinapea_echo.ogg"))
	vclient.play(source)

@bot.command()
async def breaker(ctx):
	"""(voice) This is a good game"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("breaker.ogg"))
	vclient.play(source)
	
@bot.command()
async def drown(ctx):
	"""(voice) GOOD JOB"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("drowning.ogg"))
	vclient.play(source)
	
@bot.command()
async def predictable(ctx):
	"""(voice) Die, yabo!"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("predictable.ogg"))
	vclient.play(source)
	
@bot.command()
async def diabetes(ctx):
	"""(voice) diabeetus"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("diabetes.ogg"))
	vclient.play(source)
	
@bot.command()
async def naw(ctx):
	"""(voice) hell to the naw"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("naw.ogg"))
	vclient.play(source)
	
@bot.command()
async def opticblast(ctx):
	"""(voice) from the punch dimension"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("opticblast.ogg"))
	vclient.play(source)
	
@bot.command()
async def works(ctx):
	"""(voice) buy skyrim"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("works.ogg"))
	vclient.play(source)
	
@bot.command()
async def fail(ctx):
	"""(voice) Discord? DISSSSCOOOORD!!!"""
	if not discord.opus.is_loaded():
		discord.opus.load_opus('libopus.so.0')
	if ctx.author.voice:
		vchannel = ctx.author.voice.channel
	else:
		print("no channel")
		return await ctx.send("You're not in voice Kiryu-chan!")
	vclient = await vchannel.connect()
	source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("missionfailed.ogg"))
	vclient.play(source)

#todo - add all of these to a "voicecommand" sucsection so I don't need to type out each one
@fail.after_invoke
@works.after_invoke
@opticblast.after_invoke
@diabetes.after_invoke
@naw.after_invoke
@predictable.after_invoke
@breaker.after_invoke
@drown.after_invoke
@mahinapeaa.after_invoke
@glorious.after_invoke
@ducks.after_invoke
@uwu.after_invoke	
@imjordan.after_invoke
@bees.after_invoke
@owen.after_invoke
@doit.after_invoke
@jordan.after_invoke
@stopit.after_invoke
@gethelp.after_invoke
@likethat.after_invoke
@soulfist.after_invoke
@reference.after_invoke
@dododo.after_invoke
@nut.after_invoke
@nut2.after_invoke
@finalnut.after_invoke
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


bot.run(key)