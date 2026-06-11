class HTMLNode:
	
	def __init__(self, tag = None, value = None, children = None, props = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("TBD")
	
	def props_to_html(self):
		formatted = ""
		if self.props != None:
			for key in self.props:
				formatted += f" {key}={self.props[key]}"
		return formatted
	
	def __repr__(self):
		return f"HTMLNode(tag={self.tag},value={self.value},children={self.children},props={self.props})"
		
		
class LeafNode(HTMLNode):
	
	def __init__(self, tag, value, props=None):
		super().__init__(tag=tag, value=value, props=props)
	
	def to_html(self):
		if self.value == None:
			raise ValueError("Error: leaf node without a value!")
			
		if self.props != None:
			formatted_props = self.props_to_html()
		else:
			formatted_props = ""
	
		if self.tag == "": # this means it's plain text
			return self.value
		if self.tag == "img":
			return (f"<{self.tag}{formatted_props}>")
		else:
			return (f"<{self.tag}{formatted_props}>{self.value}</{self.tag}>")
		
	def __repr__(self):
		return f"LeafNode(tag={self.tag},value={self.value},props={self.props})"
		

class ParentNode(HTMLNode):
	
	def __init__(self, tag, children, props = None):
		super().__init__(tag=tag, children=children, props=props)
		
	def to_html(self):
		if self.tag == None:
			raise ValueError("Error: parent node with no tag!")
		
		if self.children == None:
			raise ValueError("Error: parent node with no children!")
			
		if self.props != None:
			formatted_props = self.props_to_html()
		else:
			formatted_props = ""
			
		formatted = f"<{self.tag}{formatted_props}>"
		
		for child in self.children:
			formatted += child.to_html()
			
		formatted += f"</{self.tag}>"
		
		return formatted
			
