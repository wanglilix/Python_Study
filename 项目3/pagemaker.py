from xml.sax.handler import ContentHandler
from xml.sax import parse

class HeadlineHandler(ContentHandler):

	in_headline=False
	
	def __init__(self,headlines):
		ContentHandler.__init__(self)
		self.headlines = headlines
		self.data = []
	
	def startElement(self,name,attrs):
		if name=='hl':
			self.in_headline = True
			
	def endElement(self,name):
		if name == 'hl':
			text = ''.join(self.data)
			self.data = []
			self.headlines.append(text)
			self.in_headline = False
	
	def characters(self,string):
		if self.in_headline:
			self.data.append(string)
	
	
class PageMaker(ContentHandler):
	passthrough = False
	def startElement(self,name,attrs):
		if name == 'page':
			self.passthrough = True
			self.out = open(attrs['name']+'.html','w')
			self.out.write('<html><head>\n')
			self.out.write('<title>%s</title>\n'% attrs['title'])
			self.out.write('</head><body>\n')
		elif self.passthrough:
			self.out.write('<'+name)
			for key,val in attrs.items():
				self.out.write('%s="%s"'%(key,val))
			self.out.write('>')
	
	def endElement(self,name):
		if name == 'page':
			self.passthrough = False
			self.out.write('\n<body></html>\n')
			self.out.close()
		elif self.passthrough:
			self.out.write('</%s>'%name)

	def characters(self,chars):
		if self.passthrough: 
			self.out.write(chars)


# headlines = []
# parse('website.xml',HeadlineHandler(headlines))

# print 'The following<HL>elements were found:'
# for i in headlines:
	# print i

parse('website.xml',PageMaker())










