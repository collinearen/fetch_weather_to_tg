from sqlalchemy import Column, Integer, String, MetaData, Table

metadata = MetaData()

weather = Table("weather",
                metadata,
                Column("id", Integer, primary_key=True, nullable=False),
                Column("town", String, nullable=False),
                Column("temp", String, nullable=False),
                Column("time_stamp", String, nullable=False),
                )
