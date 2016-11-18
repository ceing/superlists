from selenium import webdriver

bro = webdriver.Firefox()
bro.get('http://localhost:8000')
assert 'Django' in bro.title

