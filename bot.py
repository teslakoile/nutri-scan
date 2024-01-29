import os

import discord
from dotenv import load_dotenv

from vision_ai import get_nutritional_estimate

intents = discord.Intents.default()

intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
print(token)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        if message.attachments:
            if len(message.attachments) == 1:
                attachment = message.attachments[0]
                filename = attachment.filename.lower()
                if filename.endswith(("jpg", "jpeg", "png", "gif", "bmp")):
                    image_url = attachment.url
                    nutritional_info = get_nutritional_estimate(image_url)
                    await message.reply(nutritional_info)
                else:
                    await message.reply(
                        "Please send an image in a proper format (jpg, jpeg, png, gif, bmp)."
                    )
            elif len(message.attachments) > 1:
                await message.reply("Send only 1 image attachment")
        else:
            await message.reply("No image attached")


client.run(token)
