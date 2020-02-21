import webbrowser
from webbrowser import get
import sys
import time
from time import sleep
import datetime
import selenium
from selenium import webdriver

x = datetime.datetime.now()
print(x)


def main():
  print('Opening Websites')
  print('...Successful')
  
  
  sites = "websites.txt"
  browser = "google-chrome"


 
  wbbrowser = webbrowser.get(browser)

  if len(sys.argv) >= 2:
    sites = sys.argv[1].lower()

  if len(sys.argv) >= 3:
    browser = sys.argv[2].lower()

  

  with open(sites) as fobj:
    try:
      for num, url in enumerate(fobj):
        wbbrowser.open_new(url)
        sleep(1)
    except Exception as e:
      print(e)

if __name__ == '__main__': main()

