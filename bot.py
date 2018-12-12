import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
from discord.voice_client import VoiceClient
import asyncio

bot = commands.Bot("")
BOT_PREFIX = ("")
TOKEN = "NTE5Nzc1MzIzMTA2MTgxMTQw.DukOUQ.Q_sgMp5ZojcFUBXiVXiagDUv4ME"
channel = ctx.message.channel

@bot.event
async def on_ready():
	print('시작!')
	
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



	





bot.run(TOKEN)
