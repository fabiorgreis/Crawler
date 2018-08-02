"""Test AutoEsporteCrawler Class Module"""
import json
import vcr
from crawler.auto_esporte import AutoEsporteCrawler

@vcr.use_cassette('test/fixtures/vcr_cassettes/autoesporte.yaml')
def test_processa_feed():
    """ Testa o processamento do feed com o retorno de lista de objetos"""
    crawler = AutoEsporteCrawler('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
    data = crawler.processa_feed()
    assert data[0]['title'] == 'Vídeo: Presidente das Filipinas destrói carros contrabandeados'\
                               ' avaliados em R$ 20 milhões'
    assert data[-1]['title'] == 'Nova York estuda reduzir o número de motoristas da Uber e Lyft'\
                                ' nas ruas'

@vcr.use_cassette('test/fixtures/vcr_cassettes/autoesporte.yaml')
def test_feed_to_json():
    """ Testa o processamento do feed com o retorno de json"""
    crawler = AutoEsporteCrawler('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
    resp = crawler.feed_to_json()
    data = json.loads(resp)
    assert data[0]['title'] == 'Vídeo: Presidente das Filipinas destrói carros contrabandeados'\
                               ' avaliados em R$ 20 milhões'
    assert data[-1]['title'] == 'Nova York estuda reduzir o número de motoristas da Uber e Lyft'\
                                ' nas ruas'
