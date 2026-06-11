from extract_markdown import *
from block_to_block import *
from htmlnode import *
from text_to_textnodes import *

def markdown_to_html_node(markdown):
	
	# Markdown split into blocks
	blocks = markdown_to_blocks(markdown)
	
	blocksHTML = []
	for block in blocks:
		block_type = block_to_block_type(block)
		block_text = strip_block(block)
		nodes = text_to_textnodes(block_text)
		
		match block_type:
			case BlockType.CODE:
				node = code_to_parent_child_pair(block_text)
			case BlockType.HEADING:
				hashes = str(block[0:6].count("#"))
				node = LeafNode("h"+hashes, block_text)
			case BlockType.QUOTE:
				children = text_to_children(block_text)
				node = ParentNode("blockquote", children)
			case BlockType.PARAGRAPH:
				children = text_to_children(block_text)
				node = ParentNode("p", children)
			case BlockType.UNORDERED_LIST:
				node = unordered_to_parent_node(block_text)
			case BlockType.ORDERED_LIST:
				node = ordered_to_parent_node(block_text)
		
		blocksHTML.append(node)
		
	finalHTML = ParentNode("div",blocksHTML)
	return finalHTML
				
	
def strip_block(block):
	block_type = block_to_block_type(block)
	
	match block_type:
		case BlockType.CODE:
			block = block.strip("```")
			block = block.removeprefix("\n")
			return block
		case BlockType.HEADING:
			hashes = block[0:6].count("#")
			block = block.removeprefix(hashes*"#"+" ")
			return block
		case BlockType.PARAGRAPH:
			block = block.replace("\n"," ")
			return block
		case BlockType.QUOTE:
			lines = block.split("\n")
			for i in range(len(lines)):
				lines[i] = lines[i].removeprefix(">")
				lines[i] = lines[i].strip()
			block = "\n".join(lines)
			return block
		case _:
			return block
			
def unordered_to_parent_node(unordered_list):
	items = unordered_list.split("\n")
	
	item_nodes = []
	for i in range(len(items)):
		items[i] = items[i].strip("- ")
		children_nodes = text_to_children(items[i])
		item_nodes.append(ParentNode("li",children_nodes))
		
	parent = ParentNode("ul",item_nodes)
	
	return parent
	
	
def ordered_to_parent_node(ordered_list):
	items = ordered_list.split("\n")
	
	item_nodes = []
	for i in range(len(items)):
		items[i] = items[i].strip(str(i+1)+". ")
		print(items[i])
		children_nodes = text_to_children(items[i])
		item_nodes.append(ParentNode("li", children_nodes))
		
	parent = ParentNode("ol", item_nodes)
	
	return parent


def code_to_parent_child_pair(code_block):
	
	child = LeafNode("code", code_block)
	parent = ParentNode("pre",[child])
	
	return parent
	

def text_to_children(text):
	
	children = []
	text_nodes = text_to_textnodes(text)
	
	for node in text_nodes:
		match node.text_type:
			case TextType.PLAIN:
				children.append(LeafNode("",node.text))
			case TextType.BOLD:
				children.append(LeafNode("b",node.text))
			case TextType.ITALIC:
				children.append(LeafNode("i",node.text))
			case TextType.CODE:
				children.append(LeafNode("code",node.text))
			case TextType.IMAGE:
				tag_dict = {"src":node.url, "alt":node.text}
				children.append(LeafNode("img","",tag_dict))
			case TextType.LINK:
				children.append(LeafNode("a",node.text,{"href":node.url}))
	
	return children
				
