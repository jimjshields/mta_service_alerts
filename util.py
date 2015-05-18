from StringIO import StringIO
import requests
from lxml import etree


def get_text_from_url(url):
	res = requests.get(url)
	return res.text


def get_dom_from_xml(xml):
	parser = etree.HTMLParser()
	return etree.parse(StringIO(xml), parser)