def test2():
    import http.client
    from pprint import pprint
    conn = http.client.HTTPConnection('localhost',8080)
    conn.request('GET','/?arg=value')
    r1 = conn.getresponse()
    print(r1.status,r1.reason)
    pprint(str(r1.headers))
    pprint(r1.read())
    conn.close()
def test():
#    import http.client, urllib.parse
    import urllib
    import httplib
    params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
                "Accept": "text/plain"}
    conn = httplib.HTTPConnection('localhost',8888)
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
    conn.close()
test()
