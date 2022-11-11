def log_message(msg):
    with open('logs.txt', 'a') as log_file:
        log_file.write("{0}\n".format(msg))
    