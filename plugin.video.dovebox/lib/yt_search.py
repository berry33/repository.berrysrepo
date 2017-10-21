# -*- coding: utf-8 -*-

# Utils.py
# Copyright (C) Mick3yB0y <mickeyboy12345678@gmail.com>
#
# This module is open source; you can redistribute it and/or
# modify it under the terms of the GPL or Artistic License.
# These licenses are available at http://www.opensource.org
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


"""


def YT_Search(flag,url=''):

	import urllib,urllib2, xbmc, re, xbmcgui
	import Utils
	from bs4 import BeautifulSoup
	busy	= xbmcgui.DialogBusy()

	'''
	so as you can see, we have imported BS4 into this,
	mainly because we need to parse the page, the retun in kodi is not the
	same as the source you see on the internet, youtube make it
	really difficult to use it outside of their own API.

	anyway, with that said, we grab the page and scrape it for the results
	parsing it along the way, then we turn it back into the original
	text for the title with the 
	vid['title'] = u''.join(vid['title']).encode('utf-8').strip()
	beautifulsoup does some wierd stuff sometimes with ascii characters
	statement, this puts all the non ascii characters back in there
	we then put them all in the directory structure, this time we have to make the url human readable so that the youtube plugin can work on the url.

	so if you look in the utils adddir, you will see how it does it

	then we allow it to play

	'''
	if flag:
		kb = xbmc.Keyboard(None, 'Enter Search Terms')
		kb.doModal()
		if (kb.isConfirmed()):
			st = kb.getText()
			if (st is None or st == ''): 
				return
			st = st.replace(' ','+')
			url = "https://www.youtube.com/results?search_query=" + st
	req = urllib2.Request(url)
	req.add_header('accept-language','en-US,en;q=0.8,en-GB;q=0.6')
	busy.create()
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,"html.parser")
	response.close()
	url = []; title = []; thumb = [] ; user = []; nx = []
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		url.append(str(vid['href']))
		vid['title'] = u''.join(vid['title']).encode('utf-8').strip()
		title.append(str(vid['title']))
	for thum in soup.findAll(attrs={'class':"yt-thumb-simple"}):
		thum = str(thum)
	 	match=re.compile('src="((.+?).jpg)').findall(thum)
	 	if not match:
	 		match=re.compile('href="((.+?).jpg)').findall(thum)
	 		if not match:
	 			match=re.compile('data-thumb="((.+?).jpg)').findall(thum)
		for it in match:
			thumb.append(it[0])
	for use in soup.findAll(attrs={'class':'g-hovercard'}):
		use = re.compile('">(.+?)<').findall(str(use))
		if '<div' in str(use): use = ''
		use = ''.join(use)
		use = str(use)
		user.append(use)
	for desc in soup.findAll(attrs={'class':'yt-lockup-description'}):
		desc=str(desc)
		match = re.compile('tr">(.+?)<\/div').findall(desc)
		match = ''.join(match)
	for ne in soup.findAll(attrs={'class':'yt-uix-button vve-check yt-uix-sessionlink yt-uix-button-default yt-uix-button-size-default'}):
		nx.append(str(ne['href']))
	nxt = nx[-1]
	nxt = ''.join(nxt)
	nxt = 'https://www.youtube.com'+str(nxt)
	busy.close()
	x=0
	for i in url:
		try:
			Utils.addDir(dtype='',mode='utube',url=i,title='[COLOR white]'+title[x]+'[/COLOR] [COLOR orange]uploaded by[/COLOR][COLOR hotpink] '+user[x]+'[/COLOR]',thumb=thumb[x],fanart='https://img00.deviantart.net/d82d/i/2015/308/2/f/polish_youtube__fanart_by_kdr225-d9fi2xq.jpg',referer='',preview='',info='',year='',genre='',episodes='',seasons='',poster='',showcontext='',fav_mode='')
			x+=1
		except:pass
	Utils.addDir(dtype='f',mode='ytnxt',url=nxt,title='[COLOR red]Next Page[/COLOR]',thumb='http://cdn.mos.cms.futurecdn.net/SytNGv3ZxAVCkvcspmbbvh-320-80.jpg',fanart='https://img00.deviantart.net/d82d/i/2015/308/2/f/polish_youtube__fanart_by_kdr225-d9fi2xq.jpg',referer='',preview='',info='',year='',genre='',episodes='',seasons='',poster='',showcontext='',fav_mode='')
	return




def yt_link():
	import Utils,xbmcaddon

	'''
	just add a link to the start menu
	'''



	addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
	Utils.addDir(dtype='f', mode='ytsear', url='',preview='', 
			title='Search Youtube Here',thumb='http://cdn.mos.cms.futurecdn.net/SytNGv3ZxAVCkvcspmbbvh-320-80.jpg', 
			fanart=addon_fanart,info='', year='',genre='', episodes='',
			seasons='', poster='')
	return





def DM_Search(flag,url = ''):

	import urllib,urllib2, xbmc, re, xbmcgui,xbmcaddon
	import Utils
	from bs4 import BeautifulSoup
	busy	= xbmcgui.DialogBusy()
	addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')


	
	'''
	so as you can see, we have imported BS4 into this,
	mainly because we need to parse the page, the retun in kodi is not the
	same as the source you see on the internet, dailymotion make it
	really difficult to use it outside of their own API.

	anyway, with that said, we grab the page and scrape it for the results
	parsing it along the way, then we turn it back into the original
	text for the title with the 
	vid['title'] = u''.join(vid['title']).encode('utf-8').strip()
	statement, this puts all the non ascii characters back in there
	we then put them all in the directory structure, this time we have to make the url human readable so that the youtube plugin can work on the url.

	so if you look in the utils adddir, you will see how it does it

	then we allow it to play

	'''



	if flag:
		kb = xbmc.Keyboard(None, 'Enter Search Terms')
		kb.doModal()
		if (kb.isConfirmed()):
			st = kb.getText()
			if (st is None or st == ''): 
				return
			st = st.replace(' ','+')
			url = "http://www.dailymotion.com/ph/relevance/universal/search/"+st+'/1'
	req = urllib2.Request(url)
	req.add_header('accept-language','en-US,en;q=0.8,en-GB;q=0.6')
	req.add_header('ff','off')
	busy.create()
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,"html.parser")
	response.close()
	url = []; title = []; thumb = [] ; user = []; nx = []; dat = []
	for vid in soup.findAll(attrs={'class':'preview'}):
		thum = str(vid['data-src'])
		thum = ''.join(thum)
		thumb.append(str(thum))
		vid['title'] = u''.join(vid['title']).encode('utf-8').strip()
		tit = str(vid['title'])
		tit = ''.join(tit)
		title.append(str(tit))
	for own in soup.findAll(attrs={'class':'link-on-hvr'}):
		own = str(own)
		own = re.compile(' href="/(?:.+?)">(.+?)<').findall(own)
		own =''.join(own)
		user.append(str(own))
	user = user[3:]
	for da in soup.findAll(attrs={'class':'date'}):	
		da=str(da)
		da=re.compile('<span class="date">- (.+?)<').findall(da)
		da=''.join(da)
		dat.append(str(da))
	for ur in soup.findAll(attrs={'class':'sd_video_preview'}):
		ur = str(ur['data-id'])
		url.append(str(ur))	
	for nx in soup.findAll(attrs={'class':'pages align-center'}):
		matches = re.compile('href="(.+?)"').findall(str(nx))
		nxt=matches[-1]
	x = 0
	for i in url:
		Utils.addDir(dtype='',mode='intres',url='http://www.dailymotion.com/video/'+str(i),title='[COLOR white]'+str(title[x])+'[/COLOR] [COLOR orange]uploaded by[/COLOR][COLOR hotpink] '+str(user[x])+'[/COLOR] '+str(dat[x]),thumb=str(thumb[x]),fanart='https://img00.deviantart.net/d82d/i/2015/308/2/f/polish_youtube__fanart_by_kdr225-d9fi2xq.jpg',referer='',preview='',info='',year='',genre='',episodes='',seasons='',poster='',showcontext='',fav_mode='')
		x+=1
	Utils.addDir(dtype='f', mode='dmnxt', url='http://www.dailymotion.com'+str(nxt),preview='', 
			title='[COLOR red]Next Page[/COLOR]',thumb='http://www.epsilon-esports.com/news/wp-content/uploads/2014/03/logo-Dailymotion.png', 
			fanart=addon_fanart,info='', year='',genre='', episodes='',
			seasons='', poster='')

	return









def dm_link():
	import Utils,xbmcaddon

	'''
	just add a link to the start menu
	'''



	addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
	Utils.addDir(dtype='f', mode='dmsear', url='',preview='', 
			title='Search Dailymotion Here',thumb='http://www.epsilon-esports.com/news/wp-content/uploads/2014/03/logo-Dailymotion.png', 
			fanart=addon_fanart,info='', year='',genre='', episodes='',
			seasons='', poster='')
	return

def YT_Channels(url):
    import urllib,urllib2, xbmc, re, xbmcgui
    import Utils
    from bs4 import BeautifulSoup
    busy    = xbmcgui.DialogBusy()


    req = urllib2.Request(url)
    req.add_header('accept-language','en-US,en;q=0.8,en-GB;q=0.6')
    busy.create()
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,"html.parser")
    response.close()
    soup = re.split('<ul class="channels-browse-content-grid branded-page-gutter-padding grid-lockups-container" id="channels-browse-content-grid">',str(soup))
    soup = re.split('<div class="yt-lockup-notifications-container hid" style="height:110px"></div>',str(soup[1]))
    del soup[-1]
    match = re.compile('href="\/watch\?v=(.+?)"(?:[\s\S]+?)src="(.+?)\?(?:[\s\S]+?) dir="ltr" href="(?:.+?)title="(.+?)"')
    busy.close()
    for i in soup:
        matches = match.findall(i)
        Utils.addDir('','utube',matches[0][0],matches[0][2],matches[0][1],'',)
    return
