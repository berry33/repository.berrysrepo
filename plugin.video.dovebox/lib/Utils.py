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
import xbmcaddon
import Fav

addon 		 = xbmcaddon.Addon()
addon_path	 = addon.getAddonInfo('path')
addon_name 	 = addon.getAddonInfo('name')
addon_icon 	 = addon.getAddonInfo('icon')
addon_fanart = addon.getAddonInfo('fanart')






def addDir(dtype='',mode='',url='',title='',thumb='',fanart='',
	referer='',preview='',info='',year='',genre='',episodes='',
	seasons='',poster='',showcontext='',fav_mode='',mode1=''):

	import sys, urllib, xbmcgui, xbmcplugin,xbmc
	contextMenu =[]
	'''
	Takes any ammount of parameters, but if not present, will not use
	them. 

	usage
	from main py
	import Utils
	Utils.addDir(dir_type=dtype[0], mode=param['mode'], url=param['url'],
				   preview=param['preview'], title=param['title'],
				   thumb=param['thumb'], fanart=param['fanart'],
				   info=param['info'], year=param['date'],
				   genre=param['genre'], episodes=param['episode'],
				   seasons=param['seasons'], poster=param['poster'])
	'''
	mode, url = Check_mode(mode,url,title,thumb,referer)
	if preview != '':
		if mode == '':
			mode = 'preview'; mode1 = ''
		elif mode != '':
			mode1 = mode; mode = 'preview'
	u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&title="+urllib.quote_plus(title)+"&thumb="+urllib.quote_plus(thumb)+"&fanart="+urllib.quote_plus(fanart)+"&preview="+urllib.quote_plus(preview)+"&referer="+urllib.quote_plus(referer)+"&showcontext="+urllib.quote_plus(showcontext)+"&fav_mode="+urllib.quote_plus(fav_mode)+"&mode1="+urllib.quote_plus(mode1)
	lis = xbmcgui.ListItem(title,iconImage=thumb,thumbnailImage=thumb)
	lis.setInfo(type="Video", infoLabels={"Year":year,"Title":title, 
		"Plot":info,"Genre":genre,"Episode":episodes,"Seasons":seasons, 
		"Poster":poster})
	lis.setProperty( "Fanart_Image", fanart)
	if dtype != '': fo=True
	else: fo=False ; lis.setProperty("IsPlayable","true")
	if mode == 'set': lis.setProperty("IsPlayable","false")
	if url.startswith('plugin') and not mode == 'preview': 
		lis.setProperty("IsPlayable","true")
		u=urllib.unquote_plus(url)
	if mode == 'preview': 
		lis.setProperty("IsPlayable","false")
	lis = Fav.addLink(dtype,mode,url,preview,title,thumb,fanart,info,year,
		genre,episodes,seasons,poster,showcontext,fav_mode,lis)
	link = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,
		listitem=lis,isFolder=fo)
	return link 



def Alpha_sortLIST(LI,part=0,change=False):

	from operator import itemgetter

	'''
	Alphabetically sorts a list of variables, list can contain as many
	items as you wish.
	LI = list you require sorting
	part = the number of the item in the list with which you require all
	other items to be sorted from
	example list[0],list[1],list[2]
	if part is set to part = 1, then all the items in the list
	will be sorted with part 1 being in alphabetical order, and all other
	items still matching the item which is sorted
	change = True will reorder the list so that if you choose list[1]
	as in part = 1, then the return will give you item[1] as now being
	item[0]

	usage
	from main py
	import Utils
	list = Utils.Alpha_sortLIST(list,part,change)
	'''

	if change:
		xi=0; List=[]
		for i in LI:
			x=i[part]
			i=i[:0]+(x)+i[0:]
			i=i[:part+1]+i[part+2:]
			List.append(i)
			xi +=1
		List.sort(key=itemgetter(0))
	else:
		List = LI
		List.sort(key=itemgetter(part))
	return List



def Alpha_sortDICT(DI,part=0):

	from collections import OrderedDict

	'''
	Sorts a dictionary variable Alphabetically.
	dictionary by default only has 2 parts, but this util is intelligent
	DI = the dictionary that requires to be sorted
	part = the part which requires to be sorted in the dictionary
	return will be in alphabetical order from the part required
	
	usage
	from main py
	import Utils
	Dict = Utils.Alpha_sortDICT(dictionary,partnumber)
	'''

	List = []
	for i in DI.items():
		List.append(i[0]+':@:@:'+i[1])
	alist=sorted(List,key=str.upper)
	DIC=OrderedDict()
	for i in alist:
		u=re.split(':@:@:',i)
		DIC[u[0]] = u[1]
	return DIC



