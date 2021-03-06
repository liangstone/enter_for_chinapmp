import requests
from datetime import datetime
import random
from lxml import etree
import json

'''
  title   pmp报名脚本
  author  fxckmeohbaby@gmail.com
  date    2021-04-15 11:00:00
  descrption  得益于chinapmp.cn提供的并不是互联网应用服务,其接口没有复杂的加密措施而只做了简单的cookies缓存和校验,
              所以本脚本精简了页面请求流程,只做登录和报名请求,大大提高了成功率,请仔细查看代码注释,
              填错个人信息导致的报名审核错误本人不负任何责任.
  env python3.7
  requirments requests,lxml
'''

class pmi():
  ###################################################
  #基金会登录用户名
  JJH_USER=''
  #基金会登录密码
  JJH_PWD=''
  ###################################################
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
  PMI_PXJG_ID="0"
  #报名考试地点ID, 从KSDD 里面找,"0"对应的考试地点是 "118 保定才聚",是tuple,每次随机选一个
  PMI_KSDD_ID=("0","1","2")
  ###################################################


PXJG={
  "0": [
    "567",
    "Advanced Business Analytics Specialization"
  ],
  "1": [
    "566",
    "Boston College- Woods College of Advancing Studies"
  ],
  "10": [
    "535",
    "Master of Project Academy"
  ],
  "100": [
    "496",
    "美国艾威学院（中国）培训中心"
  ],
  "101": [
    "554",
    "美国伯克利分校延展课程"
  ],
  "102": [
    "390",
    "内蒙古建设培训学校"
  ],
  "103": [
    "34",
    "南京睿煌企业管理咨询有限责任公司"
  ],
  "104": [
    "502",
    "南京思摩特企业管理咨询"
  ],
  "105": [
    "606",
    "南京松勤网络科技有限公司"
  ],
  "106": [
    "501",
    "南京远光广安信息科技有限公司"
  ],
  "107": [
    "6",
    "南京卓而越管理技术培训咨询有限公司"
  ],
  "108": [
    "602",
    "宁波诺丁汉大学"
  ],
  "109": [
    "35",
    "宁波市人才培训中心"
  ],
  "11": [
    "548",
    "MILESTONE TRAINING CENTER"
  ],
  "110": [
    "578",
    "宁夏软件工程院"
  ],
  "111": [
    "569",
    "青岛齐睿教育科技有限公司"
  ],
  "112": [
    "218",
    "青岛时代企业培训服务有限公司"
  ],
  "113": [
    "313",
    "青岛易佳盈通管理咨询有限公司"
  ],
  "114": [
    "556",
    "青岛易佳盈通管理咨询有限公司"
  ],
  "115": [
    "583",
    "清华大学（土木水利学院建设管理系）"
  ],
  "116": [
    "309",
    "睿达博创国际管理咨询（北京）有限公司"
  ],
  "117": [
    "588",
    "山东大学（管理学院）"
  ],
  "118": [
    "78",
    "山东省振鲁国际交流中心"
  ],
  "119": [
    "545",
    "山东知创管理咨询有限公司"
  ],
  "12": [
    "481",
    "Platinum Edge., Inc"
  ],
  "120": [
    "538",
    "上海艾纵企业管理咨询有限公司"
  ],
  "121": [
    "166",
    "上海创择企业管理顾问有限公司"
  ],
  "122": [
    "527",
    "上海慧谷职业技能培训中心"
  ],
  "123": [
    "582",
    "上海交通大学（机械与动力工程学院）"
  ],
  "124": [
    "327",
    "上海交通大学继续教育学院"
  ],
  "125": [
    "210",
    "上海科维安信息技术顾问有限公司"
  ],
  "126": [
    "388",
    "上海肯恩企业管理有限公司"
  ],
  "127": [
    "500",
    "上海乐凯企业管理咨询有限公司"
  ],
  "128": [
    "448",
    "上海妙坊企业管理咨询有限公司"
  ],
  "129": [
    "528",
    "上海能略企业管理咨询有限公司（第五空间）"
  ],
  "13": [
    "565",
    "Pluralsight LLC"
  ],
  "130": [
    "139",
    "上海普华科技发展有限公司"
  ],
  "131": [
    "18",
    "上海清晖管理咨询有限公司"
  ],
  "132": [
    "465",
    "上海市浦东软件园职业技能培训中心"
  ],
  "133": [
    "3",
    "上海威训企业管理咨询有限公司"
  ],
  "134": [
    "463",
    "上海项尔管理咨询有限公司"
  ],
  "135": [
    "48",
    "上海欣旋企业管理咨询有限公司"
  ],
  "136": [
    "323",
    "上海易卓企业管理有限公司"
  ],
  "137": [
    "394",
    "上海羿升企业管理咨询有限公司"
  ],
  "138": [
    "550",
    "上海渔羽管理咨询有限公司"
  ],
  "139": [
    "568",
    "上海越臻企业管理咨询有限公司"
  ],
  "14": [
    "534",
    "PMTraining"
  ],
  "140": [
    "555",
    "上海哲越企业管理咨询有限公司"
  ],
  "141": [
    "577",
    "上海中智国际教育培训中心"
  ],
  "142": [
    "498",
    "上海自源商务咨询有限公司"
  ],
  "143": [
    "359",
    "深圳伯瑞环球"
  ],
  "144": [
    "605",
    "深圳敏航管理咨询有限公司"
  ],
  "145": [
    "460",
    "深圳强矩阵企业信息咨询有限公司"
  ],
  "146": [
    "509",
    "深圳青蓝咨询服务有限公司"
  ],
  "147": [
    "432",
    "深圳世纪拓睿教育管理有限公司"
  ],
  "148": [
    "533",
    "深圳市必有师科技有限公司"
  ],
  "149": [
    "433",
    "深圳市博维职业培训中心"
  ],
  "15": [
    "558",
    "STS – Sauter Training &amp; Simulation S.A., Shanghai"
  ],
  "150": [
    "17",
    "深圳市才聚管理咨询有限公司"
  ],
  "151": [
    "229",
    "深圳市才聚管理咨询有限公司广州分公司"
  ],
  "152": [
    "506",
    "深圳市华为培训学院有限公司"
  ],
  "153": [
    "49",
    "深圳市华夏智诚企业管理咨询有限公司"
  ],
  "154": [
    "452",
    "深圳市砺志企业管理咨询有限公司"
  ],
  "155": [
    "478",
    "深圳市联合盈科企业管理有限公司"
  ],
  "156": [
    "111",
    "深圳市世纪卓越管理咨询有限公司"
  ],
  "157": [
    "604",
    "深圳市威班科技发展有限公司"
  ],
  "158": [
    "338",
    "深圳市问道兴业管理咨询有限公司"
  ],
  "159": [
    "446",
    "深圳市兴传管理咨询有限公司"
  ],
  "16": [
    "270",
    "Ten Step China"
  ],
  "160": [
    "508",
    "深圳市旭源管理咨询有限公司"
  ],
  "161": [
    "473",
    "深圳市中鹏教育科技股份有限公司"
  ],
  "162": [
    "507",
    "深圳塔塔咨询服务有限公司"
  ],
  "163": [
    "563",
    "深圳致卓信息技术有限公司"
  ],
  "164": [
    "484",
    "神州数码系统集成服务有限公司"
  ],
  "165": [
    "32",
    "沈阳海外人才交流协会"
  ],
  "166": [
    "572",
    "沈阳华信教育科技有限公司"
  ],
  "167": [
    "86",
    "沈阳惠尔智业教育培训中心"
  ],
  "168": [
    "27",
    "四川思锐项目管理有限公司"
  ],
  "169": [
    "580",
    "苏州高新区（虎丘区）子信职业培训学校"
  ],
  "17": [
    "560",
    "Tiba Managementberatung GmbH"
  ],
  "170": [
    "587",
    "天津大学（管理与经济学部）"
  ],
  "171": [
    "493",
    "天津大学国际工程管理学院"
  ],
  "172": [
    "492",
    "天津市普迅电力信息技术有限公司"
  ],
  "173": [
    "282",
    "天津易迪思高级项目管理学院"
  ],
  "174": [
    "585",
    "同济大学（经济与管理学院）"
  ],
  "175": [
    "499",
    "同曦企业管理有限公司"
  ],
  "176": [
    "30",
    "武汉爱迪泰管理咨询有限公司"
  ],
  "177": [
    "599",
    "武汉聚协企业管理咨询有限公司"
  ],
  "178": [
    "306",
    "武汉现代卓越企业管理咨询有限公司"
  ],
  "179": [
    "586",
    "西北工业大学（管理学院）"
  ],
  "18": [
    "561",
    "TRIG Limited"
  ],
  "180": [
    "571",
    "希赛网"
  ],
  "181": [
    "570",
    "厦门领才教育咨询有限公司"
  ],
  "182": [
    "37",
    "厦门市培因教育培训中心"
  ],
  "183": [
    "511",
    "厦门市运筹管理咨询有限公司(厦门市培因教育培训中心)"
  ],
  "184": [
    "547",
    "厦门外服人力资源服务有限公司"
  ],
  "185": [
    "537",
    "厦门希瑞尔教育咨询有限公司"
  ],
  "186": [
    "449",
    "厦门至格教育咨询有限公司"
  ],
  "187": [
    "491",
    "晓弈（天津）企业管理咨询有限公司"
  ],
  "188": [
    "39",
    "新疆福来威尔企业管理咨询有限公司"
  ],
  "189": [
    "532",
    "远光软件股份有限公司"
  ],
  "19": [
    "480",
    "TwentyEighty Strategy Execution"
  ],
  "190": [
    "16",
    "郑州杰创企业管理咨询有限公司"
  ],
  "191": [
    "601",
    "郑州科科过科技有限公司"
  ],
  "192": [
    "468",
    "中国航天科工集团公司培训中心"
  ],
  "193": [
    "542",
    "中国检验检疫科学研究院"
  ],
  "194": [
    "603",
    "中国检验认证集团陕西有限公司"
  ],
  "195": [
    "529",
    "中国石油大学（北京）继续教育学院"
  ],
  "196": [
    "344",
    "中国石油集团东方地球物理勘探有限责任公司物探培训中心"
  ],
  "197": [
    "595",
    "中国通信建设集团设计院有限公司"
  ],
  "198": [
    "573",
    "中海油安全技术服务有限公司海洋石油培训中心"
  ],
  "199": [
    "367",
    "中软总公司计算机培训中心"
  ],
  "2": [
    "495",
    "Global Business Management Consultants (BMC)"
  ],
  "20": [
    "552",
    "UC Berkeley Extension"
  ],
  "200": [
    "513",
    "中山市海讯企业管理咨询有限公司"
  ],
  "201": [
    "483",
    "中善明易（北京）咨询有限公司(原智鼎东方)"
  ],
  "202": [
    "591",
    "中通信息服务有限公司"
  ],
  "203": [
    "292",
    "中兴通讯股份有限公司-中兴通讯学院"
  ],
  "204": [
    "575",
    "中智优力管理咨询（北京）有限公司"
  ],
  "205": [
    "443",
    "众学网"
  ],
  "206": [
    "530",
    "重庆市高博职业培训学校"
  ],
  "207": [
    "510",
    "珠海LNG"
  ],
  "21": [
    "553",
    "UCLA Extension"
  ],
  "22": [
    "597",
    "University of Colorado Boulder"
  ],
  "23": [
    "412",
    "艾思康（深圳）科技管理咨询有限公司"
  ],
  "24": [
    "544",
    "安徽远景人力资源管理有限公司"
  ],
  "25": [
    "54",
    "安泰赛斯国际项目管理咨询（北京）有限公司"
  ],
  "26": [
    "576",
    "北京艾立克斯咨询有限公司"
  ],
  "27": [
    "486",
    "北京奥品智晟管理咨询（北京）有限公司"
  ],
  "28": [
    "455",
    "北京才聚天下管理咨询有限公司"
  ],
  "29": [
    "482",
    "北京东方迈道国际管理咨询有限公司"
  ],
  "3": [
    "440",
    "IBM"
  ],
  "30": [
    "514",
    "北京泛华卓越企业管理顾问有限公司"
  ],
  "31": [
    "541",
    "北京高远华信科技有限公司"
  ],
  "32": [
    "521",
    "北京共创时网络管理技术有限公司（项目管理者联盟）"
  ],
  "33": [
    "515",
    "北京光环致成国际管理咨询股份有限公司"
  ],
  "34": [
    "489",
    "北京国联融合科技有限公司"
  ],
  "35": [
    "590",
    "北京合创星光科技文化有限公司"
  ],
  "36": [
    "241",
    "北京恒佳时代管理咨询有限公司"
  ],
  "37": [
    "11",
    "北京华科软科技有限公司"
  ],
  "38": [
    "557",
    "北京华信乾坤科技有限公司"
  ],
  "39": [
    "273",
    "北京金色千年咨询有限公司"
  ],
  "4": [
    "479",
    "IIL 中国"
  ],
  "40": [
    "487",
    "北京经华智业教育科技有限公司"
  ],
  "41": [
    "540",
    "北京千锋互联科技有限公司"
  ],
  "42": [
    "447",
    "北京睿思力行管理咨询中心"
  ],
  "43": [
    "184",
    "北京商略达项目管理培训中心"
  ],
  "44": [
    "4",
    "北京神州巨龙管理咨询有限公司"
  ],
  "45": [
    "485",
    "北京世纪畅优互联网信息服务有限责任公司"
  ],
  "46": [
    "574",
    "北京网聘咨询有限公司"
  ],
  "47": [
    "490",
    "北京无忧创想技术咨询有限公司"
  ],
  "48": [
    "600",
    "北京无忧创想信息技术有限公司（51CTO）"
  ],
  "49": [
    "488",
    "北京协英科技顾问有限公司"
  ],
  "5": [
    "441",
    "Instructing.com,LLC"
  ],
  "50": [
    "349",
    "北京易佳盈通咨询有限公司"
  ],
  "51": [
    "584",
    "北京邮电大学（经济管理学院）"
  ],
  "52": [
    "469",
    "北京中公教育科技股份有限公司"
  ],
  "53": [
    "341",
    "北京中培伟业管理咨询有限公司"
  ],
  "54": [
    "596",
    "北京筑龙伟业科技股份有限公司"
  ],
  "55": [
    "228",
    "长沙搜题教育科技有限公司"
  ],
  "56": [
    "512",
    "成都维纳软件"
  ],
  "57": [
    "494",
    "大连鼎达管理咨询有限公司"
  ],
  "58": [
    "470",
    "大连东软信息学院"
  ],
  "59": [
    "197",
    "大连高新区立智管理培训学校"
  ],
  "6": [
    "438",
    "IPA Institute"
  ],
  "60": [
    "516",
    "大庆油田工程建设有限公司培训中心"
  ],
  "61": [
    "425",
    "德硕管理咨询公司"
  ],
  "62": [
    "364",
    "东方瑞通（北京）咨询服务有限公司"
  ],
  "63": [
    "355",
    "东莞市金指南企业管理咨询有限公司"
  ],
  "64": [
    "543",
    "福建省建设人力资源集团股份公司"
  ],
  "65": [
    "581",
    "福州近道教育咨询有限公司"
  ],
  "66": [
    "304",
    "福州领先连邦软件服务有限公司"
  ],
  "67": [
    "517",
    "福州盈通企业管理顾问有限公司"
  ],
  "68": [
    "564",
    "广东蓝海项目管理有限公司"
  ],
  "69": [
    "522",
    "广东省项目管理学会（广西办事处）"
  ],
  "7": [
    "598",
    "Iverson Associates Sdn Bhd"
  ],
  "70": [
    "523",
    "广东邮电职业技术学院"
  ],
  "71": [
    "592",
    "广东中大职业培训学院"
  ],
  "72": [
    "531",
    "广州慧翔企业管理咨询有限公司"
  ],
  "73": [
    "238",
    "广州嘉为科技有限公司"
  ],
  "74": [
    "356",
    "广州圣略科技信息咨询有限公司"
  ],
  "75": [
    "524",
    "广州石油培训中心（中石油培训基地）"
  ],
  "76": [
    "593",
    "广州市夸克企业顾问有限公司"
  ],
  "77": [
    "518",
    "广州市亚加达发展有限公司"
  ],
  "78": [
    "379",
    "广州韦雅度企业管理咨询有限公司"
  ],
  "79": [
    "562",
    "广州韦雅度企业管理咨询有限公司"
  ],
  "8": [
    "536",
    "Lancaster University"
  ],
  "80": [
    "378",
    "广州现代卓越管理技术交流中心有限公司"
  ],
  "81": [
    "505",
    "广州中培项目管理咨询有限公司"
  ],
  "82": [
    "539",
    "广州珠江文化教育培训中心"
  ],
  "83": [
    "326",
    "杭州博学信息技术服务公司"
  ],
  "84": [
    "519",
    "杭州市干部培训中心"
  ],
  "85": [
    "26",
    "杭州市干部培训中心/杭州东方舰桥教育培训中心"
  ],
  "86": [
    "25",
    "杭州新睿智业有限公司"
  ],
  "87": [
    "520",
    "河北石油职业技术学院 （中国石油管道学院）"
  ],
  "88": [
    "589",
    "河海大学（商学院）"
  ],
  "89": [
    "503",
    "河海大学商学院"
  ],
  "9": [
    "549",
    "lynda.com"
  ],
  "90": [
    "594",
    "河南省外事侨务服务中心有限公司"
  ],
  "91": [
    "472",
    "湖北省信产通信服务有限公司科技咨询分公司"
  ],
  "92": [
    "271",
    "惠普培训服务事业部"
  ],
  "93": [
    "526",
    "慧翔天地管理咨询(北京)有限公司"
  ],
  "94": [
    "307",
    "济南市现代卓越管理技术培训学校"
  ],
  "95": [
    "234",
    "嘉为科技咨询有限公司"
  ],
  "96": [
    "551",
    "嘉信和（天津）健康科技有限责任公司"
  ],
  "97": [
    "457",
    "江苏传智播客教育科技股份有限公司"
  ],
  "98": [
    "497",
    "柯马中国"
  ],
  "99": [
    "36",
    "昆明蓝血项目管理系统有限公司"
  ]
}

