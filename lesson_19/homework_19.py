from datetime import datetime
import logging


logger = logging.getLogger("heartbeat")
logger.setLevel(logging.WARNING)

handler = logging.FileHandler("hb_test.log", mode="w", encoding="utf-8")
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)

def analyze_heartbeat(file_path, key):
    filtered_log = []
    with open(file_path, encoding="utf-8") as file:
        for line in file:
            if key in line:
                filtered_log.append(line)

    #print(len(filtered_log))

    #time_stamp = filtered_log[0][filtered_log[0].find("Timestamp ") + 10 : filtered_log[0].find("Timestamp ") + 10 + 8]
    #print(time_stamp)
    timestamps = []
    for item in filtered_log:
        time_str = item[item.find("Timestamp ") + 10 : item.find("Timestamp ") + 10 + 8]
        timestamps.append(datetime.strptime(time_str, "%H:%M:%S"))

    #print(timestamps[0] - timestamps[1])
    #print((timestamps[0] - timestamps[1]).total_seconds())


    for i in range(len(timestamps) - 1):
        difference = timestamps[i] - timestamps[i + 1]
        seconds = difference.total_seconds()
        current_time = timestamps[i].strftime("%H:%M:%S")
        next_time = timestamps[i + 1].strftime("%H:%M:%S")
        if 31 < seconds < 33:
            logger.warning(f"heartbeat {seconds} sec between {next_time} and {current_time}")
        elif seconds >= 33:
            logger.error(f"heartbeat {seconds} sec between {next_time} and {current_time}")

    return "hb_test.log"


analyze_heartbeat("hblog.txt", "Key TSTFEED0300|7E3E|0400")