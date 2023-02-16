from urllib.request import urlopen
page = urlopen("http://info.cern.ch/")
content = page.read()
print (content)