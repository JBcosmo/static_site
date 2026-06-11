from copy_static_public import *
from generate_page import *

def main():
	
	print("Copying the static directory into the public directory...\n")
	copy_static_public("static", "public")
	print("Copying done!\n")
	
	generate_pages_recursive("content", "template.html", "public")
	
	
main()
