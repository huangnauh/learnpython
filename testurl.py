from urllib2 import Request, urlopen, URLError, HTTPError  
  
req = Request('http://baibai.com')  
    
try:    
    
    response = urlopen(req)    
    
except URLError, e:    
    
    if hasattr(e, 'code'):    
    
        print 'The server couldn\'t fulfill the request.'    
    
        print 'Reason: ', e.code    
    
    elif hasattr(e, 'reason'):    
    
        print 'We failed to reach a server.'    
    
        print 'Error code: ', e.reason    
    
else:    
    print 'No exception was raised.'    
    # everything is fine    