KSDD={
  "0": [
    "118",
    "保定才聚"
  ],
  "1": [
    "93",
    "长春时代"
  ],
  "10": [
    "23",
    "福州盈通"
  ],
  "11": [
    "210",
    "广州才聚-番禺区（祈福会展中心B）"
  ],
  "12": [
    "226",
    "广州才聚-天河区（广州阳光酒店）"
  ],
  "13": [
    "66",
    "广州才聚-天河区（私立华联学院）"
  ],
  "14": [
    "222",
    "广州亚加达（白云国际会议中心）"
  ],
  "15": [
    "20",
    "广州亚加达（亚加达外语学院）"
  ],
  "16": [
    "208",
    "广州亚加达-白云区（逸林假日酒店）"
  ],
  "17": [
    "215",
    "广州亚加达-天河区（广东邮电职业技术学院）"
  ],
  "18": [
    "202",
    "贵阳卓越临时"
  ],
  "19": [
    "100",
    "哈尔滨时代"
  ],
  "2": [
    "34",
    "长沙卓而越"
  ],
  "20": [
    "69",
    "海口华科软"
  ],
  "21": [
    "213",
    "杭州新睿-滨江区"
  ],
  "22": [
    "6",
    "杭州新睿-江干区"
  ],
  "23": [
    "227",
    "杭州新睿-西湖区"
  ],
  "24": [
    "228",
    "杭州新睿-西湖区2"
  ],
  "25": [
    "5",
    "合肥卓而越-蜀山区"
  ],
  "26": [
    "229",
    "合肥卓而越-瑶海区"
  ],
  "27": [
    "170",
    "呼和浩特"
  ],
  "28": [
    "72",
    "济南振鲁"
  ],
  "29": [
    "13",
    "昆明蓝血"
  ],
  "3": [
    "225",
    "长沙卓而越2"
  ],
  "30": [
    "61",
    "昆山科兹纳"
  ],
  "31": [
    "205",
    "昆山科兹纳临时"
  ],
  "32": [
    "64",
    "廊坊管院"
  ],
  "33": [
    "203",
    "南昌爱迪泰临时"
  ],
  "34": [
    "230",
    "南京睿煌（南京市博览中心）"
  ],
  "35": [
    "224",
    "南京睿煌-浦口区"
  ],
  "36": [
    "3",
    "南京睿煌-玄武区"
  ],
  "37": [
    "231",
    "南京卓而越-建邺区"
  ],
  "38": [
    "70",
    "南京卓而越-江宁开发区"
  ],
  "39": [
    "204",
    "南宁才聚临时"
  ],
  "4": [
    "95",
    "常州清晖"
  ],
  "40": [
    "200",
    "南通清晖临时"
  ],
  "41": [
    "14",
    "宁波人才"
  ],
  "42": [
    "60",
    "青岛时代"
  ],
  "43": [
    "214",
    "上海侨港-长宁区（虹桥会议中心）"
  ],
  "44": [
    "217",
    "上海侨港-长宁区（上海建滔中心）"
  ],
  "45": [
    "232",
    "上海侨港-长宁区（新世纪中学）"
  ],
  "46": [
    "7",
    "上海侨港-长宁区（业余大学）"
  ],
  "47": [
    "145",
    "上海侨港-杨浦区（商学院国科路）"
  ],
  "48": [
    "216",
    "上海仁士-宝山区（交通职业技术学院）"
  ],
  "49": [
    "206",
    "上海仁士-虹口区（南湖职业学校）"
  ],
  "5": [
    "22",
    "成都思锐（成都职业技术学院B区）"
  ],
  "50": [
    "116",
    "上海仁士-浦东区（上海医药学校）"
  ],
  "51": [
    "220",
    "上海仁士-徐汇区（材料机械学校）"
  ],
  "52": [
    "15",
    "上海仁士-徐汇区（立信会计学院）"
  ],
  "53": [
    "96",
    "绍兴爱迪泰"
  ],
  "54": [
    "27",
    "深圳才聚-龙岗区（深圳信息职业技术学院）"
  ],
  "55": [
    "209",
    "深圳才聚-南山区（广东新安职业技术学院）"
  ],
  "56": [
    "141",
    "深圳才聚-南山区（深圳职业技术学院留仙洞校区）"
  ],
  "57": [
    "233",
    "深圳才聚-南山区（深圳职业技术学院西丽湖校区）"
  ],
  "58": [
    "17",
    "沈阳海外"
  ],
  "59": [
    "115",
    "石家庄卓越"
  ],
  "6": [
    "18",
    "大连东软"
  ],
  "60": [
    "16",
    "苏州清晖"
  ],
  "61": [
    "211",
    "太原临时"
  ],
  "62": [
    "234",
    "天津光环-河东区1"
  ],
  "63": [
    "235",
    "天津光环-河东区2"
  ],
  "64": [
    "88",
    "天津光环-南开区"
  ],
  "65": [
    "236",
    "天津威训-和平区"
  ],
  "66": [
    "11",
    "天津威训-河东区"
  ],
  "67": [
    "87",
    "潍坊时代"
  ],
  "68": [
    "10",
    "乌鲁木齐"
  ],
  "69": [
    "62",
    "无锡清晖"
  ],
  "7": [
    "84",
    "大连立智"
  ],
  "70": [
    "19",
    "武汉爱迪泰"
  ],
  "71": [
    "90",
    "武汉卓越"
  ],
  "72": [
    "108",
    "西安卓越-长安区"
  ],
  "73": [
    "12",
    "厦门培因"
  ],
  "74": [
    "31",
    "郑州杰创-惠济区"
  ],
  "75": [
    "25",
    "重庆巨龙"
  ],
  "76": [
    "29",
    "珠海才聚"
  ],
  "77": [
    "85",
    "淄博卓越"
  ],
  "8": [
    "28",
    "东莞才聚"
  ],
  "9": [
    "201",
    "佛山亚加达临时"
  ]
}


