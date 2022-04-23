import math  # 올림을 위해 만든 함수


def parking_time(time):
    hour, min = time.split(':')
    return int(hour) * 60 + int(min)


def solution(fees, records):
    answer = []
    parking_lot = dict()

    return answer


fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]
