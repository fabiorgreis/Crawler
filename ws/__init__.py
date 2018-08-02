""" Rest Web Service modulo"""
from flask import Flask, json
from crawler.auto_esporte import AutoEsporteCrawler

APP = Flask(__name__)
CRAWLER = AutoEsporteCrawler('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')

@APP.route("/")
def index():
    """Retorna o json com a informacao estruturada do feed"""
    return json.jsonify(CRAWLER.processa_feed())
