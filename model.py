# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Unicode, Integer, DateTime, create_engine, MetaData
import os


MYSQL_CONNECTION_STRING = os.environ['MYSQL_CONNECTION_STRING']


engine = create_engine(MYSQL_CONNECTION_STRING)
metadata = MetaData(bind=engine)


mta_feed = Table('mta_feed', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('scrape_time', DateTime),
                 Column('feed', Unicode(500000))
                 )


def setup_database():
    print 'Setting up database...'
    metadata.create_all()
    print 'Database all ready!'


def reset_database():
    print 'Deleting all database data...'
    metadata.drop_all()
    print 'All database data gone!'