def Check_mode(mode, url, title, thumb, referer):

	'''
	Checks the mode before adding to directory
	to see if the link is resolvable by one of the methods
	listed in the modes

	if it is, change the link
	then set the mode to nothing so that kodi sees a playable
	link, and send both back to directory
	
	usage
	from main py
	import Utils
	mode, url = Check_mode(mode,url)
	'''
	
	if mode == 'sportsdevil':
		url = Make_SD_link(url,title,thumb,referer)
		mode = ''
		return mode,url
	elif mode =='f4m':
		url = Make_f4m_link(url,title,thumb)
		mode = ''
		return mode,url
	elif mode == 'sopcast':
		url = Make_Sop_link(url,title,thumb)
		mode = ''
		return mode,url
	elif mode == 'acestream':
		url = Make_Ace_link(url,title,thumb)
		mode = ''
		return mode,url
	elif mode =='utube':
		url = Make_Utube_link(url)
		mode = ''
		return mode,url
	else: return mode, url




def Clean_Up_whitespace(text):

	import re

	'''
	Does Exactly what it says
	feed it content, and it will clear the white space out,
	return just a single space instead of line feeds, tabs etc..
	
	usage
	from main py
	import Utils
	text = Utils.Clean_Up_whitespace(text)
	'''

	scratch = ''
	for i in text:
		scratch = scratch+''.join(i)
	return re.sub('\s+',' ',scratch)



def Clean_Up_url(text):

	import re

	'''
	Another one that does exactly what it says.
	feed it some text with url coding inside, and it will return
	a cleaned up version

	usage
	from main py
	import Utils
	text = Utils.Clean_Up_url(text)
	'''

	rpldict = {'%3a':':', '%2f':'/', '%25':'%', '%3f':'?', '%23':'#', 
	'%3d':'=', '%20':' ', '%26':'&', '%2c':',','%21':'!','%22':'"',
	'%24':'$','%27':"'",'%28':'(','%29':')','%2A':'*','%2B':'+',
	'%2D':'-','%2E':'.','%30':'0','%31':'1','%32':'2','%33':'3','%34':'4'
	,'%35':'5','%36':'6','%37':'7','%38':'8','%39':'9','%3B':';','%3C':'<'
	,'%3E':'>','%40':'@','%5B':'[','%5D':']','%5E':'^','%5F':'_','%60':'`'
	,'%7B':'{','%7C':'|','%7D':'}','%7E':'~'}

				 
	  
	match 	= re.compile('(%\w{2})')
	if '%' in text:
		rpl = match.findall(text)
		for i in rpl :
			text = re.sub(i,rpldict[i],text)
	return text	





def Get_From_To(text, f_str, t_strg, excluding=True):

	import re

	'''
	Another that does exactly what it says.
	text = the content you want to search for a match
	f_str = the first part of the search
	t_str = the latter part of the search
	exluding = False if you want to include f_str and t_str in the result returned

	usage
	from main py
	import Utils
	result = Utils.Get_From_To(text, f_str, t_strg, excluding=)
	'''

	if excluding:
		try: r = re.search("(?i)"+f_strg+"([\S\s]+?)"+t_strg, text).group(1)
		except: r = ''
	else:
		try: r = re.search("(?i)("+f_strg+"[\S\s]+?"+t_strg+")", text).group(1)
		except: r = ''
	return r




def Get_Params():
	import re, sys, urlparse
	'''
	Gets parameters from kodi, and parses them into a dictionary
	in your main py, import Utils, then use
	params = Utils.Get_Params()
	params will then contain the dictionary returned tuples

	usage
	usage
	from main py
	import Utils
	params = Utils.Get_Params

	to use params returned, just use the same as other tuples
	example
	mode = params['mode']

	'''
	args	= sys.argv[2]
	if len(args)<=2: return
	text = re.split('[?]',args,1)
	params1	= {}
	params = urlparse.parse_qs(text[1])
	for i in params:
		x = ''.join(params[i])
		params1.update({i:x})
	return params1




