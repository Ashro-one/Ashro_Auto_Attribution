import argparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from openpyxl import Workbook
from tqdm import tqdm
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SERVICES = [
    {"name": "灯塔资产系统", "url_pattern": "https://{ip}:{port}", "keyword": "资产灯塔系统"},
    {"name": "Viper", "url_pattern": "https://{ip}:{port}/#/user/login", "keyword": "VIPER"},
    {"name": "AWVS漏洞扫描器", "url_pattern": "https://{ip}:{port}/#/user/login", "keyword": "<title>Acunetix</title>"},
    {"name": "大宝剑-实战化攻防对抗系统", "url_pattern": "http://{ip}:{port}/auth/login", "keyword": "大宝剑-实战化攻防对抗系统"},
    {"name": "H资产收集平台", "url_pattern": "http://{ip}:{port}/login", "keyword": "Flask Datta Able"},
    {"name": "LangSrc(资产监控平台)", "url_pattern": "http://{ip}:{port}", "keyword": "LangSrc"},
    {"name": "Manjusaka(牛屎花C2管理)", "url_pattern": "http://{ip}:{port}/manjusaka/static/#/login?redirect=/agents", "keyword": "Manjusaka"},
    {"name": "美杜莎红队武器库平台", "url_pattern": "https://{ip}:{port}/#/user/login", "keyword": "Medusa doesn't work properly without JavaScript"},
    {"name": "nemo(自动化信息收集)", "url_pattern": "http://{ip}:{port}/", "keyword": "Nemo"},
    {"name": "Nessus(漏洞扫描器)", "url_pattern": "https://{ip}:{port}/#/", "keyword": "Nessus"},
    {"name": "NextScan(黑盒扫描)", "url_pattern": "http://{ip}:{port}/", "keyword": "NextScan"},
    {"name": "NPS(穿透工具)", "url_pattern": "http://{ip}:{port}/login/index", "keyword": "nps"},
    {"name": "NPS(穿透工具)", "url_pattern": "http://{ip}:{port}/login/index", "keyword": '<a href="https://ehang.io/nps"'},
    {"name": "Frp面板", "url_pattern": "http://{ip}:{port}/", "keyword": "frp"},
    {"name": "DNSLOG平台", "url_pattern": "http://{ip}:{port}/", "keyword": "dnslog"},
    {"name": "Supershell-c2", "url_pattern": "http://{ip}:{port}/supershell/login", "keyword": "Supershell"},
    {"name": "xray Cland Beta 反连平台", "url_pattern": "http://{ip}:{port}/cland/", "keyword": "cland"}
]

def scan_target(ip, port):
    for service in SERVICES:
        try:
            url = service["url_pattern"].format(ip=ip, port=port)
            res = requests.get(url, verify=False, timeout=3)
            res.encoding = "utf-8"
            if service["keyword"] in res.text:
                return {"ip": ip, "port": port, "title": service["name"]}
        except Exception as e:
            pass

def scan_ports(ip, ports):
    results = []
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(scan_target, ip, port) for port in ports]
        for future in tqdm(as_completed(futures), total=len(ports), desc="正在扫描 ", colour='green', ncols=100):
            result = future.result()
            if result:
                results.append(result)
    return results

def scan_all_ports(ip):
    results = []
    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = [executor.submit(scan_target, ip, port) for port in range(1, 65536)]
        for future in tqdm(as_completed(futures), total=65535, desc="正在扫描 ", colour='green', ncols=100):
            result = future.result()
            if result:
                results.append(result)
    return results

def Ashro_ports():

    ports_to_scan = [80, 443, 8080, 22, 3389, 5003, 8888, 3443, 5000, 6000, 7000, 7500, 8081, 5005, 3200, 8001,
                     8834, 8082, 8083, 8084, 8085, 60000, 50050, 8777]
    results = []

    # 指定文件路径为 ./output/higt.txt
    file_path = ".//output//high.txt"

    with open(file_path, "r") as file:
        target_ips = [line.strip() for line in file if line.strip()]

    for target_ip in target_ips:
        print(f"正在扫描 {target_ip} ")
        target_results = scan_ports(target_ip, ports_to_scan)
        results.extend(target_results)

    if results:
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["IP", "Port", "Title"])
        for result in results:
            sheet.append([result["ip"], result["port"], result["title"]])
        workbook.save("./output/result.xlsx")
    else:
        print("没有找到红队服务器")
