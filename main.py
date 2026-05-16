import datetime
import discord
from discord.ext import tasks
import os
from dotenv import load_dotenv
import check_status

load_dotenv()

token = os.getenv("TOKEN")
channel_id = int(os.getenv("CHANNEL_ID"))
time = datetime.time(hour=7, minute=5)

class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        print(f"Logged on as {self.user}")
        self.do_run_check = False
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
            await channel.send("Maintenance has finished.\nThaemine is back online")
            self.run_check.cancel()

client = Client()
client.run(token)
