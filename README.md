# enter_for_chinapmp
pmp项目管理人才基金会报名脚本，如果有机会再用，请珍惜，勿乱用，分享乃快乐之本，分享乃进步的动力。
本脚本仅试验过2021年6月中国pmp考试报名，不清楚以后的报名还会不会卡顿，api会不会变，仅供参考。

使用教程:
1.联网安装python3.7及以上版本
2.安装requirements
  pip install requests
  pip install lxml
3.修改脚本报名信息 pmi 里的内容
  #基金会登录用户名
  JJH_USER=''
  #基金会登录密码
  JJH_PWD=''
  #PMI用户名
  PMI_USER=''
  #PMI密码
  PMI_PWD=''
  #PMI ID
  PMI_ID=''
  #PMI 姓,拼音
  PMI_XING=''
  #PMI 名,拼音
  PMI_MING=''
  #PMI 起始有效期 yyyy-mm-dd格式,比如2020-09-11
  PMI_VALID_BEGIN=''
  #PMI 结束有效期 yyyy-mm-dd格式,比如2021-09-11
  PMI_VALID_END=''
  #培训机构ID,从PXJG 里面找,"0"对应的培训机构是 "567 Advanced Business Analytics Specialization"
  PMI_PXJG_ID='0'
  #报名考试地点ID, 从KSDD 里面找,"0"对应的考试地点是 "118 保定才聚",是tuple,每次随机选一个
  PMI_KSDD_ID=('0','1','2')
  
  --说明：信息必须填对，填错导致的报名审核不通过自己拿脑袋撞墙去；
         培训机构从PXJG中选择key填入，考试地点从KSDD中选择key填入；
         PMI_KSDD_ID可以只选一个考点，但是必须填tuple格式，比如('0',)、('1',)，添加多个考点是为了给那些选不到心仪考场只能就近找其他考场的网友提供方便。
         
4.执行脚本
  控制台或终端执行 python chinapmp.py
  输入2，回车：
    load_params函数提供导出培训机构和考试地点的功能，导出到工程目录下的“培训和考试点.txt”，两个json替换代码中的PXJG和KSDD即可，注意对应的key值可能发生变化。
  输入1，回车：
    享受极速报名的乐趣吧。
    
写在最后：
  形形色色的网站我见过不少，公益且稳定运维的，能扛得住爬虫抓取数据(Invitation Code)的，我只服1024。
  国内大部分机构的门户网站都没有多大的抗压能力，面对一年只需应对报名和查分这几天高峰访问量导致的服务宕机问题，
  人力运维比起平时投入几倍甚至几十倍的资金做互联网服务架构要划算的多，所以网站会大改吗？呵呵~~~
  最后，谢谢运维们的辛苦付出，使我们这些码农能报上名，还祝网友们都能考过，做好真正的项管，为自己的公司发展出力，为祖国建设出力！
  
  
  
  
  
