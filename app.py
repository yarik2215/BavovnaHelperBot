import os
from pyrogram import Client, filters

# Welcome message template
MESSAGE = """Hello from BAVOVNA TEAM ✋
FAQ группа з питаннями та відповідями (https://t.me/FAQYOU)

Форми замовлення старлінку:
    ЦИВІЛЬНА (https://forms.gle/AZFuj16HWwurJzWM9)
    ВІЙСЬКОВА (https://forms.gle/Hk6vdsZ3mTT7jBdV9)

Підтримати команду (https://send.monobank.ua/jar/5FHk8pEfDG)
"""

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

app = Client("BavovnaHelperBot", api_id=api_id, api_hash=api_hash)

# Filter in only new_chat_members updates generated in TARGET chat
@app.on_message(filters.new_chat_members)
async def welcome(client, message):
    for u in message.new_chat_members:
        await client.send_message(chat_id=u.id, text=MESSAGE)


app.run()  # Automatically start() and idle()
