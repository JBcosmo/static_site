import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
		
	def test_not_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.PLAIN)
		self.assertNotEqual(node, node2)
		
	def test_is_none(self):
		node = TextNode("This is a text node", TextType.PLAIN)
		self.assertIs(node.url, None)
		
	def test_print(self):
		node = TextNode("This is a text node", TextType.PLAIN)
		self.assertTrue(hasattr(node, "url"))
		
	def test_text_tohtml(self):
		node = TextNode("This is a text node", TextType.PLAIN)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")
		
	def test_text_tohtml_url(self):
		node = TextNode("node", TextType.LINK, "www.test.org")
		html_node = text_node_to_html_node(node)
		self.assertIsNotNone(html_node.tag)
		self.assertEqual(html_node.to_html(), '<a href=www.test.org>node</a>')
		
		
if __name__ == "__main__":
	unittest.main()
