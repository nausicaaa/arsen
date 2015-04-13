from datetime import datetime
from bs4 import BeautifulSoup
import requests
from lib.models import Price

# print 'arsen'
# print Price.objects.all()
# Price(price=12, product_name='awokado', time=datetime.now()).save()
# print Price.objects.all()

def get_soup(url):
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc)
    return soup


def get_product_name(soup):
    title_tag = soup.find('h1')
    return title_tag.text

def get_variants_and_prices(soup):
    ret = {}
    trs = soup.find_all('tr', attrs={'itemprop':'offerDetails'})
    for tr in trs:
        variant_name = tr.td.text.strip()
        price = tr.find('span', attrs={'itemprop':'price'}).text.strip()
        ret.update({variant_name:price})
    return ret

urls = [
    'http://www.zooplus.pl/shop/psy/zabawki_szkolenie_psa/kong_dla_psa/classic/140097',
    'http://www.zooplus.pl/shop/psy/zabawki_szkolenie_psa/kong_dla_psa/pilka/194239',
    'http://www.zooplus.pl/shop/psy/transporter_klatka_dla_psa/klatki_transportowe/transportowe/372486'
]

for url in urls:
    soup = get_soup(url)
    print get_product_name(soup)
    print get_variants_and_prices(soup)
