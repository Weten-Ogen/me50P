import logger

def counting(n):
    for i in range(n):
        logger.log_message(f'values from counting:{i}')

if __name__ == '__main__':
    counting(20)