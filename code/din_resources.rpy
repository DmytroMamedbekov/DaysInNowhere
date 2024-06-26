init python:
    import time
    from os import path
    
    for file_name in renpy.list_files():
        if "din" in file_name:
            file_path = path.splitext(path.basename(file_name))[0]

            if file_name.startswith("din/images/bg/"):
                renpy.image("bg " + file_path, file_name)

            elif file_name.startswith("din/images/gui/"):
                renpy.image(file_path, file_name)

            elif file_name.startswith("din/images/sprites/"):
                renpy.image(file_path, ConditionSwitch("persistent.sprite_time == 'sunset'", im.MatrixColor(file_name, im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time == 'night'", im.MatrixColor(file_name, im.matrix.tint(0.63, 0.78, 0.82)), True, file_name))

            elif file_name.startswith("din/sounds/"):
                globals()[file_path] = file_name

    din_std_set_for_preview = {}
    din_std_set = {}
    store.din_colors = {}
    store.din_names = {}
    store.din_names_list = []
    din_speaker_color = "speaker_color"

    store.din_names_list.append("din_narrator")

    store.din_names_list.append("din_th")

    din_colors["din_teapot"] = {"speaker_color": (85, 19, 19, 255)}
    din_names["din_teapot"] = "Чайник"
    store.din_names_list.append("din_teapot")

    din_colors["din_third"] = {"speaker_color": (0, 73, 121, 255)}
    din_names["din_third"] = "Третий"
    store.din_names_list.append("din_third")

    din_colors["din_third_i"] = {"speaker_color": (0, 73, 121, 255)}
    din_names["din_third_i"] = "Я"
    store.din_names_list.append("din_third_i")

    din_colors["din_nit"] = {"speaker_color": (159, 147, 147, 255)}
    din_names["din_nit"] = "Ниточник"
    store.din_names_list.append("din_nit")

    din_colors["din_nit_he"] = {"speaker_color": (159, 147, 147, 255)}
    din_names["din_nit_he"] = "Он"
    store.din_names_list.append("din_nit_he")

    din_colors["din_hall"] = {"speaker_color": (85, 19, 19, 255)}
    din_names["din_hall"] = "Халл"
    store.din_names_list.append("din_hall")

    din_colors["din_pi_teapot"] = {"speaker_color": (85, 19, 19, 255)}
    din_names["din_pi_teapot"] = "Пионер"
    store.din_names_list.append("din_pi_teapot")

    din_colors["din_gensek"] = {"speaker_color": (209, 209, 65, 255)}
    din_names["din_gensek"] = "Генсек"
    store.din_names_list.append("din_gensek")

    din_colors["din_pi1"] = {"speaker_color": (204, 204, 0)}
    din_names["din_pi1"] = "Пионер"
    store.din_names_list.append("din_pi1")

    din_colors["din_pi2"] = {"speaker_color": (102, 102, 153)}
    din_names["din_pi2"] = "Пионер"
    store.din_names_list.append("din_pi2")

    din_colors["din_pi_generic"] = {"speaker_color": (94, 91, 90)}
    din_names["din_pi_generic"] = "Пионер"
    store.din_names_list.append("din_pi_generic")

    din_colors["din_dv"] = {"speaker_color": "#ffaa00"}
    din_names["din_dv"] = "Алиса"
    store.din_names_list.append("din_dv")

    din_colors["din_sl"] = {"speaker_color": "#ffd200"}
    din_names["din_sl"] = "Славяна"
    store.din_names_list.append("din_sl")

    din_colors["din_un"] = {"speaker_color": "#aa64d9"}
    din_names["din_un"] = "Лена"
    store.din_names_list.append("din_un")

    class DinBlackRectangle(renpy.Displayable):
        def __init__(self, width, height, alpha, **kwargs):
            super(DinBlackRectangle, self).__init__(**kwargs)
            self.width = width
            self.height = height
            self.alpha = alpha
            self.frame = Solid("#000000", xsize=self.width, ysize=self.height)

        def render(self, width, height, st, at):
            t = Transform(child=self.frame, alpha=self.alpha)
            obj = renpy.render(t, width, height, st, at)
            render = renpy.Render(self.width, self.height)
            render.blit(obj, (0, 0))
            return render

    def din_shrinking_text_tag(tag, argument, contents):
        if persistent.font_size == "large":
            start_size = 32

        elif persistent.font_size == "small":
            start_size = 28
        
        modified_contents = []
        current_size = start_size
        
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    size_tag = "size={}".format(current_size)
                    modified_contents.append((renpy.TEXT_TAG, size_tag))
                    modified_contents.append((renpy.TEXT_TEXT, char))
                    modified_contents.append((renpy.TEXT_TAG, "/size"))
                    
                    current_size -= 1

        return modified_contents

    def din_char_define(character_name, is_nvl=False):
        global DynamicCharacter
        global nvl
        global din_store
        global din_speaker_color
        din_gl = globals()
        
        if character_name == "din_narrator":
            if is_nvl:
                din_gl["din_narrator"] = Character(None, kind=nvl, what_style="din_text_style")
            
            else:
                din_gl["din_narrator"] = Character(None, what_style="din_text_style")
            
            return
        
        if character_name == "din_th":
            if is_nvl:
                din_gl["din_th"] = Character(None, kind = nvl, what_style = "din_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            else:
                din_gl["din_th"] = Character(None, what_style = "din_text_style", what_prefix = "~ ", what_suffix = " ~")
            
            return
        
        if is_nvl:
            din_gl[character_name] = DynamicCharacter("%s_name" % character_name, color = store.din_colors[character_name][din_speaker_color], kind = nvl, what_style="din_text_style", who_suffix=":")
            din_gl["%s_name" % character_name] = store.din_names[character_name]
        
        else:
            din_gl[character_name] = DynamicCharacter("%s_name" % character_name, color=store.din_colors[character_name][din_speaker_color], what_style="din_text_style")
            din_gl["%s_name" % character_name] = store.din_names[character_name]

    def din_set_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global din_store
        
        for character_name in store.din_names_list:
            din_char_define(character_name)

    def din_set_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global din_narrator
        global din_th
        din_narrator_nvl = din_narrator
        th_nvl = din_th
        
        global din_store
        
        for character_name in store.din_names_list:
            din_char_define(character_name, True)

    def din_reload_names():
        global din_store
        
        for character_name in store.din_names_list:
            din_char_define(character_name)

    din_reload_names()

    def din_frame_animation(image_name, frames_quantity, retention, loop, transition, start=1, **properties):
        anim_args = []
        
        for i in xrange(start, start + frames_quantity):
            anim_args.append(renpy.display.im.image(image_name + "_" + str(i) + ".png"))
            
            if loop:
                anim_args.append(retention)
                anim_args.append(transition)
        
        return anim.TransitionAnimation(*anim_args, **properties)

    def din_blink(blink_pause):
        renpy.show("blink")
        renpy.pause(blink_pause, hard=True)

    def din_unblink(scene_name, unblink_pause):
        renpy.hide("blink")
        renpy.scene()
        renpy.show(scene_name)
        renpy.show("unblink")
        renpy.pause(unblink_pause, hard=True)

    def din_story_intro(_save_name, daytime, background, sprite, lbl, desc, amb): #TODO: использовать эмбиенс
        global save_name

        save_name = _save_name
        persistent.timeofday = daytime
        persistent.sprite_time = daytime
        renpy.music.play('sound/ambiences/{}.ogg'.format(amb), 'ambience', fadein=2)
        renpy.scene()
        renpy.show(background)
        renpy.show(sprite)
        renpy.show('din_story_frame', at_list=[Transform(xalign=0.5, yalign=0.85)])
        renpy.show('text', what=Text(lbl, xalign=0.5, yalign=0.75, style=style.din_story_label), tag='lbl')
        renpy.show('text', what=Text(desc, xalign=0.5, yalign=0.85, style=style.din_story_description), tag='desc')
        renpy.with_statement(dissolve)
        renpy.pause(3.0, hard=True)
        renpy.music.stop('ambience', 2)
            
    def din_onload(type):
        global din_lock_quit
        global din_lock_quick_menu

        if type == "lock":
            renpy.config.skipping = None
            din_lock_quit = True
            din_lock_quick_menu = True
            config.allow_skipping = False

        elif type == "unlock":
            din_lock_quit = False
            din_lock_quick_menu = False
            config.allow_skipping = True

    din_onload_curried = renpy.curry(din_onload)

    def din_current_time(): #TODO: выпилить глобальные переменные
        global din_hour
        
        din_time = time.strftime("%H:%M:%S", time.localtime())
        din_hour, din_min, din_sec = din_time.split(":")
        din_hour = int(din_hour)

    def din_set_main_menu_cursor():
        config.mouse_displayable = MouseDisplayable(din_gui_path + "misc/din_cursor.png", 0, 0)

    din_set_main_menu_cursor_curried = renpy.curry(din_set_main_menu_cursor)

    def din_set_timeofday_cursor():
        global din_set_timeofday_cursor_var

        if din_set_timeofday_cursor_var:
            config.mouse_displayable = MouseDisplayable(din_gui_path + "dialogue_box/" + persistent.timeofday + "/cursor.png", 0, 0)

    din_set_timeofday_cursor_curried = renpy.curry(din_set_timeofday_cursor)

    def din_set_null_cursor():
        config.mouse_displayable = MouseDisplayable(din_gui_path + "misc/din_none.png", 0, 0)

    din_set_null_cursor_curried = renpy.curry(din_set_null_cursor)

init:
    $ din_main_menu_var = True
    $ din_lock_quit_game_main_menu_var = True
    $ din_lock_quit = False
    $ din_lock_quick_menu = False

    $ din_take_everything = False
    #$ din_winterlong_story_bar = False

    #TODO: перекинуть персистенты в словарь

    if persistent.din_ikarus_story_completed == None:
        $ persistent.din_ikarus_story_completed = False

    if persistent.din_winterlong_story_completed == None:
        $ persistent.din_winterlong_story_completed = False

    if persistent.din_rolegame_story_completed == None:
        $ persistent.din_rolegame_story_completed = False

    $ din_wiperight = CropMove(.5, "wiperight")
    $ din_wipeleft = CropMove(.5, "wipeleft")

    $ din_set_timeofday_cursor_var = False

    $ din_night_hours = [22, 23, 24, 0, 1, 2, 3, 4, 5, 6]
    $ din_sunset_hours = [20, 21]
    $ din_morning_hours = [7, 8]

    image din_main_menu_frame = DinBlackRectangle(width=720, height=1080, alpha=0.6)
    image din_main_menu_options_frame = DinBlackRectangle(width=1804, height=1028, alpha=0.7)
    image din_intro_frame = DinBlackRectangle(width=1920, height=689, alpha=0.6)

    image din_story_frame = DinBlackRectangle(width=630, height=240, alpha=0.5)

    image bg din_stars_anim = din_frame_animation("din/images/bg/din_stars_anim/din_stars", 2, 1.5, True, Dissolve(1.5))
    image bg din_fireplace_winterlong_anim = din_frame_animation("din/images/bg/din_fireplace_winterlong_anim/din_fireplace_winterlong", 10, 1.8, True, Dissolve(1.2))
    image bg din_stars_bush_anim = din_frame_animation('din/images/bg/din_stars_bush_anim/din_stars_bush', 15, 1.8, True, Dissolve(1.2))
    image din_main_menu_day_anim = din_frame_animation("din/images/gui/main_menu/day/din_day", 5, 4, True, Dissolve(2))
    image din_main_menu_night_anim = din_frame_animation("din/images/gui/main_menu/night/din_night", 5, 4, True, Dissolve(2))
    image din_main_menu_sunset_anim = din_frame_animation("din/images/gui/main_menu/sunset/din_sunset", 5, 4, True, Dissolve(2))
    image din_main_menu_morning_anim = din_frame_animation("din/images/gui/main_menu/morning/din_morning", 5, 4, True, Dissolve(2))

    image din_gensek silhouette normal = im.MatrixColor("din/images/sprites/gensek/normal/din_gensek stay normal.png", im.matrix.tint(0, 0, 0))

    image din_blank_skip = renpy.display.behavior.ImageButton(Null(1920, 1080), Null(1920, 1080), clicked=[Jump('din_after_intro')])

    transform din_buttons_atl():
        on idle:
            linear 0.5 zoom 1.0

        on hover:
            linear 0.5 zoom 1.018

    transform din_buttons_transition():
        on hover:
            alpha 1.0
            linear 0.5 alpha 0.0
            
        on idle:
            alpha 0.0
            linear 0.5 alpha 1.0

    transform din_zoom_in_center():
        xalign 0.5 yalign 0.5 zoom 1.0
        pause 2.0
        linear 20 zoom 2.0 xalign 0.5 yalign 0.5