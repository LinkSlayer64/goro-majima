from datetime import datetime
import cacobot.base as base
import random, asyncio
import feedparser
import urllib.parse
import urllib.request
import json
import requests
import discord

@base.cacofunc
async def nekro(message, client, *args, **kwargs):
	'''
	**/nekro**
	Demand more lewd images, as if he needed encouragement
	'''
	await client.send_message(message.channel, "Nekro, post more hentai")
nekro.server = 'Destructoid Users'

global versenum
versenum = -1

verse = ['Hello darkness, my old friend',
'I\'ve come to talk with you again',
'Because a vision softly creeping',
'Left its seeds while I was sleeping',
'And the vision that was planted in my brain',
'Still remains',
'Within the sound of silence',

'In restless dreams I walked alone',
'Narrow streets of cobblestone',
'\'Neath the halo of a street lamp',
'I turned my collar to the cold and damp',
'When my eyes were stabbed, by the flash of a neon light',
'That split the night',
'And touched the sound of silence',

'And in the naked light I saw',
'Ten thousand people, maybe more',
'People talking without speaking',
'People hearing without listening',
'People writing songs',
'That voices never share',
'No one dare',
'Disturb the sound of silence',

'"Fools" said I, "you do not know',
'Silence, like a cancer, grows',
'Hear my words that I might teach you',
'Take my arms that I might reach you"',
'But my words like silent raindrops fell',
'And echoed in the wells of silence',

'And the people bowed and prayed',
'To the neon God they made',
'And the sign flashed out its warning',
'And the words that it was forming',

'And the sign said,',
'"The words of the prophets',
'Are written on the subway walls',
'And tenement halls."',
'And whispered in the sound of silence']

verse2 = [
'Domo arigato, Mr. Roboto [どうもありがとうミスターロボット],',
'Mata au hi made [また会う日まで]',
'Domo arigato, Mr. Roboto [どうもありがとうミスターロボット],',
'Himitsu wo shiri tai [秘密を知りたい]',

'You\'re wondering who I am (secret secret I\'ve got a secret)',
'Machine or mannequin (secret secret I\'ve got a secret)',
'With parts made in Japan (secret secret I\'ve got a secret)',
'I am the modren man',

'I\'ve got a secret I\'ve been hiding under my skin',
'My heart is human, my blood is boiling, my brain I.B.M.',
'So if you see me acting strangely, don\'t be surprised',
'I\'m just a man who needed someone, and somewhere to hide',

'To keep me alive, just keep me alive',
'Somewhere to hide, to keep me alive',

'I\'m not a robot without emotions. I\'m not what you see',
'I\'ve come to help you with your problems, so we can be free',
'I\'m not a hero, I\'m not the saviour, forget what you know',
'I\'m just a man whose circumstances went beyond his control',

'Beyond my control. We all need control',
'I need control. We all need control',

'I am the modren man (secret secret I\'ve got a secret)',
'Who hides behind a mask (secret secret I\'ve got a secret)',
'So no one else can see (secret secret I\'ve got a secret)',
'My true identity',

'Domo arigato, Mr. Roboto, domo...domo',
'Domo arigato, Mr. Roboto, domo...domo',
'Domo arigato, Mr. Roboto,',
'Domo arigato, Mr. Roboto,',
'Domo arigato, Mr. Roboto,',
'Domo arigato, Mr. Roboto,',

'Thank you very much, Mr. Roboto',
'For doing the jobs that nobody wants to',
'And thank you very much, Mr. Roboto',
'For helping me escape just when I needed to',
'Thank you, thank you, thank you',
'I want to thank you, please, thank you',

'The problem\'s plain to see:',
'Too much technology',
'Machines to save our lives.',
'Machines dehumanize.',

'The time has come at last (secret secret I\'ve got a secret)',
'To throw away this mask (secret secret I\'ve got a secret)',
'Now everyone can see (secret secret I\'ve got a secret)',
'My true identity...',

'I\'m Kilroy! Kilroy! Kilroy! Kilroy!'
]

verse3 = [
'All around me are familiar faces',
'Worn out places, worn out faces',
'Bright and early for their daily races',
'Going nowhere, going nowhere',

'Their tears are filling up their glasses',
'No expression, no expression',
'Hide my head, I wanna drown my sorrow',
'No tomorrow, no tomorrow',

'And I find it kinda funny',
'I find it kinda sad',
'The dreams in which I\'m dying',
'Are the best I\'ve ever had',
'I find it hard to tell you',
'I find it hard to take',
'When people run in circles',
'It\'s a very, very',
'Mad world,',
'Mad world',

'Children waiting for the day they feel good',
'Happy Birthday, Happy Birthday',
'And I feel the way that every child should',
'Sit and listen, sit and listen',

'Went to school and I was very nervous',
'No one knew me, no one knew me',
'Hello teacher tell me what\'s my lesson',
'Look right through me, look right through me',

'And I find it kinda funny',
'I find it kinda sad',
'The dreams in which I\'m dying',
'Are the best I\'ve ever had',
'I find it hard to tell you',
'I find it hard to take',
'When people run in circles',
'It\'s a very, very',
'Mad world,',
'Mad world',

'Enlarging your world',
'Mad world'
]
# global tracknum
# tracklist = [verse, verse2, verse3]
# tracknum = 0


# async def sing(message, client, *args, **kwargs):
	# def check(msg):
		# return msg.author.id != client.user.id
	# msg = await client.wait_for_message(timeout=1200, channel=message.channel, check=check)
	# if msg == None:
		# global versenum
		# global tracknum
		# versenum = 0
		
		# tracknum = random.randint(0,len(tracklist) - 1)
		# print(versenum)
		# print(tracknum)
		# await client.send_message(message.channel, (tracklist[tracknum])[versenum])
		# await sing2(message, client, *args, **kwargs) 


# async def sing2(message, client, *args, **kwargs):
	# def check(msg):
		# return msg.author.id != client.user.id
	# msg = await client.wait_for_message(timeout=5, channel=message.channel, check=check)
	# if msg == None:
		# global versenum
		# global tracknum
		# versenum += 1
		# print('sing2 versenum:')
		# print(versenum)
		# await client.send_message(message.channel, (tracklist[tracknum])[versenum])
		# if versenum < len(tracklist[tracknum]):
			# await sing2(message, client, *args, **kwargs) 
		# #else:
			

# @base.cacofunc
# async def startsong(message, client, *args, **kwargs):
	# '''
	# stuff
	# '''
	# base.globchan = message.channel
	# print(base.globchan)
	
	# await client.send_message(message.channel, "The song will be sung")
	# await sing(message, client, *args, **kwargs)

# @base.postcommand
# async def continuesong(message, client, *args, **kwargs):
	# if message.channel == base.globchan and message.author.id != client.user.id:
		# await sing(message, client, *args, **kwargs)

@base.cacofunc
async def nekrogif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://i.imgur.com/RanwneF.gif")
nekrogif.server = 'Destructoid User Gifs'

@base.cacofunc
async def puke(message, client, *args, **kwargs):
	'''
	**/puke**
	WHY IS THIS A THING
	'''
	await client.send_message(message.channel, "http://i.makeagif.com/media/5-22-2015/sEX89t.gif")

	
@base.cacofunc
async def ls64(message, client, *args, **kwargs):
	'''
	**/ls64**
	Question in a gramatically incorrect way, when Nintendo's all-star massacre will occur.
	'''
	await client.send_message(message.channel, "WHEN'S SMESH!?")
ls64.server = 'Destructoid Users'	

@base.cacofunc
async def ls64gif(message, client, *args, **kwargs):
	'''
	**/ls64gif**
	Use this to express your sudden displeasure as the king of evil, Ganondorf.
	'''
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/140603735620583424/143815133867671552/1442179038399.gif")
ls64gif.server = 'Destructoid User Gifs'

