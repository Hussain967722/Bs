# ba_meta require api 6
from __future__ import annotations
from typing import TYPE_CHECKING
import base64

if TYPE_CHECKING: pass

import ba,_ba,random,time,datetime,weakref,json,os
from bastd.ui.settings import advanced
from ba._enums import SpecialChar
from bastd.ui.confirm import ConfirmWindow
from bastd.ui.popup import PopupWindow
from bastd.actor.spaz import Spaz

def getlanguage(txt):
    lang = _ba.app.lang.language
    texts = {"Tittle":{"Spanish": "Añade tus textos",
                 "English": "Add your texts",
                 "Portuguese": "Adicione seus textos"},
             "Tittle2":{"Spanish": "Todos tus textos guardados",
                 "English": "All your saved texts",
                 "Portuguese": "Todos os seus textos salvos"},
             "Confirm":{"Spanish": "¿Estás seguro de querer \n borrar todos los textos?",
                 "English": "Are you sure you want to delete all the texts?",
                 "Portuguese": "Tem certeza de que deseja excluir todos os textos?"},
             "Add Text":{"Spanish": "Texto Guardardo",
                 "English": "Saved Text",
                 "Portuguese": "Texto Salvo"},
             "Del Tex":{"Spanish": "Texto eliminado",
                 "English": "Text removed",
                 "Portuguese": "Texto removido"},
             "Double Text":{"Spanish": "Este texto ya existe",
                 "English": "This text already exists",
                 "Portuguese": "Este texto já existe"},
             "Nothing text":{"Spanish": "Ya no hay textos",
                 "English": "There are no texts",
                 "Portuguese": "Não há textos"},
             "Confirm date":{"Spanish": "Todos los textos han sido eliminados",
                 "English": "All texts have been removed",
                 "Portuguese": "Todos os textos foram removidos"},
             "Multicolor Text":{"Spanish": "Color Cambiante",
                 "English": "Changing Color",
                 "Portuguese": "Mudança de cor"},
             "Add":{"Spanish": "Agregar",
                 "English": "Add",
                 "Portuguese": "Adicionar"},
             "Del":{"Spanish": "Borrar",
                 "English": "Delete",
                 "Portuguese": "Excluir"},
             "Del All":{"Spanish": "Borrar todo",
                 "English": "Delete everything",
                 "Portuguese": "Limpar tudo"},
             "Flags":{"Spanish": "Banderas",
                 "English": "Flags",
                 "Portuguese": "Bandeiras"},
             "Icons":{"Spanish": "Íconos",
                 "English": "Icons",
                 "Portuguese": "Ícones"},
             "Picker Color":{"Spanish": "Escoge tu color personalizado",
                 "English": "Choose your custom color",
                 "Portuguese": "Escolha sua cor personalizada"},
             "Tittle3":{"Spanish": "Añade un texto aquí",
                 "English": "Add text here",
                 "Portuguese": "Adicione texto aqui"}}
                 
    language = ['Spanish', 'Portuguese', 'English']
    if lang not in language:
        lang = 'English'
    return texts[txt][lang]

def thanks():
    return ['_BMB-SPT_']

def getcolors():
    return {"Rojo":
                (1,0,0),
            "Naranja":
                (1,0.5,0),
            "Amarillo":
                (1,1,0),
            "Verde":
                (0,1,0),
            "Azul":
                (0,1,1),
            "Indigo":
                (0.5,0.5,1),
            "Violeta":
                (1,0,1)}

def configs():
    return [("Window", True),
            ("Multicolor", True),
            ("Texts", 'TextMod'),
            ("Icon List", 'Icons'),
            ("Texts List",thanks()),
            ("Colors",(1,1,1)),
            ("Color Text",{thanks()[0]: (1,1,1)})]

cfg = ba.app.config
for config, settings in configs():
    if cfg.get(config) is None:
        cfg[config] = settings
cfg.apply_and_commit()

def random_colors():
    c = [(1,0,0),(1,0.5,0),(1,1,0),(0,1,0),
         (0,1,1),(0.5,0.5,1),(0,0,1),(1,0,1)]
    return random.choice(c)

def random_texts():
    return random.choice(cfg['Texts List'])

def colors(color):
    c = [(1,0,0),(1,0.5,0),(1,1,0),(0,1,0),
         (0,1,1),(0.5,0.5,1),(0,0,1),(1,0,1)]
    return c[color]

