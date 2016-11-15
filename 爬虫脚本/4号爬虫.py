#!/usr/bin/env python
# encoding: utf-8

import re
import os
import os.path
import requests
import wx

class GameSkyCrawler():
	"""抓取游民星空的高清壁纸"""
	def __init__(self):
		"""魔法方法"""
		self.homeUrl = "http://www.gamersky.com/ent/201608/792791.shtml"
		self.homeUrlCPY = self.homeUrl
		self.images = []
		if not os.path.exists('./images'):
			os.mkdir('./images')
	
	def seturl(self,url):
		self.homeUrl = url
		self.homeUrlCPY = url
		
	def __load_homePage(self):
		"""加载主页面"""
		return requests.get(url = self.homeUrl).content
	
	def __save_image(self, imageName, content):
		""" 保存图片 """
		fp = open(imageName, 'wb')
		fp.write(content)
	
	def __process_data(self,htmlPage):
		"""从html中提取图片信息"""
		prog = re.compile(r'<p align="center">.*\n.*')
		appPins = prog.findall(htmlPage)
		# 将js中的null定义为Python中的None
		null = None
		true = True
		if appPins == []:
			return None
		#字符串转为字典
		prog2 = re.compile(r'(id_gamersky.shtml\?)(.*?)(">)')
		#prog3 = re.compile(r'(\.)(.*?)("><img )')
		prog4 = re.compile(r'(\n)(.*?)(</p>)')
		for i in appPins:
			info = {}
			imgurl = prog2.search(i).group(2)
			info['url'] = imgurl
			type = info['url'].split('.')[-1]
			name = info['url'].split('.')[-2]
			name = name.split(r'/')[-1]
			info['type'] = name+'.'+type
			self.images.append(info)
		return True
			
	def get_image_info(self):
		"""得到图片信息"""
		self.__process_data(self.__load_homePage())
		i = 2
		while i :
			try:
				Urlpice = self.homeUrlCPY.split('.')
				Urlpice[-2] =  Urlpice[-2] + '_' + str(i)
				self.homeUrl = '.'.join(Urlpice)
				i += 1 
				if None == self.__process_data(self.__load_homePage()):
					i = 0
			except:
				i = 0
				
	def down_images(self):
		""" 下载图片 """
		print "{} image will be download".format(len(self.images))
		for key, image in enumerate(self.images):
			print 'download {0} ...'.format(key)
			try:
				req = requests.get(image["url"])
			except :
				print 'error'
			imageName = os.path.join("./images", image["type"])
			self.__save_image(imageName, req.content)
			
			
			
			
def save(event):
	GSC = GameSkyCrawler()
	GSC.seturl(Url.GetValue())
	GSC.get_image_info()
	GSC.down_images()
	
	
	
if __name__ == '__main__':
	app = wx.App()
	win = wx.Frame(None,title = 'Save GameSky Image',size=(410,335))
	bkg = wx.Panel(win)
	
	saveButton = wx.Button(bkg,label='Save')
	saveButton.Bind(wx.EVT_BUTTON,save)
	
	Url = wx.TextCtrl(bkg,style= wx.TE_MULTILINE|wx.HSCROLL)
	
	hbox = wx.BoxSizer()
	hbox.Add(saveButton)
	
	vbox = wx.BoxSizer(wx.VERTICAL)
	vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
	vbox.Add(Url,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
	
	bkg.SetSizer(vbox)
	win.Show()
	
	
	app.MainLoop()
	
	
	
	


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
