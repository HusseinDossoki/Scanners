import threading, socket, sys
import tld # Top Level Domain
from queue import Queue

user_inputs = sys.argv # It's a LIST of STRING


print_lock = threading.Lock()

# Can be a Domain name or IP Address
# Note: user_inputs[0] it's a script's path so you don't need it
target = user_inputs[1]

q = Queue()


def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        con = s.connect((target, port))
        with print_lock:
            print('Port ', port, ' is Open!!!!!!!!')

        con.close()
    except:
        pass

for port in range(int(user_inputs[2]), int(user_inputs[3])):
    q.put(port)


def threader():

    while True:
        getting_port = q.get()
        portscan(getting_port)
        q.task_done()


for x in range(int(user_inputs[4])-1):
    t = threading.Thread(target=threader, args=())
    t.daemon = True
    t.start()

print("\n******** You have ", threading.active_count(), "Running threads ***********\n")

q.join()