def window(self):
    self.up_time_color = None
    ba.containerwidget(edit=self._root_widget,transition='out_left')
    TextWindow()

def set_icons():
    return [_ba.charstr(SpecialChar.CROWN),
            _ba.charstr(SpecialChar.DRAGON),
            _ba.charstr(SpecialChar.SKULL),
            _ba.charstr(SpecialChar.HEART),
            _ba.charstr(SpecialChar.FEDORA),
            _ba.charstr(SpecialChar.HAL),
            _ba.charstr(SpecialChar.YIN_YANG),
            _ba.charstr(SpecialChar.EYE_BALL),
            _ba.charstr(SpecialChar.HELMET),
            _ba.charstr(SpecialChar.MUSHROOM),
            _ba.charstr(SpecialChar.NINJA_STAR),
            _ba.charstr(SpecialChar.VIKING_HELMET),
            _ba.charstr(SpecialChar.MOON),
            _ba.charstr(SpecialChar.SPIDER),
            _ba.charstr(SpecialChar.FIREBALL),
            _ba.charstr(SpecialChar.MIKIROG),
            "\ue026","\ue020","\ue01e","\ue027"]
    
def set_flags():
    return [_ba.charstr(SpecialChar.FLAG_MEXICO),
            _ba.charstr(SpecialChar.FLAG_UNITED_STATES),
            _ba.charstr(SpecialChar.FLAG_CANADA),
            _ba.charstr(SpecialChar.FLAG_ARGENTINA),
            _ba.charstr(SpecialChar.FLAG_CHILE),
            _ba.charstr(SpecialChar.FLAG_BRAZIL),
            _ba.charstr(SpecialChar.FLAG_RUSSIA),
            _ba.charstr(SpecialChar.FLAG_JAPAN),
            _ba.charstr(SpecialChar.FLAG_CHINA),
            _ba.charstr(SpecialChar.FLAG_SOUTH_KOREA),
            _ba.charstr(SpecialChar.FLAG_GERMANY),
            _ba.charstr(SpecialChar.FLAG_UNITED_KINGDOM),
            _ba.charstr(SpecialChar.FLAG_INDIA),
            _ba.charstr(SpecialChar.FLAG_FRANCE),
            _ba.charstr(SpecialChar.FLAG_INDONESIA),
            _ba.charstr(SpecialChar.FLAG_ITALY),
            _ba.charstr(SpecialChar.FLAG_NETHERLANDS),
            _ba.charstr(SpecialChar.FLAG_QATAR),
            _ba.charstr(SpecialChar.FLAG_ALGERIA),
            _ba.charstr(SpecialChar.FLAG_KUWAIT),
            _ba.charstr(SpecialChar.FLAG_EGYPT),
            _ba.charstr(SpecialChar.FLAG_MALAYSIA),
            _ba.charstr(SpecialChar.FLAG_CZECH_REPUBLIC),
            _ba.charstr(SpecialChar.FLAG_AUSTRALIA),
            _ba.charstr(SpecialChar.FLAG_SINGAPORE),
            _ba.charstr(SpecialChar.FLAG_IRAN),
            _ba.charstr(SpecialChar.FLAG_POLAND),
            _ba.charstr(SpecialChar.FLAG_PHILIPPINES),
            _ba.charstr(SpecialChar.FLAG_SAUDI_ARABIA),
            _ba.charstr(SpecialChar.FLAG_UNITED_ARAB_EMIRATES)]

