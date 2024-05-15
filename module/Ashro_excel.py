import csv
import ast
def Ashro_excel():
    # 存储符合条件的IP地址
    high_ips = []

    # 打开CSV文件，使用utf-8编码
    with open('.//output//ip_info.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳过标题行
        for row in reader:
            # 检查第12列是否为TRUE，第11列是否不为"low"，第10列数据不是"住宅用户"也不是"移动热点"
            if row[11] == "True" and row[10] != "low" and row[9] not in ["Residence", "Mobile Network"]:#Residence=住宅用户、Mobile Network=手机热点、True为高可信
                # 解析第三列数据为列表
                tags = ast.literal_eval(row[2])
                # 检查列表中是否包含"白名单"或"CDN"或”搜索引擎爬虫“
                if 'Whitelist' not in tags or 'CDN' not in tags or 'Search Engine Crawler' not in tags:
                    # 将符合条件的IP地址加入到列表中
                    high_ips.append(row[0])

    # 将符合条件的IP地址输出到high.txt文件中
    if high_ips:
        with open('.//output//high.txt', 'w', encoding='utf-8') as txtfile:
            for ip in high_ips:
                txtfile.write(ip + '\n')
    else:
        print("No high IPs found.")
