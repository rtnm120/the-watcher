import os
import datetime
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import check_status

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
channel_id = int(os.getenv("CHANNEL_ID"))
guild_id = discord.Object(os.getenv("GUILD_ID"))
role_id = f"<@&{os.getenv("ROLE_ID")}>"

time = datetime.time(hour=7, minute=0)

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="/", intents=intents)

    async def on_ready(self):
        synced = await self.tree.sync(guild=guild_id)

        print(f"Logged on as {self.user}")
        self.check_day.start()

    @tasks.loop(time=time)
    async def check_day(self):
        current_day = datetime.date.weekday(datetime.date.today())

        if current_day == 3:
            self.run_check.start()

    @tasks.loop(minutes=5)
    async def run_check(self):
        channel = self.get_channel(channel_id)

        if check_status.check_status() == "online":
            await channel.send(f"{role_id}\nMaintenance has concluded\nThaemine is now online")
            self.run_check.cancel()

bot = Bot()

@bot.tree.command(name="monitor", description="Monitor server status during emergency maintenance", guild=guild_id)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Now monitoring server status", ephemeral=True)
    bot.run_check.start()

bot.run(bot_token)
