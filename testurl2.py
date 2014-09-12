import urllib

response = urllib.urlopen("http://localhost:8080")
print("response:",response)
print("code:",response.getcode())
print("Url: ",response.geturl())
headers = response.info()
print('DATE    :', headers['date'])
print('HEADERS :')
print('---------')
print(headers)
#print(response.read())