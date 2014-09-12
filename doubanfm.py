import requests
import json
import os

email = 'huanglibo2010@gmail.com'
password = 'xiuluochang'

login_data = {
    'email': '',
    'password': '',
    'app_name': 'radio_android',
    'version': '606',
}

params = {
    'count': 200,
    'app_name': 'radio_android',
    'version': '606',
}


def login(login_data):
    key = requests.post('https://www.douban.com/j/app/login',
                        data=login_data, verify=False).json()
    return type('key', (), key)


def fetch(email=email, password=password):
    ''' method from http://lisie.hdu.edu.cn/passionke/?p=4105 '''
    global login_data, params

    login_data['email'], login_data['password'] = email, password
    # print login_data
    key = login(login_data)
    #assert key.err == 'ok', 'Login error: {}'.format(key.err)
    if key.err != 'ok':
        return key.err

    params.update({'token': key.token,
                   'user_id': key.user_id,
                   'expire': key.expire})
    data = {}
    while 1:
        params['exclude'] = '|'.join(data.keys())
        new_data = requests.get(
            'http://www.douban.com/j/app/radio/liked_songs',
            params=params).json()['songs']

        if len(new_data) == 0:
            break
        data.update({t['sid']: t for t in new_data})
        # print 'new:{} total:{}'.format(len(new_data), len(data))
    return data

if __name__ == '__main__':
    data = fetch()
    print data[data.iterkeys().next()]