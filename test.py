import serial
import time
from slack_sdk import WebClient

ser = serial.Serial("COM3", 115200)
message = [
    "今はウェルカムですよ。",
    "集中しているので話しかけないでください。",
]
emoji = [
    ":thumbsup:",
    ":face_with_symbols_on_mouth:"
]
time_data = [0, 0]
current_condition = 100
start_time = time.time()
last_print_time = start_time

# with open("token.txt", mode="r", encoding="utf-8") as f:
#     SLACK_ACCESS_TOKEN = f.read()


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


def main():
    global current_condition, start_time, last_print_time

    while True:
        line = ser.readline()
        condition = line.strip().decode("utf-8").strip()
        if not condition.isdigit():
            condition = 1
        else:
            condition = int(condition)

        print(message[condition])

        if current_condition != condition:
            current_condition = condition
            status_text = message[current_condition]
            status_emoji = emoji[current_condition]
            # set_slack_status(SLACK_ACCESS_TOKEN, status_text, status_emoji)
            end_time = time.time()
            run_time = end_time - start_time
            time_data[current_condition] += run_time
            start_time = time.time()

        current_time = time.time()
        if current_time - last_print_time >= 30:
            current_condition = condition
            end_time = time.time()
            run_time = end_time - start_time
            time_data[current_condition] += run_time
            start_time = time.time()
            print(time_data)
            last_print_time = current_time


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
