import os
from markdown_to_html import *
from extract_markdown import extract_title

def generate_page(basepath, from_path, template_path, dest_path):
	
	cwd = os.getcwd()
	full_from = os.path.join(cwd, from_path)
	full_template = os.path.join(cwd, template_path)
	full_dest = os.path.join(cwd, dest_path)
	
	print(f"Generating page from {full_from} to {full_dest} using {full_template}...\n")
	
	with open(full_from) as f:
		markdown = f.read()
		
	if markdown != "":
		print(f"Markdown read successfully.")
	else:
		raise ValueError("Markdown read failed. File empty?")

	with open(full_template) as t:
		template = t.read()
	
	if template != "":
		print(f"Template read successfully.\n")
	else:
		raise ValueError("Template read failed. File empty?")
	
	
	contents = markdown_to_html_node(markdown).to_html()
	title = extract_title(markdown)
	
	template = template.replace("{{ Title }}", title)
	page = template.replace("{{ Content }}", contents)
	page = page.replace("href=\"/", f"href=\"{basepath}")
	page = page.replace("src=\"/", f"src=\"{basepath}")

	
	split_dest = os.path.split(full_dest)
	if not os.path.exists(split_dest[0]):
		os.mkdir(split_dest[0])
		
	with open(full_dest, "w") as d:
		d.write(page)

	print(f"Page generated and saved.")
	
	return


def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
	
	cwd = os.getcwd()
	full_from = os.path.join(cwd, dir_path_content)
	full_template = os.path.join(cwd, template_path)
	full_dest = os.path.join(cwd, dest_dir_path)
	
	dir_contents = os.listdir(full_from)
	
	with open(full_template) as t:
		template = t.read()
	
	for item in dir_contents:
		item_full = os.path.join(full_from, item)
		print(f"Item: {item_full}")
		
		if os.path.isdir(item_full):
			print("It's a directory! Going down...")
			recursive_path = os.path.join(dir_path_content,item)
			dest_recursive = os.path.join(dest_dir_path, item)
			if not os.path.exists(os.path.join(cwd, dest_recursive)):
				os.mkdir(os.path.join(cwd, dest_recursive))
			generate_pages_recursive(basepath,recursive_path, template_path, dest_recursive)
		
		if item[-2:] == "md" and os.path.isfile(item_full):
			with open(item_full) as f:
				markdown = f.read()
			contents = markdown_to_html_node(markdown).to_html()
			title = extract_title(markdown)
	
			template = template.replace("{{ Title }}", title)
			page = template.replace("{{ Content }}", contents)
			page = page.replace("href=/", f"href={basepath}")
			page = page.replace("src=\"/", f"src=\"{basepath}")
			print(page)
	
			dest_file = os.path.join(full_dest,item)
	
			split_dest = os.path.split(dest_file)
			if not os.path.exists(dest_file[0]):
				os.mkdir(split_dest[0])
			
			dest_file = dest_file.removesuffix(".md") + ".html"
			print(f"Saving HTML file in {dest_file}")
			with open(dest_file, "w") as d:
				d.write(page)
			
	
	return
