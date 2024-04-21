from telebot import TeleBot

bot = TeleBot("6984712635:AAEGvEDXBBh1-EnutVWro55bsMnBE7klQHQ")


@bot.message_handler(commands=["start"])
def start(message):
    from btns import main_menu
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}!", reply_markup=main_menu())


@bot.message_handler(content_types=["text"])
def variants1(message):
    if message.text == 'Дальше':
        from btns import choice
        text = ('Начинается с предыстории:\n\n'
                'Слава после долгой работы и проблем, '
                'начинает спускаться в метро, думая, '
                'как же ему было бы хорошо, если бы он хорошо зарабатывал и наконец то нашел своего отца. '
                'Он одинок: ни родителей, ни второй половинки. '
                'Спустившись на станцию, где было очень безлюдно, он начал засыпать под свои мысли. '
                'Позже, думая о лучшей жизни, он засыпает...')
        bot.send_message(message.chat.id, text, reply_markup=choice())
        bot.register_next_step_handler(message, variants2)
    else:
        from btns import main_menu
        bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu())


def variants2(message):
    if message.text == 'Дальше':
        from btns import variant
        text = ('Славе начинает снится сон, в котором ему еще 9 лет. '
                'В тот день у семьи был план: пойти в кино и развлечься. '
                'Слава, в предвкушении радости, начал собираться к поездке, но что-то пошло не так... '
                'Сон несколько отличался от произошедшего... '
                'После того, как он оделся и ждал своих родителей в прихожей, его отец начал во весь голос кричать на мать Славика, '
                'всячески материть и говорить на нее плохие вещи, но во сне не было такого... '
                'После того, как он оделся и начал выходить в прихожую, его родители вели себя очень подозрительно. '
                'Никакой ссоры между ними не было. На момент Слава подумал, что все хорошо, но не тут то было...\n\n'
                '1-ый вариант: Начать расспрашивать, что тут происходит \n'
                '2-ой вариант: Притворяться, что так и должно быть')
        bot.send_message(message.chat.id, text, reply_markup=variant())
    else:
        from btns import main_menu
        bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "play":
        from btns import characters
        bot.edit_message_text("Выбери Персонажа", call.message.chat.id, call.message.message_id, reply_markup=characters())
    elif call.data == "creators":
        from btns import creators
        bot.send_message(call.message.chat.id, "Создатели и Авторы: 👇", reply_markup=creators())
    elif call.data == "back":
        from btns import main_menu
        bot.edit_message_text("Главное меню", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    elif call.data == 'slava':
        from btns import choice
        history = ('Слава (24 года, др: 11 апреля)\n\n'
                   'История: Родился в Минске - отличный городок, квартира распологалась на окраине столицы на 4-ом этаже. '
                   'Славу в 9 лет бросил отец, мать не пережила такое и через месяц скончалась... '
                   'Его приютила бабушка, которую он считал как мать, дожила она до его 17-летия, позже умерев от остановки сердца... '
                   'В 17 ему пришлось не легко... Ему на плечи рухнули обязанности не по силам ему, он устроился продавцом в магазин, распологавшийся возле его дома. '
                   'Денег не хватало даже чтобы прожить месяц, растерянный и несчастный он хотел скончатся, пока не появилась цель - найти своего отца, который очень любил его, но его мать оборвала всю связь отца с сыном и было невозможно просто взять и встретиться. '
                   'Славе уже 24, а цель всё та же... Работает он грузчиком на заводе своего знакомого, получает очень мало, зарплату задерживают и как он считает - жизнь идет только под откос...\n\n'
                   'Страхи: Боится резких перемен, пауков, что не найдет отца и замкнутые помещения, социофоб')
        bot.send_message(call.message.chat.id, history, reply_markup=choice())
        bot.register_next_step_handler(call, variants1)
    elif call.data == 'angela':
        pass
    elif call.data == 'var1':
        from btns import variant1
        text = ('После того, как он начал расспрашивать о происходящем, у его родителей начали меняться лица. '
                'С доброй и в то же время устрашающей улыбки до гневного и противного лица. '
                'Слава очень испугался... В тот момент его отец резко взял его за руку и потащил вниз по лестничной площадке, '
                'дойдя до низу, Слава испугался еще больше. Вместо своего двора он увидел устрашающее место, '
                'где вокруг него были разные люди, которые были с такими же лицами, как и у его родителей. '
                'Все люди, включая его родителей выстроились вокруг него и начали что-то говорить...\n\n'
                '-1-ый выбор: начать убегать и пробиваться через толпу не живых людей\n'
                '-2-ой выбор: стоять смирно, пока они договорят')
        bot.send_message(call.message.chat.id, text, reply_markup=variant1())
    elif call.data == 'var2':
        pass
    elif call.data == 'var3':
        from btns import back_menu
        text = ('Когда 9-летний Славик начал пробиваться через приграду этих существ, его схатили... это была его мать. '
                'Она была на столько страшна, что у Славы чуть ли не остановилось сердце. Лицо у его мамы было все в крови. Когда она начала разивать рот, '
                'оттуда неслись жуткие запахи и было видно, что некоторые зубы у нее были не как у человека, а как будто перед ним стояло существо - зверь, который поймал свою добычу. '
                'За пару секунд до его гибели, он видел, как его внутренности) '
                'пожирают уже несколько таких же существ... (плохая концовка)')
        bot.send_message(call.message.chat.id, text, reply_markup=back_menu())
    elif call.data == 'var4':
        pass
    elif call.data == 'main':
        from btns import main_menu
        bot.send_message(call.message.chat.id, "Главное меню:👇", reply_markup=main_menu())


bot.infinity_polling()
