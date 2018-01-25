from urllib.parse import urlparse

# Get domain name (example.com)
def get_domain_name(url):
	try:
		results = get_sub_domain_names(url).split('.')
		return results[-2] + '.' + results[-1]
	except:
		return ''

def get_sub_domain_names(url):
	try:
		return urlparse(url).netloc # Returns only the network location of a website
	except:
		return ''

		
