import subprocess
from time import sleep

if __name__ == '__main__':
    while True:
        subprocess.run(['python', "/Users/ya/Desktop/all/projects/dockertraining/souse/collector.py"])
        sleep(10)
