import requests
import json
from urllib.parse import urlencode

API_URL = 'https://api.vk.com/method/'
API_VERSION = '5.8'
TOKEN = '10f71e1197d0cd085288568fae2a55ad9c8a029d7659271021e1dd62cdb63ccabf38a5315498b25b3678e'


def make_vk_request_url(method_name, params):
    return f'{API_URL}/{method_name}?{urlencode(params)}'


def get_mutual_friends(source_uid, target_uid):
    method_name = 'friends.getMutual'
    params = {
        'target_uid': target_uid,
        'source_uid': source_uid,
        'access_token': TOKEN,
        'v': API_VERSION
    }

    request_url = make_vk_request_url(method_name, params)
    mutual_friends_response = requests.get(request_url).text

    return json.loads(mutual_friends_response)


def make_link_by_uid(uid):
    return f'https://vk.com/id{uid}'
   


def make_vk_urls_from_list(uid_list):
    mutual_friends_url_list = list()

    for uid in uid_list:
        mutual_friends_url_list.append(make_link_by_uid(uid))

    return mutual_friends_url_list


if __name__ == '__main__':
    source_uid = input('¬ведите числовой id пользовател€, чьих общих друзей будем смотреть: ')
    target_uid = input('¬ведите числовой id пользовател€, у которого будем искать общих друзей: ')
    int(source_uid)
    int(target_uid)
    mutual_uid_list = get_mutual_friends(int(source_uid),int(target_uid))
    mutual_friends_links_list = make_vk_urls_from_list(mutual_uid_list)

    print(mutual_friends_links_list) 
    
    #3471318 ID
    #203896624 ID