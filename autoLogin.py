import sys
import webbrowser
import selenium
from selenium import webdriver
import time
from time import sleep
import datetime
x = datetime.datetime.now()
print(x)


browse = webdriver.Chrome()
browse.get('https://github.com/login')
#browse.get('https://armt.att.com/users/sign_in')

print('Opening Websites')
print('...Successful')

GithubUsr = 'ethankfrancis'    
GithubPass = 'sandhill317'

browse.find_elements_by_id('login_field')[0].send_keys(GithubUsr)
browse.find_elements_by_id('password')[0].send_keys(GithubPass)
browse.find_elements_by_name('commit')[0].click()


#Dtarmtacctid = 'andrdtm'
#Dtarmtuserid = 'ausengi'
#Dtarmtpasswd = 'ausengi'

#browse.find_elements_by_id('account_id')[0].send_keys(Dtarmtacctid)
#browse.find_elements_by_id('user_id')[0].send_keys(Dtarmtuserid)
#browse.find_elements_by_id('password')[0].send_keys(Dtarmtpasswd)
#browse.find_elements_by_class_name('btn btn-primary full-width')[0].click()



'''def main():
  print('Opening Websites')
  print('...Successful')
  
  
  sites = "websites.txt"
  browser = "google-chrome"


 
  wbbrowser = webbrowser.get(browser)
  browse = webdriver.Chrome()
  

  if len(sys.argv) >= 2:
    sites = sys.argv[1].lower()

  if len(sys.argv) >= 3:
    browser = sys.argv[2].lower()

  

  with open(sites) as fobj:
    try:
      for num, url in enumerate(fobj):
        wbbrowser.open_new_tab(url)
        sleep(1)
    except Exception as e:
      print(e)

if __name__ == '__main__': main()'''