def login():
  url = "http://exam.chinapmp.cn/App_Ajax/SHOW.Ajax.Exam.Login,SHOW.Ajax.ajax?domain=exam"

  payload = '{"JSON_DATA":[{"Name":"uType","Value":0},{"Name":"uName","Value":"%s"},{"Name":"uPass","Value":"%s"}]}' % (pmi.JJH_USER, pmi.JJH_PWD)
  
  print(payload)

  headers = {
    'Connection' : 'keep-alive',
    'X-UNEXT.Ajax-Token' : '47aa4897.18DBCDFCAF648045F5A783F4865C493E',
    'X-UNEXT.Ajax-Method' : 'Save',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type' : 'text/plain; charset=UTF-8',
    'Accept' : '*/*',
    'Origin' : 'http://exam.chinapmp.cn',
    'Referer' : 'http://exam.chinapmp.cn/',
    'Accept-Language' : 'zh-CN,zh;q=0.9' 
  }

  try:
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
      cookies = requests.utils.dict_from_cookiejar(response.cookies)
      return cookies
    print(response.status_code, response.text)
    return None
  except:
    return None

def str_time_2_long_stamp(stime:str): # example 2020-11-11
  _t = stime.split('-')
  y = int(_t[0])
  m = int(_t[1])
  d = int(_t[2])
  return str(int(datetime(y, m, d, 0, 0, 0).timestamp()) * 1000)

