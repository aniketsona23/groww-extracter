from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ser = webdriver.ChromeService(executable_path="./chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=ser)

def gettting(url):
    proper = "+".join(url.split(" "))
    driver.get("https://www.google.com/search?q=groww+"+proper)
    source = driver.page_source.split("groww.in/stocks/")[1].split('" data-ved')[0]
    return source