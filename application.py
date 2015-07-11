# -*- coding: utf-8 -*-
import requests
from datetime import datetime
from sqlalchemy import create_engine
from model import mta_feed
import os


MTA_FEED_URL = 'http://web.mta.info/status/serviceStatus.txt'
MYSQL_CONNECTION_STRING = os.environ['MYSQL_CONNECTION_STRING']


def get_mta_feed():
    scrape_time = datetime.now()
    res = requests.get(MTA_FEED_URL)
    res_unicode = res.text.encode('utf-8')
    mta_data = {
        'scrape_time': scrape_time,
        'feed': res_unicode
    }
    return mta_data


def insert_mta_feed(mta_data, conn):
    print 'Inserting MTA feed...'
    conn.execute(mta_feed.insert(values=mta_data))
    print 'Done!'


def mta_scraper_admin():
    engine = create_engine(MYSQL_CONNECTION_STRING)
    conn = engine.connect()
    mta_data = get_mta_feed()
    insert_mta_feed(mta_data, conn)
    conn.close()


if __name__ == '__main__':
    mta_scraper_admin()
