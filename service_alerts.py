import json
import os
from util import get_dom_from_xml
from sqlalchemy import create_engine

MYSQL_CONNECTION_STRING = os.environ['MYSQL_CONNECTION_STRING']
MTA_URL = 'http://web.mta.info/status/serviceStatus.txt'


def get_latest_id():
    conn = create_engine(MYSQL_CONNECTION_STRING).connect()
    latest_id = conn.execute('select max(id) from mta_feed').fetchall()[0][0]
    return latest_id


class MTAServiceAlerts(object):

    def __init__(self, id):
        self.conn = create_engine(MYSQL_CONNECTION_STRING).connect()
        self.feed = self.conn.execute('select * from mta_feed where id = {id}'.format(id=id)).fetchall()
        self.dom = get_dom_from_xml(self.feed[0][2])

    @property
    def service_alerts(self):
        return get_dom_from_xml(self.feed)

    @property
    def service(self):
        service = self.dom.getroot().getchildren()[0].getchildren()
        return service[0]

    @property
    def service_types(self):
        return self.service.getchildren()[2:]

    @property
    def service_alerts_json(self):
        return json.dumps(self.service_alerts_dict)

    @property
    def timestamp(self):
        self.timestamp_obj = self.service.getchildren()[1]
        return self.timestamp_obj

    @property
    def subway_dict(self):
        subway_obj = self.service_types[0]
        subway_dict = {}
        for line in subway_obj.getchildren():
            name = line.getchildren()[0].text
            subway_dict[name] = {}
            subway_dict[name]['status'] = line.getchildren()[1].text
            subway_dict[name]['text'] = line.getchildren()[2].text
            subway_dict[name]['date'] = line.getchildren()[3].text
            subway_dict[name]['time'] = line.getchildren()[4].text
        return subway_dict

    @property
    def bus_dict(self):
        bus_obj = self.service_types[1]
        bus_dict = {}
        for line in bus_obj.getchildren():
            name = line.getchildren()[0].text
            bus_dict[name] = {}
            bus_dict[name]['status'] = line.getchildren()[1].text
            bus_dict[name]['text'] = line.getchildren()[2].text
            bus_dict[name]['date'] = line.getchildren()[3].text
            bus_dict[name]['time'] = line.getchildren()[4].text
        return bus_dict

    @property
    def bt_dict(self):
        bt_obj = self.service_types[2]
        bt_dict = {}
        for line in bt_obj.getchildren():
            name = line.getchildren()[0].text
            bt_dict[name] = {}
            bt_dict[name]['status'] = line.getchildren()[1].text
            bt_dict[name]['text'] = line.getchildren()[2].text
            bt_dict[name]['date'] = line.getchildren()[3].text
            bt_dict[name]['time'] = line.getchildren()[4].text
        return bt_dict

    @property
    def lirr_dict(self):
        lirr_obj = self.service_types[3]
        lirr_dict = {}
        for line in lirr_obj.getchildren():
            name = line.getchildren()[0].text
            lirr_dict[name] = {}
            lirr_dict[name]['status'] = line.getchildren()[1].text
            lirr_dict[name]['text'] = line.getchildren()[2].text
            lirr_dict[name]['date'] = line.getchildren()[3].text
            lirr_dict[name]['time'] = line.getchildren()[4].text
        return lirr_dict

    @property
    def mn_dict(self):
        mn_obj = self.service_types[4]
        mn_dict = {}
        for line in mn_obj.getchildren():
            name = line.getchildren()[0].text
            mn_dict[name] = {}
            mn_dict[name]['status'] = line.getchildren()[1].text
            mn_dict[name]['text'] = line.getchildren()[2].text
            mn_dict[name]['date'] = line.getchildren()[3].text
            mn_dict[name]['time'] = line.getchildren()[4].text
        return mn_dict

    @property
    def service_alerts_dict(self):
        return {
            'timestamp': self.timestamp.text,
            'subways': self.subway_dict,
            'buses': self.bus_dict,
            'bt': self.bt_dict,
            'lirr': self.lirr_dict,
            'metro_north': self.mn_dict,
        }
