import urllib3

from services.VoiceCall import VoiceCall


class TelestaxVoiceCall(VoiceCall):
    def __init__(self, url: str, from_number: str, token: str) -> None:
        self.__url = url
        self.__from_numer = from_number
        self.__token = token

    def call(self, number: str, text: str) -> bool:
        http = urllib3.PoolManager()
        url = self.__url
        params = {
            'from' : self.__from_numer,
            'to' : number,
            'token' : self.__token,
            'alertBody': text
        }
        try:
            http.request('GET', url, params)
        except(Exception):
            print("exception")
            return False

        return True