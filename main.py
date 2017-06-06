import threading 
from queue import Queue
from spider import Spider
from domain import *
from General import *

PROJECT_NAME = 'thenewboston';
HOMEPAGE = 'https://thenewboston.com/';
DOMAIN_NAME = get_domain_name(HOMEPAGE);
QUEUE_FILE = PROJECT_NAME + '/queue.txt';
CROWLED_FILE = PROJECT_NAME + '/crowled.txt';
NUMBER_OF_THREADS = 8;
queue = Queue();
#print("All details: " + PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
S1 = Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME);

# Create worker threads (will die when main exits)
def create_workers():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work);
		t.daemon = True;
		t.start();

# Do the next job in the queue
def work():
	while True:
		url = queue.get();
		Spider.crowl_page(threading.current_thread().name, url);
		queue.task_done();

# Each queued link is a new job
def create_jobs():
	set_queue = file_to_set(QUEUE_FILE);
	for link in set_queue:
		queue.put(link);
	queue.join();
	crowl();

# Check if there are items in the queue, if so, then crowl them
def crowl():
	queued_links = file_to_set(QUEUE_FILE);
	set_length = len(queued_links);
	if set_length > 0:
		print(str(set_length) + 'links are there in the queue.');
		create_jobs();

create_workers(); # Creating workers
crowl(); # Create Jobs 
