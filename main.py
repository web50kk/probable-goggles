import telebot
from telebot import types

# Твой токен от BotFather
TOKEN = '8487035470:AAF74Pzq9Nycm3Qb-G-L9saEmHgtX5x7azQ'
bot = telebot.TeleBot('8487035470:AAF74Pzq9Nycm3Qb-G-L9saEmHgtX5x7azQ')

# Оригинальный алфавит (нижний регистр)
NORMAL = "йцукенгшщзхфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm1234567890"

# Список твоих шрифтов (я добавил те, что ты прислал)
FONTS_LIST = [
    "Ύʯƴκϱʜӷɯɰʒχϕыɞαηρσ᧘∂ж϶яɥсɱυτьɓюQWERTYUIOPASDFGHJKLZXCVBNM1234567890",
    "ᛋᛪᚴᛕᛊᚺᛚⰞⰞ℥ᚷᛄⰓᛆᛒᚣᚢᚹᛟᚳᚦᛯⰅᚱᚶᛈᛖᛋᛠⰓƃᚿθQWERTYUIOPASDFGHJKLZXCVBNM1234567890",
    "ẏƈὗќἔᾗĝʂнʂƈнẓнғẏνᾄῥʀὄłḋẓнἔẏᾄƈнʂмἷҭвẏὗҩᾧἔʀҭẏὗἷὄῥᾄʂḋғĝнʝќłẓẋƈνвᾗм1234567890",
    "ყƈųƙɛŋɠʂɧʂƈɧʑɧʄყ۷ą℘rơƖɖʑɧɛყąƈɧʂɱıɬცყųզῳɛrɬყųıơ℘ąʂɖʄɠɧʝƙƖʑҳƈ۷ცŋɱ1234567890",
    "ꌩꉓꀎꀘꍟꈤꁅꌗꃅꌗꉓꃅꁴꃅꎇꌩᐯꍏᖘꋪꂦ꒒ꀸꁴꃅꍟꌩꍏꉓꃅꌗꎭꀤ꓄ꌃꌩꀎꆰꅏꍟꋪ꓄ꌩꀎꀤꂦᖘꍏꌗꀸꎇꁅꃅꀭꀘ꒒ꁴꊼꉓᐯꌃꈤꎭ1234567890",
    "YᑕᑌKEᑎGSᕼSᑕᕼZᕼᖴYᐯᗩᑭᖇOᒪᗪZᕼEYᗩᑕᕼSᗰITᗷYᑌᑫᗯEᖇTYᑌIOᑭᗩSᗪᖴGᕼᒍKᒪZ᙭ᑕᐯᗷᑎᗰ1234567890",
    "ʏᴄᴜᴋᴇɴɢsʜsᴄʜᴢʜꜰʏᴠᴀᴘʀᴏʟᴅᴢʜᴇʏᴀᴄʜsᴍɪᴛʙʏᴜǫᴡᴇʀᴛʏᴜɪᴏᴘᴀsᴅꜰɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ1234567890",
    "Ɏ₵Ʉ₭Ɇ₦₲₴Ⱨ₴₵ⱧⱫⱧ₣ɎV₳₱ⱤØⱠĐⱫⱧɆɎ₳₵Ⱨ₴₥ł₮฿ɎɄQ₩ɆⱤ₮ɎɄłØ₱₳₴Đ₣₲ⱧJ₭ⱠⱫӾ₵V฿₦₥1234567890",
    "ㄚ匚ㄩҜ乇几Ꮆ丂卄丂匚卄乙卄千ㄚᐯ卂卩尺ㄖㄥᗪ乙卄乇ㄚ卂匚卄丂爪丨ㄒ乃ㄚㄩɊ山乇尺ㄒㄚㄩ丨ㄖ卩卂丂ᗪ千Ꮆ卄ﾌҜㄥ乙乂匚ᐯ乃几爪1234567890",
    "𝔜ℭ𝔘𝔎𝔈𝔑𝔊𝔖𝔥𝔖𝔠𝔥ℨℌ𝔉𝔜𝔙𝔄𝔓ℜ𝔒𝔏𝔇ℨ𝔥𝔈𝔜𝔞ℭ𝔥𝔖𝔐ℑ𝔗𝔅𝔜𝔲𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏ℨ𝔛ℭ𝔙𝔅𝔑𝔐1234567890",
    "𝚈𝙲𝚄𝙺𝙴𝙽𝙶𝚂𝚑𝚂𝚌𝚑𝚉𝙷𝙵𝚈𝚅𝙰𝙿𝚁𝙾𝙻𝙳𝚉𝚑𝙴𝚈𝚊𝙲𝚑𝚂𝙼𝙸𝚃𝙱𝚈𝚞𝚀𝚆𝙴𝚁𝚃𝚈𝚄𝙸𝙾𝙿𝙰𝚂𝙳𝙵𝙶𝙷𝙹𝙺𝙻𝚉𝚇𝙲𝚅𝙱𝙽𝙼𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶",
    "ⓎⒸⓊⓀⒺⓃⒼⓈⓗⓈⓒⓗⓏⒽⒻⓎⓋⒶⓅⓇⓄⓁⒹⓏⓗⒺⓎⓐⒸⓗⓈⓂⒾⓉⒷⓎⓤⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅⒶⓈⒹⒻⒼⒽⒿⓀⓁⓏⓍⒸⓋⒷⓃⓂ①②③④⑤⑥⑦⑧⑨⓪",
    "𝕐ℂ𝕌𝕂𝔼ℕ𝔾𝕊𝕙𝕊𝕔𝕙ℤℍ𝔽𝕐𝕍𝔸ℙℝ𝕆𝕃𝔻ℤ𝕙𝔼𝕐𝕒ℂ𝕙𝕊𝕄𝕀𝕋𝔹𝕐𝕦ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃ℤ𝕏ℂ𝕍𝔹ℕ𝕄𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘",
    "𝓨𝓒𝓤𝓚𝓔𝓝𝓖𝓢𝓱𝓢𝓬𝓱𝓩𝓗𝓕𝓨𝓥𝓐𝓟𝓡𝓞𝓛𝓓𝓩𝓱𝓔𝓨𝓪𝓒𝓱𝓢𝓜𝓘𝓣𝓑𝓨𝓾𝓠𝓦𝓔𝓡𝓣𝓨𝓤𝓘𝓞𝓟𝓐𝓢𝓓𝓕𝓖𝓗𝓙𝓚𝓛𝓩𝓧𝓒𝓥𝓑𝓝𝓜1234567890"
]

