
import random
import discord

from discord.ext.commands import Bot
from discord.voice_client import VoiceClient


startup_extensions = ["Music"]
BOT_PREFIX = ("")
TOKEN = "NDc3NDU3OTQyNzQwOTkyMDEx.DlAmXA.q5949JRoED9yZgIOEDT9vLPfb5o"
 

bot = Bot(command_prefix=BOT_PREFIX)
client = discord.Client()

@bot.event
async def on_ready():
	print('시작!')

class Main_Commands():
        def __init__(self, bot):
         self.bot = bot
        def setup(bot):
            bot.add_cog(Music(bot))
            print("Music is loaded")

@bot.command()
async def 냥이야():
    possible_responses = [
        '왜 불렀느냐',
        '왜 그러느냐',
        '무슨 문제있느냐',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 안녕():
    possible_responses = [
        '인사를 받아주겠느니라',
        '갑자기 인사를 왜 하는것이냐',
        '안녕하느냐',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 고마워():
    possible_responses = [
        '치...칭찬을 한다고..  내가 널 좋아할..것.. 같으냐..!.',
        '칭찬해준다고 아무것도 나오지 않느니라',
        '너 머리가 잘못된 것이냐 갑자기 이상한 말을 지껄이는 구나',
        '흥, 내가 잘했으니 당연히 칭찬을 받아야 하는 것이니라',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 놀아줘():
    possible_responses = [
        '그럴 시간에 우리 흰둥이나 신경쓰거라',
        '쯧 쯧 그러니 니가 머리가 나쁜것이니라',
        '귀찮느니라 혼자서 놀거라',
        '난 내 소중한 흰둥이랑 놀아줘야하니 귀찮게 하지 말거라',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 시발():
    possible_responses = [
        '이런 미친놈이',
        '욕 하면 죽인다',
        '경고임 ㅅㄱ',

    ]
    await bot.say(random.choice(possible_responses))

if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '{}: {}' .format(type(e).__name__, e)
                print('failed to load extension {}/n{}'.format(extension, exc))

        








bot.run(TOKEN)
