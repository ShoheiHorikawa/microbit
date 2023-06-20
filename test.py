import serial
import time

ser = serial.Serial("COM3", 115200)
message = [
    "今はウェルカムですよ。",
    "集中しているので話しかけないでください。",
]
time_data = [0, 0]
current_condition = 100
start_time = time.time()
last_print_time = start_time

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
# 
        if current_condition != condition:
            current_condition = condition
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
