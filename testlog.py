import logging
import logging.handlers

#logging.basicConfig(level=logging.DEBUG,
#		    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#		    datefmt='%a, %d %b %Y %H:%M:%S',
#		    filename="E:/code/huang/b/learnpy/myapp.log",
#		    filemode='w')
            
#console = logging.StreamHandler()
#console.setLevel(logging.INFO)
#formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
#console.setFormatter(formatter)
#logging.getLogger('').addHandler(console)
#log = logging.getLogger('root.test')
#log.setLevel(logging.WARN)


    
filename="E:/code/huang/b/learnpy/myapp.log"

handler = logging.handlers.RotatingFileHandler(filename,'w',maxBytes = 1024*1024,backupCount = 5)

fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s' 
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger = logging.getLogger('root.tst')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.debug('this is a debug message')
logger.info('this is a info message')
logger.warning('this is a warning message')
logger.debug('%s, %s, %s', 'error', 'debug', 'info') 
logger.debug('this is a debug message')
logger.info('this is a info message')
logger.warning('this is a warning message')
logger.debug('%s, %s, %s', 'error', 'debug', 'info') 
try:  
    raise Exception, 'this is a exception'  
except:  
    logger.exception('huanglibo') 