class TextWindow(PopupWindow):
    def __init__(self, transition= 'in_right'):
        self._transition = transition
        self._container = None
        self._refresh()

    def _refresh(self):
        
        if self._container is not None and self._container.exists():
            self._container.delete()
        
        app = ba.app.ui
        uiscale = app.uiscale

        self._width = width = 800
        self._height = height = 500
        self._sub_height = 200
        self._scroll_width = self._width*0.90
        self._scroll_height = self._height - 180
        self._sub_width = self._scroll_width*0.95;
        
        self._window = cfg['Window']
        self._name = cfg['Texts List']

        self._root_widget = ba.containerwidget(size=(width+90,height+80),transition=self._transition,
                           scale=1.5 if uiscale is ba.UIScale.SMALL else 1.0,
                           stack_offset=(0,-30) if uiscale is ba.UIScale.SMALL else  (0,0))
        
        self._backButton = b = ba.buttonwidget(parent=self._root_widget,autoselect=True,
                                               position=(60,self._height-50),size=(130,60),
                                               scale=0.8,text_scale=1.2,label=ba.Lstr(resource='backText'),
                                               button_type='back',on_activate_call=ba.Call(self._back))
        ba.buttonwidget(edit=self._backButton, button_type='backSmall',size=(60, 60),label=ba.charstr(ba.SpecialChar.BACK))
        ba.containerwidget(edit=self._root_widget,cancel_button=b)

        self.titletext = ba.textwidget(parent=self._root_widget,position=(40, height),size=(width,50),
                          h_align="center",color=ba.app.ui.title_color, v_align="center",maxwidth=width*1.3)

        self.oth = ba.buttonwidget(parent=self._root_widget,autoselect=True,
                             position=(55,self._height-130),size=(60,60),
                             color=(0,0,1) if self._window else (0,1,1),scale=0.8,label='',button_type='square',
                             texture=ba.gettexture('replayIcon'),on_activate_call=ba.Call(self._other))

        self._scrollwidget = ba.scrollwidget(parent=self._root_widget,
                             position=(self._width*0.14,51*1.7),
                             size=(self._sub_width,self._scroll_height+100),selection_loops_to_parent=True)

        self._tab_container = None
        self._set_window(self._window)

    def _other(self):
        if self._window:
            self._window = False
            ba.buttonwidget(edit=self.oth,color=(0,1,1))
            self._saved_text()
        else:
            self._window = True
            ba.buttonwidget(edit=self.oth,color=(0,0,1))
        self._set_window(self._window)
        cfg.apply_and_commit()

    def _set_window(self, tag):
        cfg['Window'] = tag
        cfg.apply_and_commit()
        
        if self._tab_container is not None and self._tab_container.exists():
            self._tab_container.delete()
        self.text_time = None

        if tag:
            sub_height = 300
            v = sub_height - 55
            width = 300
            ba.textwidget(edit=self.titletext,text=getlanguage('Tittle'))

            self._tab_container = c = ba.containerwidget(parent=self._scrollwidget,
                                size=(self._sub_width,sub_height),
                                background=False,selection_loops_to_parent=True)

            up = 60
            upx = 10
            
            t = ba.textwidget(parent=c,position=(60*2.2+upx,v-80+up),size=(205 * 1.8,53),h_align="center",
                              color=ba.app.ui.title_color, text=getlanguage('Tittle3'), v_align="center",maxwidth=width*1.6)
            
            self.editable_text = ba.textwidget(parent=c,position=(60*2.2+upx,v-70*2+up),size=(205 * 1.8,53),selectable=True,
                              editable=True,max_chars=40,description=ba.Lstr(resource='editProfileWindow.nameText'),
                              h_align="center",color=(1,1,1), text=cfg['Texts'], v_align="center",maxwidth=width*1.6)

            b = ba.buttonwidget(parent=c,autoselect=True,
                                   position=(120*3.4+upx,v-70*2.7+up),size=(130,60),
                                   color=(0,1,0),scale=0.8,label=getlanguage('Add'),button_type='square',
                                   textcolor=ba.app.ui.title_color,on_activate_call=ba.Call(self.do_not_duplicate,'Color'))

            b2 = ba.buttonwidget(parent=c,autoselect=True,
                                   position=(120*2.2+upx,v-70*2.7+up),size=(130,60),
                                   color=(1,1,0),scale=0.8,label=getlanguage('Del'),button_type='square',
                                   textcolor=ba.app.ui.title_color,on_activate_call=ba.Call(self._remove))

            b3 = ba.buttonwidget(parent=c,autoselect=True,
                                   position=(120*1+upx,v-70*2.7+up),size=(130,60),
                                   color=(1,0,0),scale=0.8,label=getlanguage('Del All'),button_type='square',
                                   textcolor=ba.app.ui.title_color,on_activate_call=ba.Call(self._remove_all))
            self.iconpos = (120*4.4,v-70*1.1)
            b4 = ba.buttonwidget(parent=c,autoselect=True,
                                   position=self.iconpos,size=(60,60),
                                   color=(0.52,0.48,0.63),scale=0.8,label=set_icons()[1],
                                   button_type='square',on_activate_call=ba.Call(self._icon))

            u = -30
            self.check = ba.checkboxwidget(parent=c,position=(120*1.8,v-70*4-u),value=cfg['Multicolor'],
                             on_value_change_call=ba.Call(self._switches,'Multicolor'),maxwidth=self._scroll_width*0.9,
                             text=getlanguage('Multicolor Text'),autoselect=True)

        else:
            if len(self._name) >= 8: sub_height = (len(self._name) / 0.5 * 30)
            else: sub_height = 400
            
            width = 700
            v = sub_height - 55
            self.texts_widgets = {}
            ba.textwidget(edit=self.titletext,text=getlanguage('Tittle2'))
            
            self._tab_container = c = ba.containerwidget(parent=self._scrollwidget,
                                size=(self._sub_width,sub_height),
                                background=False,selection_loops_to_parent=True)

            position = 0
            for names in self._name:
                self.txtnames = ba.textwidget(parent=c,position=(-40,v-position),size=(width,50),selectable=True,
                              h_align="center",color=cfg['Color Text'][names],text=names,v_align="center",maxwidth=width*1.6)
                self.texts_widgets[names] = self.txtnames
                position += 60
                
            if self.texts_widgets == {}:
                self.text_time = None
            else:
                if cfg['Multicolor']:
                    self.text_time = ba.Timer(
                          0.1,ba.WeakCall(
                              self.text_update_color),repeat=True)
                else: pass
        
    def _multicolor(self):
        if cfg['Multicolor']:
            cfg['Multicolor'] = False
            ba.buttonwidget(edit=self.button_color,color=(1,0,0))
        else:
            ba.buttonwidget(edit=self.button_color,color=(0,1,0))
            cfg['Multicolor'] = True
    
    def _switches(self,tag,m):
        cfg[tag] = False if m==0 else True
        apg.apply_and_commit()
    
    def _save(self):
        self._name.append(cfg['Texts'])
        ba.screenmessage(f"{getlanguage('Add Text')}: {self._name[-1]}",cfg['Colors'])
        cfg['Color Text'][self._name[-1]] = cfg['Colors']
        ba.playsound(ba.getsound('gunCocking'))
        cfg.apply_and_commit()
        
    def _remove(self):
        if len(self._name) == 0:
            ba.screenmessage(getlanguage('Nothing text'),(1,0,0))
        else:
            ba.screenmessage(f"{getlanguage('Del Tex')}: {self._name[-1]}",(1,0,0))
            del cfg['Color Text'][self._name[-1]]
            self._name.pop()
    
    def _remove_all(self):
        def confirm():
            delname = []
            for x in cfg['Texts List']:
                delname.append(x)
            for n in delname:
                del cfg['Color Text'][n]
                cfg['Texts List'].remove(n)
            ba.screenmessage(getlanguage('Confirm date'),(1,1,0))
            cfg.apply_and_commit()
        ConfirmWindow(getlanguage('Confirm'),
                          width=400, height=120, action=confirm, ok_text=ba.Lstr(resource='okText'))
    
    def do_not_duplicate(self, c):
        self._saved_text()
        if cfg['Texts'] not in self._name:
            self._make_picker(c)
        else:
            ba.playsound(ba.getsound('error'))
            ba.screenmessage(getlanguage('Double Text'),(1,1,0))
    
    def _make_picker(self,tag):
        from bastd.ui.colorpicker import ColorPicker
        if tag == 'Color': initial_color = cfg['Colors']
        ColorPicker(parent=self._root_widget,position=(0,0),
        initial_color=initial_color,delegate=self,tag=tag)
        
    def color_picker_closing(self, picker):
        pass

    def color_picker_selected_color(self, picker, color):
        tag = picker.get_tag()
        if tag == 'Color':
            cfg['Colors'] = color
            self._save()
    
    def _saved_text(self):
        self._name_editable = ba.textwidget(query=self.editable_text)
        cfg['Texts'] = self._name_editable
    
    def text_update_color(self):
        for update in self._name:
            ba.textwidget(edit=self.texts_widgets[update],color=(random_colors()))
    
    def _icon(self):
        IconWindow(pos=(self.iconpos[0]-60*6,self.iconpos[1]-60*2),
                   callback=ba.Call(window, self))
        self._saved_text()
    
    
    def _back(self):
        self.text_time = None
        ba.containerwidget(edit=self._root_widget,transition='out_left')
        advanced.AdvancedSettingsWindow()
        self._saved_text()
    
