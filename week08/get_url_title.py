import requests
from bs4 import BeautifulSoup


def get_url_title(*, url):
    try:
        # Pretend to be a bot.
        headers = {'User-Agent': 'Testbot'}
        response = requests.get(url, headers=headers, timeout=10)
    except RequestException as request_exception:
        raise Exception(f'Couldn\'t request {url}. This was the exception {request_exception}')

    if not response.ok:
        raise Exception(f'Response for {url} was not ok.')

    soup = BeautifulSoup(response.content, 'html.parser')
    title_tag = soup.title

    if title_tag:
        return title_tag.string

    return ''
