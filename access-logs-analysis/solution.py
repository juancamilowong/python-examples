from datetime import datetime
from collections import defaultdict
from typing import Dict

def calculate_connection_time(path: str) -> Dict[str, int]:
    date_format = "%Y-%m-%d %H:%M:%S"
    opened_sesions = {}
    total_time = defaultdict(int)

    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            data = line.split()
            date_str = f"{data[0]} {data[1]}"
            _user = data[2]
            action = data[3]

            timestamp = datetime.strptime(date_str, date_format)

            if action == "LOGIN":
                if _user not in opened_sesions:
                    opened_sesions[_user] = timestamp

            elif action == "LOGOUT":
                if _user in opened_sesions:
                    login_time = opened_sesions.pop(_user)
                    _time = timestamp - login_time
                    minutes = int(_time.total_seconds() // 60)
                    total_time[_user] += minutes

    for _user in opened_sesions.keys():
        if _user not in total_time:
            total_time[_user] = 0

    return dict(total_time)


result = calculate_connection_time("access.log")
print(result)
