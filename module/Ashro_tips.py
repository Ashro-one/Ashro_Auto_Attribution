import requests
import random
import argparse
import csv

api_keys =  [
    '062dc71eb1ea4fffb1301dd5b9abf7ee84ce2d3ea7bc4d8ab2fc92927c8ffc7e',
    '7a668c5eda1a4bba9884582c3f8be46d59a6c74ed2ca476eb0df305ce45c27a3',
    'e37a3a7a5671446595a21f346cb903ff6c1074e5b4c348dfa19b13320c06655b',
    '4221435794bc4f63a28c77eb93b36bf0e651ccbd14b34e9888a2fa1ceb198c60',
    'e901ad781089404cafb6c2838bb5ad54affc95238e844c16b974ca7b314e3756',
    '415f32bad8f94fb8bda90237298ceb35286233fa77ba4f2685b5915734403da0',
    '90de501f42fd4e46b45cba9ba4a8b16a0e57922fedc247aa8d1c240c76e21450'
]

url = "https://api.threatbook.cn/v3/scene/ip_reputation"


def process_resource(resource):
    api_key = random.choice(api_keys)

    query = {
        "apikey": api_key,
        "resource": resource
    }

    try:
        response = requests.get(url, params=query)
        response.raise_for_status()
        response_json = response.json()

        if response_json.get('response_code') == 0:
            if 'data' in response_json and len(response_json['data']) > 0:
                for ip, info in response_json['data'].items():
                    save_to_csv(ip, info)
            else:
                print("未找到数据:", resource)
        else:
            print("响应代码不为0. 响应内容: %s" % response_json)
            with open('error.txt', 'a') as error_file:  # 使用'a'模式打开文件以追加内容
                error_file.write(f"{resource}\n")  # 写入资源信息

    except requests.exceptions.RequestException as e:
        print("发生错误: %s" % str(e))
    except (KeyError, IndexError) as e:
        print("处理响应时发生错误: %s" % str(e))


def save_to_csv(ip, info):
    fieldnames = ['IP地址', '严重程度', '判断', '标签', '运营商', '国家', '省份', '城市', 'ASN信息', '场景', '可信度水平', '是否恶意', '更新时间']
    filename = './/output//ip_info.csv'

    with open(filename, mode='a', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'IP地址': ip,
            '严重程度': info.get('severity'),
            '判断': info.get('judgments'),
            '标签': info.get('tags_classes'),
            '运营商': info.get('basic', {}).get('carrier'),
            '国家': info.get('basic', {}).get('location', {}).get('country'),
            '省份': info.get('basic', {}).get('location', {}).get('province'),
            '城市': info.get('basic', {}).get('location', {}).get('city'),
            'ASN信息': info.get('asn'),
            '场景': info.get('scene'),
            '可信度水平': info.get('confidence_level'),
            '是否恶意': info.get('is_malicious'),
            '更新时间': info.get('update_time')
        })




def Ashro_tips():
    parser = argparse.ArgumentParser(description='处理文件中的IP或域名地址.')
    parser.add_argument('-f', '--file', type=str, required=True, help='包含IP或域名地址列表的文件')
    args = parser.parse_args()

    with open(args.file, 'r', encoding='utf-8') as file:
        for line in file:
            resource = line.strip()
            process_resource(resource)




