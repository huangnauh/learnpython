>>> environ = {'PROCESSOR_ARCHITECTURE': 'x86', 'PATH': 'C:\\Tcl\\bin;E:\\GnuWin32\\bin;C:\\MinGW\\bin;E:\\ruby\\bin;C:\\Program Files\\Haskell\\bin;D:\\Program Files\\Haskell Platform\\2012.4.0.0\\lib\\extralibs\\bin;D:\\Program Files\\Haskell Platform\\2012.4.0.0\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\Windows7Master;D:\\Program Files\\Haskell Platform\\2012.4.0.0\\mingw\\bin;E:\\Python27;E:\\Python27\\Scripts;C:\\Program Files\\WinRAR;C:\\Program Files\\MicrosoftSQL Server\\90\\Tools\\binn\\;C:\\Program Files\\Oracle\\VirtualBox;C:\\ProgramFiles\\Microsoft Windows Performance Toolkit\\;C:\\Users\\Administrator\\AppData\\Local\\Pandoc;C:\\Tcl\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\cabal\\bin;C:\\Tcl\\bin;E:\\GnuWin32\\bin;C:\\MinGW\\bin;E:\\ruby\\bin;C:\\Program Files\\Haskell\\bin;D:\\Program Files\\Haskell Platform\\2012.4.0.0\\lib\\extralibs\\bin;D:\\Program Files\\Haskell Platform\\2012.4.0.0\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\Windows7Master;D:\\Program Files\\Haskell Platform\\2012.4.0.0\\mingw\\bin;E:\\Python27;E:\\Python27\\Scripts;C:\\Program Files\\WinRAR;C:\\Program Files\\Microsoft SQL Server\\90\\Tools\\binn\\;C:\\Program Files\\Oracle\\VirtualBox;C:\\Program Files\\Microsoft Windows Performance Toolkit\\;C:\\Users\\Administrator\\AppData\\Local\\Pandoc;;C:\\Users\\Administrator\\AppData\\Local\\Pandoc\\', 'HTTP_ACCEPT': '', '__COMPAT_LAYER': 'RunAsInvoker', 'COMPUTERNAME': 'HUANGLIBO', 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming', 'PATH_TRANSLATED': 'E:\\code\\huang\\b\\learnpy', 'LOGONSERVER': '\\\\HUANGLIBO', 'USERPROFILE': 'C:\\Users\\Administrator', 'SERVER_PROTOCOL': 'HTTP/1.0', 'TEMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'VS80COMNTOOLS': 'C:\\Program Files\\Microsoft Visual Studio 8\\Common7\\Tools\\', 'REMOTE_ADDR': '127.0.0.1', 'SERVER_PORT': '8888', 'NUMBER_OF_PROCESSORS': '3', 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log', 'PROCESSOR_REVISION': '0503', 'PROMPT': '$P$G', 'REMOTE_HOST': '', 'VBOX_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\', 'QUERY_STRING': '', 'GATEWAY_INTERFACE': 'CGI/1.1', 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local', 'HOMEDRIVE': 'C:', 'PROCESSOR_LEVEL': '16', 'FP_NO_HOST_CHECK': 'NO', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'CONTENT_LENGTH': '54', 'ASL.LOG': 'Destination=file', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.RB;.RBW;.PY;.tcl', 'WINDOWS_TRACING_FLAGS': '3', 'HTTP_REFERER': 'http://127.0.0.1:8888/cgi101.html', 'SYSTEMROOT': 'C:\\Windows', 'RUBYOPT': '-rubygems', 'SCRIPT_NAME': '/cgi-bin/cgi101.py', 'HTTP_COOKIE': '', 'HOMEPATH': '\\Users\\Administrator', 'SESSIONNAME': 'Console', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'SYSTEMDRIVE': 'C:','PROCESSOR_IDENTIFIER': 'x86 Family 16 Model 5 Stepping 3, AuthenticAMD', 'USERDOMAIN': 'HUANGLIBO', 'PROGRAMFILES': 'C:\\Program Files', 'CONTENT_TYPE': 'application/x-www-form-urlencoded', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36', 'SERVER_SOFTWARE': 'SimpleHTTP/0.6 Python/3.4.1', 'OS': 'Windows_NT', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'USERNAME': 'Administrator', 'PATH_INFO': '', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'REQUEST_METHOD': 'POST', 'PUBLIC': 'C:\\Users\\Public', 'PROGRAMDATA': 'C:\\ProgramData', 'TMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'WINDIR': 'C:\\Windows', 'SERVER_NAME': 'rad.msn.com'}
>>> from pprint import pprint
>>> pprint(environ)
{'ALLUSERSPROFILE': 'C:\\ProgramData',
 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming',
 'ASL.LOG': 'Destination=file',
 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
 'COMPUTERNAME': 'HUANGLIBO',
 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe',
 'CONTENT_LENGTH': '54',
 'CONTENT_TYPE': 'application/x-www-form-urlencoded',
 'FP_NO_HOST_CHECK': 'NO',
 'GATEWAY_INTERFACE': 'CGI/1.1',
 'HOMEDRIVE': 'C:',
 'HOMEPATH': '\\Users\\Administrator',
 'HTTP_ACCEPT': '',
 'HTTP_COOKIE': '',
 'HTTP_REFERER': 'http://127.0.0.1:8888/cgi101.html',
 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1)AppleWebKit/537.36 (KHTML, '
                    'like Gecko) Chrome/36.0.1985.125 Safari/537.36',
 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local',
 'LOGONSERVER': '\\\\HUANGLIBO',
 'NUMBER_OF_PROCESSORS': '3',
 'OS': 'Windows_NT',
 'PATH': 'C:\\Tcl\\bin;E:\\GnuWin32\\bin;C:\\MinGW\\bin;E:\\ruby\\bin;C:\\Program '
         'Files\\Haskell\\bin;D:\\Program Files\\Haskell '
         'Platform\\2012.4.0.0\\lib\\extralibs\\bin;D:\\Program '
         'Files\\Haskell '
         'Platform\\2012.4.0.0\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program '
         'Files\\Windows7Master;D:\\Program Files\\Haskell '
         'Platform\\2012.4.0.0\\mingw\\bin;E:\\Python27;E:\\Python27\\Scripts;C:\\Program '
         'Files\\WinRAR;C:\\Program Files\\MicrosoftSQL '
         'Server\\90\\Tools\\binn\\;C:\\Program '
         'Files\\Oracle\\VirtualBox;C:\\ProgramFiles\\Microsoft Windows '
         'Performance '
         'Toolkit\\;C:\\Users\\Administrator\\AppData\\Local\\Pandoc;C:\\Tcl\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\cabal\\bin;C:\\Tcl\\bin;E:\\GnuWin32\\bin;C:\\MinGW\\bin;E:\\ruby\\bin;C:\\Program '
         'Files\\Haskell\\bin;D:\\Program Files\\Haskell '
         'Platform\\2012.4.0.0\\lib\\extralibs\\bin;D:\\Program '
         'Files\\Haskell '
         'Platform\\2012.4.0.0\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program '
         'Files\\Windows7Master;D:\\Program Files\\Haskell '
         'Platform\\2012.4.0.0\\mingw\\bin;E:\\Python27;E:\\Python27\\Scripts;C:\\Program '
         'Files\\WinRAR;C:\\Program Files\\Microsoft SQL '
         'Server\\90\\Tools\\binn\\;C:\\Program '
         'Files\\Oracle\\VirtualBox;C:\\Program Files\\Microsoft Windows '
         'Performance '
         'Toolkit\\;C:\\Users\\Administrator\\AppData\\Local\\Pandoc;;C:\\Users\\Administrator\\AppData\\Local\\Pandoc\\',
 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.RB;.RBW;.PY;.tcl',
 'PATH_INFO': '',
 'PATH_TRANSLATED': 'E:\\code\\huang\\b\\learnpy',
 'PROCESSOR_ARCHITECTURE': 'x86',
 'PROCESSOR_IDENTIFIER': 'x86 Family 16 Model 5 Stepping 3, AuthenticAMD',
 'PROCESSOR_LEVEL': '16',
 'PROCESSOR_REVISION': '0503',
 'PROGRAMDATA': 'C:\\ProgramData',
 'PROGRAMFILES': 'C:\\Program Files',
 'PROMPT': '$P$G',
 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\',
 'PUBLIC': 'C:\\Users\\Public',
 'QUERY_STRING': '',
 'REMOTE_ADDR': '127.0.0.1',
 'REMOTE_HOST': '',
 'REQUEST_METHOD': 'POST',
 'RUBYOPT': '-rubygems',
 'SCRIPT_NAME': '/cgi-bin/cgi101.py',
 'SERVER_NAME': 'rad.msn.com',
 'SERVER_PORT': '8888',
 'SERVER_PROTOCOL': 'HTTP/1.0',
 'SERVER_SOFTWARE': 'SimpleHTTP/0.6 Python/3.4.1',
 'SESSIONNAME': 'Console',
 'SYSTEMDRIVE': 'C:',
 'SYSTEMROOT': 'C:\\Windows',
 'TEMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp',
 'TMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp',
 'USERDOMAIN': 'HUANGLIBO',
 'USERNAME': 'Administrator',
 'USERPROFILE': 'C:\\Users\\Administrator',
 'VBOX_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\',
 'VS80COMNTOOLS': 'C:\\Program Files\\Microsoft Visual Studio '
                  '8\\Common7\\Tools\\',
 'WINDIR': 'C:\\Windows',
 'WINDOWS_TRACING_FLAGS': '3',
 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log',
 '__COMPAT_LAYER': 'RunAsInvoker'}