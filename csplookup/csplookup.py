import requests
from .result import LookupResult

LookupEndPoint = "https://lookup.configserver.pro/api/v1/lookup/ip?ip="


class CSPClient(object):
    def __init__(self, api_key):
        self.key = api_key

    @staticmethod
    def _get_url(ip):
        return LookupEndPoint + ip

    def _get_headers(self):
        return {"apiKey": self.key}

    def lookup(self, ip):
        response = requests.get(url=self._get_url(ip), headers=self._get_headers())
        return LookupResult(raw_result=response)

    def test_response_time(self):
        return requests.get(url=self._get_url("4.2.2.4"), headers=self._get_headers()).elapsed

