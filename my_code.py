import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='my_logs.log',
    encoding='utf-8',
    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])',
    datefmt='%d/%m/%Y %I:%M:%S %p',
)

x: int = 10 + 10
logging.info('The answer is: %s', x)
logging.error('some error!!')
