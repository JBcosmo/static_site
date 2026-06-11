from split_nodes import *
from textnode import *

def text_to_textnodes(text):
	delimiters = {"**": TextType.BOLD,
				"_": TextType.ITALIC,
				"`": TextType.CODE}
				
	initial_node = TextNode(text, TextType.PLAIN)
	
	nodes = [initial_node]
	for delimiter in list(delimiters):
		delim_nodes = split_nodes_delimiter(nodes, delimiter, delimiters[delimiter])
		nodes = delim_nodes
	
	delimimage_nodes = split_nodes_image(delim_nodes)
	
	final = split_nodes_link(delimimage_nodes)
	
	return final
