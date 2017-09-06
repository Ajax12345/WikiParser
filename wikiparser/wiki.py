import urllib
import re
import collections
import itertools
import requests
from bs4 import BeautifulSoup as soup

class InvalidParameterError(ValueError):
    def __init__(self, message):
        ValueError.__init__(self, message)

class InvalidKeyWordError(ValueError):
    def __init__(self, message):
        ValueError.__init__(self, message)

class NoArticlesFoundError(ValueError):
    def __init__(self, message):
        ValueError.__init__(self, message)

class KeyWordYieldedNoArticles(ValueError):
    def __init__(self, message):
        ValueError.__init__(self, message)



class Wiki:
    __slots__ = ["query", "topics", "kwargs", "url", "data", "header", "supported_languages"]
    def __init__(self, query, **kwargs):

        self.query = query
        self.topics = None
        self.kwargs = kwargs
        self.url = "https://{}.wikipedia.org{}".format(kwargs.get("lang", "en"), self.query) if self.kwargs.get("by_url", False) else "https://{}.wikipedia.org/wiki/{}".format(kwargs.get("lang", "en"), self.query)
        self.data = str(urllib.urlopen(self.url).read())
        self.check_invalid_article(self.data)
        self.header = self.get_header(self.data)
        self.supported_languages = None#open('wiki_supported_languages.txt').read()


    def disambiguation(self):
        data_info = collections.namedtuple("data_info", "extension1 name name1")
        new_url = "https://en.wikipedia.org{}_(disambiguation)".format(self.query) if self.kwargs.get("by_url", False) else "https://en.wikipedia.org/wiki/{}_(disambiguation)".format(self.query)
        data = str(urllib.urlopen(new_url).read())
        possible_error = re.findall("<b>(.*?)</b>", data)

        if possible_error and "Wikipedia does not have an article with this exact name." in possible_error:
            raise InvalidKeyWordError("unable to find disambiguation from entered keyword '{}'. Please broaded your search".format(new_url))

        s = soup(data, 'lxml')
        new_data = [i.text for i in s.find_all("li")]
        new_data = list(itertools.chain.from_iterable([i.split("\n") for i in new_data]))
        headers = [i for i in new_data if i and i[0].isdigit()]
        new_data = [i for i in new_data[len(headers):] if i]

        return {"headers":headers, "topics":new_data[:-58]}

    def check_invalid_article(self, data):
        possible_error = re.findall("<b>(.*?)</b>", data)

        if possible_error and "Wikipedia does not have an article with this exact name." in possible_error:
            raise NoArticlesFoundError("no articles were found")





    def get_header(self, page_data):
        r = '<h1 id="firstHeading" class="firstHeading" lang="en">(.*?)</h1>'
        #return re.findall(r, str(urllib.urlopen(self.url).read()))[0]
        return re.findall(r, page_data)[0]



    def get_article_info(self, **kwargs):
        '''
        data = str(urllib.urlopen(self.url).read())
        if check_invalid_article(data):
            raise NoArticlesFoundError("no articles with the query '{}' were found".format(self.query))
        '''

        req = requests.get(self.url)

        s = soup(req.text, 'lxml')#html.parser

        article_paragraphs = [i.text for i in s.find_all("p")]
        #print "article_paragraphs", article_paragraphs

        if len(article_paragraphs) == 1 and re.findall("[a-zA-Z0-9]{1,}\smay refer to\:", article_paragraphs[0]):
            raise KeyWordYieldedNoArticles("could not find standalone article by name '{}'".format(re.sub("https\:\/\/en.wikipedia.org\/wiki\/", '', self.url)))

        lines = kwargs.get("lines", None)
        if lines is None:
            return article_paragraphs

        else:
            if len(lines) < 3:
                return article_paragraphs[lines[0]:lines[1]] if len(lines) > 1 else article_paragraphs[lines[0]]
            else:
                raise InvalidParameterError("Please provide one or two line numbers, not {}".format(len(lines)))



    def article_sources(self):


        #data = str(urllib.urlopen(self.url).read())

        s = '<li id="cite_note-(.*?)">(.*?)</li>'
        raw_sources = re.findall(s, self.data)
        #final_dict = collections.defaultdict(dict)
        final_dict = []

        for number, raw_content in raw_sources:
            s = soup(raw_content, "lxml")
            full_citation = s.get_text()

            short_name = number
            if re.findall("^\^", full_citation) or re.findall("(\w\s){2,}", full_citation):
                full_citation = re.sub("^\^|(\w\s){2,}", '', full_citation)


            final_dict.append([short_name, full_citation])



        return final_dict




    def bibliography(self):


        #page_data = str(urllib.urlopen(self.url).read())
        if '<span class="mw-headline" id="Bibliography">Bibliography</span>' not in self.data:
            return None

        else:
            new_data = self.data.split("\n")
            #print [i for i, a in enumerate(page_data.split("\n")) if "Bibliography" in a]
            final_data = re.findall("<li>(.*?)</li>", '\n'.join(new_data[100:]))

            new_data = [{"full_title":i[:i.index("(<a href")] if "(<a href" in i else i, "ISBN":re.findall('<a href="/wiki/Special:BookSources/(.*?)"', i)[0] if re.findall('<a href="/wiki/Special:BookSources/(.*?)"', i) else "No Exterior ISBN"} for i in final_data]
            return new_data



    def external_links(self):

        #page_data = str(urllib.urlopen(self.url).read())
        if '<span class="mw-headline" id="External_links">External links</span>' not in self.data:
            return None

        else:

            page_data = self.data.split("\n")
            indices = [i for i, a in enumerate(page_data) if '<span class="mw-headline" id="External_links">External links</span>' in a]
            final_data = '\n'.join(page_data[indices[-1]:])

            sites = re.findall('<a rel="nofollow" class="external text" href="(.*?)">(.*?)</a>', final_data)

            site = collections.namedtuple("site", "url name")
            new_sites = map(site._make, sites)
            return new_sites

    def contents(self):


        #page_data = str(urllib.urlopen(self.url).read())
        r = '<span class="mw-headline" id="(.*?)">(.*?)</span>'
        contents = re.findall(r, self.data)
        return [i[-1] for i in contents]




    def info_box(self):

        data = str(urllib.urlopen(self.url).read()).split("\n")
        seen_header = False
        indices = []
        for i, a in enumerate(data):

            if '<table class="infobox' in a:
                seen_header = True
                indices.append(i)

            elif '</table>' in a and seen_header:
                indices.append(i)
                break

        a, b = indices
        infobox_data = data[a:b]

        new_data = [soup(i, "lxml").getText().encode("ascii", errors="ignore") for i in infobox_data]
        new_data = [i for i in new_data if i]

        return new_data

    def __str__(self):
        return self.supported_languages