def Make_dir_From_XML(content,mode):

	import re,xbmc

	
	'''
	Does exactly what it says.
	this util needs to be used with other util addDir
	Another that is artificially intelligent
	feed it content in the xml format, and it will do its best
	to make a directory from it.
	if you dont know what the xml format is, then take a look at the xml
	template bundled with this tutorial pack

	usage
	from main py
	import Utils
	Utils.Make_dir_From_XML(content)

	'''



	flst = [('<type>','</type>','dtype'),('<mode>','</mode>','mode'),
	('<title>','</title>','title'),('<url>','</url>','url'),
	('<preview>','</preview>','preview'),('<thumb>','</thumb>','thumb'),
	('<fanart>','</fanart>','fanart'),('<info>','</info>','info'),
	('<genre>','</genre>','genre'),('<date>','</date>','date'),
	('<seasons>','</seasons>','seasons'),
	('<episodes>','</episodes>','episodes'),
	('<poster>','</poster>','poster')]

	if mode == None:
		addDir(dtype='folder', mode='fav_mode', url='', preview='', 
			title='Favorites', thumb='https://i.imgur.com/HCFybZP.png', 
			fanart=addon_fanart,info='', year='', genre='', 
			episodes='', seasons='', poster='',showcontext='')

	mtchs = re.compile('(?sm)<item>(.+?)<\/item>').findall(content)
	for itm in mtchs:
		param = {}
		for i in flst:
			try:
				cont = itm.split(i[0])
				cont = cont[1].split(i[1])
				param.update({i[2]:cont[0]})
			except: param.update({i[2]:''})
		if param['url'] == 'none':
			addDir(title=param['title'])
		elif param['url'] != '':
			addDir(dtype=param['dtype'], mode=param['mode'], url=param['url'],
				   preview=param['preview'], title=param['title'],
				   thumb=param['thumb'], fanart=param['fanart'],
				   info=param['info'], year=param['date'],
				   genre=param['genre'], episodes=param['episodes'],
				   seasons=param['seasons'], poster=param['poster'])
	return





def Make_ply_From_XML(content):

	import re,xbmc

	
	'''
	Does exactly what it says.
	this util needs to be used with other util addDir
	Another that is artificially intelligent
	feed it content in the xml format, and it will do its best
	to make a directory from it.
	if you dont know what the xml format is, then take a look at the xml
	template bundled with this tutorial pack

	usage
	from main py
	import Utils
	Utils.Make_ply_From_XML(content)

	'''



	flst = [('<type>','</type>','dtype'),('<mode>','</mode>','mode'),
	('<title>','</title>','title'),('<url>','</url>','url'),
	('<preview>','</preview>','preview'),('<thumb>','</thumb>','thumb'),
	('<fanart>','</fanart>','fanart'),('<info>','</info>','info'),
	('<genre>','</genre>','genre'),('<date>','</date>','date'),
	('<seasons>','</seasons>','seasons'),
	('<episodes>','</episodes>','episodes'),
	('<poster>','</poster>','poster')]

	mtchs = re.compile('(?sm)<item>(.+?)<\/item>').findall(content)
	for itm in mtchs:
		param = {}
		for i in flst:
			try:
				cont = itm.split(i[0])
				cont = cont[1].split(i[1])
				param.update({i[2]:cont[0]})
			except: param.update({i[2]:''})
		if param['url'] == 'none':
			addDir('', '', '', '',param['title'] ,'','','','','','','')
		elif param['url'] != '':
			addDir(dtype='', mode=param['mode'], url=param['url'],
				   preview=param['preview'], title=param['title'],
				   thumb=param['thumb'], fanart=param['fanart'],
				   info=param['info'], year=param['date'],
				   genre=param['genre'], episodes=param['episodes'],
				   seasons=param['seasons'], poster=param['poster'])
	return



def makecookie(name, value, dom):

	import cookielib

	'''
	Does exactly as it says

	usage
	from main py
	import Utils
	Utils.makecookie(name,value,dom)

	in your addon main use this

	cj = cookielib.CookieJar()
	ck = utils.makecookie("name", "__sharethis_cookie_test__","www.whatever.com")
	cj.set_cookie(ck)

	'''

	ck = cookielib.Cookie(
		version=0, 
		name=name, 
		value=value, 
		port=None, 
		port_specified=False, 
		domain=dom, 
		domain_specified=True, 
		domain_initial_dot=False, 
		path="/", 
		path_specified=True, 
		secure=False, 
		expires=None, 
		discard=False, 
		comment=None, 
		comment_url=None, 
		rest=None)
	return ck




