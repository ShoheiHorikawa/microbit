from slack_sdk import WebClient

with open("token.txt", mode="r", encoding="utf-8") as f:
    SLACK_ACCESS_TOKEN = f.read()

client = WebClient(SLACK_ACCESS_TOKEN)
channnel_id = "C05BQEDEWJ2"

msg = "hello"
response = client.chat_postMessage(
    channel=channnel_id,
    text = msg
)