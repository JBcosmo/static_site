import os
import shutil

def clear_destination(path):
	
	print(f"Clearing destination: {path}\n")
	
	if not os.path.exists(path):
		os.mkdir(path)
		return
		
	contents = os.listdir(path)
	for content in contents:
		content_full = os.path.join(path,content)
		if os.path.isdir(content_full):
			shutil.rmtree(content_full)
		else:
			os.remove(content_full)
			
	return
			

def list_to_copy(static, list_of_files, list_of_directories):
	
	contents = os.listdir(static)
	
	for content in contents:
		content = os.path.join(static,content)
		if os.path.isdir(content):
			list_of_directories.append(content)
			list_to_copy(content, list_of_files, list_of_directories)
		else:
			list_of_files.append(content)
			
	return
	

def copy_static_public(static, public):

	full_static = os.path.join(os.getcwd(), static)
	full_public = os.path.join(os.getcwd(), public)
	clear_destination(full_public)
	
	list_of_files = []
	list_of_directories = []
	list_to_copy(full_static, list_of_files, list_of_directories)
	
	print(f"List of files to copy: {list_of_files}")
	print(f"List of directories to create: {list_of_directories}\n")
	
	common = os.path.commonpath([full_static,full_public])
	
	for directory in list_of_directories:
		dir_path = full_public + directory.removeprefix(common+"/"+static)
		os.mkdir(dir_path)
		
	for file_path in list_of_files:
		new_path = full_public + file_path.removeprefix(common+"/"+static)
		shutil.copy(file_path, new_path)
		
	return
