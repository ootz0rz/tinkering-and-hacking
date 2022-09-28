import urllib.request
import urllib
import json

API_URI_BASE = "https://jsonmock.hackerrank.com/api/countries"

"""
{'data': [{'alpha2Code': 'AF',
           'alpha3Code': 'AFG',
           'altSpellings': ['AF', 'Afġānistān'],
           'area': 652230,
           'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
           'callingCodes': ['93'],
           'capital': 'Kabul',
           'currencies': ['AFN'],
           'demonym': 'Afghan',
           'gini': 27.8,
           'language': ['Pashto', 'Dari'],
           'languages': ['ps', 'uz', 'tk'],
           'latlng': [33, 65],
           'name': 'Afghanistan',
           'nativeName': 'افغانستان',
           'numericCode': '004',
           'population': 26023100,
           'region': 'Asia',
           'relevance': '0',
           'subregion': 'Southern Asia',
           'timezones': ['UTC+04:30'],
           'topLevelDomain': ['.af'],
           'translations': {'de': 'Afghanistan',
                            'es': 'Afganistán',
                            'fr': 'Afghanistan',
                            'hr': 'Afganistan',
                            'it': 'Afghanistan',
                            'ja': 'アフガニスタン',
                            'nl': 'Afghanistan'}}],
 'page': 1,
 'per_page': 10,
 'total': 1,
 'total_pages': 1}
"""


def _encode_payload(payload):
    return urllib.parse.urlencode(payload)


def _get_country_request_uri(country):
    return "{}?{}".format(API_URI_BASE, _encode_payload({"name": country}))


def getCapitalCity(country):
    capital_city = "-1"

    raw = (
        urllib.request.urlopen(
            urllib.request.Request(_get_country_request_uri(country), method="GET")
        )
        .read()
        .decode("utf-8")
    )

    json_data = json.loads(raw)

    # data exists?
    if (
        ("data" not in json_data)
        or (json_data["data"] == None)
        or (len(json_data["data"]) == 0)
    ):
        return capital_city

    # capital exists?
    if (
        ("capital" not in json_data["data"][0])
        or (json_data["data"][0]["capital"] == None)
        or (len(json_data["data"][0]["capital"]) == 0)
    ):
        return capital_city

    capital_city = json_data["data"][0]["capital"]

    return capital_city


r = getCapitalCity("Canada")
print()
print("capital: ", r)
