from datetime import datetime


def greeting(datetime: datetime):
    if 6 < datetime.time().hour < 12:
        return "Доброе утро"
    elif 12 <= datetime.time().hour < 18:
        return "Добрый день"
    elif 18 <= datetime.time().hour < 22:
        return "Добрый вечер"
    else:
        return "Добрый ночи"

if __name__ == "__main__":
    time_now = datetime.now()
    print(greeting(time_now))

