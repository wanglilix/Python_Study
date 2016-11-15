from xml.sax.handler import ContentHandler
from xml.sax import parse
import os

class Dispatcher:
	def dispatch(self,perfix,name,attrs= None)
		mname = prefix + name.capitalize()
		dname = 'default' + prefix.captalize()
		method = getattr(self,mname,None)
		if callable(method):
			args = ()
		else:
			method = getattr(self,dname,None)
			args = name
		if prefix == 'start':
			args += attrs
		if callable(method):
			method(*args)
	
	def startElement(self,name,attrs):
		self.dispatch('start',mname,attrs)
		
	def endElement(self,name):
		self.dispatch('end',name)
		
class WebsiteConstructor(Dispatcher,ContentHandler):
	
		