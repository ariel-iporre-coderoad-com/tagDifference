import starflex
import time
from threading import Thread
import json

def pull_developer_message():
    message = read_developer_message()
    while len(message) > 0:
        message = read_developer_message()
        time.sleep(3)
    else:
        print '===> finished inventory'
        client.stop_listening()
        print client.summary()
    print ' !!!!!!!!!!!!!!!   --===============>>  thread 2 stopped'
    print 'press enter to exit'

def read_developer_message():
    response = client.get_msg('/apps/inventory')
    x = json.loads(response)
    dev_msg = ''
    if 'developerMsg' in x:
        dev_msg = x['developerMsg']
    return dev_msg
def client_listening():
    # client.listen_during(-1, end_point='/rfid/events/deepInv?override')  # same endpoint
    client.listen_during(-1, end_point='/rfid/events?override')  # same endpoint
    print ' !!!!!!!!!!!!!!!   --===============>>  thread 1 stopped'
    pass

client = starflex.star_client('10.100.1.71')
# Start
client.post_msg(end_point='/apps/inventory') # inventory started
# Listening for 10 seconds
t1 = Thread(target=client_listening)  # run the some_task function in another
t1.daemon = True
t1.start()

t2 = Thread(target=pull_developer_message)  # run the some_task function in another
t2.daemon = True
t2.start()


try:
    a=''
    while not a=='e':
        a = input(raw_input("Press Enter to continue..."))
except:
    print 'End'


# print r.content