def Make_Ace_link(url,title,thumb):

	'''
	makes a plexus acestream link
	plexus is a peer 2 peer player
	
	you might want to think about using a vpn with these links
	although not required, it could help out to hide it from 
	your isp

	requires a working Plexus, if using Mick3yB0y template
	it will automatically download with template
	handy piece of kit to have, thanks go to enen and TVaddons 
	for the updates and original

	usage
	from main.py
	import Utils
	Util.Make_Ace_link(url,title,thumb)
	'''

	p2p = 'plugin://program.plexus/?mode=1&url='+url+'&name='+title+'&iconimage='+thumb
	return p2p


def Make_f4m_link(url,title,thumb):

	import urllib

	'''
	makes a ts,m3u8,f4m link playable
	requires f4m tester, if using Mick3yB0y template
	it will automatically download with template
	handy piece of kit to have, thanks go to Shani for the addon

	usage
	from main.py
	import Utils
	Utils.Make_f4m_link(url,title,thumb,info)
	'''

	if '.f4m' in url:
		f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)+'&amp;name='+title+'&iconImage='+thumb
	elif '.m3u8' in url:
		f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)+'&amp;streamtype=HLSRETRY;name='+title+'&iconImage='+thumb
	elif '.ts' in url:
		f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)+'&amp;streamtype=TSDOWNLOADER;name='+title+'&iconImage='+thumb
	else:
		f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)+'&amp;streamtype=SIMPLE;name='+title+'&iconImage='+thumb	
	return f4m


def Make_m3u_dir(content,f4m=True):

	import re, xbmcaddon, xbmc
	addon 			= xbmcaddon.Addon()
	addon_icon 		= addon.getAddonInfo('icon')
	addon_fanart	= addon.getAddonInfo('fanart')
	Listing 		= []

	'''
	Makes a playable list from and m3u file
	the links will be returned in the f4m format, just in 
	case they are ts links, which they usually are

	looks for Country id first, if not present shows only 
	channel id, if present shows country id

	f4m false if you want the links put together in f4m format
	f4m true if the m3u file already contains f4m links (default)

	usage
	from main.py
	import Utils
	Make_m3u_dir(content,bool)
	'''

	content = Split_Up(content,'#EXTINF:-1',am=0,ns=2,nf=0)
	cont = content['content']
	ID = re.compile('(?sm)[\,](.+?)[\:] ').findall(cont[0])
	if not ID:
		matches = re.compile('(?sm),(.+?)\n^(.+?)$')
	else:
		matches = re.compile('(?sm)[\,](.+?)[\:] (.+?)\\n^(.+?)\\n')
	for i in cont:
		if 'logo' in i:
			thumb = re.search('logo="(.+?)"',i).group(1)
		else: thumb = addon_icon
		ch = matches.findall(i)
		for x in ch:
			if ID: 
				url = x[2]
				title = x[1]
				cid = x[0]
			else: 
				url = x[1]
				title = x[0]
			if not f4m :
				url = Make_f4m_link(url,title,thumb)
			if not url.startswith('plugin') and url.endswith('.ts') :
				url = Make_f4m_link(url,title,thumb)
			if ID: z=title,cid,url
			else: 
				cid = ' '; z=title,cid,url
			Listing.append(z)

	'''the list will be alphabetically sorted by the channel id
	if you do not require this comment out this line'''
	Listing = Alpha_sortLIST(Listing)

	''' set the default view '''

	xbmc.executebuiltin("Container.SetViewMode(50)")

	for items in Listing:
		addDir(dtype='', mode='play', url=items[2],
			preview='', title=items[1]+' Channel id '+items[0],
			thumb=thumb, fanart=addon_fanart)
	return	



	


def Make_SD_link(url,title,thumb,referer):



	'''
	makes a sportsdevil link
	sportsdevil can resolve a good many links
	so if you have a link that refuses to play elsewhere
	hand it to sportsdevil and see if it can play it for you
	it also helps to give it a referer, i.e where the link came from

	requires sportsDevil, if using Mick3yB0y template
	it will automatically download with template
	handy piece of kit to have, thanks go to SD boys for the addon

	usage
	from main.py
	import Utils
	Util.Make_SD_link(url,title,thumb,referer)
	'''

	SD = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26icon='+thumb+'%26videoTitle%3d'+title
	if referer:
		SD = SD + '%26referer=' +referer
	return SD



def Make_Sop_link(url,title,thumb):

	'''
	makes a plexus sopcast link
	plexus is a peer 2 peer player
	
	you might want to think about using a vpn with these links
	although not required, it could help out to hide it from 
	your isp

	requires a working Plexus, if using Mick3yB0y template
	it will automatically download with template
	handy piece of kit to have, thanks go to enen and TVaddons 
	for the updates and original

	usage
	from main.py
	import Utils
	Util.Make_Sop_link(url,title,thumb)
	'''

	sop = 'plugin://program.plexus/?mode=2&url='+url+'&name='+title+'&iconimage='+thumb
	
	return sop



