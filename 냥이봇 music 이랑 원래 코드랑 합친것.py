
import random
import discord
import asyncio
import discord
from discord.ext import commands
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')
     
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient


startup_extensions = ["Music"]
BOT_PREFIX = ("")
TOKEN = "NDUzNTIwOTUxODQ2NjMzNDcz.DfgF4g.CdyJtDRmJur-AjUXXMh-kOkufOs"
 

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

def __init__(self, bot):
        self.bot = bot

class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = ' {0.title} uploaded by {0.uploader} and requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()
class Music:
    """Voice related commands.
    Works in multiple servers at once.
    """
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx, *, channel : discord.Channel):
        """Joins a voice channel."""
        try:
            await self.create_voice_client(channel)
        except discord.ClientException:
            await self.bot.say('Already in a voice channel...')
        except discord.InvalidArgument:
            await self.bot.say('This is not a voice channel...')
        else:
            await self.bot.say('Ready to play audio in **' + channel.name)

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):
        """Summons the bot to join your voice channel."""
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            await self.bot.say('왜 들어와있지 않은것이냐?')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    @commands.command(pass_context=True, no_pm=True)
    async def 냥이야(self, ctx, *, song : str):
        """Plays a song.
        If there is a song currently in the queue, then it is
        queued until the next song is done playing.
        This command automatically searches as well from YouTube.
        The list of supported sites can be found here:
        https://rg3.github.io/youtube-dl/supportedsites.html
        """
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await ctx.invoke(self.summon)
            await self.bot.say("불러오는 중이니라")
            if not success:
                return

        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            await self.bot.say('Enqueued ' + str(entry))
            await state.songs.put(entry)

    @commands.command(pass_context=True, no_pm=True)
    async def volume(self, ctx, value : int):
        """Sets the volume of the currently playing song."""

        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            await self.bot.say('Set the volume to {:.0%}'.format(player.volume))
    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        """Resumes the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(pass_context=True, no_pm=True)
    async def stop(self, ctx):
        """Stops playing audio and leaves the voice channel.
        This also clears the queue.
        """
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
            await self.bot.say("흥이 깨졌느니라")
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        """Vote to skip a song. The song requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            await self.bot.say('아무것도 틀고있지 않느니라')
            return

        voter = ctx.message.author
        if voter == state.current.requester:
            await self.bot.say('넘기겠느니라')
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            if total_votes >= 3:
                await self.bot.say('넘기겠느니라')
                state.skip()
            else:
                await self.bot.say('찬성에 한표 더 늘었느니라 [{}/3]'.format(total_votes))
        else:
            await self.bot.say('이미 투표하지 않았느냐')

    @commands.command(pass_context=True, no_pm=True)
    async def playing(self, ctx):
        """Shows info about the currently played song."""

        state = self.get_voice_state(ctx.message.server)
        if state.current is None:
            await self.bot.say('아무것도 하고 있지 않느니라')
        else:
            skip_count = len(state.skip_votes)
            await self.bot.say('이번 노래는 {} [skips: {}/3]'.format(state.current, skip_count))
            
def setup(bot):
    bot.add_cog(Music(bot))
    print('노래 틀 준비 끝났느니라')



if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '{}: {}' .format(type(e).__name__, e)
                print('failed to load extension {}/n{}'.format(extension, exc))

        








bot.run(TOKEN)
