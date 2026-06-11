from textnode import *
from extract_markdown import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
	new_nodes = []
	
	for node in old_nodes:
		# We want to append this as is if text is not plain
		if node.text_type != TextType.PLAIN:
			new_nodes.append(node)
			continue
		
		text = node.text
		blocks = text.split(delimiter)
		if len(blocks) % 2 == 0:
			raise ValueError("Error: delimiter not closed somewhere!")
			
		for i in range(len(blocks)):
			if i % 2 == 0:
				new_nodes.append(TextNode(blocks[i], TextType.PLAIN))
			if i % 2 == 1:
				new_nodes.append(TextNode(blocks[i], text_type))
		
	i = 0
	while i < len(new_nodes):
		if new_nodes[i].text == "":
			new_nodes.pop(i)
			i -= 1
		i += 1
	
	return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
	new_nodes = []
	
	for node in old_nodes:
		images = extract_markdown_images(node.text)
		if images == []:
			new_nodes.append(node)
			continue
		
		text = node.text
		for image in images:
			image_format = (f"![{image[0]}]({image[1]})")
			split = text.split(image_format, 1)
			new_nodes.append(TextNode(split[0], TextType.PLAIN))
			image_node = TextNode(image[0], TextType.IMAGE, image[1])
			new_nodes.append(image_node)
			text = split[1]
			
		new_nodes.append(TextNode(text, TextType.PLAIN))
	
	i = 0
	while i < len(new_nodes):
		if new_nodes[i].text == "":
			new_nodes.pop(i)
			i -= 1
		i += 1
	
	# for i in range(len(new_nodes)):
		# if new_nodes[i].text == "":
			# new_nodes.pop(i)
			
	return new_nodes
			
			
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
	new_nodes = []
	
	for node in old_nodes:
		links = extract_markdown_links(node.text)
		if links == []:
			new_nodes.append(node)
			continue
		
		text = node.text
		for link in links:
			link_format = (f"[{link[0]}]({link[1]})")
			split = text.split(link_format, 1)
			new_nodes.append(TextNode(split[0], TextType.PLAIN))
			link_node = TextNode(link[0], TextType.LINK, link[1])
			new_nodes.append(link_node)
			text = split[1]
			
	i = 0
	while i < len(new_nodes):
		if new_nodes[i].text == "":
			new_nodes.pop(i)
			i -= 1
		i += 1
			
	return new_nodes
			
			
