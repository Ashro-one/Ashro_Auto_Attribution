from module.Ashro_tips import *
from module.Ashro_excel import *
from module.Ashro_ports import *
import os
import subprocess
import shutil
from datetime import datetime
# "自动化溯源工具"
# "Version: 2.0"
# "Author: Ashro"
# "Date: 2024-5-10


def clear_output_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def clear_output_directory(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

if __name__ == "__main__":
    output_directory = ".//output"
    clear_output_directory(output_directory)
    Ashro_tips()
    print("微步api调用完成")
    Ashro_excel()
    print("表格数据梳理完成，请查看output/high.txt文件")
    print("开始红队服务器识别")
    Ashro_ports()
    # 获取当前时间并格式化
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = f"./output/{current_time}.html"
    print("红队服务器识别完毕，开始肉鸡抓取")
    # 构建并执行系统命令
    command = [".\\module\\afrog.exe", "-T", ".\\output\\high.txt", "-output", output_file]
    subprocess.run(command, check=True)
