import telebot
import requests
from bs4 import BeautifulSoup



def wort_gen():
    global i
    global art
    global word
    global score 
    
    art = 'n'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 100.0.4896.127Safari / 537.36'
               }
    while art == 'n' or 'oder' in art:
        response = requests.get('https://www.palabrasaleatorias.com/zufallige-worter.php', headers = headers).text
        soup = BeautifulSoup(response,'lxml')
        word = soup.find('div',style = 'font-size:3em; color:#6200C5;').text.split('\n')[1]
        
        url = f'https://www.dwds.de/wb/{word}'
        
        
        response1 = requests.get(url, headers = headers).text
        soup1 = BeautifulSoup(response1,'lxml')
        
        
        try:
            art = soup1.find('h1', class_ = 'dwdswb-ft-lemmaansatz').text.split(', ')[1]
            
        except: art = 'n'


def kufar1_(ms):
    global link_string
    string = ''
    ms_list = ms.split(' ')[1:]
    link_string =  ''
    for k in ms_list:
        link_string += f'{k}+'
    link_string = link_string[:-1]
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 100.0.4896.127Safari / 537.36'
               }
    if link_string == '':
        response = requests.get('https://www.kufar.by/l?ot=1&query=%D0%B1%D0%BB%D0%BE%D0%BA+%D0%BF%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D1%8F+%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&sort=lst.d', headers = headers).text

    else:
        response = requests.get(f'https://www.kufar.by/l/r~belarus?ar=&ot=1&query={link_string}&rgn=all', headers = headers).text
    
    soup = BeautifulSoup(response,'lxml')
    soup_list = soup.find('div', class_='kf-skxm-8023f').find_all('section')
    for i in soup_list:
        price = i.find('p',class_='kf-bgcl-cf2e2').text
        name = i.find('h3',class_='kf-bgso-73276').text
        city = i.find('div',class_='kf-bgLe-c0928').find('p').text
        
        if city.split(',')[0] == 'Минская' and price != 'Договорная' and price != 'Бесплатно': 
            string += f'{price}/ {name}/ {city}\n'

    string += '\n\n'

    for i in soup_list:
        price = i.find('p',class_='kf-bgcl-cf2e2').text
        name = i.find('h3',class_='kf-bgso-73276').text
        city = i.find('div',class_='kf-bgLe-c0928').find('p').text
        
        if city.split(',')[0] == 'Минск' and price != 'Договорная' and price != 'Бесплатно': 
            string += f'{price}/ {name}/ {city}\n'
        
    return string

def dwds(ms):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 100.0.4896.127Safari / 537.36'
               }
    string = ""
    word = ms.split(' ')[1]
    try:
        response = requests.get(f'https://www.dwds.de/wb/{word}',headers = headers).text
    except:
        pass


    soup = BeautifulSoup(response,'lxml')
    soup_1 = soup.find_all('span',class_='dwdswb-definition')
    try:
        artikel = soup.find('h1', class_ = 'dwdswb-ft-lemmaansatz').text.split(', ')[1]
        artikel_word = artikel + ' ' + word + '\n'
        string += artikel_word
    except:
        artikel = ''


    for i in soup_1:
        string += f'-{i.text}\n\n'

    return string




def camb(ms):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 100.0.4896.127Safari / 537.36'
               }
    string = ""
    word = ms.split(' ')[1]
    try:
        response = requests.get(f'https://dictionary.cambridge.org/dictionary/english-russian/{word}',headers = headers).text
    except:
        pass


    soup = BeautifulSoup(response,'lxml')
    soup_1 = soup.find_all('div',class_='pr dsense')
    for i in soup_1:
        word = i.find('div',class_='def ddef_d db')
        string += f'-{word.text}\n\n'

    return string




def rate(ms):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 100.0.4896.127Safari / 537.36'
               }
    string = ""
    # word = ms.split(' ')[1]
    try:
        response = requests.get(f'https://myfin.by/currency/eur',headers = headers).text
    except:
        pass


    soup = BeautifulSoup(response,'lxml')
    soup_1 = soup.find('tr',class_='tr-tb acc-link_30').find_all('td')[2]
    string += f'eur: {soup_1.text}\n'



    try:
        response = requests.get(f'https://myfin.by/currency/usd',headers = headers).text
    except:
        pass


    soup = BeautifulSoup(response,'lxml')
    soup_1 = soup.find('tr',class_='tr-tb acc-link_30 not_h').find_all('td')[2]
    string += f'usd: {soup_1.text}\n'


    return string





def rail_parcer(ms):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 100.0.4896.127Safari / 537.36'
               }

    global response
    global resp
    resp = ''
    response = ''


    message_list = ms.split(' ')
    try:
        response = requests.get(
            f'https://pass.rw.by/ru/route/?from={message_list[1]}&from_exp=&from_esr=&to={message_list[2]}&to_exp=&to_esr=&front_date=%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F&date=today',
            headers=headers).text
    except:
        pass



    soup = BeautifulSoup(response,'lxml')
    soup_list = soup.find_all('div', class_='sch-table__row')

    for i in soup_list:
        try:
            time = i.find('div', class_ = 'sch-table__time train-from-time').text

            if i.find('div', class_='sch-table__train-type').find('i')['class'] == ['svg-regional_economy']:
                 resp = resp + ' ' + time + '\n'
            elif i.find('div', class_='sch-table__train-type').find('i')['class'] == ['svg-city']:
                resp = resp + '*' + time + '\n'
            else: resp = resp + '$' + time + '\n'
        except: pass

    return resp

    