def sign(cookies):
  url = 'http://user.chinapmp.cn/App_Ajax/SHOW.Ajax.User.Examsign,SHOW.Ajax.ajax?doing=info&domain=user'
  _ksdd = pmi.PMI_KSDD_ID[random.randint(0, len(pmi.PMI_KSDD_ID)-1)]
  payload = '{"JSON_DATA":[{"Name":"Ed","Value":10000044},{"Name":"Etitle","Value":" 2021年6月20日项目管理资格认证考试"},{"Name":"Stype","Value":101},{"Name":"StypeName","Value":"项目管理师(PMP®)"},{"Name":"Xing","Value":"%s"},{"Name":"Zhong","Value":""},{"Name":"Ming","Value":"%s"},{"Name":"Peixunjigou","Value":"%s"},{"Name":"Peixunjigouming","Value":"%s"},{"Name":"PMIUname","Value":"%s"},{"Name":"PMIUpass","Value":"%s"},{"Name":"IsPMIUser","Value":false},{"Name":"PMINumber","Value":""},{"Name":"_PMIUtimeB","Value":""},{"Name":"_PMIUtimeE","Value":""},{"Name":"PMItimeB","Value":"/Date(%s+0800)/"},{"Name":"PMItimeE","Value":"/Date(%s+0800)/"},{"Name":"Kaodian","Value":"%s"},{"Name":"Kaodianming","Value":"%s"},{"Name":"PMIID","Value":"%s"}]}' % (pmi.PMI_XING, pmi.PMI_MING, PXJG[pmi.PMI_PXJG_ID][0], PXJG[pmi.PMI_PXJG_ID][1], pmi.PMI_USER, pmi.PMI_PWD, str_time_2_long_stamp(pmi.PMI_VALID_BEGIN), str_time_2_long_stamp(pmi.PMI_VALID_END), KSDD[_ksdd][0], KSDD[_ksdd][1], pmi.PMI_ID)

  print(payload)

  headers = {
    'Connection' : 'keep-alive',
    'X-UNEXT.Ajax-Token' : 'f32b5425.E855D6CDF20F4C2B331368F3062770B1',
    'X-UNEXT.Ajax-Method' : 'Sign',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type' : 'text/plain; charset=UTF-8',
    'Accept' : '*/*',
    'Origin' : 'http://user.chinapmp.cn',
    'Referer' : 'http://user.chinapmp.cn/examsign;sign.shtml',
    'Accept-Language' : 'zh-CN,zh;q=0.9'
  }

  try:
    response = requests.request("POST", url, headers = headers, data = payload.encode('utf-8'), cookies = cookies)
    if response.status_code == 200:
      print(response.text)
      if 'error' in response.text:
        if '登陆' in response.text:
          return False, 2
        else:
          return False, 1
      else:
        return True, 0
    print (response.status_code)
    return False, 0
  except:
    return False, 0