def Make_Utube_link(url):


	'''
	makes a youtube link
	
	requires youtube addon, if using Mick3yB0y template
	it will automatically download with template
	handy piece of kit to have, thanks go to dev team for the addon

	shout out to the folks who develop and maintain the youtube
	addon

	usage
	from main.py
	import Utils
	Util.Make_Utube_link(url)
	'''
	if 'watch' in url:
		url = url.replace('/watch?v=','')
	if 'channel' in url:
		url = url.replace('/channel/','')
	if '&list=' in url:
		url=url.split('&list=')
		url=url[0]
	import xbmc
	if len(url) == 11:
		utube = 'plugin://plugin.video.youtube/play/?video_id='+url
	elif url.startswith('PL') and not '&order=' in url :
		utube = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id='+url
	else:
		utube = 'plugin://plugin.video.youtube/play/?playlist_id='+url


	return utube


def No_link():


    import xbmcgui
    dialog = xbmcgui.Dialog()

    dialog.ok('NO Links Found','No Playable Links were found for this stream service','Try another stream','Click ok to continue')
    return

def Split_Up(content,split_key,am=0,ns=0,nf=0):

	import re

	'''
	Yet another that does exactly what it says on the tin
	feed it some content in the form of content =
	feed it a split key =
	this is where the content will be split
	feed it an ammount of times to split the content(optional)
	am = 
	how many splits at the start to delete(optional)
	ns = 
	how many splits at the rear to delete(optional)
	nf = (must be a minus figure)
	return wil be in the form of a dictionary
	usage
	from main py
	import Utils
	split = Utils.Split_up(content,split_key)
	return usage
	x = split['item_count']
	x now equals the ammount of items in the variable content
	content = split['content']
	content now holds all the splits
	'''


	content = re.split(split_key,content,am)
	while ns>0 :
		ns -= 1
		del content[0]
	if nf <0 :
		del content[nf]
	length 	= len(content)
	return {'content':content, 'item_count':length}




def Standard_player(url,title,thumb):

	import xbmc, xbmcplugin, xbmcgui, sys
	busy = xbmcgui.DialogBusy()
	'''
	just a bog standard player
	'''
	busy.create()
	player = xbmc.Player()
	lis = xbmcgui.ListItem(title,iconImage=thumb,thumbnailImage=thumb)
	lis.setInfo(type='Video', infoLabels ={'Title':title})
	lis.setProperty("IsPlayable","true")
	lis.setPath(url)
	busy.close()
	player.play(url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, lis)
	for i in range(0, 120):
		if player.isPlayingVideo(): break
		xbmc.sleep(1000)
	while player.isPlaying():
		xbmc.sleep(2000)
	xbmc.sleep(4000)
	return





def Player(url,title,thumb,info=''):

	import sys, xbmcgui, xbmcplugin, xbmc
	busy = xbmcgui.DialogBusy()
	player = xbmc.Player()
	busy.create()
	'''
	Does exactly what it says on the tin
	just feed it what it wants

	usage 
	from main.py
	import Utils
	Utils.player(url,title,thumb)
	'''

	lis	= xbmcgui.ListItem(title,iconImage=thumb,thumbnailImage=thumb)
	lis.setInfo(type='Video', infoLabels ={'Title':title,"Plot":info})
	lis.setPath(url)
	busy.close()
	player.play(url, lis)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, lis)
	for i in range(0, 120):
		if player.isPlayingVideo(): break
		xbmc.sleep(1000)
	while player.isPlaying():
		xbmc.sleep(2000)
	xbmc.sleep(4000)
	return



def URLresolver(url):
	import urlresolver

	'''
	does what it says
	module is available for download on most repos
	if using the Mick3yB0y template, module will automatically 
	download
	uses the module urlresolver to resolve the link
	then pushes the info to the player
	for a list of resolvable links and sites, see inside templates

	shout out to the guys who develop and maintain the urlresolver
	addon

	usage
	from main.py
	import Utils
	Utils.URLresolver(url,title,thumb,info) info optional
	'''


	url = urlresolver.resolve(url)

	return url



def urlset():

	import urlresolver


	#open urlresolver settings menu 

	urlresolver.display_settings()
	return