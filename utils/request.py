import requests

from config import DEFAULT_TIMEOUT


def get(url, params=None, headers=None, timeout=DEFAULT_TIMEOUT):
    return requests.get(url, params=params, headers=headers, timeout=timeout)


def put(url, data=None, json=None, headers=None, timeout=DEFAULT_TIMEOUT):
    return requests.put(url, data=data, json=json, headers=headers, timeout=timeout)


def post(url, data=None, json=None, headers=None, timeout=DEFAULT_TIMEOUT):
    return requests.post(url, data=data, json=json, headers=headers, timeout=timeout)
