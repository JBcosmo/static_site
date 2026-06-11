import re
from block_to_block import *

def extract_markdown_images(text):
	images = re.findall(r"\!\[(.*?)\]\((.*?)\)",text)

	return images

def extract_markdown_links(text):
	# anchors = re.findall(r"\[(.*?)\]", text)
	# urls = re.findall(r"\((.*?)\)", text)
	
	# if len(anchors) != len(urls):
		# raise ValueError(f"Error: incorrect markdown syntax! {text}")
	
	# result = []
	# for i in range(len(anchors)):
		# duo = (anchors[i], urls[i])
		# result.append(duo)
		
	images = re.findall(r"\[(.*?)\]\((.*?)\)",text)
		
	return images
	

def markdown_to_blocks(markdown):
	blocks = markdown.split("\n\n")
	i = 0
	while i < len(blocks):
		blocks[i] = blocks[i].strip()
		if blocks[i] == "":
			blocks.pop(i)
			i -= 1
		i += 1
	
	return blocks
		
		
def extract_title(markdown):
	blocks = markdown_to_blocks(markdown)
	
	for block in blocks:
		block_type = block_to_block_type(block)
		if block_type == BlockType.HEADING:
			hashes = block[0:6].count("#")
			if hashes == 1 and block[0:2] == "# ":
				return block[2:]
				
	raise Exception("No title found in the markdown file!")
