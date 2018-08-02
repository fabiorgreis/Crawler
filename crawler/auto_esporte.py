""" Auto Esporte Crawler Modulo """
import json
import requests
from bs4 import BeautifulSoup
from .auto_esporte_item import AutoEsporteItem


class AutoEsporteCrawler:
    """ Auto Esporte Crawler Class """
    def __init__(self, url):
        self._url = url
        self._proc_item = AutoEsporteItem()

    def processa_feed(self):
        """ Processa o feed baixado da url.
            Retorna uma lista de objetos com a informacao estruturada"""
        resp = []
        req = requests.get(self._url)
        soup = BeautifulSoup(req.text, 'html.parser')
        items = soup.find_all('item')
        # itera items do feed
        for item in items:
            resp += (self._proc_item.processa_item(item),)
        return resp

    def feed_to_json(self):
        """ Processa o feed baixado da url.
            Retorna uma a informacao estruturada no formato json"""
        return json.dumps(self.processa_feed())
