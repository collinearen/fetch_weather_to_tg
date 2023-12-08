import datetime

from sqlalchemy import Column, Integer, String, MetaData, Table, DateTime

metadata = MetaData()

weather = Table("weather",
                metadata,
                Column("id", Integer, primary_key=True, nullable=False),
                Column("town", String, nullable=False),
                Column("temp", Integer, default=0),
                Column("time_stamp", DateTime(timezone=True), onupdate=datetime.datetime.now()),
                )
