import requests
from lxml import etree
import json
from StringIO import StringIO


def _get_text_from_url(url):
	res = requests.get(url)
	return res.text


def get_dom_from_xml(xml):
	parser = etree.HTMLParser()
	return etree.parse(StringIO(xml), parser)


class MTAServiceAlerts(object):

	def __init__(self):
		pass
	
	@property
	def service_alerts(self):
		self.MTA_URL = 'http://web.mta.info/status/serviceStatus.txt'
		self.url_text = _get_text_from_url(self.MTA_URL)
		return get_dom_from_xml(self.url_text)
		# self.service_alerts_json = json.dumps(self.service_alerts)

	@property
	def service(self):
		service = self.service_alerts.getroot().getchildren()[0].getchildren()
		return service[0]

	@property
	def service_types(self):
		return self.service.getchildren()[2:]

	@property
	def service_alerts_dict(self):
		return {
			'timestamp': TimeStamp().timestamp,
			'subways': Subways().subway_dict,
			'buses': Buses().bus_dict,
			'bt': BT().bt_dict,
			'lirr': LIRR().lirr_dict,
			'metro_north': MetroNorth().mn_dict,
		}

	@property
	def service_alerts_json(self):
		return json.dumps(self.service_alerts_dict)


class TimeStamp(MTAServiceAlerts):

	def __init__(self):
		self.timestamp_obj = self.service.getchildren()[1]

	@property
	def timestamp(self):
		return self.timestamp_obj.text

	def __str__(self):
		return self.timestamp_obj.text


class Subways(MTAServiceAlerts):

	def __init__(self):
		self.subway_obj = self.service_types[0]
		self.subway_dict = {}
		for line in self.subway_obj.getchildren():
			name = line.getchildren()[0].text
			self.subway_dict[name] = {}
			self.subway_dict[name]['status'] = line.getchildren()[1].text
			self.subway_dict[name]['text'] = line.getchildren()[2].text
			self.subway_dict[name]['date'] = line.getchildren()[3].text
			self.subway_dict[name]['time'] = line.getchildren()[4].text


class Buses(MTAServiceAlerts):

	def __init__(self):
		self.bus_obj = self.service_types[1]
		self.bus_dict = {}
		for line in self.bus_obj.getchildren():
			name = line.getchildren()[0].text
			self.bus_dict[name] = {}
			self.bus_dict[name]['status'] = line.getchildren()[1].text
			self.bus_dict[name]['text'] = line.getchildren()[2].text
			self.bus_dict[name]['date'] = line.getchildren()[3].text
			self.bus_dict[name]['time'] = line.getchildren()[4].text


class BT(MTAServiceAlerts):

	def __init__(self):
		self.bt_obj = self.service_types[2]
		self.bt_dict = {}
		for line in self.bt_obj.getchildren():
			name = line.getchildren()[0].text
			self.bt_dict[name] = {}
			self.bt_dict[name]['status'] = line.getchildren()[1].text
			self.bt_dict[name]['text'] = line.getchildren()[2].text
			self.bt_dict[name]['date'] = line.getchildren()[3].text
			self.bt_dict[name]['time'] = line.getchildren()[4].text


class LIRR(MTAServiceAlerts):

	def __init__(self):
		self.lirr_obj = self.service_types[3]
		self.lirr_dict = {}
		for line in self.lirr_obj.getchildren():
			name = line.getchildren()[0].text
			self.lirr_dict[name] = {}
			self.lirr_dict[name]['status'] = line.getchildren()[1].text
			self.lirr_dict[name]['text'] = line.getchildren()[2].text
			self.lirr_dict[name]['date'] = line.getchildren()[3].text
			self.lirr_dict[name]['time'] = line.getchildren()[4].text


class MetroNorth(MTAServiceAlerts):

	def __init__(self):
		self.mn_obj = self.service_types[4]
		self.mn_dict = {}
		for line in self.mn_obj.getchildren():
			name = line.getchildren()[0].text
			self.mn_dict[name] = {}
			self.mn_dict[name]['status'] = line.getchildren()[1].text
			self.mn_dict[name]['text'] = line.getchildren()[2].text
			self.mn_dict[name]['date'] = line.getchildren()[3].text
			self.mn_dict[name]['time'] = line.getchildren()[4].text
