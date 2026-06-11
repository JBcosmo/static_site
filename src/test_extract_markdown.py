import unittest
from extract_markdown import *

class TestExtractImages(unittest.TestCase):
	def test_basic_find(self):
		matches = extract_markdown_images(
		"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
		
	def test_two_finds(self):
		matches = extract_markdown_images(
		"Text with one ![image](https:/link.png) and second ![image](https:/link2.png)")
		self.assertListEqual([("image", "https:/link.png"), ("image", "https:/link2.png")], matches)
	
class TestExtractTitle(unittest.TestCase):
	def test_heading_is_here(self):
		md = """
### This is not a title.

We have some **text**.

# This is a title!

And some more text.	
"""
		
		title = extract_title(md)
		
		shouldbe = "This is a title!"
		
		self.assertEqual(shouldbe, title)
	
	def test_no_title(self):
		md = """
### This is not a title.

We have some **text**.

#### This is not a title either.

And some more text.	
"""
		with  self.assertRaises(Exception) as raises:
			title = extract_title(md)
			
		self.assertIn("No title found in the markdown file!", str(raises.exception))

class TestBlocks(unittest.TestCase):
	def test_blank_str(self):
		text = """This is block 1.

		This is block 2.

		   

		This is block 3.
		"""
		
		blocks = markdown_to_blocks(text)
		
		shouldbe = ["This is block 1.","This is block 2.", "This is block 3."]
		
		self.assertEqual(shouldbe, blocks)
		
		
		
	def test_from_bootdev(self):
		md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
				"- This is a list\n- with items",
			],
		)
