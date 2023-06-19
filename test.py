import serial
import time

ser = serial.Serial("COM3", 115200)
message = [
    "今はウェルカムですよ。",
    "集中しているので話しかけないでください。",
]
time_data = [0, 0]
current_condition = 100
start_time = 0
end_time = 0
run_time = 0

def main():
    global current_condition, start_time, end_time, run_time

    while True:
        line = ser.readline()
        condition = line.strip().decode("utf-8")
        if condition == "":
            condition = 0
        else:
            condition = int(condition)

        print(message[condition])

        if current_condition != condition:
            if start_time != 0:
                end_time = time.time()
                run_time = end_time - start_time
                time_data[current_condition] += run_time
                print(time_data[current_condition])
            current_condition = condition
            run_time = 0
            start_time = time.time()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
