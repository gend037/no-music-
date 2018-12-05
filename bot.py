import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random



BOT_PREFIX = ("")
TOKEN = "NTE5Nzc1MzIzMTA2MTgxMTQw.DukOUQ.Q_sgMp5ZojcFUBXiVXiagDUv4ME"

@bot.event
async def on_ready():
	print('시작!')

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
	
filter = ["fuck","hell","Token"]
	
for filter in filter:
    if filter in message:
        await bot.send_message(message.channel, "{}, your message has been censored.".format(message.author.mention))
        await bot.delete_message(message)




bot.run(TOKEN)
