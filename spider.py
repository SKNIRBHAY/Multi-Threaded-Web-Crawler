from urllib.request import urlopen 
from link_finder import LinkFinder
from General import *

class Spider():

	# Class Variables (shared between all instances of a class)
	project_name = '';
	base_url = '';
	domain_name = '';
	queue_file = '';
	crowled_file = '';
	queue = set();
	crowled = set();

	def __init__(self, project_name, base_url, domain_name):
		#print("All details: " + project_name, base_url, domain_name)
		Spider.project_name = project_name;
		Spider.base_url = base_url;
		Spider.domain_name = domain_name;
		Spider.queue_file = Spider.project_name + '/queue.txt';
		Spider.crowled_file = Spider.project_name + '/crowled.txt';
		self.boot();
		#print("The URL: " + Spider.base_url);
		self.crowl_page('first spider', Spider.base_url);

	@staticmethod
	def boot():
		create_project_dir(Spider.project_name);
		create_data_files(Spider.project_name, Spider.base_url);
		Spider.queue = file_to_set(Spider.queue_file);
		Spider.crowled = file_to_set(Spider.crowled_file);

	@staticmethod
	def crowl_page(thread_name, page_url):
		#print("The URL: " + page_url);
		if page_url not in Spider.crowled:
			print(thread_name + ' is now crowling ' + page_url);
			print('Queue: ' + str(len(Spider.queue)) + ' | Crowled: ' + str(len(Spider.crowled)));
			Spider.add_links_to_queue(Spider.gather_links(page_url));
			Spider.queue.remove(page_url);
			Spider.crowled.add(page_url);
			Spider.update_files();

	@staticmethod
	def gather_links(page_url):
		html_string = '';
		try: 
			response = urlopen(page_url);
			if(response.getheader('Content-Type') == 'text/html'):
				html_bytes = response.read();
				html_string = html_bytes.decode('utf-8');
			finder = LinkFinder(Spider.base_url, page_url);
			finder.feed(html_string);
		except:
			print('Error: Can not crowl the page!!!');
			return set();
		return finder.page_links();

	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			# If the URL is present in the queue already then do not add it to the queue 
			if(url in Spider.queue):
				continue;
			# If the URL is present in the crowled list already, then do not add it to the queue 
			if(url in Spider.crowled):
				continue;
			# The url which is being crowled, must contain the domain name on which the crowling is being performed
			# Other wise a webpage can also contain a link to a really huge website like youtube, facebook, tweeter, etc.
			if(Spider.domain_name not in url):
				continue;
			Spider.queue.add(url);

	@staticmethod
	def update_files():
		set_to_file(Spider.queue, Spider.queue_file);
		set_to_file(Spider.crowled, Spider.crowled_file);

