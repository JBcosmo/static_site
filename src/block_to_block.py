from enum import Enum

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "quote"
	UNORDERED_LIST = "unordered list"
	ORDERED_LIST = "ordered list"
	
def block_to_block_type(block):
	
	hashes = block[0:6].count("#")
	if hashes > 0:
		prefix = hashes*"#"
		if block.startswith(prefix+" "):
			block_type = BlockType.HEADING
			return block_type
			
	if block.startswith("```\n") and block.endswith("```"):
		block_type = BlockType.CODE
		return block_type
		
	lines = block.splitlines()
	
	quote = True
	unordered_list = True
	ordered_list = True
	numbers = []
	
	for line in lines:
		if line[0] != ">":
			quote = False
		if line[0:2] != "- ":
			unordered_list = False
		temp = line.split(". ",1)
		numbers.append(temp[0])
		if not temp[0].isnumeric():
			ordered_list = False
			
	if ordered_list:
		for i in range(len(lines)):
			if numbers[i] != str(i+1):
				ordered_list = False
			
	if quote:
		return BlockType.QUOTE
	if unordered_list:
		return BlockType.UNORDERED_LIST
	if ordered_list:
		return BlockType.ORDERED_LIST
	
	return BlockType.PARAGRAPH
