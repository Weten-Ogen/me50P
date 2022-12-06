import logging
logger = logging.getLogger(__name__)

# Create handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Set Levels
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)


logger.addHandler(stream_h)
logger.addHandler(file_h)





if __name__ == "__main__":
    logger.warning('this is a warning')
    logger.error('this is an error')