import unittest
from markdown_to_html import *

class TestStripBlock(unittest.TestCase):
	def test_quote(self):
		block = ">Some quote\n> on multiple lines\n>more quote"
		shouldbe = "Some quote\non multiple lines\nmore quote"
		
		result = strip_block(block)
		
		self.assertEqual(shouldbe, result)
		
	def test_code_strip(self):
		code = """
```
This is some code.
```
"""
		shouldbe = "This is some code.\n"
		
		code = markdown_to_blocks(code)[0]
		result = strip_block(code)
		
		self.assertEqual(shouldbe, result)
		
		
class TestCodeToParentChildPair(unittest.TestCase):
	def test_code(self):
		md = "This is some code."
		node = code_to_parent_child_pair(md)
		html = node.to_html()
		
		shouldbe = "<pre><code>This is some code.</code></pre>"
		
		self.assertEqual(shouldbe, html)
		
		

class TestMarkdownToHTML(unittest.TestCase):
	def test_paragraphs(self):
		md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
		)

	def test_codeblock(self):
		md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
		)
