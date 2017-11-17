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

addonID = 'plugin.video.thewoo'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "TheDailyWoo" 	#
YOUTUBE_CHANNEL_ID_2 = "adamthewoo" 	#



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
        title="The Daily Woo",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-7cmuWk3x9L4/AAAAAAAAAAI/AAAAAAAAAAA/_ieuIiPHNT8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/woo/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Adam The Woo",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-I-08Ixv_ops/AAAAAAAAAAI/AAAAAAAAAAA/dOH0oWRAtac/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/woo/fanart.jpg",
        folder=True )



		
run()
