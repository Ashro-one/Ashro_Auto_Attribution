import requests
import random
import argparse
import csv

api_keys =  [
    '微步apikey',
    '',
    '',
    '',
    '',
    '',
    ''
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




