import subprocess
from time import sleep

from sourse import settings


def main():
    sleep_time = 3600

    try:
        while True:
            subprocess.run(['python', settings.MAIN_PATH])
            sleep(sleep_time)
    except KeyboardInterrupt:
        print("Вы остановили процесс")


if __name__ == '__main__':
    main()
