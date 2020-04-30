# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 19:16
# @Author  : zhaihuide@jiandan100.cn
# @Site    : 
# @File    : compare_json_files.py
# @Software: PyCharm
import os
import requests
import json
import re
from lxml import etree

# TODO: 使用前去gitlab中更新cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Cookie': 'experimentation_subject_id=IjRiZDc2YmY3LTc2ZTMtNDg2ZS05OTg0LWIzYTJmZTNlZWZjNCI%3D--130bec20ce49167cad1c7f90a82315e3da8c0283; _gitlab_session=81536d319f7b35db8eabdba45876bd8f; event_filter=all; sidebar_collapsed=false'
}


def compare_update_client_json_208(client_name, version, flag=None):
    """
    :param client_name:
    :param version:
    :param flag: flag=1 为灰度，正式版不传flag参数
    :return:
    """
    main_url = 'http://172.16.0.208/'
    key = 'Modules'
    if flag:
        client_name = client_name + 'Beta'
        key = 'Beta' + key
    files_url = main_url + client_name + '/' + version + '/'
    files_response = requests.get(files_url)
    html = etree.HTML(files_response.text)
    files_list = []
    json_file_list = []
    result = html.xpath("/html/body/pre/a")
    json_file = None
    for i in result:
        if i.text.endswith('json'):
            json_file = i.text
        if i.text != '../' and i.text.endswith('.gz'):
            files_list.append(i.text.strip('.gz'))
    json_file_url = files_url + json_file
    json_file_response = requests.get(json_file_url)
    with open('EasyClient-3.44.18.2004.json', 'w', encoding='utf-8') as f:
        f.write(str(json_file_response.text))

    res_json_list = json_file_response.json()[key]
    for i in res_json_list:
        json_file_list.append(i['name'])
    for i in json_file_list:
        if i not in files_list:
            print(i.ljust(50) + 'failed'.rjust(10))
        else:
            print(i.ljust(50) + 'ok'.rjust(10))
    # for i in files_list:
    #     if i not in json_file_list:
    #         print(i)
    print('json_count: ', len(json_file_list))
    print('files_list: ', len(files_list))


def compare_update_client_json_gitlab(file_path):
    """
    :param client_name:
    :param version:
    :param flag: flag 不传为正式版  flag=1为灰度
    :return:
    """
    key = 'Modules'
    client_name = 'ETClient'
    if 'Beta' in file_path:
        client_name = client_name + 'Beta'
        key = 'Beta' + key
    # start_index = file_path.find('_EasyClient') + 1;
    # client_name=file_path[start_index:-5]
    version=re.findall(r"[\d+][\.\d+]*",file_path)[0]
    gitlab_main_url = "http://gitlab.easytech-main.com/Package/AutomaticPublish{}/tree/master/".format(
        client_name) + version + "/"
    response = requests.get(url=gitlab_main_url, headers=headers)
    file_list_pattern = re.compile(
        r'<a class="str-truncated" href="/Package/AutomaticPublish{}/blob/master/{}/.+?" title="(.*?)">'.format(
            client_name, version)
    )
    files = file_list_pattern.findall(response.text)
    files_list = []
    for i in files:
        if i.endswith(".gz"):
            files_list.append(i.strip('.gz'))
    with open(file_path.format(version), 'r', encoding='utf-8') as f:
        json_file_string = json.loads(f.read())
    if not files_list:
        print('need update Cookie')
        return
    for i in json_file_string[key]:
        if i['name'] not in files_list:
            print(i['name'].ljust(50) + "failed".rjust(10))
        else:
            print(i['name'].ljust(50) + "ok".rjust(10))

def compare_two_json(Beta=None):
    file_list = os.listdir(os.path.dirname(__file__))
    for i in file_list:
        if not i.endswith('.json'):
            file_list.remove(i)
    with open(file_list[0], 'r', encoding='utf-8') as f:
        json_git = f.read()
    with open(file_list[1], 'r', encoding='utf-8') as f:
        json_208 = f.read()
    if json_git == json_208:
        print('OK')
        return
    print('gitlab 与 208 json文件不一致')


if __name__ == '__main__':
    compare_update_client_json_gitlab("C:/Users/chenxiuying/Desktop/3.44.17.2002_EasyClientBeta.json")
    # compare_update_client_json_208('ETClient', '3.44.18.2004')
    # compare_two_json()
