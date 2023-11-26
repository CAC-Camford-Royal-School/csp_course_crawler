import requests
import datetime
from fake_useragent import UserAgent
import urllib.request,urllib.error
import re


def get_random_user_agent():
    """get random user agent."""
    user_agent = UserAgent()
    return user_agent.random


def askUrl(url):
    """return HTML"""
    head = {
        "User-Agent" : get_random_user_agent()
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as error:
        if hasattr(error,"code"):
            print(error.code)
        if hasattr(error,"reason"):
            print(error.reason)
    return html