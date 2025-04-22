import os
import requests
import json

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USER_ID = os.getenv('USER_ID')
ALERT_WEBHOOK = os.getenv('ALERT_WEBHOOK')
BALLOON_WEBHOOK = os.getenv('BALLOON_WEBHOOK')
GATHER_WEBHOOK = os.getenv('GATHER_WEBHOOK')
TIME_GATHER_WEBHOOK = os.getenv('TIME_GATHER_WEBHOOK')

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.channel.id != 1058962316357554298:
        return
    
#alerts webhook
    if message.embeds and message.content == f'<@{USER_ID}>':
    # if message.embeds:
        for idx, embed in enumerate(message.embeds):
            # print(f"\n📦 Embed #{idx + 1} in message by {message.author}:")
            # print(f"Title: {embed.title}")
            # print(f"Description: {embed.description}")
            # print(f"URL: {embed.url}")
            # print(f"Fields: {[{'name': f.name, 'value': f.value} for f in embed.fields]}")
            # print(f"Footer: {embed.footer.text if embed.footer else None}")
            # print(f"Thumbnail: {embed.thumbnail.url if embed.thumbnail else None}")
            # print(f"Image: {embed.image.url if embed.image else None}")
            # print(f"Color: {embed.color}")

            payload = {
                "content": f"<@{USER_ID}>",
                "embeds": [
                    {
                        "title": embed.title,
                        "description": embed.description,
                        "fields": [{"name": field.name, "value": field.value} for field in embed.fields],
                        "footer": {"text": embed.footer.text} if embed.footer else None,
                        "thumbnail": {"url": embed.thumbnail.url} if embed.thumbnail else None,
                        "image": {"url": embed.image.url} if embed.image else None,
                        "color": embed.color.value if embed.color else None
                    }
                ]
            }

            try: 
                response = requests.post(ALERT_WEBHOOK, json=payload)
                response.raise_for_status()
                print('Webhook sent successfully!')
            except requests.exceptions.RequestException as e:   
                print(f'Error sending webhook: {e}')

        # print(message.content)

#balloon webhook
    if message.embeds:
        for idx, embed in enumerate(message.embeds):
            if 'Balloon' in embed.description:
                payload = {
                    "content": f"",
                    "embeds": [
                        {
                            "title": embed.title,
                            "description": embed.description,
                            "fields": [{"name": field.name, "value": field.value} for field in embed.fields],
                            "footer": {"text": embed.footer.text} if embed.footer else None,
                            "thumbnail": {"url": embed.thumbnail.url} if embed.thumbnail else None,
                            "image": {"url": embed.image.url} if embed.image else None,
                            "color": embed.color.value if embed.color else None
                        }
                    ]
                }

                try: 
                    response = requests.post(BALLOON_WEBHOOK, json=payload)
                    response.raise_for_status()
                    print('Webhook sent successfully!')
                except requests.exceptions.RequestException as e:   
                    print(f'Error sending webhook: {e}')

#gather webhook
    if message.embeds:
        for idx, embed in enumerate(message.embeds):
            if 'Gathering: Pine Tree' in embed.description:
                payload = {
                    "content": f"",
                    "embeds": [
                        {
                            "title": embed.title,
                            "description": embed.description,
                            "fields": [{"name": field.name, "value": field.value} for field in embed.fields],
                            "footer": {"text": embed.footer.text} if embed.footer else None,
                            "thumbnail": {"url": embed.thumbnail.url} if embed.thumbnail else None,
                            "image": {"url": embed.image.url} if embed.image else None,
                            "color": embed.color.value if embed.color else None
                        }
                    ]
                }

                try: 
                    response = requests.post(GATHER_WEBHOOK, json=payload)
                    response.raise_for_status()
                    print('Webhook sent successfully!')
                except requests.exceptions.RequestException as e:   
                    print(f'Error sending webhook: {e}')
     
#time gatgher webhook
    if message.embeds:
        for idx, embed in enumerate(message.embeds):
            if 'Gathering: Ended' in embed.description:
                if "Time Limit" in embed.description or "Bag Limit" in embed.description:
                    payload = {
                        "content": f"",
                        "embeds": [
                            {
                                "title": embed.title,
                                "description": embed.description,
                                "fields": [{"name": field.name, "value": field.value} for field in embed.fields],
                                "footer": {"text": embed.footer.text} if embed.footer else None,
                                "thumbnail": {"url": embed.thumbnail.url} if embed.thumbnail else None,
                                "image": {"url": embed.image.url} if embed.image else None,
                                "color": embed.color.value if embed.color else None
                            }
                        ]
                    }
    
                    try: 
                        response = requests.post(TIME_GATHER_WEBHOOK, json=payload)
                        response.raise_for_status()
                        print('Webhook sent successfully!')
                    except requests.exceptions.RequestException as e:   
                        print(f'Error sending webhook: {e}')
        


client.run(TOKEN)