def load_params(cookies):
  url = 'http://user.chinapmp.cn/examsign;sign.shtml'
  headers = {
    'Host' : 'user.chinapmp.cn',
    'Connection' : 'keep-alive',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.9'
  }
  response = requests.request('GET', url, headers = headers, cookies = cookies)
  if response.status_code == 200:
    content = etree.HTML(response.text):
    peixunjigou = content.xpath('//*[@id="Peixunjigou"]')
    if len(peixunjigou) == 0:
      print('检查一下是否报名成功,已报名成功的话是请求不到这个网页的!!!')
      return True
    pxjgdic = dict()
    index = 0
    for _p in peixunjigou[0]:
      pxjgdic[str(index)] = (_p.values()[0], _p.text)
    kaoshididian = content.xpath('//*[@id="Kaodian"]')
    ksdddic = dict()
    index = 0
    for _p in kaoshididian[0]:
      ksdddic[str(index)] = (_p.values()[0], _p.text)

    with open('培训和考试点.txt', 'w') as fp:
      fp.write(json.dumps(pxjgdic, ensure_ascii=False))
      fp.write(json.dumps(ksdddic, ensure_ascii=False))
    return True
  else:
    return False

def _login():
  i = 1
  while True:
    print('第%s次登陆尝试.' % i)
    cookies = login()
    if cookies:
      break
    i = i+1
  print('登陆成功,开始报名')
  return cookies

def _sign(cookies):
  j = 1
  while True:
    print('第%s次报名尝试.' % j)
    b, r = sign(cookies)
    if b:
      break
    if r == 2:
      cookies = _login()
    j = j+1
  print('报名成功?请看最后输出的内容,可能登录已失效或报名点已满额,请重启程序!!!')


def run():
  cookies = _login()
  choise = input('您要干什么?\n1 报名\n2 获取培训机构和考试地点信息\n')
  if str(choise) == '2':
    load_params(cookies)
  elif str(choise) == '1':
    _sign(cookies)
  else:
    print('fxck off.')
    
if __name__ == '__main__':
  run()
