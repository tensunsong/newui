import os
import requests
from ...typing import sha256, Dict, get_type_hints

url = 'https://chatanywhere.cn'
model = ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k',
         'gpt-3.5-turbo-16k-0613', 'gpt-3.5-turbo-0613']
supports_stream = True
needs_auth = False


def _create_completion(model: str, messages: list, stream: bool, chatId: str, **kwargs):
    headers = {
        'authority': 'chatanywhere.cn',
        'method': 'POST',
        'path': '/v1/chat/gpt/',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        'authorization': '',
        'content-length': '289',
        'content-type': 'application/json',
        'origin': 'https://chatanywhere.cn',
        'referer': 'https://chatanywhere.cn/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    json_data = {
        'Id': chatId,
        'model': model,
        'list': messages,
    }

    response = requests.post('https://chatanywhere.cn/v1/chat/gpt/',
                             headers=headers, json=json_data, stream=stream)

    for token in response.iter_content(chunk_size=2046):
        yield (token.decode('utf-8'))


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