class IconWindow(PopupWindow):
    def __init__(self, pos=(0,0), callback=None):
        self.callback = callback
        uiscale = ba.app.ui.uiscale
        self._transitioning_out = False
        scale = 2 if uiscale is ba.UIScale.SMALL else 1.3
        ipos = 0
        self._width = 380
        self._height = 300
        sub_width = self._width - 90
        sub_height = 100*6
        v = sub_height - 30
        bg_color = (0.5, 0.4, 0.6)

        self._current_tab = cfg['Icon List']
        self.collect = {}

        PopupWindow.__init__(self,position=pos,
                             size=(self._width, self._height),
                             scale=scale,bg_color=bg_color)

        self._cancel_button = ba.buttonwidget( parent=self.root_widget,
            position=(50, self._height - 30), size=(50, 50),
            scale=0.5, label=ba.charstr(ba.SpecialChar.BACK),button_type='backSmall',
            color=(1,0,0),on_activate_call=self.on_popup_cancel,autoselect=True)
        ba.containerwidget(edit=self.root_widget,cancel_button=self._cancel_button)

        self._scrollwidget = ba.scrollwidget(parent=self.root_widget,
                                             size=(self._width - 60,
                                                   self._height - 70),
                                             position=(30, 30))

        iconlist = [("Icons",getlanguage('Icons')), ("Flags",getlanguage('Flags'))]
        for x,j in iconlist:
            self.collect[x] = ba.buttonwidget(parent=self.root_widget,size=(150*1.3, 60),
                scale=0.5,position=(60*1.5+ipos, self._height - 45),label=j,
                button_type='tab',enable_sound=False,autoselect=True,
                on_activate_call=ba.Call(self._set_tab,x,sound=True))
            ipos += 100
            
        self._subcontainer = None
        self._set_tab(self._current_tab)

    def _set_tab(self, tab, sound=False):
        self.sound = sound
        cfg['Icon List'] = tab
        cfg.apply_and_commit()

        if self._subcontainer is not None and self._subcontainer.exists():
            self._subcontainer.delete()
            
        if self.sound:
            self._tick_and_call()

        if tab == 'Icons':
            sub_height = 240
            v = sub_height - 50
            u = 10
            self._subcontainer = c = ba.containerwidget(parent=self._scrollwidget,
                                     size=(self._width, sub_height),
                                     background=False)
               
            pos1 = 0
            for icon1 in range(5):
                b = ba.buttonwidget(parent=c,position=(u+pos1,v),size=(40,40),button_type='square',
                    label=set_icons()[icon1],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._icons,icon1),autoselect=True)
                pos1 += 60
                
            pos2 = 0
            for icon2 in range(5,10):
                b = ba.buttonwidget(parent=c,position=(u+pos2,v-60),size=(40,40),button_type='square',
                    label=set_icons()[icon2],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._icons,icon2),autoselect=True)
                pos2 += 60
                      
            pos3 = 0
            for icon3 in range(10,15):
                b = ba.buttonwidget(parent=c,position=(u+pos3,v-60*2),size=(40,40),button_type='square',
                    label=set_icons()[icon3],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._icons,icon3),autoselect=True)
                pos3 += 60
                      
            pos4 = 0
            for icon4 in range(15,20):
                b = ba.buttonwidget(parent=c,position=(u+pos4,v-60*3),size=(40,40),button_type='square',
                    label=set_icons()[icon4],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._icons,icon4),autoselect=True)
                pos4 += 60
                      
        elif tab == 'Flags':
            sub_height = 360
            v = sub_height - 50
            u = 10
            self._subcontainer = c = ba.containerwidget(parent=self._scrollwidget,
                                     size=(self._width, sub_height),
                                     background=False)
               
            pos1 = 0
            for flag1 in range(5):
                b = ba.buttonwidget(parent=c,position=(u+pos1,v),size=(40,40),button_type='square',
                    label=set_flags()[flag1],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._flags,flag1),autoselect=True)
                pos1 += 60
                
            pos2 = 0
            for flag2 in range(5,10):
                b = ba.buttonwidget(parent=c,position=(u+pos2,v-60),size=(40,40),button_type='square',
                    label=set_flags()[flag2],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._flags,flag2),autoselect=True)
                pos2 += 60
                      
            pos3 = 0
            for flag3 in range(10,15):
                b = ba.buttonwidget(parent=c,position=(u+pos3,v-60*2),size=(40,40),button_type='square',
                    label=set_flags()[flag3],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._flags,flag3),autoselect=True)
                pos3 += 60
                      
            pos4 = 0
            for flag4 in range(15,20):
                b = ba.buttonwidget(parent=c,position=(u+pos4,v-60*3),size=(40,40),button_type='square',
                    label=set_flags()[flag4],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._flags,flag4),autoselect=True)
                pos4 += 60

            pos5 = 0
            for flag5 in range(20,25):
                b = ba.buttonwidget(parent=c,position=(u+pos5,v-60*4),size=(40,40),button_type='square',
                    label=set_flags()[flag5],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._flags,flag5),autoselect=True)
                pos5 += 60

            pos6 = 0
            for flag6 in range(25,30):
                b = ba.buttonwidget(parent=c,position=(u+pos6,v-60*5),size=(40,40),button_type='square',
                    label=set_flags()[flag6],color=(0.8,0.8,0.8),on_activate_call=ba.Call(self._flags,flag6),autoselect=True)
                pos6 += 60

        for icons in self.collect:
            if icons == tab:
                ba.buttonwidget(edit=self.collect[icons],color=(0.5, 0.4, 0.93))
            else: ba.buttonwidget(edit=self.collect[icons],color=(0.52, 0.48, 0.63))

    def _icons(self, icon):
        cfg['Texts'] += set_icons()[icon]
        self._on_cancel_press()

    def _flags(self, flag):
        cfg['Texts'] += set_flags()[flag]
        self._on_cancel_press()

    def _tick_and_call(self):
        ba.playsound(ba.getsound('click01'))

    def _on_cancel_press(self) -> None:
        self._transition_out()
        self.callback()

    def _transition_out(self) -> None:
        if not self._transitioning_out:
            self._transitioning_out = True
            ba.containerwidget(edit=self.root_widget, transition='out_scale')
            
    def on_popup_cancel(self) -> None:
        ba.playsound(ba.getsound('swish'))
        self._transition_out()
        
