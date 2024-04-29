label din_winterlong_story:
    $ renpy.block_rollback()
    $ din_set_mode_adv()
    # pi_generic - Пионер серого непримечательного цвета
    stop music fadeout 3
    $ renpy.pause(2, hard=True)
    $ din_story_intro('Длиною в зиму\nДень Третьего', 'night', 'bg din_fireplace_winterlong_anim', 'din_third normal', 'Длиною в зиму', 'День Третьего', 'forest_night')
    scene bg black with Dissolve(2)
    $ persistent.sprite_time = "sunset"
    $ persistent.timeofday = "sunset"
    scene bg din_int_dining_hall_people_sunset with Dissolve(2)
    play ambience ambience_dining_hall_full fadein 3
    din_narrator "Обычный, непримечательный день."
    din_narrator "Я прохлаждался на галёрке стандартного сценария какого-то Пионерчика. Он романтично болтал с двумя красноволосыми за столом у окна."
    scene bg din_food_normal_sunset with dissolve
    din_narrator "До этого я наблюдал из массовки за местным ритмом жизни, но сейчас просто лениво рассматривал свою порцию еды."
    din_narrator "По факту, к еде можно и не притрагиваться. При должной сноровке всю неделю несложно протянуть и без еды. Книги говорят, что протянуть можно около месяца, но для меня такая информация - бесполезна."
    scene bg din_int_dining_hall_people_sunset with dissolve
    din_narrator "Я подпер кулаком голову."
    din_narrator "Вмешаться в события этого лагеря или молча наблюдать дальше?"
    $ renpy.pause(3, hard=True)
    ##Внизу важный комментарий
    ##звук резкого открытия двери.
    ##Спрайт злого чайника
    ##Музыка активная, как в боевке в лесу из ОУД
    ##Выключить эмбиэнт разговоров
    din_narrator "От решения меня отвлек новый гость, рывком открывший дверь. Кроме двух ножей в руках - ничего примечательного."
    din_pi_teapot "Девочки и мальчики, берегите ваши руки, ноги, пальчики! {w}А еще лучше - просто испаритесь на счет три."
    din_narrator "Куклы застыли в недоумении, а вот местный Пионер быстро начал собираться в окно. {w}Смышлёный парень. Знает, что с незнакомцами, у которых есть нож, лучше не разговаривать."
    din_pi_teapot "Три."
    din_narrator "Куклы всё еще сидели, раскрыв рты. Пионер успел улизнуть."
    din_pi_teapot "Ну кто бы сомневался."
    din_pi_teapot "Лады, давайте по старинке."
    ##звук броска и лязга ножа об пол. 
    ##звук вскрика Алисы
    din_narrator "Быстрым движением гость выкинул нож, который прочертил прямую траекторию и просвистел в паре сантиметров от головы Алисы."
    din_narrator "Потом снаряд с лязгом упал на пол, а стрелок грозно поигрывал в руке вторым."
    din_narrator "Куклы сменили смятение на панику в своих пустых глазах. Смекнули, что сейчас будет нечто не очень хорошее."
    scene bg din_int_dining_hall_sunset_crashed with dissolve
    ##звук суматохи
    din_narrator "Они начали резко вставать, опрокидывая стулья, и панически искать пути побега."
    din_pi_teapot "Выход на кухне, если кому интересно."
    din_narrator "С занудным тоном бросил гость."
    din_narrator "Толпа не задумываясь бросилась бежать за стойку раздачи."
    stop ambience fadeout 2
    din_narrator "Скоро остались только я, гость и мой остывший ужин."
    din_narrator "У меня не было моральных сил убегать куда-то. Кажется, остается только один выход."
    din_narrator "Ненавижу насилие."
    din_narrator "Гость, похоже, собирался уходить, но заметил, что какая-то дефектная кукла еще сидит в столовой. Аккуратно разглядывая, он взял нож лезвием вперед и медленно пошел ко мне."
    din_th "Бросить в него стул или побежать по столам? {w}Можно еще осколок стекла раздобыть..."
    din_narrator "Между нами стало с десяток метров. Я уже приготовился к марш броску."
    din_pi_teapot "В рот мне грот, Третий! {w}Ты!"
    din_third "Аааа, Чайник... {w}Ну здравствуй."
    din_narrator "Я сел обратно за свой трапезный стол."
    din_teapot "Третий, я ради тебя полмира обошел! Я придумал десять разных фраз для врывов в столовые! Какого черта ты торчишь непонятно где?"
    din_narrator "Ну начина-а-ается."
    din_third "Может быть, хотел недельку тишины. Как ты меня вообще нашел?"
    din_teapot "Шел по зову своего сердца. Оно сразу указало верный путь. {w}Пришлось обойти всего-то двенадцать лагерей."
    din_third "Почему искал меня именно в столовой? Я мог быть буквально где угодно."
    din_teapot "Ой, не будь таким доверчивым, Третий. Я сюда просто за мукой зашел. {w}Но тебя тоже рад видеть, ты не подумай."
    din_third "Мука в столовой?"
    din_teapot "Звучит дико, да? {w}Она не только в библиотеке есть. А мне понадобится еще много."
    din_third "Что ты теперь задумал?"
    din_teapot "Что {b}Я{/b} задумал? Под насколько большим камнем ты жил, Третий? В конце этой семидневки Неделя Зимы! И раз ты уже здесь и ничем не занят, то мне понадобится твоя грубая сила."
    din_th "Ах да, эта чушь..."
    din_third "Не сочти за грубость, но плевать я хотел на этот праздник и на вашу Зиму."
    din_teapot "Да не будь ты старым нудным пнём, Третий. Тебе там тоже найдется чем заняться. Тем более праздник для всех."
    din_teapot "Даже Ниточник будет."
    din_third "Он что, согласился помочь с организацией?"
    din_teapot "Пха-ха-ха! Нет конечно, он же не дурачок какой-нибудь."
    din_third "Мне нужно напоминать, что ты-то на это подписался?"
    din_teapot "Ну, мне не жалко. {w}Я огнеупорный."
    din_narrator "Чайник улыбнулся глупо и счастливо. {w}Две стороны одной медали."
    din_third "Точно сказано."
    din_narrator "Он посмотрел на меня пристально и укоризненно."
    din_third "Хорошо-хорошо. Ты огнеупорный."
    din_narrator "Я начал глазами искать что-то лекговоспламеняющееся в этой столовой."
    stop ambience fadeout 2
    scene bg black with Dissolve(2)
    $ renpy.block_rollback()
    $ persistent.timeofday = "night"
    scene bg din_fireplace_winterlong_anim with dissolve
    play ambience din_voices fadein 2
    play music din_god_is_an_astronaut_first_day_of_sun fadein 5
    din_narrator "С высоты дерева было хорошо видно поляну, покрытую смесью муки и штукатурки."
    din_narrator "Не слишком равномерно, но с земли это было мало заметно."
    din_narrator "Я высыпал последний мешок по ветру, закончив украшать поляны."
    din_teapot "Отлично, Третий! Можешь слезать. Скоро начнут подтягиваться все остальные!"
    din_narrator "Я бережно спрыгнул на землю."
    din_narrator "Остальные тоже заканчивали свою часть. В центре постепенно разгоралось кострище, вокруг него расходились скромные места, чтобы хватило всем желающим. В отдалении находилась небольшая деревянная платформа для выступлений."
    din_narrator "Она нужна исследователям, которым всегда неймется обсудить с кем-то свои идеи. Так что им выделили отдельный уголок, где собираются единомышленники."
    din_narrator "Зимний вид поляны навевал слабознакомое ощущение. Неделя Зимы проводится очень редко. Многие даже не помнят, что когда-то были на ней."
    #звук упавшего на траву тела
    din_narrator "Я откинулся, коснувшись спиной холодной земли."
    scene bg din_stars_bush_anim with fade
    din_narrator "Только я и еще пара-тройка Пионеров никогда не забывают традицию. Сейчас еще Чайник помнит, но это вряд ли надолго."
    din_narrator "Из-за такой редкости Неделя Зимы была чем-то невероятным, даже удивительным для новичков. А помнящие лишь завидуют этим давно забытым эмоциям."
    din_narrator "Но здесь каждый сам себе судья."
    ##звук слабого порыва ветра.
    din_narrator "Прохладно. Интересно, так ли представляли зиму фантазёры, придумавшие Внешний Мир?"
    din_narrator "Чайник вместе с двумя знакомыми подкинул пару дров в костёр. Огонь довольно затрещал."
    #din_narrator "Я сел возле пламени, скрестив ноги."
    din_narrator "Костер был идеально собран, чтобы всем хватило места вокруг него, но согреться было сложно."
    din_narrator "Один за другим из леса появлялись Пионеры. Кто-то -длиннаяпалка- группой, другие -длиннаяпалка- в одиночку, внимательно смотря по сторонам."
    din_narrator "Все друг за другом молча занимали места у очага. Новенькие нервно смотрели по сторонам, а мои сверстники расслабленно откидывались назад, закрыв глаза и наслаждаясь холодом ночи и теплом огонька."
    din_narrator "Некоторые даже спустя столько циклов верят, что когда-то жизнь была другой, что Внешний Мир -длиннаяпалка- не плод чьей-то давно поломанной фантазии."
    din_narrator "Может, эта надежда дает им держать себя в руках. Пускай. Каждый сам вправе решать во что ему верить."
    din_narrator "Смешно, что это, по большей части, праздник надежды, хотя поддерживают его те, кто от надежды давно отказался."
    din_th "У вечности определённо есть чувство юмора."
    $ renpy.pause(3, hard=True)
    din_narrator "Всё сложнее следить за ходом времени. Особенно в таких... Ситуациях."
    scene bg black with Dissolve(2)
    $ renpy.pause(1, hard=True)
    scene bg din_fireplace_winterlong_anim with Dissolve(2)
    din_narrator "Когда я поднялся, то большинство мест у костра пустовали. Все занялись более «живыми» занятиями."
    din_narrator "В другом конце поляны красовалась состоящая из пары досок барная стойка с изрядным запасом Столичной. Многим было сложно справиться с эмоциями."
    din_narrator "Небольшая группа любопытствующих пошла послушать речи исследователей."

    menu:
        "К стойке":
            #$ din_winterlong_story_bar_var = True
            jump din_winterlong_story_bar

        "Подойти к учёным": 
            jump din_winterlong_story_science   
    
