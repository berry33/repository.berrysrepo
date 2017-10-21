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
import cookielib
import urllib2
cj = cookielib.CookieJar()


def Read_It(url):

	import urllib2

	'''
	Standard html opener for when you dont need any frills
	no cookies or other stuff, just a quick opener

	usage
	from your main.py
	import Net
	content = Net.Read_It(url)
	'''

	req	= urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (X11; Linux i686; rv:42.0) Gecko/20100101 Firefox/42.0 Iceweasel/42.0')
	response 	= urllib2.urlopen(req)
	scratch		= response.read()
	response.close()
	return scratch






def Read_It_Full(url,headers=None,post=None,timeout=10,gzip=False):

	import urllib2, cookielib

	'''
	ok, so the the polar opposite of the above opener.
	this one has whistles and bells
	give it a list of headers in the form of
	headers = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'), ('referer', url1)]
	if you want to use the post method, then feed it some post info, the
	same method as above
	set the timeout in seconds
	if gzip is true, you are taking in a gzip encoded page and decrypting it
	the result will be in unzipped format

	automatic cookie handling is performed

	usage
	from your main.py
	import Net
	content = Net.Read_It_Full(url)****(all other args are optional)

	'''

	# try:
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),urllib2.HTTPBasicAuthHandler(), urllib2.HTTPSHandler(),urllib2.HTTPHandler())
	req = urllib2.Request(url)
	if headers:
		for h,hv in headers:
			req.add_header(h,hv)
	scr = opener.open(req,post,timeout=timeout).read()
	if gzip :
		import StringIO, gzip
		cmps = StringIO.StringIO(scr)
		ugzp = gzip.GzipFile(fileobj=cmps)
		scr  = ugzp.read()
	return scr
	# except urllib2.URLError, e: Errhandler(e)





def Errhandler(e):


	import xbmc, xbmcaddon, xbmcgui
	addon 		= xbmcaddon.Addon()
	IconImage 	= addon.getAddonInfo('icon')
	addonname 	= addon.getAddonInfo('name')
	dialog 		= xbmcgui.Dialog()

	'''
	A simple html error handler.
	makes some noise and puts a dialog on the screen to tell you what
	went wrong

	usage
	from main py
	import Utils
	at the end of your html request, use this line

	except urllib2.URLError, e: Utils.Errhandler(e)
	'''	
	if hasattr(e, 'code'):
		xbmc.executebuiltin("XBMC.Notification("+addonname+" , We failed with error code - "+str(e.code)+",5000,"+IconImage+")")
		dialog.ok(addonname+' Connection Error', addonname+' , We failed with an error code -', '( '+str(e.code)+' )')
	elif hasattr(e, 'reason'):
		xbmc.executebuiltin("XBMC.Notification("+addonname+" , We failed to reach a server. - "+str(e.reason)+",5000,"+IconImage+")")
		dialog.ok(addonname+' Connection Error', addonname+' , We failed to reach a server -', '( '+str(e.reason)+' )')
	return






class NoRedirection(urllib2.HTTPErrorProcessor):
   def http_response(self, request, response):
	   return response
   https_response = http_response

'''
Does exactly what it says
no redirection thankyou
just add this to your opener
copy and paste this into your main.py if you want to use it
but with correct handling of cookies, you shouldnt be redirected

opener2 = urllib2.build_opener(NoRedirection)

''' 

