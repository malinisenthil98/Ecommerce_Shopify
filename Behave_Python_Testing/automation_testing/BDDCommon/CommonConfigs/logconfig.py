import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
     filename='%slog' % __file__[:-2],
     filemode='w'
)
logging.critical('This is a critical level msg!')
logging.error('This is a error level msg!')
logging.warning('This is a warning level msg!')
logging.info('This is a info level msg!')
logging.debug('This is a debug level msg!')
