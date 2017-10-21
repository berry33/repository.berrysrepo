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

addonID = 'plugin.video.techie'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "TechGuyLabs" 	#
YOUTUBE_CHANNEL_ID_2 = "TWiTWindowsWeekly" 	#
YOUTUBE_CHANNEL_ID_3 = "TWiTTechNews" 	#
YOUTUBE_CHANNEL_ID_4 = "TWiTGizWiz"   #


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
        title="The Tech Guy",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-C7L9B9aDApM/AAAAAAAAAAI/AAAAAAAAAAA/JhcOeFCm6Pw/s176-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://yt3.ggpht.com/-C7L9B9aDApM/AAAAAAAAAAI/AAAAAAAAAAA/JhcOeFCm6Pw/s176-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Windows Weekly",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-QxIpvqH_T_c/AAAAAAAAAAI/AAAAAAAAAAA/I9yLiPbx1eA/s176-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://yt3.ggpht.com/-QxIpvqH_T_c/AAAAAAAAAAI/AAAAAAAAAAA/I9yLiPbx1eA/s176-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tech News Weekly",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/--6h0tC9q0l0/AAAAAAAAAAI/AAAAAAAAAAA/vJqwIGbNTGs/s176-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="https://yt3.ggpht.com/--6h0tC9q0l0/AAAAAAAAAAI/AAAAAAAAAAA/vJqwIGbNTGs/s176-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Giz Wiz",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-qUlrIjmUlnU/AAAAAAAAAAI/AAAAAAAAAAA/c3vNDDuhqzY/s176-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="https://yt3.ggpht.com/-qUlrIjmUlnU/AAAAAAAAAAI/AAAAAAAAAAA/c3vNDDuhqzY/s176-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

		
run()
