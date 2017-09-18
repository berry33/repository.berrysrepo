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

addonID = 'plugin.video.steeple'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "martind28picker" 	#
YOUTUBE_CHANNEL_ID_2 = "PL0L1bxiTMVFgwBMWThSUkHsscz5N2SC0J"


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
        title="Evangelistic Outreach",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/calvinray_brian.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Beth Moore",
        url="plugin://plugin.video.youtube/search/?q=Beth Moore"+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/beth.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Creflo Dollar",
        url="plugin://plugin.video.youtube/search/?q=creflo dollar"+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/Greflo.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )


    plugintools.add_item( 
        #action="", 
        title="Joel Osteen",
        url="plugin://plugin.video.youtube/search/?q=joel osteen"+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/Joel.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="John Hagee",
        url="plugin://plugin.video.youtube/search/?q=john hagee"+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/John.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Charles Stanley",
        url="plugin://plugin.video.youtube/search/?q=charles stanley"+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/charles.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="David Jeremiah",
        url="plugin://plugin.video.youtube/search/?q=david jeremiah"+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/david.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jesse Duplantis",
        url="plugin://plugin.video.youtube/search/?q=jesse duplantis"+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/jesse.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Joyce Meyer",
        url="plugin://plugin.video.youtube/search/?q=joyce meyer"+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/joyce.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="T.D. Jakes",
        url="plugin://plugin.video.youtube/search/?q=td jakes"+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/td.jpg",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christian Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://berryburchett.net/kodi/addons/steeple/icons/movie-icon-6.png",
		fanart="http://berryburchett.net/kodi/addons/steeple/fanart.jpg",
        folder=True )

    		
run()
