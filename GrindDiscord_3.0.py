import requests as r
import time
import telebot
session_girl = r.session()
session_boy = r.session()
data_for_bot = open ('data_for_bot.txt', 'r', encoding = 'utf-8')
list_data_for_bot_dirty = data_for_bot.readlines ()

def cleaner(list_data_for_bot_dirty):
    list_data_for_bot = []
    a = list_data_for_bot_dirty [0]
    b = a.replace('Token girl:','')
    b = b.replace('\n','')
    list_data_for_bot += [b]
    a = list_data_for_bot_dirty [1]
    b = a.replace('Token boy:','')
    b = b.replace('\n','')
    list_data_for_bot += [b]
    a = list_data_for_bot_dirty [2]
    b = a.replace('channel id:','')
    b = b.replace('\n','')
    list_data_for_bot += [b]
    a = list_data_for_bot_dirty [3]
    b = a.replace('guild id:','')
    b = b.replace('\n','')
    list_data_for_bot += [b]
    a = list_data_for_bot_dirty [4]
    b = a.replace('pause:','')
    b = b.replace('\n','')
    list_data_for_bot += [b]
    a = list_data_for_bot_dirty [5]
    b = a.replace('Your_telegram_id:','')
    b = b.replace('\n','')
    list_data_for_bot += [b]
    return (list_data_for_bot)

list_data_for_bot = cleaner(list_data_for_bot_dirty)
token_girl  = list_data_for_bot [0]
token_boy = list_data_for_bot [1]
header_girl  = {'authorization': token_girl}
header_boy  = {'authorization': token_boy}
file_girl = open('girl.txt', 'r', encoding = 'utf-8')
file_boy = open('boy.txt', 'r', encoding = 'utf-8')
channel_id = list_data_for_bot [2]
guild_id = list_data_for_bot [3]
total_sent_girl = 0
total_sent_boy = 0
indicator = 0
pausex2 = int (list_data_for_bot[4])
pause = pausex2 / 2
delay = int (pause / 10)
remainder = pause - (8 * delay)
if remainder > 3:
    remainder -=3
else:
    remainder = 0.001
token_telegram_bot = '5203497261:AAEC68-h7YtybJtdP0hCZIzxM6zS3hxXtMs'
bot = telebot.TeleBot (token_telegram_bot)
ID_telegram = int (list_data_for_bot [5])
first_girl_sentence = file_girl.readline()
file_girl.close()
file_girl = open('girl.txt', 'r', encoding = 'utf-8')
 #telegram sender function
list_repeatedID_tags_girl = []
list_repeatedID_tags_boy = []
list_repeatedID_replay_girl = []
list_repeatedID_replay_boy = []
Del1 = []
Del2 = []
Del3 = []
Del4 = []
def tags_replays (header_girl, list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy,
                  bot, ID_telegram, ID_discord_girl, ID_discord_boy):
    request = session_girl.get (f'https://discord.com/api/v9/channels/{channel_id}/messages', headers = header_girl).json()
    for i in request:
        if (i['mentions'] != []) and  (i['mentions'][0]['id'] == f'{ID_discord_girl}') and  (('message_reference' in i) == False) and ((i['id'] in list_repeatedID_tags_girl) == False) and ((i['author']['id'] in [ID_discord_girl, ID_discord_boy]) == False):
            list_repeatedID_tags_girl.append (i['id'])
            bot.send_message (ID_telegram, f"Твоего первого человека тегнул: {i['author']['username']} Его сообщение: {i['content']}")
        elif (i['mentions'] != []) and  (i['mentions'][0]['id'] == f'{ID_discord_boy}') and  (('message_reference' in i) == False) and ((i['id'] in list_repeatedID_tags_boy) == False) and ((i['author']['id'] in [ID_discord_girl, ID_discord_boy]) == False):
            list_repeatedID_tags_boy.append (i['id'])
            bot.send_message (ID_telegram, f"Твоего второго человека тегнул: {i['author']['username']} Его сообщение: {i['content']}")
        if (i['mentions'] != []) and (i['mentions'][0]['id'] == f'{ID_discord_girl}') and (('message_reference' in i) == True) and ((i['id'] in list_repeatedID_replay_girl) == False) and ((i['author']['id'] in [ID_discord_girl, ID_discord_boy]) == False):
            list_repeatedID_replay_girl.append (i['id'])
            bot.send_message (ID_telegram,  f"сообщение твоего первого человека переслал: {i['author']['username']} его сообщение: {i['content']}" )    
        elif (i['mentions'] != []) and (i['mentions'][0]['id'] == f'{ID_discord_boy}') and (('message_reference' in i) == True) and ((i['id'] in list_repeatedID_replay_boy) == False) and ((i['author']['id'] in [ID_discord_girl, ID_discord_boy]) == False): 
            list_repeatedID_replay_boy.append (i['id'])
            bot.send_message (ID_telegram, f"сообщение твоего второго человека переслал: {i['author']['username']} его сообщение: {i['content']}")
    return list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy

def id_from_storage  ():
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list_repeatedID_tags_girl = []
    list_repeatedID_tags_boy = []
    list_repeatedID_replay_girl = []
    list_repeatedID_replay_boy = []
    file_repeatedID_tags_girl = open ('file_repeatedID_tags_girl.txt', 'r')
    file_repeatedID_tags_boy = open ('file_repeatedID_tags_boy.txt', 'r')
    file_repeatedID_replay_girl = open ('file_repeatedID_replay_girl.txt', 'r')
    file_repeatedID_replay_boy = open ('file_repeatedID_replay_boy.txt', 'r')
    list1 = file_repeatedID_tags_girl.readlines ()
    for i in list1:
        a = i.replace ('\n','')
        list_repeatedID_tags_girl += [a]
    list2 =  file_repeatedID_tags_boy.readlines ()
    for i in list2:
        a = i.replace ('\n','')
        list_repeatedID_tags_boy += [a]
    list3 =  file_repeatedID_replay_girl.readlines ()
    for i in list3:
        a = i.replace ('\n','')
        list_repeatedID_replay_girl += [a]
    list4 =  file_repeatedID_replay_boy.readlines ()
    for i in list4:
        a = i.replace ('\n','')
        list_repeatedID_replay_boy += [a]
    file_repeatedID_tags_girl.close ()
    file_repeatedID_tags_boy.close ()
    file_repeatedID_replay_girl.close () 
    file_repeatedID_replay_boy.close ()
    return list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy

                                                 #start function id_from_storage:
list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy  = id_from_storage ()
Del1 , Del2, Del3 , Del4 = id_from_storage ()

def finally_function (list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy , Del1 , Del2, Del3 , Del4 ):
    file_repeatedID_tags_girl = open ('file_repeatedID_tags_girl.txt', 'w')
    file_repeatedID_tags_boy = open ('file_repeatedID_tags_boy.txt', 'w')
    file_repeatedID_replay_girl = open ('file_repeatedID_replay_girl.txt', 'w')
    file_repeatedID_replay_boy = open ('file_repeatedID_replay_boy.txt', 'w')
    for  i in list_repeatedID_tags_girl:
        if (i in Del1) == True:
            continue
        else:
            file_repeatedID_tags_girl.write (i + '\n')
    for  i in list_repeatedID_tags_boy:
        if (i in Del2) == True:
            continue
        else:
            file_repeatedID_tags_boy.write (i + '\n')
    for  i in list_repeatedID_replay_girl:
        if (i in Del3) == True:
            continue
        else:
            file_repeatedID_replay_girl.write (i + '\n')
    for  i in list_repeatedID_replay_boy:
        if (i in Del4) == True:
            continue
        else:
            file_repeatedID_replay_boy.write (i + '\n')
    file_repeatedID_tags_girl.close ()
    file_repeatedID_tags_boy.close ()
    file_repeatedID_replay_girl.close () 
    file_repeatedID_replay_boy.close ()

                                                 #Imitation of a boy typing keys
def prints_boy (delay, header_boy):
    for i in range (delay):
        try:
            prints_boy_requests = session_boy.post(f'https://discord.com/api/v9/channels/{channel_id}/typing', headers = header_boy )
            time.sleep (8)
            if i == delay - 1:
                prints_boy_requests = session_boy.post(f'https://discord.com/api/v9/channels/{channel_id}/typing', headers = header_boy )
                break
        except Exception:
            continue 

                                                 #Imitation of a girl typing keys
def prints_girl (delay, header_girl):
    for i in range (delay):
        try:
            prints_girl_requests = session_girl.post(f'https://discord.com/api/v9/channels/{channel_id}/typing', headers = header_girl )
            time.sleep (8)
            if i == delay - 1:
                prints_girl_requests = session_girl.post(f'https://discord.com/api/v9/channels/{channel_id}/typing', headers = header_girl)
                break
        except Exception:
            continue
    
