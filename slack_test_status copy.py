import os
from slack_sdk import WebClient

with open("token.txt", mode="r", encoding="utf-8") as f:
    SLACK_ACCESS_TOKEN = f.read()

def set_slack_status(token, status_text, status_emoji):
    client = WebClient(token=token)

    profile = {
        "status_text": status_text,
        "status_emoji": status_emoji
    }

    try:
        response = client.users_profile_set(profile=profile)
        if response["ok"]:
            print("Slackのステータスを変更しました。")
        else:
            print("Slackのステータス変更に失敗しました。")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

# 以下は使用例です
status_text = "今は忙しいです"
status_emoji = ":hourglass_flowing_sand:"
set_slack_status(SLACK_ACCESS_TOKEN, status_text, status_emoji)
