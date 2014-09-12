import logging
logging.basicConfig(level=logging.DEBUG,
   filename='log.txt',
   filemode='w',  
   format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
)

logging.info('calling method g() in f()')