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
"""

import Net
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP


def getSoup(url,data=None):

	data = Net.Read_It(url)
	return BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)


def parse_regex(reg_item):
	try:
		regexs = {}
		for i in reg_item:
			regexs[i('name')[0].string] = {}
			try:
				regexs[i('name')[0].string]['expre'] = i('expres')[0].string
				if not regexs[i('name')[0].string]['expre']:
					regexs[i('name')[0].string]['expre']=''
			except: pass
			regexs[i('name')[0].string]['page'] = i('page')[0].string
			try:
				regexs[i('name')[0].string]['refer'] = i('referer')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['connection'] = i('connection')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['notplayable'] = i('notplayable')[0].string
			except: pass	
			try:
				regexs[i('name')[0].string]['noredirect'] = i('noredirect')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['origin'] = i('origin')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['includeheaders'] = i('includeheaders')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['x-req'] = i('x-req')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['x-forward'] = i('x-forward')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['agent'] = i('agent')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['post'] = i('post')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['rawpost'] = i('rawpost')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['htmlunescape'] = i('htmlunescape')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['readcookieonly'] = i('readcookieonly')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['cookiejar'] = i('cookiejar')[0].string
				if not regexs[i('name')[0].string]['cookiejar']:
					regexs[i('name')[0].string]['cookiejar']=''
			except: pass                          
			try:
				regexs[i('name')[0].string]['setcookie'] = i('setcookie')[0].string
			except: pass
			try:
				regexs[i('name')[0].string]['appendcookie'] = i('appendcookie')[0].string
			except: pass					
			try:
				regexs[i('name')[0].string]['ignorecache'] = i('ignorecache')[0].string
			except: pass
		regexs = urllib.quote(repr(regexs))
		return regexs   
	except:
		regexs = None


def getRegexParsed(regexs, url,cookieJar=None,forCookieJarOnly=False,recursiveCall=False,cachedPages={}, rawPost=False, cookie_jar_file=None):

	if not recursiveCall:
		regexs = eval(urllib.unquote(regexs))
	doRegexs = re.compile('\$doregex\[([^\]]*)\]').findall(url)
	setresolved=True
		  
	for k in doRegexs:
		if k in regexs:
			m = regexs[k]
			cookieJarParam=False

			if  'cookiejar' in m: 
				cookieJarParam=m['cookiejar']
				if  '$doregex' in cookieJarParam:
					cookieJar=getRegexParsed(regexs, m['cookiejar'],cookieJar,True, True,cachedPages)
					cookieJarParam=True
				else:
					cookieJarParam=True
			if cookieJarParam:
				if cookieJar==None:
					cookie_jar_file=None
					if 'open[' in m['cookiejar']:
						cookie_jar_file=m['cookiejar'].split('open[')[1].split(']')[0]
					cookieJar=getCookieJar(cookie_jar_file)
					if cookie_jar_file:
						saveCookieJar(cookieJar,cookie_jar_file)
				elif 'save[' in m['cookiejar']:
					cookie_jar_file=m['cookiejar'].split('save[')[1].split(']')[0]
					complete_path=os.path.join(profile,cookie_jar_file)
					print 'complete_path',complete_path
					saveCookieJar(cookieJar,cookie_jar_file)
			if  m['page'] and '$doregex' in m['page']:
				m['page']=getRegexParsed(regexs, m['page'],cookieJar,recursiveCall=True,cachedPages=cachedPages)

			if 'setcookie' in m and m['setcookie'] and '$doregex' in m['setcookie']:
				m['setcookie']=getRegexParsed(regexs, m['setcookie'],cookieJar,recursiveCall=True,cachedPages=cachedPages)
			if 'appendcookie' in m and m['appendcookie'] and '$doregex' in m['appendcookie']:
				m['appendcookie']=getRegexParsed(regexs, m['appendcookie'],cookieJar,recursiveCall=True,cachedPages=cachedPages)

			if  'post' in m and '$doregex' in m['post']:
				m['post']=getRegexParsed(regexs, m['post'],cookieJar,recursiveCall=True,cachedPages=cachedPages)
				print 'post is now',m['post']

			if  'rawpost' in m and '$doregex' in m['rawpost']:
				m['rawpost']=getRegexParsed(regexs, m['rawpost'],cookieJar,recursiveCall=True,cachedPages=cachedPages,rawPost=True)

			if 'rawpost' in m and '$epoctime$' in m['rawpost']:
				m['rawpost']=m['rawpost'].replace('$epoctime$',getEpocTime())

			if 'rawpost' in m and '$epoctime2$' in m['rawpost']:
				m['rawpost']=m['rawpost'].replace('$epoctime2$',getEpocTime2())

			link=''
			if m['page'] and m['page'] in cachedPages and not 'ignorecache' in m and forCookieJarOnly==False :
				link = cachedPages[m['page']]
			else:
				if m['page'] and  not m['page']=='' and  m['page'].startswith('http'):
					if '$epoctime$' in m['page']:
						m['page']=m['page'].replace('$epoctime$',getEpocTime())
					if '$epoctime2$' in m['page']:
						m['page']=m['page'].replace('$epoctime2$',getEpocTime2())

					page_split=m['page'].split('|')
					pageUrl=page_split[0]
					header_in_page=None
					if len(page_split)>1:
						header_in_page=page_split[1]
					req = urllib2.Request(pageUrl)
					req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1')
					if 'refer' in m:
						req.add_header('Referer', m['refer'])
					if 'agent' in m:
						req.add_header('User-agent', m['agent'])
					if 'x-req' in m:
						req.add_header('X-Requested-With', m['x-req'])
					if 'x-forward' in m:
						req.add_header('X-Forwarded-For', m['x-forward'])
					if 'setcookie' in m:
						print 'adding cookie',m['setcookie']
						req.add_header('Cookie', m['setcookie'])
					if 'appendcookie' in m:
						print 'appending cookie to cookiejar',m['appendcookie']
						cookiestoApend=m['appendcookie']
						cookiestoApend=cookiestoApend.split(';')
						for h in cookiestoApend:
							n,v=h.split('=')
							w,n= n.split(':')
							ck = cookielib.Cookie(version=0, name=n, value=v, port=None, port_specified=False, domain=w, domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
							cookieJar.set_cookie(ck)

					if 'origin' in m:
						req.add_header('Origin', m['origin'])
					if header_in_page:
						header_in_page=header_in_page.split('&')
						for h in header_in_page:
							n,v=h.split('=')
							req.add_header(n,v)

					if not cookieJar==None:
						cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
						opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
						opener = urllib2.install_opener(opener)
						if 'noredirect' in m:
							opener2 = urllib2.build_opener(NoRedirection)
							opener = urllib2.install_opener(opener2)
							
					if 'connection' in m:
						print '..........................connection//////.',m['connection']
						from keepalive import HTTPHandler
						keepalive_handler = HTTPHandler()
						opener = urllib2.build_opener(keepalive_handler)
						urllib2.install_opener(opener)
						
					post=None

					if 'post' in m:
						postData=m['post']
						if '$LiveStreamRecaptcha' in postData:
							(captcha_challenge,catpcha_word)=processRecaptcha(m['page'])
							if captcha_challenge:
								postData+='recaptcha_challenge_field:'+captcha_challenge+',recaptcha_response_field:'+catpcha_word
						splitpost=postData.split(',');
						post={}
						for p in splitpost:
							n=p.split(':')[0];
							v=p.split(':')[1];
							post[n]=v
						post = urllib.urlencode(post)

					if 'rawpost' in m:
						post=m['rawpost']
						if '$LiveStreamRecaptcha' in post:
							(captcha_challenge,catpcha_word)=processRecaptcha(m['page'])
							if captcha_challenge:
							   post+='&recaptcha_challenge_field='+captcha_challenge+'&recaptcha_response_field='+catpcha_word

					if post:
						response = urllib2.urlopen(req,post)
					else:
						response = urllib2.urlopen(req)

					link = response.read()
					link=javascriptUnEscape(link)

					if 'includeheaders' in m:
						link+=str(response.headers.get('Set-Cookie'))

					response.close()
					cachedPages[m['page']] = link
					
					if forCookieJarOnly:
						return cookieJar
				elif m['page'] and  not m['page'].startswith('http'):
					if m['page'].startswith('$pyFunction:'):
						val=doEval(m['page'].split('$pyFunction:')[1],'',cookieJar )
						if forCookieJarOnly:
							return cookieJar
						link=val
					else:
						link=m['page']
			if '$pyFunction:playmedia(' in m['expre'] or 'ActivateWindow'  in m['expre']   or  any(x in url for x in g_ignoreSetResolved):
				setresolved=False
			if  '$doregex' in m['expre']:
				m['expre']=getRegexParsed(regexs, m['expre'],cookieJar,recursiveCall=True,cachedPages=cachedPages)

			if not m['expre']=='':
				print 'doing it ',m['expre']
				if '$LiveStreamCaptcha' in m['expre']:
					val=askCaptcha(m,link,cookieJar)

					url = url.replace("$doregex[" + k + "]", val)
				elif m['expre'].startswith('$pyFunction:'):

					val=doEval(m['expre'].split('$pyFunction:')[1],link,cookieJar )
					if 'ActivateWindow' in m['expre']: return 
					print 'still hre'
					print 'url k val',url,k,val

					url = url.replace("$doregex[" + k + "]", val)
				else:
					if not link=='':
						reg = re.compile(m['expre']).search(link)
						val=''
						try:
							val=reg.group(1).strip()
						except: traceback.print_exc()
					else:
						val=m['expre']
					if rawPost:
						print 'rawpost'
						val=urllib.quote_plus(val)
					if 'htmlunescape' in m:
						import HTMLParser
						val=HTMLParser.HTMLParser().unescape(val)                     
					url = url.replace("$doregex[" + k + "]", val)
			else:           
				url = url.replace("$doregex[" + k + "]",'')
	if '$epoctime$' in url:
		url=url.replace('$epoctime$',getEpocTime())
	if '$epoctime2$' in url:
		url=url.replace('$epoctime2$',getEpocTime2())

	if '$GUID$' in url:
		import uuid
		url=url.replace('$GUID$',str(uuid.uuid1()).upper())
	if '$get_cookies$' in url:
		url=url.replace('$get_cookies$',getCookiesString(cookieJar))   

	if recursiveCall: return url
	print 'final url',url
	if url=="": 
		return
	else:
		return url,setresolved