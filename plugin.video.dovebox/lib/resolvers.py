# -*- coding: utf-8 -*-

# Utils.py
# Copyright (C) Mick3yB0y <mickeyboy12345678@gmail.com>
#
# This module is open source; you can redistribute it and/or
# modify it under the terms of the GPL or Artistic License.
# These licenses are available at http://www.opensource.orgxbmc.log('####################3 '+str(url),2)
#
# This software must be used and distributed in accordance
# with the law. The author claims no liability for its
# misuse.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""
Simply a Template or a Stepping stone.

This Template has been coded for kodi using python 2.7.
Hopefully, it is clear enough for you to understand the
processess as they happen, and you find it easy enough to 
follow and to use.

I have tried to make it as general and diverse as possible,
so as to help those who have no desire to get into the code
aspect, and just want to put a link in that works.

There is a tutorial to go with this template, find it on my 
youtube channel, email address above, and spread the word.
template updates will come from there, also new stuff added will have
its own tutorial.

Have fun, and dont do anything Illegal

Mick3yB0y


Basically, this is just an exercise to show you how
resolvers work, feel free to add your own resolvers on here 
dont forget to add them to the resolve function.

"""
import xbmcgui
busy = xbmcgui.DialogBusy()


def Resolve(url,title,thumb):
	import xbmc
	if 'dailymotion' in url: link,title,thumb = DMres(url,title,thumb)
	elif 'liveonlinetv247' in url: link,title,thumb = L247res(url,title,thumb)
	elif 'fmovies' in url: link,title,thumb = Fmres(url,title,thumb)
	elif 'streamlive.to' in url: link,title,thumb = SLres(url,title,thumb)
	elif 'topchristianmovies' in url:link,title,thumb = Tcm(url, title, thumb)
	elif 'estream.to' in url: link,title,thumb = Estream_res(url,title,thumb)
	elif 'vshare' in url: link,title,thumb = Vshare(url,title,thumb)
	# add your own resolvers here

	# before this line
	else: link,title,thumb = Genres(url,title,thumb)
	return link,title,thumb

def DMres(url,title='',thumb=''):
	import re
	import Net
	busy.create()
	if not 'embed' in url:
		part = url.rsplit('/', 1)[-1]
		url = 'http://www.dailymotion.com/embed/video/'+part
	headers = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'), ('Cookie', 'ff=off')]
	content = Net.Read_It_Full(url,headers)
	link = []; res = []
	try:
		lin = re.search('=144\"[\}],[\{]\"type\":\"video\\\/mp4\",\"url\":\"(http.+?)\"[\}][\]]',content).group(1)
		lin = re.sub(r'\\','', lin)
		link.append(lin)
		if lin: res.append('144')
	except: pass
	try:
		lin = re.search('=240\"[\}],[\{]\"type\":\"video\\\/mp4\",\"url\":\"(http.+?)\"[\}][\]]',content).group(1)
		lin = re.sub(r'\\','', lin)
		link.append(lin)
		if lin: res.append('240')
	except: pass
	try:
		lin = re.search('=380\"[\}],[\{]\"type\":\"video\\\/mp4\",\"url\":\"(http.+?)\"[\}][\]]',content).group(1)
		lin = re.sub(r'\\','', lin)
		link.append(lin)
		if lin: res.append('380')
	except: pass
	try:
		lin = re.search('=480\"[\}],[\{]\"type\":\"video\\\/mp4\",\"url\":\"(http.+?)\"[\}][\]]',content).group(1)
		lin = re.sub(r'\\','', lin)
		link.append(lin)
		if lin: res.append('480')
	except: pass
	try:
		lin = re.search('=720\"[\}],[\{]\"type\":\"video\\\/mp4\",\"url\":\"(http.+?)\"[\}][\]]',content).group(1)
		lin = re.sub(r'\\','', lin)
		link.append(lin)
		if lin: res.append('720')
	except: pass
	busy.close()
	link, title, thumb = Choose_res(link,res,title,thumb)
	re.purge				
	return link, title, thumb

def L247res(url,title,thumb):
	import Net
	import re
	busy.create()
	if not 'embed' in url:
		part = url.rsplit('/', 1)[-1]
		url = 'http://www.liveonlinetv247.info/embed/'+part
	headers = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')]
	content	= Net.Read_It_Full(url,headers)
	link	= re.compile('<source src="(.+?)"').findall(content)
	link 	= ''.join(link)
	url 	= link+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
	busy.close()
	re.purge
	return url,title,thumb
	
def Fmres(url,title,thumb):
	import Net
	import re
	busy.create()
	link = []; res = []
	headers = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')]
	content	= Net.Read_It_Full(url,headers)
	content = re.split('player current',content)
	content = re.split('<article class="player"',content[1])
	lin 	= re.search('src="(.+?)"',content[0]).group(1)
	lin 	= 'http:'+str(lin)
	content	= Net.Read_It_Full(lin,headers)
	content = re.split('video id="my-video-player"',content)
	content = re.split('<script>',content[1])
	content = re.split('source ',content[0])
	del content[0]
	match 	= re.compile("(?is)src='(.+?)' type(?:.+?)label='(.+?)'")
	for i in content:
		lin = match.findall(i)
		link.append(lin[0][0])
		res.append(lin[0][1])
	busy.close()
	link,title,thumb = Choose_res(link,res,title,thumb)
	re.purge
	return link,title,thumb

def SLres(url,title='',thumb=''):
	import Net
	import re, xbmc
	busy.create()
	headers = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')]
	contenta= Net.Read_It_Full(url,headers)
	content = re.split('<div id="container"></div>',contenta)
	content = re.split('<div class="col-md-3 col-sm-3 col-lg-3" style="padding-top:150px;">',content[1])
	wrkfl = re.search(r'(?s)return\(\["\\\/","\\\/"(.+?)\]\.join\(""\) \+ ', content[0]).group(1)
	var1 = re.search(r'(?s)\]\.join\(""\) \+ (.+?)\.join\(""\)',content[0]).group(1)
	var2 = re.search(r'(?s)getElementById\("(.+?)"\)\.innerHTML\)',content[0]).group(1)
	wrkfl = re.sub(r'\\','', wrkfl)
	wrkfl = re.sub(r'"','', wrkfl)
	wrkfl = re.sub(r',','', wrkfl)
	wrkfl = 'https://'+wrkfl
	var1 = re.search(r'(?s)var '+str(var1)+' \= \[(.+?)\]\;',content[0]).group(1)
	var1 = re.sub(r',','', var1)
	var1 = re.sub(r'"','', var1)
	var2 = re.search(r'(?s)id\='+str(var2)+'>(.+?)<\/span><span style\=\'display\:none\'',contenta).group(1)
	link = str(wrkfl)+str(var1)+str(var2)
	busy.close()
	re.purge
	return link,title,thumb

def Genres(url,title='',thumb=''):
	import Net
	import re, xbmc
	headers = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')]
	content= Net.Read_It_Full(url,headers)
	knwn = ['.m3u8','.mp4','.mkv']
	for i in knwn:
		if str(i) in content:
			match = re.search(r'(?:href=|src=|file:)(.+?'+i+r'.+?[^\'"\;\]\}\, >]+)',content).group(1)
			if match:
				match = re.sub(r'"','', match)
				match = re.sub(r"'","", match)
				match = match+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
				break
	re.purge
	if match: return match,title,thumb
	else: return '',title,thumb

def Tcm(url, title, thumb):
	import Net
	import re
	busy.create()
	headers = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')]
	content = Net.Read_It_Full(url,headers)
	src = re.search('<iframe src="(.+?)"',content).group(1)
	content = Net.Read_It_Full(src,headers)
	link = re.findall('<source src="(.+?)"',content)
	busy.close()
	re.purge
	return link[0],title,thumb

def Estream_res(url,title,thumb):
	import Net
	import re
	busy.create()
	headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')]
	if not 'embed' in url:
		url = re.search('-(.+?)$',url).group(1)
		prt = 'https://estream.to/embed'
		url = prt+url
	content = Net.Read_It_Full(url,headers)
	link = re.findall('<source src="(.+?)\/>',content)
	if len(link)>1:
		res = []
		for i in link:
			try:
				r = re.search("res='(.+?)'",i).group(1)
			except:
				r = 'Auto'
			res.append(r)
		busy.close()
		link, title, thumb = Choose_res(link,res,title,thumb)
	busy.create()
	link = re.search('(^.+?)"',link).group(1)
	link = link+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
	busy.close()
	re.purge
	return link, title, thumb

def Vshare(url,title,thumb):
	import Net
	import re, xbmc
	busy.create()
	if not 'embed' in url:
		url1 = re.split('vshare.eu/',url)
		url = 'http://vshare.eu/embed-'+url1[1]+'-729x400.html'
	headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36')]
	content = Net.Read_It_Full(url,headers)
	link = re.search('<source src="(.+?)".+?type="video/.+?">',content).group(1)
	link = link+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36&Referer='+url
	busy.close()
	re.purge
	return link, title, thumb

def Choose_res(link,res,title='',thumb=''):
	import xbmcgui
	List=[]; ListU=[]; c=0
	for i in link:
		c=c+1; List.append('[B][COLOR cyan]Play link Num [/COLOR][/B]['
			+str(c)+']  @ '+res[c-1]+'P for '+title); ListU.append(i)
		
		''' above lines make a list of items '''

	dialog 	= xbmcgui.Dialog()
	rNo 	= dialog.select(' Link Resolution, Select A link.', List)
	if rNo>=0:
		rName 	=title
		rURL 	=str(ListU[rNo])
		# choose a link and return it
		return rURL, title, thumb


