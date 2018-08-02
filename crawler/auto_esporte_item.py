""" Auto Esporte Feed Item Modulo"""
from bs4 import BeautifulSoup

class AutoEsporteItem:
    """Classe que representa o item no feed do Auto Esporte"""
    def __init__(self):
        self.proc_tags = {
            'div': self._processa_div,
            'p': self._processa_p,
            'img': self._processa_img,
            'ul': self._processa_ul
        }

    def processa_item(self, item):
        """Processa o item, retornando um dicionario do conteudo.
        Input: item - instancia do BeautifulSoap Tag com o conteudo do item
        Output: Retorna dicionario com a informação estruturada"""
        resp = {
            'title': self._limpa_texto(item.title.text),
            'link': self._limpa_texto(item.link.next_sibling),
            'content': []
        }
        # extrai conteudo da tag description
        descr = item.description.contents[0]
        soup = BeautifulSoup(descr, 'html.parser')
        # itera conteudo da tag description
        for content in soup.contents:
            if content.name in self.proc_tags:
                data = self.proc_tags[content.name](content)
                if data:
                    resp['content'] += (data,)
        return resp


    def _processa_div(self, tag):
        for content in tag.contents:
            if content.name in self.proc_tags:
                return self.proc_tags[content.name](content)

    def _processa_p(self, tag):
        if tag.text.strip():
            return {
                'type': 'text',
                'content': self._limpa_texto(tag.text)
            }

    @staticmethod
    def _processa_img(tag):
        return {
            'type': 'image',
            'content': tag['src']
        }

    @staticmethod
    def _processa_ul(tag):
        links = []
        for content in tag.contents:
            if content.name == 'li':
                links += (content.a['href'],)
        return {
            'type': 'links',
            'content': links
        }

    @staticmethod
    def _limpa_texto(texto):
        return texto.strip('/r').strip('/n').strip('/t').strip()
