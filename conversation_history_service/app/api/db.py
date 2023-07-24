import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

conversations = Table(
    'conversations',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('question', String(250), index=True),
    Column('answer', String(250)),
    Column('timestamp', String(250)),
)

database = Database(DATABASE_URI)