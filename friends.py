from friendscon import *
import requests
import json
from urllib.parse import urlencode
from urllib.parse import urlencode
print('Start!')
print ('TEST 1:',getdata())


class User_Defenition2:
    def __init__(self):
        def getdata():
            params = {
            'client_id': friendscon.APP_ID,
            'display': 'page',
            'scope': 'friends',
            'response_type': 'token',
        '   v': '5.8'
        }
        return params

        
user =  User_Defenition2()
print(user.getdata())
response = requests.get('?'.join([friendscon.AUTH_URL, urlencode(params)]))

print('?'.join([friendscon.AUTH_URL, urlencode(params)]))

def make_vk_request_url(method_name, params):
    return f'{friendscon.API_URL}/{method_name}?{urlencode(params)}'

def get_mutual_friends(source_uid, target_uid):
    method_name = 'friends.getMutual'
    User_Defenition.params = {
        'target_uid': target_uid,
        'source_uid': source_uid,
        'access_token': friendscon.TOKEN,
        'v': friendscon.API_VERSION
    }

    request_url = make_vk_request_url(method_name, User_Defenition.params)
    mutual_friends_response = requests.get(request_url).text

    return json.loads(mutual_friends_response)#['response']


def make_link_by_uid(uid):
    return f'https://vk.com/id{uid}'
   


def make_vk_urls_from_list(uid_list):
    mutual_friends_url_list = list()

    for uid in uid_list:
        mutual_friends_url_list.append(make_link_by_uid(uid))

    return mutual_friends_url_list


if __name__ == '__main__':
    source_uid = input('Введите числовой id пользователя, чьих общих друзей будем смотреть: ')
    target_uid = input('Введите числовой id пользователя, у которого будем искать общих друзей: ')
    int(source_uid)
    int(target_uid)
    mutual_uid_list = get_mutual_friends(int(source_uid),int(target_uid))
    mutual_friends_links_list = make_vk_urls_from_list(mutual_uid_list)
    print(response)
    print(mutual_uid_list)
    print('Список общих друзей: ',mutual_friends_links_list) 
    
    #3471318 ID
    #203896624 ID