label din_winterlong_story_bar:
    din_th "Возможно, стоило бы отказаться от алкоголя. {w}Хотя бы на эмоциональные праздники."
    din_th "С другой стороны, сколько выпивка вызывает истерик, столько и останавливает. В конце концов, по итогу ничего и не изменится."
    din_th "Да и не в моих это привычках - решать за других."
    scene bg din_ext_bar_night with dissolve
    ##Другая музыка
    din_narrator "Заправлявший баром Пионер молча налил мне стакан. {w}Не разобрать кто."
    din_narrator "Никаких ламп тут не было, а костёр был слишком далеко. Обычно можно распознать по повадкам и движениям, но более «старые» личности любят маскироваться друг под друга, особенно по праздникам. "
    din_narrator "Как раз на фоне костра сейчас пара расслабленных, но энергичных Чайников, выслушивала слова от фигуры со знакомо наклонённой головой."
    din_th "А у них отлично получается."
    din_narrator "Бармен же не делал никаких лишних движений."
    din_th "Разве что об интересах этого силуэта можно судить. Вряд ли этим бы занимался кто-то кроме любителей посмотреть на чужую печаль."
    din_th "Или... {w}Я ошибаюсь? {w}Буду надеяться, что осталось хоть что-то, в чём я могу ошибаться."
    din_narrator "Забрав стакан, я отсел за стол к одинокому Пионеру, безвольно допивавшему очередную бутылку."
    din_narrator "Вот эту-то личность я хорошо знал."
    din_narrator "Огонёк когда-то был невероятным. Он излучал счастье и радость, чуть ли не единственный. Не безумное счастье Чайника, не садистическую радость всяких слабаков, а обычное счастье, каким его описывают в книгах Внешнего Мира."
    din_narrator "С ним было что-то определённо не так, я хотел понять что именно, поэтому мы провели слишком много времени в одной компании."
    din_narrator "А потом в одну прекрасную смену Огонёк всё забыл. {w}Встретил меня паникой, страхом, не помнил ничего про других."
    din_narrator "Стал «новичком»."
    din_narrator "Такое случается с каждым. С разной периодичностью, но все возвращаются в начало мыслей."
    din_narrator "Сейчас только я и Ниточник, кажется, имя он не менял, еще не «омолаживались». Мы помним всех остальных, но не друг друга."
    din_narrator "Возможно, мы восстановились в одну смену."
    din_narrator "В любом случае наша очередь - только вопрос времени."
    din_narrator "Наш срок изменений может стремиться к бесконечности, но... {w}Мы здесь. {w}Бесконечность непременно наступит."
    din_narrator "Мой поток мыслей прервали негромкие шаги рядом." 
    show din_gensek_silhouette_normal at center with dissolve
    din_narrator "Кто-то проходил мимо, но, заметив меня, придвинул соседний стул и сел к нам."
    din_th "Кто настолько смелый, чтобы подсесть без приглашения?"
    din_narrator "Я уже размышлял как бы убрать новоприбывшего предельно болезненно, без табуированного сегодня прямого насилия, но неприятное узнавание заставило пересмотреть планы."
    din_narrator "Генсек. Если я был третий по летальности Пионер, то Генсек был вторым, причем на голову меня выше."
    din_narrator "Выше него только Чокнутый, но эти двое слишком хорошо ладят, чтобы всерьёз угрожать друг другу."
    din_gensek "Какая встреча, Третий."
    din_narrator "Говорил Генсек всегда ровно, спокойно и уверенно. {w}Как и полагается его статусом."
    din_third "И ты здравствуй. Зашел к нам опохмелиться?"
    din_narrator "Генсек тихо улыбнулся."
    din_gensek "Не совсем. Но спасибо за предложение."
    din_gensek "Пропущу этап любезностей, если ты не возражаешь."
    din_gensek "Не знаю, слышал ли ты, но через две смены пляжная вечеринка."
    din_third "Это точно не ко мне."
    din_th "Валяться под солнцем изредка плавая и бросая мяч? Может, моё мнение и не распростарнённое, но это - трата времени. {w}И такие слова кое-что да значат в наших масштабах."
    din_gensek "Там пройдет небольшой морской конфликт и нам с Чокнутым не хватает рук."
    din_third "Хотите завербовать меня к себе?"
    din_gensek "Нет, конечно. У конфликта три стороны, и нам не хватает еще одного приемлемого соперника."
    din_third "Польщен. Но это не грубое один на один. Нужна не только сноровка, но и изобретательность."
    din_gensek "Она и в грубом один на один нужна. Ты отлично подходишь."
    din_third "Предложи это Чайнику. Он обрадуется."
    din_narrator "Мой собеседник на треть секунды посмотрел в сторону, представляя себе картину."
    din_gensek "Хорошая идея. Но было бы неплохо, если бы корабль противника не пошел на дно в самом начале под весом собственной «изобретательности»."
    din_narrator "В этом я не мог не согласиться. Соревнование действительно получилось бы... {w}разочаровывающим."
    din_gensek "Можешь взять его в команду. Вы можете отлично сработаться."
    din_third "А если я откажусь? Что тогда?"
    din_gensek "Да ничего нового, Третий. Мы с Чокнутым проявим злопамятность, только и всего."
    din_third "Хоть Чокнутый и несравнимо сильнее меня, это не значит, что я боюсь боли."
    din_gensek "Как забавно вы все делаете из него непобедимого дьявола. {w}ТЫ боли не боишься. А вот твои знакомые...."
    din_third "Будешь пытать Чайника только чтобы позлить меня?"
    din_gensek "О, нет. Смотри шире."
    din_gensek "Пока он будет занят, ты сможешь переключиться на кого-то другого. Так что втягивать его в нашу небольшую политику бесполезно."
    din_gensek "Но втянуть можно не его одного. Представь, что в общем лагере висит обьявление, что каждый, кто заговорит с тобой, подписывается на наше плохое отношение."
    din_gensek "Даже если кто-то имеет высокий болевой порог или безумное самовнушение, то его образумят знакомые, пригрозив изоляцией. Не прими за оскорбление, но не думаю, что ты стоишь таких жертв."
    din_narrator "Идея была крайне хороша. Она не могла меня не удивить своей продуманностью."
    din_third "Я тебя услышал."
    din_narrator "Старое, почти забытое чувство собственной беспомощности перед другими. {w}Хотя нет. Я всегда могу отказаться. Нужно лишь быть готовым к последствиям."
    din_gensek "Вот и славно."
    din_third "Куда ты вообще шел до того, как я тебя отвлёк?"
    din_narrator "Хотелось перевести тему."
    din_gensek "Хотел зайти сюда за Чокнутым."
    din_third "За столами и с той, и с этой стороны, кроме нас, никого нет."
    din_gensek "Я знаю."
    din_narrator "Он произнёс это чуть удивлённо, словно я сказал бесполезную информацию."
    din_gensek "Что же, мне, как ты заметил, пора. {w}Веселитесь. Неделя Зимы же."
    din_narrator "Сказал он, как какой-то праздничный дух, и оставил наш стол."
    din_narrator "А ведь Генсек прав."
    din_narrator "Всё равно желания еще хоть что-то делать уже не было."
    din_narrator "Я взял одну из немногих еще не открытых бутылок Огонька и, открыв, поднёс её ко рту."
    jump din_winterlong_story_interlude
    
