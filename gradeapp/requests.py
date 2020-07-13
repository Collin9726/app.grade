import urllib.request, json
from .models import Quote


def get_quote():

    get_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)
        
        author = get_quote_response.get('author')
        quote = get_quote_response.get('quote')

        quote_object = Quote(author,quote)
        
    return quote_object

