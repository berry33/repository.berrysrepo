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

addonID = 'plugin.video.crabbyq'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "quiltinaday" 	#
YOUTUBE_CHANNEL_ID_2 = "MissouriQuiltCo" 	#
YOUTUBE_CHANNEL_ID_3 = "SewVeryEasy" 	#
YOUTUBE_CHANNEL_ID_4 = "UCx44Zf6KYNL53ikyk7insIA"
YOUTUBE_CHANNEL_ID_5 = "UCn4Dv2omn_Z9MI1jragzvTg"
YOUTUBE_CHANNEL_ID_6 = "talkquilting"
YOUTUBE_CHANNEL_ID_7 = "FatQuarterShop"
YOUTUBE_CHANNEL_ID_8 = "GourmetQuilter"
YOUTUBE_CHANNEL_ID_9 = "ShabbyFabrics"
YOUTUBE_CHANNEL_ID_10 = "UCjmr4EDCP5_ktyVew_h42qQ"
YOUTUBE_CHANNEL_ID_11 = "UCnJfaHpW64CECS_SEp57jwg"
YOUTUBE_CHANNEL_ID_12 = "lcvday"
YOUTUBE_CHANNEL_ID_13 = "UC0pG03YOX2DSwn8Se32TnNQ"
YOUTUBE_CHANNEL_ID_14 = "PLLNlu3SeiUIaQ7eirAbRZafIcOCmPOeBn"
YOUTUBE_CHANNEL_ID_15 = "UC5Bq6lhcBXmSxk3FZr73iNw"
YOUTUBE_CHANNEL_ID_16 = "UCjEyZXNp7HBwU32p3RT7YlA"


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
        title="Quilt in a Day",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-S65m6nYWin8/AAAAAAAAAAI/AAAAAAAAAAA/9SHRcwHT6Ww/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Missouri Star Quilt Company",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-WV_NWdK6_TU/AAAAAAAAAAI/AAAAAAAAAAA/YWd1lo9KQFQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sew Very Easy",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-uZX7yH7CI_o/AAAAAAAAAAI/AAAAAAAAAAA/nDbRHPd0UEg/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jordan Fabrics",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-eCbDYHlhtQk/AAAAAAAAAAI/AAAAAAAAAAA/Yim974U13yc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Man Sewing ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-CKMYi_zfnDo/AAAAAAAAAAI/AAAAAAAAAAA/udcsf4CQx3U/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Talk Quilting",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-KYsXoK-qTao/AAAAAAAAAAI/AAAAAAAAAAA/yPu1aaQpy_0/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fat Quarter Shop",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-UPZQ-g28l3I/AAAAAAAAAAI/AAAAAAAAAAA/9_xkbCZXFes/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )


    plugintools.add_item( 
        #action="", 
        title="Gourmet Quilter",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-6hXfhA4kU7A/AAAAAAAAAAI/AAAAAAAAAAA/NDPTo7tJS4c/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Shabby Fabrics",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-vgIadHGDnq4/AAAAAAAAAAI/AAAAAAAAAAA/YVUG9EGt1aA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sharon Schamber Network",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-JzCJpyus9tM/AAAAAAAAAAI/AAAAAAAAAAA/k5s_iaLDzlM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sewing with Nancy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-ZBNHOuaHM_I/AAAAAAAAAAI/AAAAAAAAAAA/SxCaEMemFeY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Leah Day",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-xBYd5kgI1Fk/AAAAAAAAAAI/AAAAAAAAAAA/DiwQ8BTCmIk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Angela Walters",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-NFD-yiYcSfo/AAAAAAAAAAI/AAAAAAAAAAA/rTGqtiE4pPM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Midnight Quilt Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-MSu7-Uf1SlE/AAAAAAAAAAI/AAAAAAAAAAA/ZI5u5gF9PFk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fabric Juncition",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-shUuJKHhBPE/AAAAAAAAAAI/AAAAAAAAAAA/hshsag7c27c/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Paula Storm",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-KoJyOLClOKs/AAAAAAAAAAI/AAAAAAAAAAA/qnp8nMKRsh8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="http://berryburchett.net/couch/addons/crabby/fanart.jpg",
        folder=True )








		
run()
