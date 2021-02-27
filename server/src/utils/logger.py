import logging

def init_logger():
    _logger = logging.getLogger('app-log')
    _logger.setLevel(logging.INFO)

    # format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # console logger
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    # add handlers
    _logger.addHandler(ch)

    return _logger


