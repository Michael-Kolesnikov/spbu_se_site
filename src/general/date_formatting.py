from datetime import datetime

def get_hours_since(date):
    time_diff = datetime.utcnow() - date
    return int(time_diff.total_seconds() / 3600)


def plural_hours(n):
    hours = ["час", "часа", "часов"]
    days = ["день", "дня", "дней"]

    if n > 24:
        n = int(n / 24)
        if n % 10 == 1 and n % 100 != 11:
            p = 0
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            p = 1
        else:
            p = 2

        return str(n) + " " + days[p]

    if n == 0:
        return "меньше часа"
    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2

    return str(n) + " " + hours[p]
