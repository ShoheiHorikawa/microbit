from slack_sdk import WebClient

with open("token.txt", mode="r", encoding="utf-8") as f:
    SLACK_ACCESS_TOKEN = f.read()

client = WebClient(SLACK_ACCESS_TOKEN)
channnel_id = "D04QW3CUPMF"

msg = "hello"
response = client.users_profile_set(
    user="U04QARV2M2S",
    profile={
		"status_text": "riding a train",
		"status_emoji": ":train:",
		"status_expiration": 1532627506
}
)