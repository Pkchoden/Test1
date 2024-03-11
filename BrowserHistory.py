# Import the LifoQueue class from the queue module
from queue import LifoQueue
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None
Noofvisits = int(input('enter the number of URL history:'))
print('Enter URLs to visit:')
for i in range(Noofvisits):
    url = input('URL:')
    print(f'visiting {url}')
    backward_history.put(current_page)
    current_page = url
#display current page
print(f"current page :{current_page}")