GLOBAL = {"Alm": list()}
        
super_map = ba.Map.__init__
def text_init(self, *args,**kwargs):
    super_map(self, *args,**kwargs)

    texts = cfg['Texts List']
    color_texts = cfg['Color Text']
    GLOBAL['Alm'] = []
    
    def text(scale=1.5,
             position=(0,260),
             shadow=1,h_align='center'):
        random_txt = random_texts()                     
        self.txt = ba.newnode('text',
              attrs={'text': random_txt,
                     'scale': scale,
                     'shadow': shadow,
                     'color': cfg['Color Text'][random_txt],
                     'position': position,
                     'h_align': h_align})
        ba.animate(self.txt,'opacity',
            {0:0, 2:0, 2.5:1, 27:1, 28:0}, True)
        
        if cfg['Multicolor']:
            ba.animate_array(self.txt,"color",3,
                {0: colors(0), 1: colors(1), 2: colors(2), 3: colors(3), 4: colors(4),
                 5: colors(5), 6: colors(6), 7: colors(7), 8: colors(0)},True)
        
    if any(texts) or any(color_texts):
        text()

        def update():
            alm = GLOBAL['Alm']
            while(True):
                if len(texts) == len(alm):
                    alm = []
                
                t = random_texts()
                if t not in alm:
                    self.txt.text = t
                    alm.append(t)
                    break

            GLOBAL['Alm'] = [alm[-1]]
            
        self.uptime = ba.Timer(28.0,
            ba.WeakCall(update), repeat=True)
        
def add_plugin():
    try: from baBearModz import BearPlugin
    except Exception as e:
        return ba.timer(2.5, lambda e=e:
               ba.screenmessage('Error plugin: ' + str(e), (1,0,0)))
               
    BearPlugin(icon='fontExtras',
               creator='@PatrónModz',
               button_color=(0.25, 0.25, 0.25),
               plugin=Text,
               window=TextWindow)
        
# ba_meta export plugin
class Text(ba.Plugin):
    ba.Map.__init__ = text_init
    
    def on_app_launch(self) -> None:
        add_plugin()