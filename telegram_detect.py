import re
from telethon import TelegramClient, events
from code_redeem import run


# Replace 'API_ID' and 'API_HASH' with your values
api_id = "20753068"
api_hash = "f7c9303b0539cd30b00051fc1d811160"
# group_id = -1002356653947  # 1000xgem holder
group_id = "https://t.me/+xg3i-NbFfNVkMDU9"  # test

client = TelegramClient("anon", api_id, api_hash)

pattern = re.compile(
    r"\b[A-Z0-9]{4}\b"
)  # Match exactly 4 consecutive capital letters or digits
last_message_pattern = ""


@client.on(events.NewMessage(chats=group_id))
async def handler(event):
    global last_message_pattern

    message_text = event.message.message
    current_message_pattern = pattern.findall(message_text)

    if last_message_pattern and current_message_pattern:
        combined_pattern = "".join(last_message_pattern + current_message_pattern)
        print(f"Potential Code Found: {combined_pattern}")
        run(combined_pattern)
        # Reset the patterns after a successful run
        last_message_pattern = ""
    else:
        # Update the last message pattern
        last_message_pattern = (
            current_message_pattern if current_message_pattern else last_message_pattern
        )


client.start()
client.run_until_disconnected()