label din_winterlong_story_science:
    din_narrator "Почему бы и нет?"
    scene bg din_ext_scene_night with dissolve
    ##Другая музыка
    din_narrator "Вопреки моим ожиданиям, пылких споров там не происходило. Все сдержанно слушали мысли стоящего на платформе."
    din_narrator "Я тихо стал сбоку, чтобы не привлекать внимание."
    din_narrator "Вещал, что не удивительно, Чайник."
    din_teapot "...да, как вы и могли догадаться, вопрос в источнике энергии. {w}Не важно, дрейфуем мы в абсолютном вакууме или находимся на экспериментальном полигоне, в любом случае нужно невообразимое колличество энергии, чтобы обеспечить во всех параллелях тепло."
    din_narrator "За столько времени я так привык к глупостям Чайника, что перестал воспринимать его как, без преувеличения, оплот рационализма и науки во всеобщих глазах."
    din_teapot "Рассмотрим несколько моих версий. Когда я закончу, пожалуйста, озвучьте свои."
    din_teapot "Итак, первый вариант - события берут место в чьём-то из наших воображений."
    din_teapot "Тут всё просто - законы физики могут нарушаться в любую сторону. Есть доказательства и за, и против этой теорий, но тема старая, их вы уже наверняка слышали, не буду затягивать."
    din_teapot "Второй вариант - есть источники тепла, поэтому где-то жарче, где-то, наоборот, прохладнее."
    din_teapot "Таких источников может быть около десятка, плюс местное Солнце."
    din_teapot "Оно вряд ли находится дальше пяти километров над землей, из чего можно сделать приблизительные рассчеты."
    pi_generic "Пять километров - длинна дороги?"
    din_teapot "Да, почти. Это половина длинны. Я всё еще надеюсь, что каждая параллель ограничена сферой. {w}Если создавшие эти мирки могли менять пространство, но не знали о банальном удобстве сферических структур... {w} То у нас проблемы."
    din_teapot "Рассчеты я, разумеется, уже провёл. {w}В очень сухой теории источниками могут служить крохотные ядерные синтезы. {w}Молекулярные, можно сказать."
    din_teapot "В теории, потому что я их не нашел. {w}Но их нужно как-то запускать и координировать. Возможно, какими-то волнами."
    din_teapot "Поэтому попрошу вас в течение следующих двух недель проследить за поведением радио и самоделок в разных участках ваших лагерей. "
    din_teapot "Список мест напишу и оставлю в общей столовой. Результаты идеально оформить в письменном виде. Сложите там же, в столовой, возле доски обьявлений."
    din_teapot "Последний вариант - источник энергии - мы сами, но в разных местах реагируем и действуем иначе. Отсюда и разница температур в разных точках."
    din_teapot "Эту теорию у меня пока не было желания рассмотреть, поговорим о ней после результатов. {w}На этом всё, спасибо."
    din_narrator "Он в тишине сошел с трибуны. Поискав свободное место, заметил меня."
    din_teapot "О, какая компания! Ты вовремя. {w}Сыграем в города? {w}Райцентр!"
    din_third "Райцентр."
    din_teapot "..."
    din_teapot "Ладно, ты выиграл."
    din_third "До тебя рассказывали что-то интересное?"
    din_teapot "Да нет, ничего такого, что бы ты не предлагал раньше. {w}Настолько ты умён, Третий."
    din_third "Слишком уж топорный комплимент. Я от тебя ждал большего."
    din_teapot "Не всё же мне алмазами мысли сыпать? Иногда надо брать перерыв. {w}Не хочешь выступить?"
    din_narrator "Я еще раз бросил взгляд на платформу. Новый лектор сейчас рисовал несколько систем координат. {w}Искренне надеюсь, что это не четырёхмерность."
    din_third "Никогда не буду этим заниматься."
    din_teapot "Никогда? От кого я это слышу. Это может убить пару дней твоего времени. А если повезёт, то и пару смен, задумайся!"
    din_third "Не хочу прикасаться к системе."
    din_teapot "О, боишься найти выход?"
    din_third "Боюсь, что могу нечто подвинуть и нас сплющит в единственную микроскопически маленькую точке пространства. Узнать вас поближе я и так могу."
    din_teapot "Разве не ты говорил, что система безупречна и нам на неё не повлиять?"
    din_third "Да, говорил..."
    din_teapot "Но ты еще и уверен, что можно что-то поломать."
    din_third "Я... {w}Так, Чайник, оставь эту тему в покое! Свои алмазы мыслей держи для других."
    din_third "Это - лучшее, что случилось с нами."
    din_teapot "...единственное, что случилось с нами."
    din_third "Не вижу противоречия."
    din_teapot "Да, да, противоречия нет, никто не спорит."
    din_narrator "Он примирительно поднял руки вверх."
    $ renpy.pause(2, hard = True)
    din_narrator "Его взгляд проскользил где-то над моей головой, за спину."
    din_teapot "О, это тебя обрадует!"
    din_third "Очень в этом сомневаюсь."
    din_narrator "Когда я развернулся, ничего сначала не бросилось в глаза."
    din_narrator "Вернее, не было понятно где искать - проблему мог создать кто-угодно."
    din_narrator "Разве что дальше всего от костра, на отшибе сегодняшнего праздника двое личностей о чём-то спорили."
    din_narrator "Слов отсюда услышать было нельзя, но было легко заметить у одного из участников характерно дрожащий подбородок и дергающийся нос, как у девчонки - стандартные для новых личностей признаки гнева и жажды неприятностей."
    din_third "Может, ты ими займешься?"
    din_teapot "О, нет, спасибо. Вон тот, что справа, вроде двадцатый в общем списке. Он, конечно, тупой, как пень, но моя челюсть от этого прочнее не становится."
    din_teapot "А тебе это погоды не сделает."
    din_third "Напомни мне научить тебя делать удобный компактный нож."
    din_narrator "Я ускорил шаг и пошел к сладкой парочке."
    din_narrator "За то время, что мы шли, эти двое уже стали кричать друг на друга. Пока внимания они не привлекали, но это временно."
    din_narrator "Моё желание улаживать детские разборки измерялось отрицательными числами, но статус обязывал."
    din_th "Сколько раз повторять: ЛЮБОЕ насилие сегодня запрещено! Но нет, всега найдется недоверчивый новичок, который посчитает себя выше правил!"   
    ## появляются два тёмных силуэта дефолтных пионеров.
    scene bg ext_polyana_night with dissolve
    show silhouette din_normal at left as silhouette1
    show silhouette din_normal at right as silhouette2
    with dissolve
    din_narrator "Я остановился за пять шагов от них, но меня всё равно не заметили. Шорох за спиной подсказывал, что Чайник не отстал."
    din_pi1 "Еще раз что-то про неё скажешь и я за себя не ручаюсь."
    din_th "Как же неубедительно и безопасно звучал голос «левого». {w}И что это за расплывчатая угроза «за себя не ручаюсь»? Он в приступе злости в дерево врежется? {w}Сейчас в обморок упаду от страха."
    din_pi2 "Ты что, правда веришь в эту тупость? {w}Послушай, твоя ненаглядная с каждым, кого ты сегодня мог встретить, «уединялась» минимум раза...{nw}"
    ##вспышка, фон стандартной ночной поляны (Третий портировал этих двоих и себя)
    play sound din_sfx["din_portal_use"]
    scene bg ext_polyana_night with flash
    din_th "Отлично, свидетелей теперь нет."
    din_narrator "Неожиданная смена обстановки заставила их ненадолго остановить разговор."
    din_narrator "Теперь они, наконец, изволили меня заметить."
    din_third "Прекращайте спор. {w}Продолжите на следующей неделе."
    din_narrator "Но эти двое плохо понимали что сейчас произойдёт."
    din_pi2 "А не пошёл бы ты отсюда? Не лезь, если не хочешь получить!"
    din_narrator "Левый, судя по всему, думал что-то похожее."
    din_th "Почему? {w}ПОЧЕМУ в крохотном черепе этих одарённых нет хоть одной пары нейронов, которая бы связала их мгновенное перемещение и меня? {w}Это ведь несложно!"
    din_narrator "Но угроза Правого звучала убедительнее.  {w}Чуть-чуть."
    din_pi1 "Ты кем это себя возомнил?"
    din_narrator "Именно в такие моменты мне приходят мысли огромными красными буквами написать слово «ОПАСНО» на своём лбу. {w}Может, хоть так новички будут задумываться, прежде чем бросаться словами?"
    din_th "Ладно, время разговоров вышло."
    din_narrator "Я совершил рваный рывок к Левому, увернувшись от двух несмелых взмахов руками - он, очевидно, ждал еще болтовни."
    din_narrator "Подобравшись достаточно близко, я одновременно поддел его ногу своим носком и приготовил удар локтем в корпус, чтобы сбить с ног и приложить о землю."
    din_narrator "Велико же было моё удивление, когда мой аккуратный манёвр прервался внезапным ударом ноги со спины."
    din_narrator "Сила удара была невелика, но я всё же отбежал в сторону, чтобы оценить происходящее."
    din_narrator "Левый только оступился, а не упал, как я надеялся. Правый спокойно стоял рядом с ним."
    din_narrator "Я был частично удивлён. В первую очередь, не ждал, что его друг так быстро начнёт действовать, а во вторую - был уверен, что тот не будет вмешиваться, пока его недавнего раздражителя не сбросят в пыль."
    din_th "Впрочем, они вполне могут препираться прямо сейчас."
    din_narrator "Двое пионеров передо мной молча переглянулись и начали расходиться в стороны."
    din_th "Сначала показалось, что они идут подальше друг от друга. {w}Так и было, но вдруг я понял зачем."
    din_th "Они брали меня с двух сторон в кольцо."
    din_th "С этим было нечто совершенно не так."
    din_th "Двое Пионеров после спора не сговариваясь, работали вместе и теперь - слаженно."
    din_th "Это не было сверхсложно в принципе, но не для Пионеров. Каждый всегда был в первую очередь эгоистом, не важно, новичок или долгожитель. {w}Всегда все предпочитали действовать в одиночку."
    din_th "Исключениями были разве что заранее спланированные события, вроде командых игр или взаимопомощи, но даже тогда каждый тянул одеяло на себя, не полагаясь лишний раз на другого."
    din_th "Хм, я слишком сильно озадачен. {w}Значит, где-то ошибаюсь."
    din_narrator "Оба теперь снова стояли справа и слева от меня, за пять метров каждый. Отвернусь полностью в одну сторону - оставлю вторую неприкрытой."
    din_narrator "Левый взял в руку камень для броска. {w}Хороший трюк, я его запомню."
    din_narrator "Правый ничего не подбирал, только стал в стойку для спринта."
    din_narrator "Он-то меня беспокоил больше. Если Левый очевидно был просто импульсивным и этим его тактика ограничивалась, то Правый был чем-то сложнее."
    din_narrator "Первый сразу бросит камень и ринется напролом, если я повернусь к нему спиной, но что сделает второй, я пока не мог сказать."
    din_th "Что бы я сделал на его месте?"
    din_narrator "Ответ пришел сам собой."
    din_narrator "Я бы дождался, пока моего напарника вырубят и разобрался бы сам. Теперь, когда Правша уже один раз прикрыл соратника, у последнего больше не было оправданий своей слабости. Так, вспоминать ему это будет на порядок унизительнее."
    din_narrator "А ведь это действительно прекрасный план."
    din_narrator "Я снял перед Правшой вображаемую шляпу."
    din_narrator "Отлично. Я снова почувствовал землю под ногами."
    din_th "Поехали."
    din_narrator "На предельной скорости я метнулся к слабаку. Перехватив обе его руки своими, я провёл удар лбом и отбросил его назад."
    din_narrator "Противник наконец-то потерял равновесие и выронил камень."
    din_narrator "Схватив новое оружие, я метнул его прямо под дых, сбивая немногие остатки воздуха."
    din_narrator "Сразу после этого я пригнулся от возможного удара второго."
    din_th "Теперь посмотрим что...{nw}"
    ##звук удара, моргание, всё чернеет. **Несмотря на все предосторожности, ГГ вырубили.
    ##пауза на 3 сек. Размограние, гг на всё той же обычной поляне, но никого нет.
    ##тихие звуки хлопков по щекам.
    din_narrator "Спина мёрзнет. Как бы не простыть."
    din_narrator "Стоп, что произошло?"
    din_narrator "Кто-то назойливо хлопал ладонями по моим щекам."
    te_mysdin_third "Вставай-вставай-вставай-вставай.{w}Вставай-вставай-и-песню-запевай."
    din_th "Да что за!.."
    din_narrator "После того, как я рывком перешел в сидячее положение, ощутились изменения."
    din_narrator "А конкретно - новая форма моей головы."
    din_th "Похоже, образовался немаленький синяк. И, судя по липкости головы..."
    din_third "А, очнулся!"
    din_narrator "Рядом со мной лежала весомая палка с небольшим пятном крови."
    din_th "Что же, Правша, я запомню вас двоих."
    din_narrator "Чайник, заметив как я пришел в сознание, перестал стучать по моему лицу."
    din_teapot "Ты не хочешь в следующий раз на разборках вспомнить  обо мне? Если что, лагерей много и нормальные люди перемещаются по ним медленно. {w}В следующий раз искать тебя не буду."
    din_teapot "Из-за этого я пропустил, как тебя вздули! Такое не каждую Неделю Зимы бывает, знаешь ли! {w}Ты хоть записал всё? {w=.4}Сделал фотки? {w=0.4}Нет?!"
    din_narrator "Тише, Чайник, и так голова трещит."
    din_narrator "Я аккуратно провёл пальцами по эпицентру боли на затылке. Рана уже практически не кровоточила, затянулась."
    din_teapot "Отвыкай от этого имени. Неделя Зимы заканчивается, скоро его поменяю. Следующая буква по плану - Ша. {w}Но что бы такое придумать..."
    din_th "Нужно как-то спрятать эту дыру на голове. Кто-то меня узнает - головной боли станет еще больше."
    din_teapot "Шум, Шарф, Шпала, Шуруп... {w}Всё не то! Хотя нет, Шарф мне нравится, пока обдумаю."
    din_teapot "А, да. Держи!"
    din_narrator "Мне в руки попал обвязаный кругом красный галстук, теперь напоминающий бандану. {w}Судя по тому, что галстук Чайника был на своём стабильном месте, материал бандану он успел у кого-то отобрать, пока я был без сознния."
    din_teapot "Тебе повезло так быстро очухаться. Обычно после таких историй валяются где-то восемь часов."
    din_third "Сколько я проспал?!"
    din_teapot "Минут пятнадцать. Мне надоело ждать."
    din_narrator "Я многозначно глянул на него."
    din_th "Ну пускай."
    din_narrator "Повязка отлично закрывала рану. В ней я был похож на идиота, но сегодня общий праздник - идиотов много, выделятся не буду."
    din_teapot "Идём? {w}Как тебе имя Шаррум-итер? Достаточно пафосно или ему чего-то не хватает?"
    ##Затемнение
    ##Типо пропуск времени
    ##Растемнение на общей ''Зимней'' поляне
    din_narrator "Я устроил себе место на покрывале, недалеко от главного костра. Достаточно близко, чтобы не замёрзнуть, достаточно далеко, чтобы свет не выхватывал меня из общей массы."
    din_narrator "По мере того, как Неделя Зимы приближалась к концу, все меньше и меньше оставалось мест у костра. Все уже обсудили что хотели. Сейчас наступала почти ритуальная часть. Все молча садились и смотрели в костёр."
    din_narrator "Каких-то особых правил на этот счет не было. Просто сложилось, что в конце каждой такой смены все хотели подумать о своём, и нет для этого лучше места, чем рядом с костром и единомышленниками."
    din_narrator "Первая фигура легла, задремав на своём месте. Захотелось последовать её примеру."
    din_th "В конце концов, сегодня был утомительный день."
    din_narrator "Я не забыл про тёх двоих. Уже был четкий план, как привязать Левого к дереву вверх ногами на шесть часов. Но что делать с Правшой, я пока что не решил."
    din_narrator "Гораздо важнее была их нетипичная кооперация. Просто совпадение?"
    din_th "Но, если это первый звоночек социальных перемен, то грядёт интересное время. Приятно."
    din_th "С другой стороны..."
    din_narrator "Я устало вдохнул воздух."
    din_th "..это всё позже, не сейчас."
    din_th "Сейчас просто отдохну. И пусть мне не приснится не один сон."
    jump din_winterlong_story_interlude
    
