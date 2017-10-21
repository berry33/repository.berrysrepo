# -*- coding: utf-8 -*-

# Eggz.py
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

This Template has been coded for kodi 17.4 using python 2.7.
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

#######################################################################
# lets import stuff that we need to run, modules from python and kodi #
#######################################################################

import xbmc, xbmcgui, xbmcplugin, xbmcaddon
import os, sys, cookielib, re
from urllib import urlopen
from lib import Edit
from lib import Utils
from lib import Net
from lib import Fav
from lib import yt_search
from lib import resolvers

#######################################################################
#  Lets set some tickety boo stuff to help our cramped fingers later  #
#######################################################################

HOME			= xbmc.translatePath('special://home')
dialog 			= xbmcgui.Dialog()
addon 			= xbmcaddon.Addon()
addon_path		= addon.getAddonInfo('path')
addon_name 		= addon.getAddonInfo('name')
addon_icon 		= addon.getAddonInfo('icon')
addon_fanart	= addon.getAddonInfo('fanart')
addon_handle 	= int(sys.argv[1])
player 			= xbmc.Player()
cj 				= cookielib.CookieJar()
busy			= xbmcgui.DialogBusy()

######################################################################
# 	 and now lets set what the menu is Going to look like in kodi	 #
######################################################################

xbmcplugin.setContent(int(sys.argv[1]), 'movies')


'''

This is just an example

<folder>

	<item>
		<type></type>
		<mode>intres</mode>
        <title>Unbroken</title>
        <url>http://topchristianmovies.com/video/1208</url>
        <thumb>http://berryburchett.net/kodi/mainstreet/movie-night-popcorn-clipart-4TbRqEaTg.jpeg</thumb>
        <fanart></fanart>
	</item>

	<item>
		<type></type>
		<mode></mode>
		<title>[B][COLOR lime]•[/COLOR] [COLOR royalblue]DC[/COLOR] [COLOR azure]and[/COLOR] [COLOR crimson]MARVEL[/COLOR] MOVIES[/B]</title>
		<thumb></thumb>
		<preview></preview>
		<url>none</url>
		<genre></genre>
		<info></info>
		<fanart></fanart>
		<year></year>
		<seasons></seasons>
		<episodes></episodes>
	</item>

	<item>
		<type></type>
		<mode>urlresolver</mode>
		<title>[B]Iron Man (2008) m720p Lat/Eng[/B]</title>
		<thumb>https://moviefiles.alphacoders.com/227/poster-thumb-227.jpg</thumb>
		<preview>plugin://plugin.video.youtube/?action=play_video&videoid=Ke1Y3P9D0Bc&feature=youtu.be</preview>
		<url>http://www.dailymotion.com/video/x5ypm1x</url>
		<genre>Action, Adventure, Sci-Fi</genre>
		<info>After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.</info>
		<fanart></fanart>
		<year>2008</year>
		<seasons></seasons>
		<episodes></episodes>
	</item>

	<item>
		<type></type>
		<mode></mode><!--going to play a youtube link-->
		<title>[B]Iron Man (2008) m720p Lat/Eng[/B]</title>
		<thumb>https://moviefiles.alphacoders.com/227/poster-thumb-227.jpg</thumb>
		<preview>plugin://plugin.video.youtube/?action=play_video&videoid=bK_Y5LjSJ-Y&feature=youtu.be</preview>
		<url>https://3.bp.blogspot.com/SNcu-N9Q8xNGUiSatuM_Tb3fqJ5tG2wmheVceMXa48nfgEEAVMSE_uuK1X8cds4rVazQAlU2RDUCUmUOfHzLDlu6cAlUCz-xg55RfO5qDKw96h0qG9t9eUpQ71O4ljB5pWkUzapiOmtsGk_qyHxqEDYSKRVHT3WMJ1CKQfgnLuz8D5gHJ5T4OiUXB6FeG218sHjf2rMRAPCJ_yDjbAiu1r0exY4HqKQ7IOefU-41deVqpv7riK-RC92qXxhilLC2ogd551F7wSI2Dh5_2j0eS8oWybW1UvXA3XPqrfo1VpPwExdV8mkRZQFQSS6rbaYI3QMFcuMlc79DqEJ0CLXiaA8pajJnHqcNtxE_nazR93Yjuvc7ivcKIlJvDJcA1UH03-YRtg3YkyulW4_bwbSyRljZMUrunPF09PyoPgiM7zdTvrBXk2By0TgI3vU2mgDSc0GZzvfPjTJS8p4uhBd09FjAGiSzT18QTrUBWwutw7j764qJ-8HhUy78Xv_35rUrJ_1k9xuUUl5HFd_zkCUWa8G6sak0-AT3DMkLgr2DrE3ZHj1NreUdJ9Knrhk1EZOiDA4SKI0dV_KFAhpD3poLi8MVu2Jk9T1OEtqj3JF5U10=m18</url><!-- the last numbers after the = in the youtube url-->
		<genre>Action, Adventure, Sci-Fi</genre>
		<info>After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.</info>
		<fanart></fanart>
		<year>2008</year>
		<seasons></seasons>
		<episodes></episodes>
	</item>

	<item>
		<type></type>
		<mode>intres</mode>
		<title>[B]Batman The dark knight (2008) 1080p Lat/Eng[/B]</title>
		<thumb>https://picfiles.alphacoders.com/127/thumb-127248.jpg</thumb>
		<preview>plugin://plugin.video.youtube/?action=play_video&videoid=kmJLuwP3MbY&feature=youtu.be</preview>
		<url>https://estream.to/embed-2fu0oh2ftnhz.html</url>
		<genre>Action, Crime, Drama</genre>
		<info>When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.</info>
		<fanart></fanart>
		<year>2008</year>
		<seasons></seasons>
		<episodes></episodes>
	</item>

	<item>
		<type>folder</type>
		<mode>m3u</mode>
		<title>[B]Guardians Of The Galaxy (2014) 1080p. Lat/Eng[/B]</title>
		<thumb>https://moviefiles.alphacoders.com/198/poster-thumb-1982.jpg</thumb>
		<preview></preview>
		<url>https://raw.githubusercontent.com/fluxustv/IPTV/master/list.m3u</url>
		<genre>Action, Adventure, Sci-Fi </genre>
		<info>A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.</info>
		<fanart></fanart>
		<year>2014</year>
		<seasons></seasons>
		<episodes></episodes>
	</item>

</folder>


'''


