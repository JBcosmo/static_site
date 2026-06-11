import unittest
from block_to_block import *

class TestBlockToBlockType(unittest.TestCase):
	def test_headings(self):
		block = "### This is a block of text\nthat is a heading."
		block_type = block_to_block_type(block)
		
		self.assertEqual(BlockType.HEADING, block_type)
		
	def test_code(self):
		block = "```\nThis is some code\non multiple lines.```"
		block_type = block_to_block_type(block)
		
		self.assertEqual(BlockType.CODE, block_type)
		
	def test_quote(self):
		block = ">Some quote\n> on multiple lines\n>more quote"
		block_type = block_to_block_type(block)

		self.assertEqual(BlockType.QUOTE, block_type)

	def test_ordered_list(self):
		block = "1. This is an ordered list\n2. I hope I got it right"
		block_type = block_to_block_type(block)
		
		self.assertEqual(BlockType.ORDERED_LIST, block_type)
