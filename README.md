hello, two servers are implemented here - one is a weather collector using an API, the other provides this weather for a certain place at a certain time

(using a telegram bot and deferred functions in <a href="https://github.com/gawel/aiocron?ysclid=lq24qu7d78798047487">aiocron</a> (to visualize it somehow and be able to view it)

using <a href="https://docs.sqlalchemy.org/en/20/">SQLAlchemy</a> I created **two** entities - two tables without foreign keys
(in the Users table we put the user and by default empty rows "" in time_sending and town, which are ultimately updated as changes are made by the user

The engine, sessions and the requests themselves in the database are written **asynchronously** to get the maximum gain over time. Also, the API will fly in queries every certain time (as an asynchronously, which allows you to process all cities (their temperature) in less than one second, which allows you to quickly update the weather data

You can also try this code in action by launching it at yourself by adding your token Telegram bot, as well as the access key to the API (or use another API)
This is just a frame that allows you to work with API, put it in a database and visualize it, pulling it out

<img src="/Users/ya/Desktop/image.png"  width="650" height="800"></img>

I divided the entire program into 2 parts - Fetch_Server contains all the logic to update the weather in the database,
Telegram_weather contains all the logic for working with the user, to initialize the tablets you will need to in the ***Init*** folder, launch the Init_models file, which will delete the old tables (if available) and create new ones, as well as fill all available cities (stored in settings) with default values.
Previously, before the launch of ```main.py```, it will be necessary to create .env in which the paths to the script ```collector.py```, as well as other fields that are in settings will be stored

# **Installation**

### <p align="center">you need to download the project to your local computer</p>
```shell
git clone https://github.com/collinearen/fetch_weather_to_tg.git
```
### <p align="center">Next you need to create a virtual environment in Python and activate it</p>
```shell
python -m venv venv
```
### <p align="center">and activate her</p>

```shell
source venv/bin/activate
```
### <p align="center">Enter the following commands to upgrade pip and download all modules and libraries that were used (they are located in the ```reqirements.txt``` folder)</p>
```shell
pip install --upgrade pip
```

```shell
pip install requrements.txt
```
<p align="center"></p>
You also need to run make up. This file defines one service application named "db". It uses the "postgres:14.1-alpine" container image, which is a PostgreSQL version 14.1 database on a lightweight version of Alpine Linux. The database container will restart automatically when it stops or crashes, thanks to the "restart: always" setting. The "environment" section defines environment variables for configuring the database container. In this case, the ```
POSTGRES_USER```, ```POSTGRES_PASSWORD```, and ```POSTGRES_DB``` variables are set to define the PostgreSQL username, password, and database name, respectively. Port 5432 of the database container is proxied to port 5432 of the host so that the database can be accessed from external devices. A network named "custom" is also defined, which is used for communication between containers. In this case, the database container will be connected to this network. This file allows you to start the database container **PostgreSQL** data with specified parameters and settings within the application. 
```shell
make up
```

<p align="center"></p>
После этого запустить файл Init.py, чтобы инициализировать таблицы и заполнить weather дефолтными значениями, чтобы в дальнейшем их обновлять.

Создать .env и заполнить своими данными, которые требуются в ```
settings.py``` 

Перейти в папку **fetch_server** запустить ```main.py```(Который запускает ```collector.py``` каждые ***3600*** секунд (ровно один час), так же можно настроить под себя)

```shell
python main.py
```


<p align="center">Next, go to the telegram_weather folder and launch only the bot (enter your token this way)</p>

```shell
python server_tg.py
```


<p align="center">and run pending tasks (in our case, notifying users who have chosen a specific time at which it is convenient for them to receive weather messages)</p>

```shell
python schedule_message.py
```


# Examples of using
![[Pasted image 20231212131359.png]]