label din_winterlong_story_interlude:
    $ renpy.block_rollback()
    $ persistent.timeofday = "day"
    scene bg din_ext_camp_plain_sight_day with dissolve
    play music din_if_these_trees_could_talk_barren_lands_of_the_modern_dinosaur fadein 5
    din_th "Это место выводит из привычного равновесия."
    din_th "Я испытываю определённую... {w}Злость? {w}Или это безразличие? {w}Бессилие?"
    din_th "Но если эмоции испытываю я, то разве тогда лагерь меня раздражает?"
    din_th "Или я сам — своя главная проблема?"
    din_narrator "Передо мной с закрытыми глазами лежал второй и последний житель этого места."
    din_th "Он никогда не проснется. {w}Без моей помощи."
    din_th "За всё время, что мы здесь, ничего не изменилось."
    din_th "{b}Ничего.{/b}"
    din_th "Небо всё того же цвета, тени той же длины."
    din_th "Даже мы сами. Мы не захотели ни есть, ни спать, не устали ни капли."
    din_th "Повезло, что хоть собственные мысли мы можем менять."
    din_th "Он был прав. {w}Здесь попросту не от чего проснуться."
    din_th "В этом и была его просьба — разбудить через тысячу часов."
    din_th "Думаю, в конце концов мы оба уснем, чтобы избавиться от голоса своей головы."
    din_th "Что не говори, но, похоже, даже для нас вечность может быть неприятной."
    din_narrator "Я отошел от спящего тела, на время оставить эти идеи."
    din_narrator "Трава сгибалась под моими ногами."
    din_th "Как ни странно, но больше всего я боялся вытоптать крохотный участок растительности в этой зеленой пустоши."
    din_th "Тогда бы образовалась крохотная несовершенность на необьятном полотне, которая мозолила бы мне глаза своим существованием всю вечность."
    din_th "Мог бы отвернуться, но не забыть её."
    din_th "Вторым выходом было вытоптать всю траву в этой утопии."
    din_th "Хороший вариант. {w}С условием, что у этой равнины есть край."
    $ din_blink(2)
    din_narrator "Я закрыл глаза."
    din_th "А что, если ничего из этого не существует?"
    din_th "Ни солнца, ни равнины, ни травы, ни меня?"
    din_th "Как это понять?"
    din_th "Как проверить, что хотя бы я сам когда-то был?"
    din_narrator "Кожа перестала чувствовать дуновения ветра и едва теплый свет."
    din_narrator "Эта мысль дарила чувство внутреннего спокойствия."
    din_th "Если нет меня, то и не нужно о чем-то беспокоиться, думать о будущем, планировать наперёд..."
    din_narrator "Любопытно, если меня, или того, что я собой считаю, нет, то что тогда есть?"
    din_narrator "Что задаёт вопросы? Что сейчас прогоняет эти мысли в своей голове?"
    $ din_unblink("bg din_ext_camp_plain_sight_day", 2)
    din_narrator "Это красивое место. {w}Красивое, но пустое."
    din_narrator "Параллели..."
    din_narrator "Ладно, хватит бездельничать."
    din_narrator "Пошла уже шестидесятая тысяча минут. {w}Кому-то пора просыпаться."
    ##Затемнение, переход к третьей истории.
    jump din_rolegame_story