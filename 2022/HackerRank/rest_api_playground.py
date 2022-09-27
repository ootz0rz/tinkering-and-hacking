import urllib.request
import urllib
from urllib.parse import urlencode
import json

# http://httpbin.org/
# https://restninja.io/
BASE = "http://httpbin.org/anything/"
BASE_GET = BASE + "get/"
BASE_PUT = BASE + "put/"


def url_encode_payload(payload):
    # https://stackoverflow.com/questions/40557606/how-to-url-encode-in-python-3
    """
    payload = {'a': 'b', 't': [1, 2, 3]}
        =>
            'a=b&t=%5B1%2C+2%2C+3%5D'
    """
    return urlencode(payload)


def _get(payload):
    return __req(BASE_GET, payload)


def _put(payload):
    return __req(BASE_PUT, payload, method="PUT")


def __req(url, payload, method="GET"):
    return __decode(
        urllib.request.Request(url + "?" + url_encode_payload(payload), method=method)
    )


def __decode(r):
    res = ""
    try:
        decoded = urllib.request.urlopen(r).read().decode("utf-8")
        res = json.loads(decoded)
    except:
        pass
    finally:
        return res


if __name__ == "__main__":
    import pprint

    def print_get(payload):
        print("\n" + ("-" * 20))
        print("GET", payload)
        print()
        pprint.pprint(_get(payload))

    def print_put(payload):
        print("\n" + ("-" * 20))
        print("PUT", payload)
        print()
        pprint.pprint(_put(payload))

    print_get({"a": 1337})
    print_put({"b": 1337})
