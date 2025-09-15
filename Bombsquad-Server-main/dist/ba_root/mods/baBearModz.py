# ba_meta require api 6
from __future__ import annotations
from typing import TYPE_CHECKING

import ba,_ba,random,time,datetime,weakref,json,os
from bastd.ui.settings.allsettings import AllSettingsWindow as Asw
from bastd.ui.popup import PopupWindow

if TYPE_CHECKING:
    from typing import List, Sequence, Optional, Dict, Any
    
MODZ = dict()

def getlanguage(text):
    lang = _ba.app.lang.language
    setphrases = {"Name":
                      {"Spanish": "Nombre",
                       "English": "Name",
                       "Portuguese": "Nome"},
                  "Creator":
                      {"Spanish": "Creador",
                       "English": "Creator",
                       "Portuguese": "Criador"},
                  "No Creator":
                      {"Spanish": "Desconocido",
                       "English": "Unknown",
                       "Portuguese": "Desconhecido"},
                 }
                 
    language = ["Spanish", "English", "Portuguese"]
    if lang not in language:
        lang = "English"
        
    if text not in setphrases:
        return text
    return setphrases[text][lang]

class BearPlugin:
    def __init__(self,
                 icon: str = 'nub',
                 creator: str = '',
                 plugin: Any = None,
                 window: ba.Window = None,
                 icon_color: Sequence[float] = (1.0, 1.0, 1.0),
                 button_color: Sequence[float] = (0.9, 0.2, 0.2),
                 window_color: Sequence[float] = (0.1, 0.4, 0.7)):
        self.plugin = plugin
        
        if creator == '':
            creator = getlanguage('No Creator')
        
        if plugin:
            name = self.getname()
            data = dict(
                icon=icon,
                plugin=plugin,
                window=window,
                creator=creator,
                icon_color=icon_color,
                button_color=button_color,
                window_color=window_color)
            MODZ[name] = data
    
    def getname(self):
        plugin = str(self.plugin)
        plugin = plugin.split("'")[1]
        return plugin

def plugins_window(self):
    ba.containerwidget(edit=self._root_widget,transition='out_left')
    ModzWindow()

salls = Asw.__init__
def new_init_alls(self, *args, **kwargs):
    salls(self, *args, **kwargs)

    uiscale = ba.app.ui.uiscale
    width = (100 if uiscale is
             ba.UIScale.SMALL else -14)
    position = (width,180)
    
    self.bm_button = ba.buttonwidget(parent=self._root_widget,
                     autoselect=True,position=position,
                     size=(70,70),button_type='square',
                     label='',on_activate_call=ba.Call(plugins_window, self))
                  
    self.bm_text = ba.textwidget(parent=self._root_widget,
                   position=(position[0]+35,position[1]+20),
                   size=(0, 0),scale=0.6,color=(0.7,0.9,0.7,1.0),
                   draw_controller=self.bm_button,maxwidth=100,
                   text=("Modz"),h_align='center',v_align='center')
                  
    self.bm_image = ba.imagewidget(parent=self._root_widget,
                    size=(40,40),draw_controller=self.bm_button,
                    position=(position[0]+15,position[1]+30),
                    color=(0.9,0.8,0.0),texture=ba.gettexture('folder'))

class ModzWindow(PopupWindow):
    def __init__(self, transition= 'in_right'):
        columns = 2
        self._width = width = 1200
        self._height = height = 500
        self._sub_height = 200
        self._scroll_width = self._width*0.90
        self._scroll_height = self._height - 180
        self._sub_width = self._scroll_width*0.95;

        app = ba.app.ui
        uiscale = app.uiscale

        self._root_widget = ba.containerwidget(size=(width+90,height+80),transition=transition,
                           scale=1.5 if uiscale is ba.UIScale.SMALL else 1.0,
                           stack_offset=(0,-30) if uiscale is ba.UIScale.SMALL else  (0,0))
        
        self._backButton = b = ba.buttonwidget(parent=self._root_widget,autoselect=True,
                                               position=(200,self._height-15),size=(130,60),
                                               scale=0.8,text_scale=1.2,label=ba.Lstr(resource='backText'),
                                               button_type='back',on_activate_call=ba.Call(self._back))
        ba.buttonwidget(edit=self._backButton, button_type='backSmall',size=(60, 60),label=ba.charstr(ba.SpecialChar.BACK))
        ba.containerwidget(edit=self._root_widget,cancel_button=b)
        
        self.titletext = ba.textwidget(parent=self._root_widget,position=(30, height-15),size=(width,50),
                          h_align="center",color=(0,1,0), text='Modz / Plugins', v_align="center",maxwidth=width*1.3)
        
        self._scrollwidget = ba.scrollwidget(parent=self._root_widget,
            position=(self._width*0.17,51*1.8),size=(self._sub_width -140,self._scroll_height +60*1.2))

        self._tab_container = None
        self._set_plugins()
    
    def _set_plugins(self):
        if self._tab_container is not None and self._tab_container.exists():
            self._tab_container.delete()
    
        len_modz = len(MODZ)
        sub_height = max(len_modz * 126, 0)
        v = sub_height - 55
        width = 300
        pos = (110, v-8)
        i = 0
        
        self._tab_container = c = ba.containerwidget(parent=self._scrollwidget,
            size=(self._sub_width,sub_height),
            background=False,selection_loops_to_parent=True)

        for mod in MODZ:
            info = MODZ[mod]
            
            ba.containerwidget(parent=c,position=(pos[0]*1.6-140,pos[1]-50-i),
                color=info['window_color'],scale=1.3,size=(600,80),background=True)
            
            txt = 'Plugin: ' + mod
            t = ba.textwidget(parent=c,position=(pos[0], pos[1]-i),size=(width,50),
                      scale=1.4,color=(0.2,1.2,0.2),h_align="center",v_align="center",
                      text=txt,maxwidth=400)
                      
            txt = getlanguage('Creator') + ': ' + info['creator']
            t = ba.textwidget(parent=c,position=(pos[0], pos[1]-40-i),size=(width,50),
                      scale=1.4,h_align="center",v_align="center",
                      color=ba.app.ui.title_color,text=txt,maxwidth=300)
                      
            if info['window'] is not None:
                pos2 = (pos[0]+560, pos[1]-32)
                b = ba.buttonwidget(parent=c,
                         autoselect=True,position=(pos2[0], pos2[1]-i),
                         size=(70,70),button_type='square',color=info['button_color'],
                         label='',on_activate_call=ba.Call(self.open_mod_window, info['window']))
    
                ic = ba.imagewidget(parent=c,
                        size=(60,60),draw_controller=b,
                        position=(pos2[0]+5, pos2[1]+8-i),
                        color=info['icon_color'],
                        texture=ba.gettexture(info['icon']))
            i += 126
            
    def open_mod_window(self, window: ba.Window):
        self.button_mod_back(window)
        ba.containerwidget(edit=self._root_widget,transition='out_left')
        window()

    def button_mod_back(self, window: ba.Window):
        """Esto es importante para regresar a la ventana principal.
           Asegúrese de usar 'self._back' como llamada."""
        """This is important to return to the main window.
           Be sure to use 'self._back' as the callback."""
           
        window._back = ModzWindow._back_mod
        
    def _back_mod(self):
        ba.containerwidget(edit=self._root_widget,transition='out_left')
        ModzWindow()

    def _back(self):
        ba.containerwidget(edit=self._root_widget,transition='out_left')
        Asw()

# ba_meta export plugin
class Plugins(ba.Plugin):
    def on_app_launch(self) -> None:
        Asw.__init__ = new_init_alls
