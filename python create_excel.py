#import urllib.request
    #page = urllib.request.urlopen('https://www.zubzz.com/menus')
    #print(page.read())  


import webbrowser
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
url = "https://www.zubzz.com/menus"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)                               
          