while True:
    try:
        message_girl = file_girl.readline()
        message_boy = file_boy.readline()
        if message_girl == first_girl_sentence:
            print(f'Sending message girl {message_girl}')
            _data_girl = {'content': message_girl, 'tts': False}
            responce_girl = session_girl.post(
            f'https://discord.com/api/v9/channels/{channel_id}/messages', json=_data_girl, headers = header_girl).json()
            message_id_girl = responce_girl['id']
            ID_discord_girl = responce_girl ['author']['id']
            total_sent_girl += 1
            print (f'Message girl sent (Already {total_sent_girl} in total).')
            prints_boy (delay, header_boy)
            time.sleep (remainder + 3)
            print(f'Sending message boy {message_boy}')
            _data_boy = {'content': message_boy, 'tts': False, 'message_reference' : {'channel_id': f'{channel_id}' ,'guild_id': f'{guild_id}','message_id': f'{message_id_girl}' }}
            responce_boy = session_boy.post(
            f'https://discord.com/api/v9/channels/{channel_id}/messages', json=_data_boy, headers = header_boy).json()
            message_id_boy = responce_boy['id']
            ID_discord_boy = responce_boy ['author']['id']
            total_sent_boy += 1
            print (f'Message boy sent (Already {total_sent_boy} in total).')
            prints_girl (delay, header_girl)
            list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy = tags_replays (header_girl, list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy, bot, ID_telegram, ID_discord_girl, ID_discord_boy)
            time.sleep (remainder)
            continue
        if message_girl == '':
            time.sleep (10)
            file_girl = open('girl.txt', 'r', encoding='utf-8')
            first_girl_sentence = file_girl.readline()
            file_girl.close()
            file_girl = open('girl.txt', 'r', encoding = 'utf-8')
            file_boy = open('boy.txt', 'r', encoding='utf-8')
            continue
        print(f'Sending message girl {message_girl}')
        _data_girl = {'content': message_girl, 'ttsa': False, 'message_reference' : {'channel_id': f'{channel_id}' ,'guild_id': f'{guild_id}','message_id': f'{message_id_boy}'}}
        responce_girl = session_girl.post(
        f'https://discord.com/api/v9/channels/{channel_id}/messages', json=_data_girl, headers = header_girl).json()
        message_id_girl = responce_girl['id']
        total_sent_girl += 1
        print (f'Message girl sent (Already {total_sent_girl} in total).')
        prints_boy (delay, header_boy)
        list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy = tags_replays (header_girl, list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy, bot, ID_telegram, ID_discord_girl, ID_discord_boy)
        time.sleep (remainder)
        print(f'Sending message boy {message_boy}')
        _data_boy = {'content': message_boy, 'tts': False, 'message_reference' : {'channel_id': f'{channel_id}' ,'guild_id': f'{guild_id}','message_id': f'{message_id_girl}' }}
        responce_boy = session_boy.post(
        f'https://discord.com/api/v9/channels/{channel_id}/messages', json=_data_boy, headers = header_boy).json()
        message_id_boy = responce_boy['id']
        total_sent_boy += 1
        print (f'Message boy sent (Already {total_sent_boy} in total).')
        prints_girl (delay, header_girl)
        list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy = tags_replays (header_girl, list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy, bot, ID_telegram, ID_discord_girl, ID_discord_boy)
        time.sleep (remainder)
    except Exception as e:
        while True:
            try:
                print(f'Some error: {e}')
                time.sleep (10) ####ИСправь Потом!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
                prints_girl (delay, header_girl)
                time.sleep (remainder +3)
                message_girl = 'Хээй, ' + message_girl 
                print(f'Sending message girl {message_girl}')
                _data_girl = {'content': message_girl, 'tts': False, 'message_reference' : {'channel_id': f'{channel_id}' ,'guild_id': f'{guild_id}','message_id': f'{message_id_boy}'}}
                responce_girl = session_girl.post(
                f'https://discord.com/api/v9/channels/{channel_id}/messages', json=_data_girl, headers = header_girl).json()
                message_id_girl = responce_girl['id']
                total_sent_girl += 1
                print (f'Message girl sent (Already {total_sent_girl} in total).')
                prints_boy (delay, header_boy)
                time.sleep (remainder)
                print(f'Sending message girl {message_boy}')
                _data_boy = {'content': message_boy, 'tts': False, 'message_reference' : {'channel_id': f'{channel_id}' ,'guild_id': f'{guild_id}','message_id': f'{message_id_girl}' }}
                responce_boy = session_boy.post(
                f'https://discord.com/api/v9/channels/{channel_id}/messages', json=_data_boy, headers = header_boy).json()
                message_id_boy = responce_boy['id']
                total_sent_boy += 1
                print (f'Message boy sent (Already {total_sent_boy} in total).')
                prints_girl (delay, header_girl)
                time.sleep (remainder + 3)
                break
            except Exception:
                print ('error again')
                message_girl = message_girl.replace ('Хээй, ','')
    finally:
        finally_function (list_repeatedID_tags_girl, list_repeatedID_tags_boy, list_repeatedID_replay_girl, list_repeatedID_replay_boy, Del1 , Del2, Del3 , Del4)

######OTE1NzYyMTMxNTYyMDM3MzI5.YlWBNQ.5BR5qQxBy5Rfk1gSxJ4Lz8Iu-qk
