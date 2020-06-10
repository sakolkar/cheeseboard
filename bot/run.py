from twitchio.ext import commands
import os
import logging
import sys
from logic import Logic


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            irc_token=os.environ['TWITCH_IRC_TOKEN'],
            client_id=os.environ['TWITCH_CLIENT_ID'],
            nick='CheeseBoard_Bot',
            prefix='!',
            initial_channels=list(os.environ['TWITCH_CHANNELS'].split(',')))

    async def event_ready(self):
        logger.info(f'Ready | {self.nick}')

    async def event_message(self, message):
        await self.handle_commands(message)

    @commands.command(name='cheeseboard')
    async def cheeseboard(self, ctx):
        await ctx.send('Pick your top two all-time favourite clips of Cheesewiz. '
                       'Check out !submithelp to see how to make a submission. '
                       'Take a look at all the submissions here: '
                       'https://cheeseboard.satyen.dev')

    @commands.command(name='submithelp')
    async def submit_help(self, ctx):
        await ctx.send('You can submit up to two of your all-time favourite '
                       'clips. Do "!submit clip_link" to set only one clip or '
                       'do "!submit clip1 clip2" for both at the same time. '
                       'You can resubmit to change your picks. If you cant '
                       'post links, you can use the clip slug. Ex: "!submit '
                       'PeacefulGiantGrasshopperAMPEnergyCherry"')

    @commands.command(name='submit')
    async def submit_cmd(self, ctx):
        if Logic.submission(message=ctx.message, logger=logger):
            await ctx.send(f'{Logic.randstr()} | '
                           f'Thanks {ctx.author.tags["display-name"]}! '
                            'Your clips have been submitted.')
        else:
            await ctx.send(f'{Logic.randstr()} | '
                           f'Sorry {ctx.author.tags["display-name"]}, '
                            'that submission failed. Use !submithelp to '
                            'see how to format the submission')


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
sys.stderr = sys.stdout
bot = Bot()
bot.run()
