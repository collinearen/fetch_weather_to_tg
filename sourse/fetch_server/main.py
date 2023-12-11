import subprocess
from time import sleep

from sourse import settings


def main():
    sleep_time = 3600

    try:
        subprocess.run(['python', settings.BOT_PATH])

        while True:
            subprocess.run(['python', settings.COLLECTOR_PATH])

            sleep(sleep_time)
    except KeyboardInterrupt:
        print("Вы остановили процесс")


if __name__ == '__main__':
    main()
