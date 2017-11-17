# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: SkymashiTV
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.mainstreetdisney'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "FreshBakedDisney" 	# Fresh Baked Disney
YOUTUBE_CHANNEL_ID_2 = "MickeyViews" 				# MickeyViews
YOUTUBE_CHANNEL_ID_3 = "UCpXzU9rOlKNOQqthCee8zEw" 	# Network 1901
YOUTUBE_CHANNEL_ID_4 = "UCAjpFyA7FCRoGOuj5i4kq9g"	# Resort TV1
YOUTUBE_CHANNEL_ID_5 = "DISUnplugged"				# Dis Unplugged Podcast
YOUTUBE_CHANNEL_ID_6 = "UCnpWedLQdHpZqhgTLdB9Yyg"   # Disney Food Blog(DFB) 
YOUTUBE_CHANNEL_ID_7 = "UCRH49DSFyl8oPwsiHyZ9O0g"   # DSNY Newscast
YOUTUBE_CHANNEL_ID_8 = "JeffLangeDVD"				# MouseSteps
YOUTUBE_CHANNEL_ID_9 = "InsideTheMagic"				# Inside the Magic  
YOUTUBE_CHANNEL_ID_10= "PL0L1bxiTMVFiCIM4siPeD9pXLylB23WCr" # rides playlist
YOUTUBE_CHANNEL_ID_11="PL0L1bxiTMVFikz90Dc_q0iglsj-RYtYis"  # shows playlist 
YOUTUBE_CHANNEL_ID_12="AllCentralFlorida"                   #All Central Florida 



# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Fresh Baked Disney",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-ZfzE5DaVG3M/AAAAAAAAAAI/AAAAAAAAAAA/19M2tTnZuuc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MickeyViews",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-r0HwtrE0yOg/AAAAAAAAAAI/AAAAAAAAAAA/4xH638WADys/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Network 1901",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-RtP6VgKAIhQ/AAAAAAAAAAI/AAAAAAAAAAA/Om9tVkkt--Y/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Resort TV1",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-gW2DFTsDngs/AAAAAAAAAAI/AAAAAAAAAAA/-YET1pZHfAI/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Dis Unplugged",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-nEVT-SlFvnY/AAAAAAAAAAI/AAAAAAAAAAA/aeyyr0cPfvQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Disney Food Blog (DFB)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-MGge2enahgQ/AAAAAAAAAAI/AAAAAAAAAAA/tXZaNAmyYSw/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="DSNY Newscast",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/--hVDILJ4jkE/AAAAAAAAAAI/AAAAAAAAAAA/M6_SbistgG4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Mouse Steps",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-PvvwOIrt6U0/AAAAAAAAAAI/AAAAAAAAAAA/wG9FTeUDFSM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Inside The Magic (Disney & More)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-4UNiG4mCZhg/AAAAAAAAAAI/AAAAAAAAAAA/PJnWvP7ewvA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="All Central Florida",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-qyLiDiQqlk0/AAAAAAAAAAI/AAAAAAAAAAA/kwf4ypudeeE/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Ride Throughs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://berryburchett.net/kodi/addons/msd/icon.png",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Disney Park Shows",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://berryburchett.net/kodi/addons/msd/icon.png",
		fanart="http://berryburchett.net/couch/addons/msd/fanart.jpg",
        folder=True )
		
		
		
		
		
		
		
	
	
		
	
		
run()
