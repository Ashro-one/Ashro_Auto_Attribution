调用微步api实现hvv期间大批量的ip自动化溯源工作


目前实现功能

1.将IP地址放入url.txt中，通过调用微步apikey进行批量查询<br>
2.在当前目录下生成ip_info.csv结果。<br>
3.当查询失败时会将失败的ip存入当前目录下的error.txt文件夹内（大概率是微步apikey额度满了，目前是每个key每天查询50次）<br>
<img width="1278" alt="image" src="https://github.com/Ashro-one/Ashro_Auto_Attribution/assets/49979071/dc1308bd-ad18-43f7-a3e0-fd47c12bc3cf">

4.利用Ashro_excel进行结果转换。<br>
  是对ip_info.csv文件内容的处理，目前的筛选条件为：属于恶意IP、可信度不为低、不是住宅用户、移动基站、白名单、CDN的对应的IP地址会输出到同目录下的higt.txt中
  
5.利用黑客工具指纹针进行红队服务器搜集

<img width="966" alt="image" src="https://github.com/Ashro-one/Ashro_Auto_Attribution/assets/49979071/c72f4f47-15ae-41c7-95cc-39f53675e2af">



脚本使用：

    等全部功能写完 在全部集成到一起
    1.python Ashro_Auto_Attribution.py -f url.txt
    
    2.python Ashro_excel.py

    3.python Ashro_ports.py  -f  high.txt








想弄IP反查域名，找了几个在线网站都不好用，在微步上找到了靠谱的api但是 俺用不了 开发计划失败！！！ 有好的IP反查域名的好网站 可以留言
以查出这个118.212.233.107ip地址域名的的算是好网站。

<img width="983" alt="image" src="https://github.com/Ashro-one/Ashro_Auto_Attribution/assets/49979071/c06d1d1c-a8f4-47b6-afdf-564ee67d7b73">






参考https://github.com/GeniusZJL/Vps_tracke/
    





