import requests

from lxml import html

# import wikipedia


class WikiInfo:
    def clean_wiki(self, location):
        # intro_text = wikipedia.summary(location)
        # print(intro_text)
        # return intro_text

        response = requests.get(
            "https://fr.wikipedia.org/w/api.php",
            params={
                "action": "parse",
                "page": location,
                "format": "json",
            },
        ).json()

        # print(response)
        raw_html = response["parse"]["text"]["*"]
        document = html.document_fromstring(raw_html)
        first_p = document.xpath("//p")[0]
        intro_text = first_p.text_content()
        return intro_text