def main():

    command_list = ['rail']
    bot = telebot.TeleBot('5383799662:AAE4OuwR5JDPgNzbh6WliITmDctV1l3zEbc')


    @bot.message_handler(commands=['de'])
    def dwds_(message):
        bot.send_message(message.chat.id, 'идет поиск...')
        try:
            bot.send_message(message.chat.id, dwds(message.text))
        except:
            bot.send_message(message.chat.id, 'что-то пошло не так...')




    @bot.message_handler(commands=['en'])
    def dwds_(message):
        bot.send_message(message.chat.id, 'идет поиск...')
        try:
            bot.send_message(message.chat.id, camb(message.text))
        except:
            bot.send_message(message.chat.id, 'что-то пошло не так...')




    @bot.message_handler(commands=['rate'])
    def dwds_(message):
        bot.send_message(message.chat.id, 'идет поиск...')
        try:
            bot.send_message(message.chat.id, rate(message.text))
        except:
            bot.send_message(message.chat.id, 'что-то пошло не так...')




    @bot.message_handler(commands=['rail'])
    def rail_(message):
        message_list = message.text.split(' ')
        bot.send_message(message.chat.id, 'идет поиск...')
        try:
            bot.send_message(message.chat.id, rail_parcer(message.text))
        except: bot.send_message(message.chat.id, 'что-то пошло не так...')



    @bot.message_handler(commands = ['k'])
    def kufar_(message):
        bot.send_message(message.chat.id, 'идет поиск...')
        try:
            bot.send_message(message.chat.id, kufar1_(message.text))
        except: bot.send_message(message.chat.id, 'что-то пошло не так...')
        




    @bot.message_handler(commands = ['b'])
    def markup_open(message):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton('/k')
        btn2 = telebot.types.KeyboardButton('/rate')
        btn3 = telebot.types.KeyboardButton('/close')
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,'--', reply_markup = markup)

    @bot.message_handler(commands = ['close'])
    def markup_close(message):
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, '--', reply_markup = markup)





    @bot.message_handler(commands = ['game', 'new_game'])
    def markup_open(message):
        global score 
        global i
        global ps
        global ps2
        i = 0
        score = 0
        markup = telebot.types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton('/der')
        btn2 = telebot.types.KeyboardButton('/die')
        btn3 = telebot.types.KeyboardButton('/das')
       
        
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id,'/start', reply_markup = markup)
        ps = 'i'
        ps2 = 'o'

    @bot.message_handler(commands = ['next', 'start'])
    def next(message): 
            global i
            global ps
            global ps2
            if i < 10 and ps == 'i':
                wort_gen()
                bot.send_message(message.chat.id, word)
                ps2 ='i'
            elif ps == 'i': 
                bot.send_message(message.chat.id, f'Ваша оценка: {score}\nНачать новую игру /new_game\nВыйти из игры /end')
                i = 0
                ps = 'o'
            else: pass


    @bot.message_handler(commands = ['der'])
    def der(message):
        global i
        global score
        global ps
        global ps2
        if art == 'der' and ps == 'i' and ps2 == 'i':
            bot.send_message(message.chat.id, '+')
            score += 1
            i += 1
            bot.send_message(message.chat.id, '/next')
            ps2 = 'o'
        elif ps == 'i' and ps2 == 'i': 
            bot.send_message(message.chat.id, art + " " + word)
            i += 1
            bot.send_message(message.chat.id, '/next')
            ps2 = 'o'
        else: pass


    @bot.message_handler(commands = ['die'])
    def der(message):
        global i
        global score
        global ps
        global ps2
        if art == 'die' and ps == 'i' and ps2 == 'i':
            bot.send_message(message.chat.id, '+')
            score += 1
            i += 1
            bot.send_message(message.chat.id, '/next')
            ps2 = 'o'
        elif ps == 'i' and ps2 == 'i': 
            bot.send_message(message.chat.id, art + " " + word)
            i += 1
            bot.send_message(message.chat.id, '/next')
            ps2 = 'o'
        else: pass

    @bot.message_handler(commands = ['das'])
    def der(message):
        global i
        global score
        global ps
        global ps2
        if art == 'das' and ps == 'i' and ps2 == 'i':
            bot.send_message(message.chat.id, '+')
            score += 1
            i += 1
            bot.send_message(message.chat.id, '/next')
            ps2 = 'o'
        elif ps == 'i' and ps2 == 'i': 
            bot.send_message(message.chat.id, art + " " + word)
            i += 1
            bot.send_message(message.chat.id, '/next')
            ps2 = 'o'
        else: pass

    

    @bot.message_handler(commands = ['end'])
    def markup_close(message):
        global ps
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, '--', reply_markup = markup)
        i = 0
        ps = 'o'



    @bot.message_handler(commands = ['help'])
    def help(message):
        
        bot.send_message(message.chat.id, 'Комманды:\n/rail (начальная станция) (конечная станция) - расписание электричек (временно не работает)\n/rate - курс продажи доллора и евро в обменниках технобанка\n/en (немецкое слово), /de (немецкое слово) - переводчики\n/k (название товара) - чек товаров на куфаре(временно не работает)\n/b - тестовое меню\n/game - игра, артикли')
       
    bot.infinity_polling()


    
  
















    bot.infinity_polling()

if __name__ == '__main__':
    main()