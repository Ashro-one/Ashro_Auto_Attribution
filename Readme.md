调用微步api实现hvv期间大批量的ip自动化溯源工作

功能逻辑：

  1.将IP地址放入url.txt中，通过调用微步apikey进行批量查询<br>
  2.在output/目录下生成ip_info.csv结果。<br>
  3.当查询失败时会将失败的ip存入当前目录下的error.txt文件夹内（大概率是微步apikey额度满了，目前是每个key每天查询50次）<br>
  
  4.利用Ashro_excel进行结果转换。<br>
    是对ip_info.csv文件内容的处理，目前的筛选条件为：属于恶意IP、可信度不为低、不是住宅用户、移动基站、白名单、CDN的对应的IP地址会输出到output/higt.txt中
    
  5.利用黑客工具指纹针进行红队服务器搜集（.Ashro_ports）

  6.利用常用漏扫工具进行肉鸡漏洞抓取（afrog）<br>
    其他的漏扫可以自己将output/high.txt文件中的ip地址拿去扫。


脚本使用：

  1.python Ashro_Auto_Attribution.py -f url.txt

配置修改：
  1.修改module/Ashro_tips.py中添加apikey
<img width="700" alt="image" src="https://github.com/Ashro-one/Ashro_Auto_Attribution/assets/49979071/d44cfd7f-288d-4e55-a7ea-d87ad2f1ac9a">

  2.修改afrog的配置文件
  https://github.com/zan8in/afrog
  <img width="859" alt="image" src="https://github.com/Ashro-one/Ashro_Auto_Attribution/assets/49979071/1d2cafac-f2ce-41d3-bffd-4a0ded770151">
  
使用截图：
<img width="984" alt="image" src="https://github.com/Ashro-one/Ashro_Auto_Attribution/assets/49979071/dbbda109-2828-4533-b4d7-27150d00f262">




想弄IP反查域名，找了几个在线网站都不好用，在微步上找到了靠谱的api但是 俺用不了 开发计划失败！！！ 有好的IP反查域名的好网站 可以留言
以查出这个118.212.233.107ip地址域名的的算是好网站。

<img width="983" alt="image" src="https://github.com/Ashro-one/Ashro_Auto_Attribution/assets/49979071/c06d1d1c-a8f4-47b6-afdf-564ee67d7b73">






参考https://github.com/GeniusZJL/Vps_tracke/
    





