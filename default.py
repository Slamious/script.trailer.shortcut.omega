# -*- coding: utf-8 -*-

from urllib.parse import quote
import xbmc
import xbmcvfs
import xbmcaddon
from xbmcgui import Dialog

__addon__ = xbmcaddon.Addon()
__addon_id__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = xbmcvfs.translatePath(__addon__.getAddonInfo('path'))
__lang__ = __addon__.getLocalizedString
__notification__ = Dialog().notification


class PlayTrailer:
    
    def __init__(self):
        
        self.getTrailer()
    
    def getTrailer(self):
    
        trailer = xbmc.getInfoLabel('ListItem.Trailer')
        if 'plugin://plugin.video.youtube' not in trailer:
            trailer = quote(trailer).replace('%3A', ':')
        
        self.debug(f'Trailer = {trailer}')
        
        if len(trailer) > 0:
            xbmc.Player().play(trailer)
        else:
            self.notify(__lang__(32000))
            return
            
    def debug(self, msg):
        if 'true' in __addon__.getSetting('debug'):
            xbmc.log(f'>>>>  {__addonname__} <<<<  {msg}', xbmc.LOGINFO)
        
    def notify(self, msg):
        if __addon__.getSettingBool('notify') is True:
            __notification__(__addonname__, msg, icon=__icon__, time=4000)

if __name__ == '__main__':
    PlayTrailer()
    