#######################################################################
# the following is just for a bit of fun with the settings menu, this #
# is just to show you what to do and how its done, then later it will #
# be implemented into the settings menu and you will see it in here   #
#######################################################################

def getPublicIp():
	data = str(urlopen('http://checkip.dyndns.com/').read())
	return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)

# that should return your ip address

def getmac():
	from uuid import getnode
	mac_num = hex(getnode()).replace('0x', '').upper()
	return ':'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
 	
# now most of the time, android is a pain and returns a set of zeros
# so dont say i didnt tell ya, but that is the mac address


######################################################################
#  lets define a few small functions that call from the Utils module #
#   if you want to know more about these, read in the Utils module   #
######################################################################


def Make_m3u_list(url):
	content = Net.Read_It(url)
	Utils.Make_m3u_dir(content)
	return

def Start(mode):
	'''if mode == None:

		Utils.addDir(dtype='', mode='set', url='',preview='', 
			title='Open Urlresolver settings Here',thumb=addon_icon, 
			fanart=addon_fanart,info='', year='',genre='', episodes='',
			seasons='', poster='')
		# above is for the urlresolver settings item in the main menu
		# if this is not required, just comment the lines out

		yt_search.yt_link()
		yt_search.dm_link()

		# above is for the youtube and dailymotion
		# search items in the main menu
		# if this is not required, just comment the lines out
'''
	content = Net.Read_It(str(Edit.MainBase))
	Utils.Make_dir_From_XML(content,mode)
	return

def Play_list(url):
	content = Net.Read_It(url)
	Utils.Make_ply_From_XML(content)
	return

def DIR_list(url,mode):
	content = Net.Read_It(url)
	Utils.Make_dir_From_XML(content,mode)
	return

#######################################################################
# 	now lets start creating some functions that will take the bind    #
# out of typing them all the time, that way we just call the function #
#######################################################################

