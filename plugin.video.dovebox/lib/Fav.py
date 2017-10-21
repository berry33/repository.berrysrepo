# -*- coding: utf-8 -*-

# Fav.py
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

A simple favorites file using cPickle

"""
import xbmc, xbmcgui, xbmcaddon, xbmcplugin, sys, os
import cPickle as pickle 
import Utils # we need Some functions from utils

################################################
# 		set some variables save on typing	   #
################################################

addon     = xbmcaddon.Addon()
profile   = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
favorites = os.path.join(profile, 'favorites.txt')

####################################################################
# check to see if favorites file exists, if it does, read contents #
####################################################################

if os.path.exists(favorites)==True:
	with open(favorites, 'rb') as handle:
		FAV = pickle.loads(handle.read())
else: FAV = []

###################################################################
# if the favorites file doesnt exist, lets put a friendly message #
# 			  up, saying there are no favorites yet				  #
###################################################################


def getFavorites():
	if not os.path.exists(favorites):
		Utils.addDir(dtype='', mode='', url='', preview='', 
			title='No Favourites yet', thumb='', 
			fanart='',info='', year='', genre='', 
			episodes='', seasons='', poster='')
		return
		
##################################################################
# if it doest exsit, read the contents, and display in directory #
##################################################################

	else:
		with open(favorites, 'rb') as handle:
				items = pickle.loads(handle.read())
		for i in items:
			mode = i[0]
			title = i[1]
			url = i[2]
			thumb = i[3]
			fanart = i[4]
			if thumb =='999':thumb = ''
			if fanart == '999':fanart = ''
			if mode == '999': mode = ''
			Utils.addDir(dtype='',mode=mode,url=url,title=title,
				thumb=thumb, fanart=fanart,showcontext='fav')
	return

##################################################################
# lets add some favorites, first we need to make sure everything #
#		   has a value, and that the title is readable			 #
##################################################################

def addFavorite(mode='',url='',title='',thumb='',
	fanart='',showcontext='fav'):
	favList = []
	try:
		title = title.encode('utf-8', 'ignore')
	except:
		pass
	if mode == '': mode = '999'
	if thumb == '': thumb = '999'
	if fanart == '': fanart = '999'

###################################################################
# Lets make sure the favorites file doesnt exist, if not lets set #
# 	  a variable then write the contents to the favorites file	  #
#   if it does exist, read the contents, and append the contents  #
#				with what we are trying to add 					  #
###################################################################

	if os.path.exists(favorites)==False:
		favList.append((mode,url,title,thumb,fanart,showcontext))
		with open(favorites, 'wb') as handle:
			pickle.dump(favList, handle)
	else:
		with open(favorites, 'rb') as handle:
			data = pickle.loads(handle.read())
		data.append((mode,url,title,thumb,fanart,showcontext))
		with open(favorites,'wb') as handle:
			pickle.dump(data, handle)
	return

#####################################################################
# and now lets set a way of removing entries from the file, here we #
# 		  use the title to match the entry and then delete it 		#
#####################################################################

def rmFavorite(title):
	with open(favorites, 'rb') as handle:
		data = pickle.loads(handle.read())
	for index in range(len(data)):
		if data[index][1]==title:
			del data[index]
			with open(favorites,'wb') as handle:
				pickle.dump(data, handle)
			break
	xbmc.executebuiltin("XBMC.Container.Refresh")
	return


######################################################################
#  now we need a way of adding and removing favorites, this is done  #
# through the context menu in kodi, so we need to make sure we add   #
# some entries to the context menu for our addon to make use of them #
######################################################################

def addLink(dtype,mode,url,preview,title,thumb,fanart,info,year,genre,
	episodes,seasons,poster,showcontext,fav_mode,lis):

	
	import urllib,xbmcgui,xbmcaddon, re

	try:
		title = title.encode('utf-8', 'ignore')
	except:pass
	if not dtype:
		contextMenu = []
		if showcontext == 'fav':
			contextMenu.append(
				('Remove from Add-on Favorites','XBMC.RunPlugin(%s?mode=remfav&title=%s)'
				 %(sys.argv[0], urllib.quote_plus(title)))
				 )
		regex =  r"'"+re.escape(title)+r"'"
		if not re.search(regex, str(FAV)):
			fav_params = (
				'%s?mode=addfav&url=%s&title=%s&thumb=%s&fanart=%s&fav_mode=0'
				%(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(title),urllib.quote_plus(thumb), urllib.quote_plus(fanart))
				)
			contextMenu.append(('Add to Add-on Favorites','XBMC.RunPlugin(%s)' %fav_params))
		lis.addContextMenuItems(contextMenu)
	return lis
