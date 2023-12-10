import subprocess
from time import sleep

from sourse import settings


def main():
    sleep_time = 3600

    while True:
        subprocess.run(['python', settings.MAIN_PATH])
        sleep(sleep_time)


if __name__ == '__main__':
    main()
