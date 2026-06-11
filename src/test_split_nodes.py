import unittest
from textnode import *
from split_nodes import *

class TestDelimiter(unittest.TestCase):
	def test_not_closed(self):
		node = TextNode("I forgot **to close", TextType.PLAIN)
		
		with self.assertRaises(ValueError) as raises:
			split_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
			
		exception = raises.exception
		self.assertEqual(exception.args[0], "Error: delimiter not closed somewhere!")
				
	def test_is_okay_in_general(self):
		node = TextNode("Not bold **bold** not bold", TextType.PLAIN)
		split_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
		test = [TextNode("Not bold ", TextType.PLAIN), 
				TextNode("bold", TextType.BOLD),
				TextNode(" not bold", TextType.PLAIN)]
		self.assertEqual(split_nodes, test)

class TestSplitImage(unittest.TestCase):
	def test_is_ok(self):
		node = TextNode("image ![image](https://image.png)",TextType.PLAIN)
		
		split_nodes = split_nodes_image([node])
		
		test = [TextNode("image ", TextType.PLAIN),
				TextNode("image", TextType.IMAGE, "https://image.png")]
				
		self.assertEqual(split_nodes, test)

	def test_several_images(self):
		text = "image1 ![image1](https://image1.png)"
		text += "image2 ![image2](https://image2.png)"
		text += "image3 ![image3](https://image3.png)"
		
		node = TextNode(text, TextType.PLAIN)
		split_nodes = split_nodes_image([node])
		
		test = [TextNode("image1 ", TextType.PLAIN),
				TextNode("image1", TextType.IMAGE, "https://image1.png"),
				TextNode("image2 ", TextType.PLAIN),
				TextNode("image2", TextType.IMAGE, "https://image2.png"),
				TextNode("image3 ", TextType.PLAIN),
				TextNode("image3", TextType.IMAGE, "https://image3.png")]
				
		self.assertEqual(split_nodes, test)
		

	def test_text_past_image(self):
		text = "image1 ![image1](https://image1.png) and some text"
		
		node = TextNode(text, TextType.PLAIN)
		split_nodes = split_nodes_image([node])
	
		test = [TextNode("image1 ", TextType.PLAIN),
				TextNode("image1", TextType.IMAGE, "https://image1.png"),
				TextNode(" and some text", TextType.PLAIN)]
				
		self.assertEqual(split_nodes, test)
		

class TestSplitLink(unittest.TestCase):
	def test_is_ok(self):
		node = TextNode("link [link](https://link.png)",TextType.PLAIN)
		
		split_nodes = split_nodes_link([node])
		
		test = [TextNode("link ", TextType.PLAIN),
				TextNode("link", TextType.LINK, "https://link.png")]
				
		self.assertEqual(split_nodes, test)

	def test_several_images(self):
		text = "link1 [link1](https://link1.png)"
		text += "link2 [link2](https://link2.png)"
		text += "link3 [link3](https://link3.png)"
		
		node = TextNode(text, TextType.PLAIN)
		split_nodes = split_nodes_link([node])
		
		test = [TextNode("link1 ", TextType.PLAIN),
				TextNode("link1", TextType.LINK, "https://link1.png"),
				TextNode("link2 ", TextType.PLAIN),
				TextNode("link2", TextType.LINK, "https://link2.png"),
				TextNode("link3 ", TextType.PLAIN),
				TextNode("link3", TextType.LINK, "https://link3.png")]
				
		self.assertEqual(split_nodes, test)
