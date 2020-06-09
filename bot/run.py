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

    @commands.command(name='submit')
    async def submit_cmd(self, ctx):
        if Logic.submission(message=ctx.message, logger=logger):
            await ctx.send(f'{Logic.randstr()} | Thanks {ctx.author.tags["display-name"]}! Your clips have been submitted.')
        else:
            await ctx.send(f'{Logic.randstr()} | Sorry {ctx.author.tags["display-name"]}, that submission failed.')


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
sys.stderr = sys.stdout
bot = Bot()
bot.run()
