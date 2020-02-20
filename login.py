import webbrowser
import sys
import datetime

x=datetime.datetime.now()
print(x)


def main():
    print ('Opening Websites')


sites="websites.txt"
browser="Chrome"


webbrowser=webbrowser.get(browser)
with open(sites) as fobj:
    try:
        for num, url in enumerate(fobj):
            webbrowser.open_new_tab(url.strip())
            time.sleep(1)
except Exception as e:
    print(e)


if __name__=='__main__':main()