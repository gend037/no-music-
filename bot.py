import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
from discord.voice_client import VoiceClient
import asyncio

bot = commands.Bot("")
BOT_PREFIX = ("")
TOKEN = "NTE5Nzc1MzIzMTA2MTgxMTQw.DukOUQ.Q_sgMp5ZojcFUBXiVXiagDUv4ME"


@bot.event
async def on_ready():
       print('시작!')
       await bot.change_presence(game=discord.Game(name='Geno37이랑 봇 코드 개발중'))
	
filter = ["fuck", "hell"]
	
@bot.event
async def on_message(message):
  if message.content in filter:
     await bot.delete_message(message)
     await bot.send_message(message.channel, "don't say that word man")

@bot.command()
async def hello():
    possible_responses = [
        'hi',
        'how are you?',
        'hi hi',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def blyat():
    possible_responses = [
        'cyka blyat',
        'omg',
        'hahaha',

    ]
    await bot.say(random.choice(possible_responses))


@bot.command()
async def cheeki_breeki():
    possible_responses = [
        'listen to stakler clear sky bandit radio',
        'soviet',
        'union',
        'omg',

    ]
    await bot.say(random.choice(possible_responses))
	
@bot.command()
async def embed():
    embed = discord.Embed(
    	title = 'Testing Embed',
	description = 'Just testing',
	color = discord.Color.blue()
    )

    embed.set_footer(text='What is footer?')
    embed.set_image(url='https://www.google.co.kr/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwil5aD-5pnfAhWEXbwKHVSEB9UQjRx6BAgBEAU&url=http%3A%2F%2Fblogs.bu.edu%2Fguidedhistory%2Fmoderneurope%2Fkatie-k-2%2F&psig=AOvVaw2S8ZwLcqM5Ea-SDy28WyJK&ust=1544687359148126')		    
    embed.set_thumbnail(url='https://www.google.co.kr/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwil5aD-5pnfAhWEXbwKHVSEB9UQjRx6BAgBEAU&url=http%3A%2F%2Fblogs.bu.edu%2Fguidedhistory%2Fmoderneurope%2Fkatie-k-2%2F&psig=AOvVaw2S8ZwLcqM5Ea-SDy28WyJK&ust=1544687359148126')



	





bot.run(TOKEN)
