from copy_static_public import *
from generate_page import *
import sys

def main():
	
	basepath = sys.argv[1]
	if not basepath:
		basepath = "/"
	
	print("Copying the static directory into the docs directory...\n")
	copy_static_public("static", "docs")
	print("Copying done!\n")
	
	generate_pages_recursive(basepath, "content", "template.html", "docs")
	
	
main()
