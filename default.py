# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Channel
# (c) 2015 - Simple TechNerd
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.youtubeAddon'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("Simple TechNerd", "channel/UCAj7O3LCDbkIR54hAn6Zz7A", 'https://i.ytimg.com/vi/W1isCkzf8vw/hqdefault.jpg'),
        ("New tech Rev.", "channel/UCgJRZOqPE2mijPl7aIzZS2Q", 'https://i.ytimg.com/vi/nc2dQCU2S7M/hqdefault.jpg'),
        ("One Tech Genius", "channel/UCP41cM9Ho0essJy06-Q9sBQ", 'https://i.ytimg.com/vi/Wlk1u2l1Ons/hqdefault.jpg'),				
]



# Entry point
def run():
    plugintools.log("youtubeAddon.run")
    
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
    plugintools.log("youtubeAddon.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()