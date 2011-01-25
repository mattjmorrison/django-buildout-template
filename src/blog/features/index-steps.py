from mock import Mock
from lettuce import *
from django.test.client import Client

@before.all
def set_browser():
    world.browser = Client()    

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = response.content

@step(r'I see the header "(.*)"')
def see_header(step, text):
    assert '<h1>%s</h1>' % text in world.dom