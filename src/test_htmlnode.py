import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
	def test_prints_ok(self):
		node = HTMLNode(tag="p",value="sample text")
		print(node)
		
	def test_to_html(self):
		node = HTMLNode(tag="p",value="sample text")
		self.assertRaises(NotImplementedError, node.to_html)
		
	def test_is_none(self):
		node = HTMLNode(tag="p",value="sample text")
		self.assertIsNone(node.children)
		
class TestLeafNode(unittest.TestCase):
	def test_prints_ok(self):
		node = LeafNode(tag="p",value="sample text")
		print(node)

	def test_leaf_to_html_print(self):
		node = LeafNode("p", "sample text")
		self.assertEqual(node.to_html(), "<p>sample text</p>")
		
	def test_is_none(self):
		node = LeafNode("p", "sample text")
		self.assertIsNone(node.props)
		
		
class TestParentNode(unittest.TestCase):
	def test_to_html(self):
		node = LeafNode(tag="p",value="sample text")
		parent_node = ParentNode("p",[node])
		self.assertEqual(parent_node.to_html(), "<p><p>sample text</p></p>")

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

		
if __name__ == "__main__":
	unittest.main()
