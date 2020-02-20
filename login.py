import webbrowser
import sys
import os
import datetime
from datetime import time

urL="http://google.com"
chrome_path="/var/lib/alternatives/google-chrome"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome %s').open_new_tab(urL)

def main():
  print('Opening Favorite Sites')

  sites = "websites.txt"
  browser = "chrome"

  if len(sys.argv) >= 2:
    sites = sys.argv[1].lower()

  if len(sys.argv) >= 3:
    browser = sys.argv[2].lower()

  global webbrowser 
  webbrowser = webbrowser.get(browser)

  with open(sites) as fobj:
    try:
      for num, url in enumerate(fobj):
        webbrowser.open_new_tab(url.strip())
        time.sleep(1)
    except Exception as e:
      print(e)

if __name__ == '__main__': 
  main()
