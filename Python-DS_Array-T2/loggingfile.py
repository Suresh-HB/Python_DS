import logging

def logg(filename):
    
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
    logging.basicConfig(filename='log.txt', level=logging.INFO, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
    logging.basicConfig(filename='log.txt', level=logging.WARNING, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
    logging.basicConfig(filename='log.txt', level=logging.ERROR, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
    logging.basicConfig(filename='log.txt', level=logging.CRITICAL, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")

    return logging.getLogger(__name__)