@base.cacofunc
async def buttslap(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://i.imgur.com/EF4Xqm6.gif")
	
@base.cacofunc
async def taunt(message, client, *args, **kwargs):
	'''
	**/taunt**
	**NSFW(?)** taunt others with all dat junk in yo' trunk
	Chooses a random gif from an assortment.
	'''
	choices = [
	'https://cdn.discordapp.com/attachments/164576366883241984/206127641919488000/z0sxiciphy1.gif',
	'http://4.bp.blogspot.com/-_0UAQGtZir8/ToPgRsIOatI/AAAAAAAABvE/CseVCWd2wac/s1600/hentai--gif--ikkitousen--panties--sonsaku-hakufu--spanking+%25282%2529.gif'
	]
	await client.send_message(message.channel, random.choice(choices))
	
@base.cacofunc
async def occams(message, client, *args, **kwargs):
	choices = [
		'**BANNED**',
		'**BANED**',
		'**BRUCE BANNERED**'
	]
	await client.send_message(message.channel, random.choice(choices))	
occams.server = 'Destructoid Users'

@base.postcommand
async def heresy(message, client, *args, **kwargs):
	if message.author.id != client.user.id:
		if 'heresy' in message.content.lower():
			choices = [
				'https://cdn.discordapp.com/attachments/165134518561275905/184405655958847489/heresy.png',
				'https://cdn.discordapp.com/attachments/165134518561275905/184405659612086273/Ifsomeonewhoyouhaveabsolutelynoconnectiontowhatsoever_15d7d1c2e6b51e230c244f54e423b763.jpg',
				'https://cdn.discordapp.com/attachments/165134518561275905/184405661445128193/Vw0HV8h.png',
				'https://cdn.discordapp.com/attachments/165134518561275905/184405637310971908/5d258ddd4b132095b02a9c178fe9997a.jpg',
				'https://cdn.discordapp.com/attachments/165134518561275905/184405628377235457/1924990_657445890981570_282440172_n.jpg',
				'https://cdn.discordapp.com/attachments/165134518561275905/184405622681370635/1237006_637957179572448_372395127_n.jpg',
				'https://cdn.discordapp.com/attachments/165134518561275905/184405610668752897/72933_533634873353200_348398133_n.jpg',
				'http://new4.fjcdn.com/thumbnails/comments/Someone+call+for+a+purge+_7590cf62f94a0ff9c20de074c3f5b94d.jpg',
				'https://cdn.discordapp.com/attachments/165134518561275905/190483291244068866/13413602_1392774777405324_8983738072358453568_n.jpg',
				'https://cdn.discordapp.com/attachments/164576366883241984/206591414098853899/heresy_warhammermark.png',
				'https://cdn.discordapp.com/attachments/164576366883241984/207268333978910720/13645108_1249924441705974_4862038027784940182_n.jpg',
				'http://i1.kym-cdn.com/photos/images/original/000/648/534/2b9.jpg',
				'https://discordcdn.com/attachments/206857689177784320/210023027512049666/e8b.jpg']
			await client.send_message(message.channel, random.choice(choices))	
			
#@base.postcommand
#async def problematic(message, client, *args, **kwargs):
#	if message.author.id != client.user.id:
#		if 'problematic' in message.content.lower():
#
#			await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/135186576195059714/197577687055859714/sjw1.jpg")	
'''
@base.cacofunc
async def heresy(message, client, *args, **kwargs):
	choices = [
		'https://cdn.discordapp.com/attachments/165134518561275905/184405655958847489/heresy.png',
		'https://cdn.discordapp.com/attachments/165134518561275905/184405659612086273/Ifsomeonewhoyouhaveabsolutelynoconnectiontowhatsoever_15d7d1c2e6b51e230c244f54e423b763.jpg',
		'https://cdn.discordapp.com/attachments/165134518561275905/184405661445128193/Vw0HV8h.png',
	]
	await client.send_message(message.channel, random.choice(choices))	
'''
	
@base.cacofunc
async def torchman(message, client, *args, **kwargs):
	await client.send_message(message.channel, "Your waifu is shit")
torchman.server = 'Destructoid Users'
	
@base.cacofunc
async def torchgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://i.imgflip.com/10e7mk.gif")	
torchgif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def larx(message, client, *args, **kwargs):
	'''
	**/larx**
	SHOW ME YOUR NEP FACE
	'''
	choices = [
		'**Top Nep**',
		'**Nep Nep**',
		'*Neps Externally*',
		'*Do you even Nep, bro?*',
		'*How Do I Nep a Nep?*'
	]
	await client.send_message(message.channel, random.choice(choices))	
larx.server = 'Destructoid Users'

@base.cacofunc
async def triggered(message, client, *args, **kwargs):
	'''
	**/triggered**
	'''
	choices = [
		'http://corn-rages.com/public/style_emoticons/default/triggered.gif',
		'http://i.imgur.com/JLhNxqV.gif',
		'https://i.imgur.com/rTWDmuc.gif',
		'https://images-ext-1.discordapp.net/eyJ1cmwiOiJodHRwOi8vNjYubWVkaWEudHVtYmxyLmNvbS8yYTc5N2FmNDdkYTJlYWIwYTk2OGExNDg0NTFmYWFkMS90dW1ibHJfbzZ2ajV3RUpoOTF2cHVmemJvMV8xMjgwLmdpZiJ9.RGh7KdwT7FH7jWSfdEtR_GD_iKI.gif'
	]
	await client.send_message(message.channel, random.choice(choices))	
	
@base.cacofunc
async def larxgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://24.media.tumblr.com/ff85f929275e02b94932c77c88c81d40/tumblr_mrpviyNQYf1s3q3hao1_400.gif")
larxgif.server = 'Destructoid User Gifs'

@base.cacofunc
async def rouge(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://0.media.dorkly.cvcdn.com/48/31/2a1e1becb2af63efce57de90cc91162e.jpg")
	await client.send_message(message.channel, "http://0.media.dorkly.cvcdn.com/60/92/5eb77dcd91ac8d8059cec6a93d5bfc69.jpg")


@base.cacofunc
async def bees(message, client, *args, **kwargs):
	'''
	**/bees**
	Share with your friends the most thoughtful gif of them all!
	'''
	await client.send_message(message.channel, "https://thewheatandthechaff.files.wordpress.com/2014/01/medium_oprah_bees-1.gif")

@base.cacofunc
async def gm34gif(message, client, *args, **kwargs):
	'''
	**/gm34gif**
	mMMMmmMMmMm
	'''
	await client.send_message(message.channel, "https://i.imgur.com/NwgCqIz.gif")
gm34gif.server = 'Destructoid User Gifs'

@base.cacofunc
async def occamsgif(message, client, *args, **kwargs):
	'''
	**/occamsgif**
	#Darksiders2
	'''
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/187307085728448512/187307460778917889/Darksiders2Redux.gif")
occamsgif.server = 'Destructoid User Gifs'

@base.cacofunc
async def descruffgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/203713478714720258/203713551976759296/DeHackMe.gif")
descruffgif.server = 'Destructoid User Gifs'

@base.cacofunc
async def sass(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://giant.gfycat.com/HotAgileDoctorfish.gif")
	
@base.cacofunc
async def eyesigil(message, client, *args, **kwargs):
	await client.send_message(message.channel, "FUCK Skype :thumbsup:")
eyesigil.server = 'Destructoid Users'

@base.cacofunc
async def scrustlegif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/135186576195059714/155597475074408450/tumblr_nsp73mh1Gv1qhhvheo2_r1_500.gif")
scrustlegif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def mike(message, client, *args, **kwargs):
	await client.send_message(message.channel, "Fuck you")
mike.server = 'Destructoid Users'
	
@base.cacofunc
async def mikegif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/135186576195059714/155598497402454017/freedom-boner.gif")
mikegif.server = 'Destructoid User Gifs'

@base.cacofunc
async def obigif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://i.giphy.com/5FzZHQIQRrxDi.gif")
obigif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def lawman(message, client, *args, **kwargs):
	'''
	**/lawman**
	The output is shorter than the command, damn Lawman is lazy.
	'''
	await client.send_message(message.channel, "heh")
lawman.server = 'Destructoid Users'

@base.cacofunc
async def lawdurst(message, client, *args, **kwargs):
	'''
	**/durst**
	Lawman is either black, or Fred Durst, YOU DECIDE!
	'''
	choices = [
		'Lawmans\' ROLLIN ROLLIN ROLLIN',
		'Lawman did it for the nookie!',

	]
	await client.send_message(message.channel, random.choice(choices))	
lawdurst.server = 'Destructoid Users'
	
@base.cacofunc
async def yoseph(message, client, *args, **kwargs):
	'''
	**/yoseph**
	Good ol' what's-his-name!
	'''
	await client.send_message(message.channel, "Stop changing your damn name")
yoseph.server = 'Destructoid Users'

@base.cacofunc
async def theblondesterling(message, client, *args, **kwargs):
	'''
	**/theblondesterling**
	Question the memetic quality of something, like only Jim Sterling could (or Bass can claim to.)
	'''
	await client.send_message(message.channel, "Is this memes?")
theblondesterling.server = 'Destructoid Users'

#@base.cacofunc
async def bass(message, client, *args, **kwargs):
	'''
	**/bass**
	Show off your French-Canadian pride.
	'''
	choices = [
		'honhonhon',
		'honhonhon baguette'
	]
	await client.send_message(message.channel, random.choice(choices))	
bass.server = 'Destructoid Users'

@base.cacofunc
async def bassgif(message, client, *args, **kwargs):
	'''
	**/bassgif**
	Bass should be more careful with expensive computer hardware, but alas, he is not
	'''
	await client.send_message(message.channel, "https://i.gyazo.com/thumb/1200/_7a72180cb65a37688b8fb7efcff48889-gif.gif")
bassgif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def amna(message, client, *args, **kwargs):
	'''
	**/amna**
	Keep up with the best love story since Twilight
	'''
#Amna started playing December 18th, 2015
	d0 = datetime(2015, 12, 23, 10, 13, 34)
	d1 = datetime.now()
	delta = d1 - d0
	split1 = str(delta).split(",")
	timeSplit = split1[1].split(":")
	await client.send_message(message.channel, "Happily married to Rocket League for " + split1[0] + ", " + timeSplit[0] + " hours, " + timeSplit[1] + " minutes, and " + timeSplit[2] + " seconds.")	
amna.server = 'Destructoid Users'
	
@base.cacofunc
async def leaves(message, client, *args, **kwargs):
	'''
	**/leaves**
	Express your intention to depart in the most tasteful of ways.
	Selects a random gif from an assortment
	'''
	choices = [
	'https://66.media.tumblr.com/tumblr_ma436sBiuz1r8ru56o4_250.gif'
	]
	await client.send_message(message.channel, "Fuck Dis Place! \n" + random.choice(choices))
	
@base.postcommand
async def darksiderstwo(message, client, *args, **kwargs):
	if message.author.id != client.user.id:
		if 'darksiders2' in message.content.lower() or 'darksiders' in message.content.lower():
			await client.send_message(message.channel, '**#Darksiders2**')
darksiderstwo.server = 'Destructoid'

@base.cacofunc
async def ricogif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://media.giphy.com/media/zW2k7bMhkUfwA/giphy.gif")
ricogif.server = 'Destructoid User Gifs'	

@base.cacofunc
async def moneyyes(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://i.imgur.com/MBJhEUX.gif")
	
@base.cacofunc
async def moneyno(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://i.imgur.com/15IV0Io.gif")

@base.cacofunc
async def pengirls(message, client, *args, **kwargs):
	'''
	**/pengirls**
	noot noot
	'''
	await client.send_message(message.channel, "https://67.media.tumblr.com/92c7edab29283ea1f7b5919947eb9c56/tumblr_obfv3r95CS1vveadmo1_500.gif")

@base.cacofunc
async def ban(message, client, *args, **kwargs):
	'''
	**/ban**
	"TWO YEARS OF SEMEN MADE A GLOPPING NOISE AS THEY FLOWED ENDLESSLY INTO ASUNA - SWORD ART ONLINE"
	'''
	await client.send_message(message.channel, "https://images-1.discordapp.net/.eJwFwdsNwyAMAMBdGABj80y2QYQSpKSOsPtVdffefc1nXWY3p-ojO8AxpfE6rCivOrodzOPq9ZliG99QVWs77_5WAXKpxEzBB8RQXMwJCH1IWyFPiA7JbRlib3bMl_n9AXdpIKg.nP8YDwvG5aO8rF-0JGmOelr5Aik.gif")

	
@base.cacofunc
async def alright(message, client, *args, **kwargs):
	'''
	**/ALRIGHT**
	ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT ALRIGHT
	'''
	await client.send_message(message.channel, "https://www.youtube.com/watch?v=8qMtsir0l9k")
	
@base.cacofunc
async def kinggm(message, client, *args, **kwargs):
	'''
	**/kinggm**
	"Ruling over us with an iron Flagella"
	'''
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/159777429521432576/216003986535350272/66963616.jpg")
	
@base.cacofunc
async def thrust(message, client, *args, **kwargs):
	'''
	**/thrust**
	"noot noot"
	'''
	await client.send_message(message.channel, "https://4.bp.blogspot.com/-V8LhQcWoG2A/VsoXDemic3I/AAAAAAAAGCs/qbuo2Sc6WT4/s1600/XALdIVG.gif")

	
@base.cacofunc
async def alphadeus(message, client, *args, **kwargs):
	await client.send_message(message.channel, "C'mon and rock me Alphadeus!")	
alphadeus.server = 'Destructoid Users'

@base.cacofunc
async def jedgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/135186576195059714/157316622967767041/zq1sr.gif")	
jedgif.server = 'Destructoid User Gifs'

@base.cacofunc
async def jed(message, client, *args, **kwargs):
	await client.send_message(message.channel, "dad pls")	
jed.server = 'Destructoid Users'

@base.cacofunc
async def seymourgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://static.comicvine.com/uploads/ignore_jpg_scale_super/11120/111202498/4225263-6775636432-tumbl.gif")		
seymourgif.server = 'Destructoid User Gifs'

@base.cacofunc
async def lawmangif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://media.giphy.com/media/ruws5s45lx05y/giphy.gif")		
lawmangif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def lexgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://s22.postimg.org/phmagmvg1/ezgif_com_optimize.gif")		
lexgif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def logeongif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://i.imgur.com/jEitxrB.gif")		
logeongif.server = 'Destructoid User Gifs'

@base.cacofunc
async def smartass(message, client, *args, **kwargs):
	'''
	**/smartass**
	Bestow an award to a special someone
	'''
	await client.send_message(message.channel, "http://i78.photobucket.com/albums/j87/jessica_adel/comments/trophy/smartass.gif")	

@base.cacofunc
async def waifu(message, client, *args, **kwargs):
	'''
	**/waifu**
	Express your love for waifus with this great command!
	'''
	await client.send_message(message.channel, "http://i.imgur.com/fzOXvOb.gif")	

	
@base.cacofunc
async def order66(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://i.imgur.com/cJlBUVL.gif")
	
@base.postcommand
async def robotoverlord(message, client, *args, **kwargs):
	if message.author.id != client.user.id:
		if 'robot overlord' in message.content.lower() or 'robotic overlord' in message.content.lower() or 'robot overlords' in message.content.lower() or 'robotic overlords' in message.content.lower():
			await client.send_message(message.channel, 'http://i3.kym-cdn.com/photos/images/original/000/775/815/a85.gif')


@base.postcommand
async def fucksigive(message, client, *args, **kwargs):
	if message.author.id != client.user.id:
		if '@mr. destructoid' in message.content.lower():
			if 'fucks do i give' in message.content.lower(): 
				print(message.content.lower())
				await client.send_message(message.channel, 'I\'m guessing it\'s a resounding ***ZERO***')

		


@base.postcommand
async def teamrocket(message, client, *args, **kwargs):
	if message.author.id != client.user.id:
		james = ''
		if 'prepare for trouble' in message.content.lower():
			james = 'And make it double!'
			await client.send_message(message.channel, james)
		elif 'to protect the world from devastation' in message.content.lower():
			james = 'To unite all people within our nation!'
			await client.send_message(message.channel, james)
		elif 'to denounce the evils of truth and love' in message.content.lower():
			james = 'To extend our reach to the stars above'
			await client.send_message(message.channel, james)
		elif 'jessie' in message.content.lower():
			james = 'James!'
			await client.send_message(message.channel, james)
		elif 'team rocket blast off at the speed of light' in message.content.lower():
			james = 'Surrender now or prepare to fight!'
			await client.send_message(message.channel, james)
			
@base.cacofunc
async def owtheedge(message, client, *args, **kwargs):
	'''
	**/owtheedge**
	Mind the quills, they're quite sharp.
	'''
	await client.send_message(message.channel, "In honor of Logeon: https://www.youtube.com/watch?v=8V1pMQKDPco")

@base.cacofunc
async def blazegif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://45.media.tumblr.com/6dac8a095c475639b589cbe7fd583eaa/tumblr_nvq0jvVh3b1rw7ngmo1_500.gif")
blazegif.server = 'Destructoid User Gifs'

@base.cacofunc
async def sayword(message, client, *args, **kwargs):
	await client.send_message(message.channel, "*Buys another PS Vita*")
sayword.server = 'Destructoid Users'

@base.cacofunc
async def towel(message, client, *args, **kwargs):
	'''
	**/towel**
	*sweating intensifies*
	'''
	choices = [
	'http://i2.kym-cdn.com/photos/images/newsfeed/000/886/249/00a.png',
	'https://cdn.discordapp.com/attachments/165134518561275905/208612473748586497/d45ea3697603cc9ade3821623783596c.jpeg',
	'https://cdn.discordapp.com/attachments/165134518561275905/208612477687037952/fbf.png',
	'https://cdn.discordapp.com/attachments/165134518561275905/208612477175332866/Weneedeveryversionofthis_a8f52ffd18535993bc37e0bbbae607a7.png',
	'https://cdn.discordapp.com/attachments/165134518561275905/208612473023102979/Ifoundsomemore_5258c6c5c96caf3e809e4015784a2d64.png',
	'https://cdn.discordapp.com/attachments/165134518561275905/208612466282856449/831.png',
	'https://cdn.discordapp.com/attachments/165134518561275905/208612468551974912/c0b.jpg',
	'https://cdn.discordapp.com/attachments/165134518561275905/208612465976541185/4875466_427054bbecf9161b6e6a2c5840a53c7f.jpg',
	'https://cdn.discordapp.com/attachments/165134518561275905/208612462067449857/9c0.jpg',
	'https://cdn.discordapp.com/attachments/165134518561275905/208612461316800512/7be.png'
	]
	await client.send_message(message.channel, random.choice(choices))


@base.cacofunc
async def zawarudo(message, client, *args, **kwargs):
	choices = [
		'http://images.uncyc.org/pt/9/96/Dio-theworld4.gif',
		'https://i.imgflip.com/118b65.jpg'
	]
	await client.send_message(message.channel, random.choice(choices))

@base.cacofunc
async def franco(message, client, *args, **kwargs):
	'''
	**/franco**
	Sass others like only James Franco could.
	'''
	await client.send_message(message.channel, "https://counterforce.files.wordpress.com/2011/08/no-explanation-required.gif")


	
@base.cacofunc
async def logeon(message, client, *args, **kwargs):
	'''
	**/logeon**
	He likes teh ladies.
	'''
	await client.send_message(message.channel, "Now you're thinking with penis!")
logeon.server = 'Destructoid Users'

@base.cacofunc
async def crazytaxi(message, client, *args, **kwargs):
	'''
	**/crazytaxi**
	Are ya' ready? HERE WE GO!
	'''
	await client.send_message(message.channel, "YA YA YA YA YA!")

	
@base.cacofunc
async def gm34(message, client, *args, **kwargs):
	'''
	**/gm34**
	You think he'd say "buzz" all the time, but no....
	'''
	mms = random.randint(3, 34)
	output = ""
	for x in range(0, mms):
		output += 'm'
	await client.send_message(message.channel, output)
gm34.server = 'Destructoid Users'

@base.cacofunc
async def rules(message, client, *args, **kwargs):
	'''
	**/rules**
	No fun allowed (jk)
	'''
	await client.send_message(message.channel, "This channel follows the rules of the Destructoid community. \nPlease read them at http://www.destructoid.com/community-blogs-terms-and-conditions-77513.phtml")
rules.server = 'Destructoid'

@base.cacofunc
async def niwagif(message, client, *args, **kwargs):
	'''
	**/niwagif**\
	I HAVE NOTHING WITTY
	'''
	await client.send_message(message.channel, "https://45.media.tumblr.com/1d2e4cc4da75f590b9f88fe2e423c900/tumblr_nttp02xe0O1r5uc2xo1_400.gif")
niwagif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def k(message, client, *args, **kwargs):
	'''
	**/k**\
	State your plain acceptance
	'''
	choices = [
		'http://files.greatermedia.com/uploads/sites/15/2016/03/145890872.jpg',
		'http://i.imgur.com/pevSPn4.gif',
		'https://media.giphy.com/media/YabqH4YYNJGOk/giphy.gif',
		'https://media.giphy.com/media/3o6UBlHJQT19wSgJQk/giphy.gif',
		'http://i.imgur.com/QnbbzxJ.gif',		
		'https://media.giphy.com/media/KyWQ96Lu2QCRi/giphy.gif',
		'https://media.giphy.com/media/3o6UBhsPwOlf1fpNVC/giphy.gif',
		'https://media.giphy.com/media/vMiQkQ507ARna/giphy.gif',
		'http://i.imgur.com/5dLMAjK.gif',
		'http://i.imgur.com/5QqMR0V.gif',
		'https://i.imgur.com/6UY6QIQ.gif',
		'https://feedmericeballsdotcom.files.wordpress.com/2016/02/opm3.gif?w=640'
	]
	await client.send_message(message.channel,  random.choice(choices))

	
@base.cacofunc
async def malthorgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://37.media.tumblr.com/8ffcb6173c404c305eb4011632e726b3/tumblr_nb1ojqoNgs1rdr926o1_250.gif")
malthorgif.server = 'Destructoid User Gifs'

@base.cacofunc
async def lenny(message, client, *args, **kwargs):
	'''
	to ad
	'''
	await client.send_message(message.channel, "( ͡° ͜ʖ ͡°)")

	
#@base.cacofunc
#async def shrug(message, client, *args, **kwargs):
#	await client.send_message(message.channel, "¯\_(ツ)_/¯")

@base.cacofunc
async def dtoid(message, client, *args, **kwargs):
	'''
	**/dtoid** [x]
	displays the *x* most recent article on dtoid
	If no argument is supplied, displays the most recent
	'''
	d = feedparser.parse('http://www.destructoid.com/index.phtml?mode=atom')
	url = ''
	try:
		params = message.content.split()
		if len(params) == 1:
			url = d['entries'][0].link
		else:
			#article = (params[1] - 1)
			url = d['entries'][int(params[1]) - 1].link
		await client.send_message(message.channel, url)
	except(IndexError, ValueError):
		# user did not format command correctly
		await client.send_message(message.channel, '{}: you did something wrong, scallywag!')
dtoid.server = 'Destructoid'
	#d = feedparser.parse('http://www.destructoid.com/index.phtml?mode=atom')
	#url = d['entries'][0].link
	#await client.send_message(message.channel, url)

	
@base.cacofunc
async def ferusgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, 'http://cdnl.complex.com/assets/CHANNEL_IMAGES/MUSIC/2013/02/content/1361858806_tumblr_m9cbxobosu1qjn9tuo1_400.gif')
ferusgif.server = 'Destructoid User Gifs'

@base.cacofunc
async def yosephgif(message, client, *args, **kwargs):
	choices = [
		'http://i.imgur.com/ofc7zrs.gif',
		'http://i.imgur.com/QAKFpPF.gif',
		'http://i.imgur.com/stf6Jam.gif',
		'http://i.imgur.com/Y1EbFxg.gif',
		'https://giant.gfycat.com/ImpoliteSinfulBuzzard.gif',
		'http://vignette2.wikia.nocookie.net/le-miiverse-resource/images/3/39/Eggman_shit_posting.gif',
		'http://i.imgur.com/pbjOtuW.gif',
		'http://i3.kym-cdn.com/photos/images/newsfeed/000/709/556/bf3.gif',
		'http://i.imgur.com/5UjR5pB.gif',
		'https://cdn.discordapp.com/attachments/206975689847603201/210876975982706688/1417232745206.gif',
		'http://i.imgur.com/tNXPrBe.gif',
		'https://i.imgur.com/7Nc3itg.gif',
		'http://i1.kym-cdn.com/photos/images/newsfeed/000/711/684/317.gif',
		'http://2new4.fjcdn.com/funny_gifs/Shitposting+intensifies_1615fe_5848566.gif',
		'https://i.warosu.org/data/ck/img/0070/42/1446663331283.gif',
		'http://i2.kym-cdn.com/photos/images/original/000/762/354/688.gif',
		'https://cdn.discordapp.com/attachments/170002524156329984/202856973056737280/Violently_Shitposting.gif',
		'https://discordcdn.com/attachments/206857243411480576/210587602611339266/tumblr_o1j55oez4H1udh5n8o1_400.gif'
	]
	await client.send_message(message.channel,  random.choice(choices))
yosephgif.server = 'Destructoid User Gifs'

@base.cacofunc
async def spooky(message, client, *args, **kwargs):
	choices = [
		'https://cdn.discordapp.com/attachments/170002524156329984/210148340787183626/tumblr_static_rmb3.gif'
		
		]
	await client.send_message(message.channel,  random.choice(choices))
yosephgif.server = 'Destructoid User Gifs'	

@base.cacofunc
async def rattlemebones(message, client, *args, **kwargs):
	choices = [
		'https://cdn.discordapp.com/attachments/170002524156329984/210148340787183626/tumblr_static_rmb3.gif'
		
		]
	await client.send_message(message.channel,  random.choice(choices))
yosephgif.server = 'Destructoid User Gifs'	
	
@base.cacofunc
async def gaston(message, client, *args, **kwargs):
	'''
	**/gaston**
	NOBODY MAKES A COMMAND, LIKE GASTON!
	'''
	await client.send_message(message.channel, 'http://i0.kym-cdn.com/photos/images/original/000/748/936/169.gif')
	
@base.cacofunc
async def magicword(message, client, *args, **kwargs):
	await client.send_message(message.channel, 'http://i.imgur.com/4C7iu09.gif')

	
@base.cacofunc
async def please(message, client, *args, **kwargs):
	await client.send_message(message.channel, "***Please! Godamnit I hate this hacker crap!***")

@base.cacofunc
async def wannago(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://45.media.tumblr.com/848ed402174a1786e7461c517dc70aad/tumblr_o234hyBusg1ufq0ayo1_500.gif")


@base.cacofunc
async def mahvel(message, client, *args, **kwargs):
	await client.send_message(message.channel, "Fuck the Knicks!")

	
@base.cacofunc
async def kramer(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/135186576195059714/167092187404697605/tumblr_o0dfb5XAQG1rn8um6o1_400.gif") 

	
@base.cacofunc
async def monster(message, client, *args, **kwargs):
	#choices  = list(message.server.members)
	choices = []
	for i in message.server.members:
		if(i.status == discord.Status.online):
			choices.append(str(i))
	
	await client.send_message(message.channel, str(random.choice(choices)) + " is a monster")
	
@base.cacofunc
async def juicegif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://ci.memecdn.com/584/7310584.gif") 
juicegif.server = 'Destructoid User Gifs'

@base.cacofunc
async def keepshappening(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://static2.fjcdn.com/thumbnails/comments/I+told+you+about+stairs+bro+_14bf046285a3a049b15ff86d69a028c5.gif") 

@base.cacofunc
async def wesgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/169553277157900289/169553504854081538/swing.gif") 
wesgif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def regret(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://i.imgur.com/Q81RPrp.gif")

@base.cacofunc
async def malikagif(message, client, *args, **kwargs):
	'''
	**/malikagif**
	FUCKING LEWD
	'''
	choices = [
		'http://img6.cache.netease.com/game/2015/11/13/20151113115319064e2.gif',
		'http://pa1.narvii.com/5827/167b610f0a77d2e5e3745e0048910d956e2c13a9_hq.gif'
	]
	await client.send_message(message.channel, random.choice(choices))
malikagif.server = 'Destructoid User Gifs'

@base.cacofunc
async def carpgif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://i.imgur.com/lxVCMM0.gif") 	
carpgif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def sausage(message, client, *args, **kwargs):
	'''
	**/sausage**
	DADDY WOULD YOU LIKE SOME SAUSAGE
	'''
	await client.send_message(message.channel, "https://49.media.tumblr.com/ed7e70b598398e49059d0fe7d48ee4eb/tumblr_n81xzfeJKB1re0c97o1_500.gif") 	


	
@base.cacofunc
async def stridergif(message, client, *args, **kwargs):
	await client.send_message(message.channel, "http://24.media.tumblr.com/2f8fea08a9e62dbd9e44a34744a85b24/tumblr_mldjraj2fI1qbaj5no1_400.gif") 	
stridergif.server = 'Destructoid User Gifs'
	
@base.cacofunc
async def carp(message, client, *args, **kwargs):
	'''
	**/carp**
	***SARCASM INTENSIFIES***
	'''
	await client.send_message(message.channel, "Carp asked for a command, now he has one, isn't it spectacular?") 
carp.server = 'Destructoid Users'	

@base.cacofunc
async def sarah(message, client, *args, **kwargs):
	'''
	**/sarah**
	'''
	await client.send_message(message.channel, "In the bin!") 
sarah.server = 'Destructoid Users'	

@base.cacofunc
async def saywordgif(message, client, *args, **kwargs):
	'''
	**/saywordgif**
	***He likes baseball, AND IS A TROLL***
	'''
	await client.send_message(message.channel, "http://24.media.tumblr.com/6380b2fab5a5930266b300a9ef191220/tumblr_mllwih5zFW1sou5ubo1_400.gif") 
saywordgif.server = 'Destructoid User Gifs'	

@base.cacofunc
async def cwgif(message, client, *args, **kwargs):
	'''
	**/cwgif**
	'''
	await client.send_message(message.channel, "http://i.imgur.com/0tykmxD.gif") 
cwgif.server = 'Destructoid User Gifs'	

@base.cacofunc
async def clap(message, client, *args, **kwargs):
	'''
	**/clap**
	CLAP CLAP CLAP CLAP
	'''
	await client.send_message(message.channel, "http://vignette2.wikia.nocookie.net/aceattorney/images/8/8c/Gant_Breakdown_2.gif") 
	
@base.cacofunc
async def words(message, client, *args, **kwargs):
	'''
	**/words**
	Welcome to the Goodburger, home of the Goodburger, can I take your order?
	'''
	await client.send_message(message.channel, "https://giant.gfycat.com/UnitedImpureAlaskajingle.gif") 
	
	
@base.cacofunc
async def sexy(message, client, *args, **kwargs):
	'''
	**/sexy**
	Shake dat ass, watch yo'self, shake dat ass, show me what your workin' with
	'''
	await client.send_message(message.channel, "http://66.media.tumblr.com/a24f821c1222cf6168ebf3de931a9531/tumblr_o120r0jmvy1v19iiro1_1280.gif") 
	
@base.cacofunc
async def dick(message, client, *args, **kwargs):
	'''
	**/dick**
	rock out with your cock out
	'''
	await client.send_message(message.channel, "http://i.imgur.com/P31JJbO.gif") 
	
@base.cacofunc
async def youths(message, client, *args, **kwargs):
	'''
	**/youths**
	Larx, don't say I never did anything for ya
	'''
	await client.send_message(message.channel, "https://s-media-cache-ak0.pinimg.com/736x/89/ae/5a/89ae5a801f74cef72aa038e095f438ea.jpg")

	
@base.cacofunc
async def malika(message, client, *args, **kwargs):
	'''
	**/malika**
	***SIR MIX-A-LOT APPROVED!***
	'''
	await client.send_message(message.channel, "I'm a sexy ass bitch") 
malika.server = 'Destructoid Users'	


@base.cacofunc
async def holdit(message, client, *args, **kwargs):
	'''
	**/holdit**
	The one who actually commited the crime... WAS YOU!
	'''
	await client.send_message(message.channel, "http://i.imgur.com/aY8N9Qq.png") 

@base.cacofunc
async def objection(message, client, *args, **kwargs):
	'''
	**/objection**
	No alibi, no justice, no dreams, no hope!
	'''
	await client.send_message(message.channel, "http://i.imgur.com/DJ1ZEft.png") 
	
@base.cacofunc
async def takethat(message, client, *args, **kwargs):
	'''
	**/takethat**
	It's time to pay for your crimes!
	'''
	await client.send_message(message.channel, "http://i.imgur.com/Ha0o02O.png") 
	
@base.cacofunc
async def fisting(message, client, *args, **kwargs):
	'''
	**/fisting**
	It's Roman Reigns, for anyone wondering
	'''
	await client.send_message(message.channel, "https://i.imgur.com/uGoAvgC.gif")

@base.cacofunc
async def ojousama(message, client, *args, **kwargs):
	choices = [
		'http://66.media.tumblr.com/5132ad30d5375606a1bd0b23433dd9b9/tumblr_o36qu0o44q1tw8np6o1_400.gif',
		'http://67.media.tumblr.com/ae35254710f68a622cb7adb5f1dcdbb1/tumblr_nuu29tmNVN1rlz9neo3_500.gif',
		'http://digilander.libero.it/nixarts/gif/sfkarin01%20laugh.gif',
		'https://cdn.discordapp.com/attachments/149664659916455936/184105258169925633/8facac463166456ca3509d1d6277511d.gif',
		'http://stream1.gifsoup.com/webroot/animatedgifs6/3809088_o.gif'
	]
	await client.send_message(message.channel,  'OOOH HO HO HO\n' + random.choice(choices))
	
@base.cacofunc
async def lewd(message, client, *args, **kwargs):
	await client.send_message(message.channel,  'http://i.imgur.com/eGaQiZp.gif')	
	
@base.cacofunc
async def hypnogif(message, client, *args, **kwargs):
	'''
	**/hypnogif**
	Concessions were made
	'''
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/197129753176571904/205416548007936000/tumblr_nc36lvmUsK1r5c02zo1_400.gif") 
hypnogif.server = 'Destructoid User Gifs'

@base.cacofunc
async def hypnooogif(message, client, *args, **kwargs):
	'''
	**/hypnooogif**
	STORY TIME!
	'''
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/197129753176571904/197388795945943052/tumblr_mjlclk98IZ1qczlqfo1_400.gif") 
hypnooogif.server = 'Destructoid User Gifs'

@base.cacofunc
async def ohyes(message, client, *args, **kwargs):
	'''
	**/ohyes**
	I feel like this could also be labeled "nekrogif"
	'''
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/170002524156329984/208349912436310016/kA8Gg8n.gif") 

@base.cacofunc
async def mfw(message, client, *args, **kwargs):
	'''
	**/mfw**
	Everything is fine
	Gif of the "IS Rock Music Evil" guy with gun
	'''
	choices = ['http://i.imgur.com/9T1kgIr.gif']
	await client.send_message(message.channel, random.choice(choices)) 

@base.cacofunc
async def gto(message, client, *args, **kwargs):
	'''
	**/gto**
	NOT MY VESPA
	
	'''
	await client.send_message(message.channel, "http://giant.gfycat.com/DelightfulUncomfortableCrossbill.gif") 	
	

# @base.cacofunc
# async def cmd_id(self, author, user_mentions):
		# """
		# Usage:
			# {command_prefix}id [@user]

		# Tells the user their id or the id of another user.
		# """
		# if not user_mentions:
			# return Response('your id is `%s`' % author.id, reply=True, delete_after=35)
		# else:
			# usr = user_mentions[0]
			# return Response("%s's id is `%s`" % (usr.name, usr.id), reply=True, delete_after=35)
			
@base.cacofunc
async def id(message, client, inv_position, *args, **kwargs):
	'''
	Usage:
	{command_prefix}id [@user]
	Tells the user their id or the id of another user.
	'''
	if inv_position != 0:
		await client.send_message(message.channel, "Unfortunately, this command does not work unless placed at the beginning of the message")
	else:
	
		#Perhaps I should be using "Member" - This is a subclass of User that extends more functionality that server members have such as roles and permissions.
		usr = None
		temp = message.content.split()
		if len(temp) == 1:
			usr = message.author
			#await client.send_message(message.channel, "```Name: " + usr.name + "\nDiscriminator: " + usr.discriminator + "\nID: " + usr.id  + "\nCreated at: " + str(usr.created_at) + "\nAvatar:```\n" + usr.avatar_url)
		else:
			print(temp[1])
			x = (temp[1])[2:-1]
			if(x.startswith('!')):
				x = x[1:]
			print(x)
			usr = message.server.get_member(x)
		await client.send_message(message.channel, "```Name: " + usr.name + "\nDiscriminator: " + usr.discriminator + "\nID: " + usr.id  + "\nCreated at: " + str(usr.created_at) + "\nAvatar:```" + usr.avatar_url)



@base.cacofunc
async def novagif(message, client, *args, **kwargs):
	'''
	**/novagif**
	He and I have similarly structured names and I respect him for that.
	'''
	await client.send_message(message.channel, "http://33.media.tumblr.com/e7b29785b128967b84cd9b78455ffaf5/tumblr_nusvovjD8D1so18vqo1_1280.gif") 
novagif.server = 'Destructoid User Gifs'

@base.cacofunc
async def played(message, client, *args, **kwargs):
	'''
	**/played**
	I think other than this GIF we're supposed to hate this guy.
	'''
	await client.send_message(message.channel, "https://media.giphy.com/media/zNXvBiNNcrjDW/giphy.gif") 

@base.cacofunc
async def moe(message, client, *args, **kwargs):
	'''
	**/moe**
	MOE~
	'''
	await client.send_message(message.channel, "https://66.media.tumblr.com/95d9c4e7aa5e56dd81d70129079adf4a/tumblr_n4e8xzdIk91s12v80o1_500.gif") 

@base.cacofunc
async def longjohngif(message, client, *args, **kwargs):
	'''
	**/longjohngif**
	'''
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/197507359432507392/197507561572925441/brando.gif") 
	
@base.cacofunc
async def thesister(message, client, *args, **kwargs):
	'''
	**/thesister**
	Hypno is banned from storytime
	'''
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/197129753176571904/197767361611300874/626.gif") 
	
@base.cacofunc
async def lordxgif(message, client, *args, **kwargs):
	'''
	**/lordxgif**
	'''
	await client.send_message(message.channel, "http://img.pandawhale.com/158770-dave-chappelle-samuel-jackson-FSq5.gif") 

@base.cacofunc
async def why(message, client, *args, **kwargs):
	'''
	**/why**
	'''
	await client.send_message(message.channel, "https://media.giphy.com/media/ePeHKwWSed0Ag/giphy.gif") 

@base.cacofunc
async def linkslayersbigdicktriggering2electricboogaloobitches(message, client, *args, **kwargs):
	'''
	**not typing that shit out again.**
	'''
	await client.send_message(message.channel, "http://i.imgur.com/Xd2VdR5.gif \n http://i.imgur.com/mgdZ5oW.gif") 
	
@base.cacofunc
async def peeping(message, client, *args, **kwargs):
	'''
	**/peeping**
	Tommy, how's the peeping?
	'''
	await client.send_message(message.channel, "https://www.youtube.com/watch?v=DBzYSA0jfOw") 
	
@base.cacofunc
async def hellmo(message, client, *args, **kwargs):
	'''
	**/hellmo**
	https://i.imgur.com/OpFcp.jpg
	'''
	await client.send_message(message.channel, "https://media.giphy.com/media/yr7n0u3qzO9nG/giphy.gif") 
	
@base.cacofunc
async def whoopwhoop(message, client, *args, **kwargs):
	'''
	**/whoopwhoop**
	https://www.madewithpizza.com/n1hjqtcs
	'''
	await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/206857689177784320/208640892129509376/giphy_7.gif \n https://www.madewithpizza.com/n1hjqtcs") 
	
@base.cacofunc
async def disappointed(message, client, *args, **kwargs):
	'''
	**/disappointed**
	No, he did not read the line incorrectly, he was actually referencing a Fish Named Wanda
	'''
	await client.send_message(message.channel, "http://i.imgur.com/26k9Td7.gif?noredirect") 
	
@base.cacofunc
async def sits(message, client, *args, **kwargs):
	'''
	**/sits**
	Outputs an image of sitting patiently
	'''
	await client.send_message(message.channel, "http://67.media.tumblr.com/7437ac37a50fd8ea2608d27bbc968302/tumblr_o9w690LK5U1s667kio5_1280.png") 

@base.cacofunc
async def amnagif(message, client, *args, **kwargs):
	'''
	**/amnagif**
	http://imagesmtv-a.akamaihd.net/uri/mgid:file:http:shared:mtv.com/news/wp-content/uploads/2015/06/hannibal2.12-eat-the-rude1-1433433246.gif?quality=.8&height=300&width=500
	'''
	await client.send_message(message.channel, "http://66.media.tumblr.com/5c106810f733246822de1c8a7c2ab5ec/tumblr_mr10rq0STn1re3x32o1_500.gif") 
amnagif.server = 'Destructoid User Gifs'

@base.cacofunc
async def mad(message, client, *args, **kwargs):
	'''
	HOW MAD ARE YOU?
	'''
	choices = [
		'http://i3.kym-cdn.com/photos/images/newsfeed/000/880/564/687.jpg',
		'http://i0.kym-cdn.com/photos/images/newsfeed/000/707/020/ba1.jpg'
	]
	await client.send_message(message.channel, random.choice(choices))

	
@base.cacofunc
async def gotime(message, client, *args, **kwargs):
	'''
	FINGERNAILS FINGERNAILS FINGERNAILS
	'''
	
	await client.send_message(message.channel, 'https://24.media.tumblr.com/tumblr_m5jfp0Cp2P1rx632yo1_500.gif')

@base.cacofunc
async def riogif(message, client, *args, **kwargs):
	'''
	
	'''
	
	await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/213791117521453056/213791380844052481/C3KiBJJ.gif')
	
	
@base.cacofunc 
async def mango(message, client, inv_position, *args, **kwargs):
	'''
	**/mango** [-s] <search terms>
	Searches for and displays an manga matching your search terms
	specify -s to bring up a list of manga matching the terms you specified, maximium of 10
	'''
	if inv_position != 0:
		await client.send_message(message.channel, "Unfortunately, this command does not work unless placed at the beginning of the message")
	else:
		try:
			params = message.content.split(' ',1)
		
			if len(params) == 1:
				await client.send_message(message.channel, '{}:  Give me a manga to search for, Baka!'.format(message.author.mention))
			else:
				values = {'grant_type' : 'client_credentials','client_id' : 'kwoth-w0ki9','client_secret' : 'Qd6j4FIAi1ZK6Pc7N7V4Z'}
				r = requests.post('http://anilist.co/api/auth/access_token', params = values)
				authy = {'access_token' : r.json()['access_token']}
				if(params[1].startswith('-s ')):
					params2 = params[1].split(' ', 1)
					search = requests.get('http://anilist.co/api/manga/search/' + params2[1], params = authy)
					search_results = search.json()
					blah = 'Search Results:\n'
					counter = 0
					for i in search_results:
						counter += 1
						blah = blah + '\n' + i['title_english']
						if( counter >= 10):
							blah = blah + '\n**Search limited to 10 results**'
							break
					await client.send_message(message.channel, blah)
				else:

					#search_word = urllib.parse.quote(params[1], safe='')
					search = requests.get('http://anilist.co/api/manga/search/' + params[1], params = authy)
					manga = requests.get('http://anilist.co/api/manga/' + str(search.json()[0]['id']), params = authy)
				
					await client.send_message(message.channel, 'Title: ' + manga.json()['title_english'] +
					'\nSynopsis: ' + manga.json()['description'] +
					'\nImage: ' + manga.json()['image_url_lge'])
		except(IndexError, ValueError):
			# user did not format command correctly
			await client.send_message(message.channel, '{}: you did something wrong, scallywag!'.format(message.author.mention))
				
@base.cacofunc 
async def animu(message, client, inv_position, *args, **kwargs):
	'''
	**/animu** [-s] <search terms>
	Searches for and displays an anime matching your search terms
	specify -s to bring up a list of anime matching the terms you specified, maximium of 10
	'''
	if inv_position != 0:
		await client.send_message(message.channel, "Unfortunately, this command does not work unless placed at the beginning of the message")
	else:
		try:
			params = message.content.split(' ',1)
			if len(params) == 1:
				await client.send_message(message.channel, '{}: Give me an anime to search for, Baka!'.format(message.author.mention))
			else:
				values = {'grant_type' : 'client_credentials','client_id' : 'kwoth-w0ki9','client_secret' : 'Qd6j4FIAi1ZK6Pc7N7V4Z'}
				r = requests.post('http://anilist.co/api/auth/access_token', params = values)
				authy = {'access_token' : r.json()['access_token']}
				
				if(params[1].startswith('-s ')):
					params2 = params[1].split(' ', 1)
					search = requests.get('http://anilist.co/api/anime/search/' + params2[1], params = authy)
					search_results = search.json()
					blah = 'Search Results:\n'
					counter = 0
					for i in search_results:
						counter += 1
						blah = blah + '\n' + i['title_english']
						if( counter >= 10):
							blah = blah + '\n**Search limited to 10 results**'
							break
					await client.send_message(message.channel, blah)
				else:

					#search_word = urllib.parse.quote(params[1], safe='')
					search = requests.get('http://anilist.co/api/anime/search/' + params[1], params = authy)
					manga = requests.get('http://anilist.co/api/anime/' + str(search.json()[0]['id']), params = authy)
				
					await client.send_message(message.channel, 'Title: ' + manga.json()['title_english'] +
					'\nSynopsis: ' + manga.json()['description'] +
					'\nImage: ' + manga.json()['image_url_lge'])
					#await client.send_message(message.channel, '{}: shouldve worked buddy boy')	
					#url = 'http://anilist.co/api/auth/access_token'
					#values = {'grant_type' : 'client_credentials','client_id' : 'kwoth-w0ki9','client_secret' : 'Qd6j4FIAi1ZK6Pc7N7V4Z'}
					#data urllib.parse.urlencode(values)
					#data = data.encode('ascii')
					#req = urllib.request.Request(url, data)
					#response = urllib.request.urlopen
					##with urllib.request.urlopen(req) as response:
					##	the_page = response.read()
		except(IndexError, ValueError):
			# user did not format command correctly
			await client.send_message(message.channel, '{}: you did something wrong, scallywag!'.format(message.author.mention))
			
		
@base.cacofunc
async def punch(message, client, inv_position, *args, **kwargs):
	'''
	**/punch** [key]
	Summons a mighty punch
	enter a key value to choose a specific punch
	Otherwise the bot will choos a punch of its own
	Enter "list" to bring up a list of available keys
	'''
	if inv_position != 0:
		await client.send_message(message.channel, "Unfortunately, this command does not work unless placed at the beginning of the message")
	else:
		fists = {'opm': 'http://i.kinja-img.com/gawker-media/image/upload/s--Anmc5Oq9--/jcc53xkcdkbezhceppdr.gif', 
		'bigo': 'http://38.media.tumblr.com/214d6fbdfbfd7a2233d4028caa01520f/tumblr_n5eeiiJ9x81rjxyrgo6_400.gif', 
		'falcon': 'http://i.makeagif.com/media/5-19-2015/YUluSx.gif',
		'ganon': 'http://i3.kym-cdn.com/photos/images/original/000/904/522/120.gif',
		'mac': 'http://i.imgur.com/UGt5sRt.gif',
		'megas': 'http://i1.kym-cdn.com/photos/images/newsfeed/000/465/380/5d8.gif',
		'dad': 'https://cdn.discordapp.com/attachments/135186576195059714/180519465186885633/uFTy1Ya.gif',
		'baseball': 'https://media.giphy.com/media/pcina0qsiPeWQ/giphy.gif',
		'line': 'http://i2.kym-cdn.com/photos/images/newsfeed/000/963/928/890.gif',
		'doom': 'https://media.giphy.com/media/m6l7DZpo2au88/giphy.gif',
		'rocket': 'http://45.media.tumblr.com/2928e619bc2ba93b4a56a939c70aaed5/tumblr_n3hgkhxB3R1rzkxhio2_400.gif',
		'working': 'https://media1.giphy.com/media/OK5O2ww3MA2XK/giphy.gif',
		'tv': 'https://cdn.discordapp.com/attachments/135186576195059714/197572353058668545/falconpunch.gif',
		'wimp': 'https://cdn.discordapp.com/attachments/197129753176571904/205416392537800725/tumblr_o63j8m8vGe1r7jzano1_500.gif',
		'self': 'https://cdn.discordapp.com/attachments/164576366883241984/205930317972766721/ed-nortan-punching.gif',
		'getoverhere': 'https://images-ext-2.discordapp.net/.eJyrViotylGyUsooKSmw0tcvyMzTS8zLzE3VS87P1S8v0E3OzytJzSvRLy3IyU9MKdY3MjA01Tcw1w_JSNV1ykzX9dcN8XDVVXU1VrUwVrU0hjIsIAwjVScDKMPRESrl5KwLsiCxJDVFNz0zTddYD0gq1QIAElcnCQ.C74yznHsfpzTuig29I6mcbed1Kk.gif',
		'getout': 'https://discordcdn.com/attachments/165134518561275905/209820533682995200/ezgif.com-video-to-gif.gif',
		'shinobu': 'https://cdn.discordapp.com/attachments/165134518561275905/260570807380606976/tumblr_mvb79z1xt31rpxpqbo1_500.gif'}
		c = random.choice(list(fists.keys()))
		try:
			params = message.content.split()
			if len(params) == 1:
				out = fists[c]
			else:
				if(params[1] == 'list' or params[1] == 'help' or params[1] == 'commands'):
					out = "Available punches: "
					out += str(list(fists.keys())).strip('[]')
				else:
					#article = (params[1] - 1)
					out = fists[params[1].lower()]
			await client.send_message(message.channel, out)
		except(IndexError, ValueError):
			await client.send_message(message.channel, '{}: you did something wrong, scallywag!')
			
@base.cacofunc
async def jontron(message, client, inv_position, *args, **kwargs):
	'''
	**/jontron** [key] [LIST]
	Summons a mighty jontron
	enter a key value to choose a specific jontron
	Otherwise the bot will choose a jontron of its own
	Enter "list" to bring up a list of available keys
	'''
	if inv_position != 0:
		await client.send_message(message.channel, "Unfortunately, this command does not work unless placed at the beginning of the message")
	else:
		ech = {'getit': 'https://cdn.discordapp.com/attachments/135186576195059714/183998364281602049/get-3.gif', 
		'cheated': 'https://cdn.discordapp.com/attachments/135186576195059714/183999086406402049/JollyHoarseFeline-size_restricted.gif', 
		'no': 'http://i.imgur.com/QoE4eEf.gif',
		'what': 'http://i.imgur.com/nKkwXJf.gif',
		'questions': 'http://i.imgur.com/wo5nFRY.gif',
		'farout': 'http://i.imgur.com/yFhgQXo.gif',
		'confetti': 'https://media.giphy.com/media/3oEduMA8EK8uf6zvHO/giphy.gif',
		'best': 'https://camo.derpicdn.net/2dcf0d8a23115cb209fcd9ca0af1de3bfaa6e788?url=http%3A%2F%2Fimages6.fanpop.com%2Fimage%2Fphotos%2F36700000%2FJonTron-image-jontron-36778399-500-282.gif',
		'food': 'http://i0.kym-cdn.com/photos/images/original/000/815/304/6f3.gif',
		'yeah': 'http://i.imgur.com/gqHmXE1.gif',
		'sinners': 'http://media.giphy.com/media/2UKdzTBok1yDe/giphy.gif',
		'complaint': 'http://67.media.tumblr.com/bfeecd85e87ee73f43844ee896cc5a69/tumblr_o75pxhUbLW1ug9uz6o1_400.gif',
		'favorite': 'http://38.media.tumblr.com/f19afb46d8dfec70fe62986e5fdf58d2/tumblr_nchlm993HW1tbqxclo1_400.gif',
		'ohmygod': 'http://25.media.tumblr.com/741f43143485270a6e614d831d024e8d/tumblr_n2b588K8Fw1rse905o1_500.gif',
		'notbrave': 'https://33.media.tumblr.com/f0b98c4b59b3287d16cc022cb2add7e9/tumblr_np3tuoHNV81suf5t1o2_500.gif',
		'braveboy': 'http://m.imgur.com/DpTpTY6',
		'stop': 'http://i.imgur.com/1TdHj1y.gif',
		'beautiful': 'https://cdn.discordapp.com/attachments/135186576195059714/197569992848310273/tumblr_mwuvg7c8Kf1s45fabo1_500.gif',
		'conker': 'https://cdn.discordapp.com/attachments/135186576195059714/197575329286455297/MedicalFortunateGrunion.gif',
		'mistake': 'http://i.imgur.com/Ab5la0F.gif',
		'nroc': 'http://i.imgur.com/onNId4b.gif',
		'vapors': 'https://38.media.tumblr.com/326aaf28f6728e57c67222101f43d364/tumblr_naj1ifSy3W1s445ico1_400.gif'}
		c = random.choice(list(ech.keys()))
		try:
			params = message.content.split()
			if len(params) == 1:
				
				out = ech[c]
			else:
				if(params[1] == 'list' or params[1] == 'help' or params[1] == 'commands'):
					out = "Available gifs: "
					out += str(list(ech.keys())).strip('[]')
				else:
					#article = (params[1] - 1)
					out = ech[params[1].lower()]
			await client.send_message(message.channel, out)
		except(IndexError, ValueError):
			await client.send_message(message.channel, '{}: ECH!')