def encode_text(text, font_index):
    """Превращает обычный текст в выбранный шрифт по индексу."""
    if font_index < 0 or font_index >= len(FONTS_LIST):
        return text
    
    font = FONTS_LIST[font_index]
    result = ""
    for char in text:
        char_lower = char.lower()
        if char_lower in NORMAL:
            idx = NORMAL.index(char_lower)
            # Если в шрифте есть этот символ, заменяем
            if idx < len(font):
                result += font[idx]
            else:
                result += char
        else:
            result += char
    return result

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Привет! Просто пришли мне любой текст, и я предложу варианты шрифтов.\n\n"
                          "Либо используй быстрый поиск: напиши номер шрифта и текст, например: `5 Привет`.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    args = message.text.split(maxsplit=1)
    
    # ПРОВЕРКА НА ПОИСК ПО ID (например "5 привет")
    if len(args) > 1 and args[0].isdigit():
        font_id = int(args[0]) - 1 # Человеческий счет с 1, а в коде с 0
        if 0 <= font_id < len(FONTS_LIST):
            res = encode_text(args[1], font_id)
            bot.send_message(message.chat.id, res)
            return

    # ОБЫЧНЫЙ ВЫВОД СПИСКА
    user_text = message.text
    response = "🔎 **Выберите вариант:**\n\n"
    
    for i in range(len(FONTS_LIST)):
        # Генерируем название "Шрифт №" этим же шрифтом
        font_name = encode_text(f"Шрифт {i+1}", i)
        # Генерируем пример текста этим шрифтом
        example = encode_text(user_text, i)
        
        response += f"🆔 {i+1} | {font_name}:\n`{example}`\n\n"
        
        # Telegram ограничивает длину сообщения, если шрифтов слишком много - разбиваем
        if len(response) > 3500:
            bot.send_message(message.chat.id, response, parse_mode="Markdown")
            response = ""

    if response:
        bot.send_message(message.chat.id, response, parse_mode="Markdown")

bot.polling(none_stop=True)
