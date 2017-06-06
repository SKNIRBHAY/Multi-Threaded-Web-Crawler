import os

# Create the project directory 
def create_project_dir(directory):
	if not os.path.exists(directory):
		print("Creating Directory: " + directory);
		os.makedirs(directory);
	else:
		print("Wow!!! Something went wrong!!!\nLike the directory you are trying to create already excist!!!\n");

# Create the crowled file and queue file
def create_data_files(project_name, base_url):
	queue = project_name + '/queue.txt';
	crowled = project_name + '/crowled.txt';
	if not os.path.isfile(queue):
		write_file(queue, base_url);
	if not os.path.isfile(crowled):
		write_file(crowled, '');

# Create the crowled list and queue list
def write_file(path, data):
	with open(path, 'w') as f:
		f.write(data);

# Add data onto an existing file
def append_to_file(path, data):
	with open(path, 'a') as f:
		f.write(data + '\n');

# Delete all the content of a file
def delete_file_contents(path):
	with open(path, 'w') as f:
		pass;

# Copy all the URLs in a file onto a set and return the set
def file_to_set(file_path):
	results = set();
	with open(file_path, 'rt') as f:
		for line in f:
			results.add(line.replace('\n',''));
	return results;

# Iterate through a set and copy all its content to a file
def set_to_file(links, file):
	delete_file_contents(file);
	for link in sorted(links):
		append_to_file(file, link);


