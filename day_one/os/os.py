import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for file in os.listdir(path):
            childpath = os.path.join(path, file)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total), path)
    return total

# disk_usage('/home/marcus/Documents/')