def Check_Preview(preview,url,title,mode1):
	if preview == '': 
		return url # check for preview link, if none then go back
	else:
		List=[]; ListU=[]; c=0
		c=c+1; List.append('[B][COLOR cyan]Watch Preview   [/COLOR][/B]['
			+str(c)+'] '); ListU.append(preview)
		c=c+1; List.append('[B][COLOR limegreen]Play Full Video  [/COLOR][/B]['+str(c)+'] '); ListU.append(url)
		''' above lines make a list of 2 items, one is the actual link, 
		the other is the preview link '''
		dialog 	= xbmcgui.Dialog()
		rNo 	= dialog.select(addon_name+' Preview or Main Links, Select A link.', List)
		if rNo>=0:
			rName 	=title
			rURL 	=str(ListU[rNo])
			# choose a link and return it
			return rURL

def Preview_Res_status(url,preview,title,mode1,thumb,referer):
	# if we have 2 links then one is returned from checkpreview
	url = Check_Preview(preview,url,title,mode1)
	''' we need to make sure the link is playable, it might not of been
	resolved yet, takes too long to do it before putting them in the 
	directory, so lets check them now '''
 	if not url.startswith('plugin'): 
 		mode,url=Utils.Check_mode(mode1, url, title, thumb, referer)
 		if mode == 'urlresolver': 
 			busy.create()
 			url = Utils.URLresolver(url)
 			busy.close()
 		elif mode == 'intres':
 			url,title,thumb = resolvers.Resolve(url,title,thumb)
		Utils.Player(url,title,thumb)
 	else: Utils.Player(url,title,thumb,info)
 	return
#########################################################
#  Start the grunting, lets get the variables we need   #
#########################################################

params = Utils.Get_Params() #look in Utils for Explanation
mode = None
try: mode = params['mode']
except: pass
try: mode1 = params['mode1']
except: mode1 = ''
try: preview = params['preview']
except: preview = ''
try: url = params['url']
except: pass
try: referer = params['referer']
except: referer = ''
try: title = params['title']
except: pass
try: thumb = params['thumb']
except: thumb = ''
try: fanart = params['fanart']
except: pass
try: info = params['info']
except: info = ''
try: year = params['year']
except: pass
try: genre = params['genre']
except: pass
try: episodes = params['episodes']
except: pass
try: seasons = params['seasons']
except: pass
try: poster = params['poster']
except: pass
try: showcontext = params['showcontext']
except: pass
try: fav_mode = params['fav_mode']
except: pass

# now a bit of fun with the settings menu

mac = addon.getSetting("MAC Address")
if not mac:
	mac = getmac()
	addon.setSetting(id = "MAC Address", value = mac)
ret = addon.getSetting("IP Address")
if not ret:
	ret = getPublicIp()
	addon.setSetting(id = "IP Address", value = ret)

# settings menu will now contain those values

##########################################################
# now lets do something with those variables we just got #
##########################################################

if mode == None or len(sys.argv[2])<2: Start(mode)#how we always start up
elif mode == 'makexmldir': DIR_list(url,mode)# use the <type> option
elif mode == 'makexmlplaylist': Play_list(url)#nothing in <type> option
elif mode == 'play': 
	url = Check_Preview(preview,url,title,mode1)
	Utils.Player(url,title,thumb,info)#look in Utils
elif mode == 'urlresolver':
	busy.create()
	url = Utils.URLresolver(url)
	busy.close()#look in Utils
	url = Check_Preview(preview,url,title,mode1)
	Utils.Player(url,title,thumb,info)#look in Utils
elif mode == 'm3u': Make_m3u_list(url)
elif mode == 'preview':
	Preview_Res_status(url,preview,title,mode1,thumb,referer)	
elif mode == 'fav_mode': Fav.getFavorites()
elif mode == 'remfav': Fav.rmFavorite(title)
elif mode == 'addfav': Fav.addFavorite(mode,title,url,thumb,fanart)
elif mode == 'set': Utils.urlset()
elif mode == 'ytsear': url = yt_search.YT_Search(True)
elif mode == 'ytnxt': yt_search.YT_Search(False,url)
elif mode == 'dmsear': url = yt_search.DM_Search(True)
elif mode == 'dmnxt': yt_search.DM_Search(False,url)
elif mode == 'intres':
	url,title,thumb = resolvers.Resolve(url,title,thumb)
	if url: Utils.Player(url,title,thumb,info)
	else: Utils.No_link()
elif mode == 'ytchannel': yt_search.YT_Channels(url)
xbmcplugin.endOfDirectory(addon_handle)
xbmcplugin.endOfDirectory(addon_handle)