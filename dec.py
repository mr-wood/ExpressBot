#!/usr/bin/python
# coding:utf-8


PROVIDER = {
    "shentong": u"申通快递",
    "ems": u"EMS",
    "shunfeng": u"顺丰速运",
    "yunda": u"韵达快递",
    "yuantong": u"圆通速递",
    "zhongtong": u"中通快递",
    "huitongkuaidi": u"百世快递",
    "tiantian": u"天天快递",
    "zhaijisong": u"宅急送",
    "xinhongyukuaidi": u"鑫飞鸿",
    "cces": u"CCES/国通快递",
    "quanyikuaidi": u"全一快递",
    "biaojikuaidi": u"彪记快递",
    "xingchengjibian": u"星晨急便",
    "yafengsudi": u"亚风速递",
    "yuanweifeng": u"源伟丰",
    "quanritongkuaidi": u"全日通",
    "anxindakuaixi": u"安信达",
    "minghangkuaidi": u"民航快递",
    "fenghuangkuaidi": u"凤凰快递",
    "jinguangsudikuaijian": u"京广速递",
    "peisihuoyunkuaidi": u"配思货运",
    "ztky": u"中铁物流",
    "ups": u"UPS",
    "fedex": u"FedEx-国际件",
    "dhl": u"DHL-中国件",
    "aae": u"AAE-中国件",
    "datianwuliu": u"大田物流",
    "debangwuliu": u"德邦物流",
    "xinbangwuliu": u"新邦物流",
    "longbanwuliu": u"龙邦速递",
    "yibangwuliu": u"一邦速递",
    "suer": u"速尔快递",
    "lianhaowuliu": u"联昊通",
    "guangdongyouzhengwuliu": u"广东邮政",
    "zhongyouwuliu": u"中邮物流",
    "tiandihuayu": u"天地华宇",
    "shenghuiwuliu": u"盛辉物流",
    "changyuwuliu": u"长宇物流",
    "feikangda": u"飞康达",
    "yuanzhijiecheng": u"元智捷诚",
    "youzhengguonei": u"邮政包裹/平邮",
    "youzhengguoji": u"国际包裹",
    "wanjiawuliu": u"万家物流",
    "yuanchengwuliu": u"远成物流",
    "xinfengwuliu": u"信丰物流",
    "wenjiesudi": u"文捷航空",
    "quanchenkuaidi": u"全晨快递",
    "jiayiwuliu": u"佳怡物流",
    "youshuwuliu": u"优速物流",
    "kuaijiesudi": u"快捷速递",
    "dsukuaidi": u"D速快递",
    "quanjitong": u"全际通",
    "ganzhongnengda": u"能达速递",
    "anjiekuaidi": u"青岛安捷快递",
    "yuefengwuliu": u"越丰物流",
    "dpex": u"DPEX",
    "jixianda": u"急先达",
    "baifudongfang": u"百福东方",
    "bht": u"BHT",
    "wuyuansudi": u"伍圆速递",
    "lanbiaokuaidi": u"蓝镖快递",
    "coe": u"COE",
    "nanjing": u"南京100",
    "hengluwuliu": u"恒路物流",
    "jindawuliu": u"金大物流",
    "huaxialongwuliu": u"华夏龙",
    "yuntongkuaidi": u"运通中港",
    "jiajiwuliu": u"佳吉快运",
    "shengfengwuliu": u"盛丰物流",
    "yuananda": u"源安达",
    "jiayunmeiwuliu": u"加运美",
    "wanxiangwuliu": u"万象物流",
    "hongpinwuliu": u"宏品物流",
    "gls": u"GLS",
    "shangda": u"上大物流",
    "zhongtiewuliu": u"中铁快运",
    "yuanfeihangwuliu": u"原飞航",
    "haiwaihuanqiu": u"海外环球",
    "santaisudi": u"三态速递",
    "jinyuekuaidi": u"晋越快递",
    "lianbangkuaidi": u"联邦快递",
    "feikuaida": u"飞快达",
    "quanfengkuaidi": u"全峰快递",
    "rufengda": u"如风达",
    "lejiedi": u"乐捷递",
    "zhongxinda": u"忠信达",
    "zhimakaimen": u"芝麻开门",
    "saiaodi": u"赛澳递",
    "haihongwangsong": u"海红网送",
    "gongsuda": u"共速达",
    "jialidatong": u"嘉里大通",
    "ocs": u"OCS",
    "usps": u"USPS",
    "meiguokuaidi": u"美国快递",
    "lijisong": u"成都立即送",
    "yinjiesudi": u"银捷速递",
    "menduimen": u"门对门",
    "disifang": u"递四方",
    "zhengzhoujianhua": u"郑州建华",
    "hebeijianhua": u"河北建华",
    "weitepai": u"微特派",
    "dhlde": u"DHL-德国件（DHL Deutschland）",
    "tonghetianxia": u"通和天下",
    "emsguoji": u"EMS-国际件",
    "fedexus": u"FedEx-美国件",
    "fengxingtianxia": u"风行天下",
    "kangliwuliu": u"康力物流",
    "kuayue": u"跨越速运",
    "haimengsudi": u"海盟速递",
    "shenganwuliu": u"圣安物流",
    "yitongfeihong": u"一统飞鸿",
    "zhongsukuaidi": u"中速快递",
    "neweggozzo": u"新蛋奥硕",
    "ontrac": u"OnTrac",
    "sevendays": u"七天连锁",
    "mingliangwuliu": u"明亮物流",
    "vancl": u"凡客配送（作废）",
    "huaqikuaiyun": u"华企快运",
    "city100": u"城市100",
    "sxhongmajia": u"红马甲物流",
    "suijiawuliu": u"穗佳物流",
    "feibaokuaidi": u"飞豹快递",
    "chuanxiwuliu": u"传喜物流",
    "jietekuaidi": u"捷特快递",
    "longlangkuaidi": u"隆浪快递",
    "emsen": u"EMS-英文",
    "zhongtianwanyun": u"中天万运",
    "hkpost": u"香港(HongKong Post)",
    "bangsongwuliu": u"邦送物流",
    "guotongkuaidi": u"国通快递",
    "auspost": u"澳大利亚(Australia Post)",
    "canpost": u"加拿大(Canada Post)",
    "canpostfr": u"加拿大邮政",
    "upsen": u"UPS-全球件",
    "tnten": u"TNT-全球件",
    "dhlen": u"DHL-全球件",
    "shunfengen": u"顺丰-美国件",
    "huiqiangkuaidi": u"汇强快递",
    "xiyoutekuaidi": u"希优特",
    "haoshengwuliu": u"昊盛物流",
    "shangcheng": u"尚橙物流",
    "yilingsuyun": u"亿领速运",
    "dayangwuliu": u"大洋物流",
    "didasuyun": u"递达速运",
    "yitongda": u"易通达",
    "youbijia": u"邮必佳",
    "yishunhang": u"亿顺航",
    "feihukuaidi": u"飞狐快递",
    "xiaoxiangchenbao": u"潇湘晨报",
    "balunzhi": u"巴伦支",
    "aramex": u"Aramex",
    "minshengkuaidi": u"闽盛快递",
    "syjiahuier": u"佳惠尔",
    "minbangsudi": u"民邦速递",
    "shanghaikuaitong": u"上海快通",
    "xiaohongmao": u"北青小红帽",
    "gsm": u"GSM",
    "annengwuliu": u"安能物流",
    "kcs": u"KCS",
    "citylink": u"City-Link",
    "diantongkuaidi": u"店通快递",
    "fanyukuaidi": u"凡宇快递",
    "pingandatengfei": u"平安达腾飞",
    "guangdongtonglu": u"广东通路",
    "zhongruisudi": u"中睿速递",
    "kuaidawuliu": u"快达物流",
    "jiajikuaidi": u"佳吉快递",
    "adp": u"ADP国际快递",
    "fardarww": u"颿达国际快递",
    "fandaguoji": u"颿达国际快递-英文",
    "shlindao": u"林道国际快递",
    "sinoex": u"中外运速递-中文",
    "zhongwaiyun": u"中外运速递",
    "dechuangwuliu": u"深圳德创物流",
    "ldxpres": u"林道国际快递-英文",
    "ruidianyouzheng": u"瑞典（Sweden Post）",
    "postenab": u"PostNord(Posten AB)",
    "nuoyaao": u"偌亚奥国际快递",
    "chengjisudi": u"城际速递",
    "xianglongyuntong": u"祥龙运通物流",
    "pinsuxinda": u"品速心达快递",
    "yuxinwuliu": u"宇鑫物流",
    "peixingwuliu": u"陪行物流",
    "hutongwuliu": u"户通物流",
    "xianchengliansudi": u"西安城联速递",
    "yujiawuliu": u"煜嘉物流",
    "yiqiguojiwuliu": u"一柒国际物流",
    "fedexcn": u"Fedex-国际件-中文",
    "lianbangkuaidien": u"联邦快递-英文",
    "zhongtongphone": u"中通（带电话）",
    "saiaodimmb": u"赛澳递for买卖宝",
    "shanghaiwujiangmmb": u"上海无疆for买卖宝",
    "singpost": u"新加坡小包(Singapore Post)",
    "yinsu": u"音素快运",
    "ndwl": u"南方传媒物流",
    "sucheng": u"速呈宅配",
    "chuangyi": u"创一快递",
    "dianyi": u"云南滇驿物流",
    "cqxingcheng": u"重庆星程快递",
    "scxingcheng": u"四川星程快递",
    "gzxingcheng": u"贵州星程快递",
    "ytkd": u"运通中港快递(作废)",
    "gatien": u"Gati-英文",
    "gaticn": u"Gati-中文",
    "jcex": u"jcex",
    "peex": u"派尔快递",
    "kxda": u"凯信达",
    "advancing": u"安达信",
    "huiwen": u"汇文",
    "yxexpress": u"亿翔",
    "donghong": u"东红物流",
    "feiyuanvipshop": u"飞远配送",
    "hlyex": u"好运来",
    "dpexen": u"Toll",
    "zengyisudi": u"增益速递",
    "kuaiyouda": u"四川快优达速递",
    "riyuwuliu": u"日昱物流",
    "sutongwuliu": u"速通物流",
    "nanjingshengbang": u"晟邦物流",
    "anposten": u"爱尔兰(An Post)",
    "japanposten": u"日本（Japan Post）",
    "postdanmarken": u"丹麦(Post Denmark)",
    "brazilposten": u"巴西(Brazil Post/Correios)",
    "postnlcn": u"荷兰挂号信(PostNL international registered mail)",
    "postnl": u"荷兰挂号信(PostNL international registered mail)",
    "emsukrainecn": u"乌克兰EMS-中文(EMS Ukraine)",
    "emsukraine": u"乌克兰EMS(EMS Ukraine)",
    "ukrpostcn": u"乌克兰邮政包裹",
    "ukrpost": u"乌克兰小包、大包(UkrPost)",
    "haihongmmb": u"海红for买卖宝",
    "fedexuk": u"FedEx-英国件（FedEx UK)",
    "fedexukcn": u"FedEx-英国件",
    "dingdong": u"叮咚快递",
    "dpd": u"DPD",
    "upsfreight": u"UPS Freight",
    "abf": u"ABF",
    "purolator": u"Purolator",
    "bpost": u"比利时（Bpost）",
    "bpostinter": u"比利时国际(Bpost international)",
    "lasership": u"LaserShip",
    "parcelforce": u"英国大包、EMS（Parcel Force）",
    "parcelforcecn": u"英国邮政大包EMS",
    "yodel": u"YODEL",
    "dhlnetherlands": u"DHL-荷兰（DHL Netherlands）",
    "myhermes": u"MyHermes",
    "dpdgermany": u"DPD Germany",
    "fastway": u"Fastway Ireland",
    "chronopostfra": u"法国大包、EMS-法文（Chronopost France）",
    "selektvracht": u"Selektvracht",
    "lanhukuaidi": u"蓝弧快递",
    "belgiumpost": u"比利时(Belgium Post)",
    "upsmailinno": u"UPS Mail Innovations",
    "postennorge": u"挪威（Posten Norge）",
    "swisspostcn": u"瑞士邮政",
    "swisspost": u"瑞士(Swiss Post)",
    "royalmailcn": u"英国邮政小包",
    "royalmail": u"英国小包（Royal Mail）",
    "dhlbenelux": u"DHL Benelux",
    "novaposhta": u"Nova Poshta",
    "dhlpoland": u"DHL-波兰（DHL Poland）",
    "estes": u"Estes",
    "tntuk": u"TNT UK",
    "deltec": u"Deltec Courier",
    "opek": u"OPEK",
    "dpdpoland": u"DPD Poland",
    "italysad": u"Italy SDA",
    "mrw": u"MRW",
    "chronopostport": u"Chronopost Portugal",
    "correosdees": u"西班牙(Correos de Espa?a)",
    "directlink": u"Direct Link",
    "eltahell": u"ELTA Hellenic Post",
    "ceskaposta": u"捷克（?eská po?ta）",
    "siodemka": u"Siodemka",
    "seur": u"International Seur",
    "jiuyicn": u"久易快递",
    "hrvatska": u"克罗地亚（Hrvatska Posta）",
    "bulgarian": u"保加利亚（Bulgarian Posts）",
    "portugalseur": u"Portugal Seur",
    "ecfirstclass": u"EC-Firstclass",
    "dtdcindia": u"DTDC India",
    "safexpress": u"Safexpress",
    "koreapost": u"韩国（Korea Post）",
    "tntau": u"TNT Australia",
    "thailand": u"泰国（Thailand Thai Post）",
    "skynetmalaysia": u"SkyNet Malaysia",
    "malaysiapost": u"马来西亚小包（Malaysia Post(Registered)）",
    "malaysiaems": u"马来西亚大包、EMS（Malaysia Post(parcel,EMS)",
    "jd": u"京东",
    "saudipost": u"沙特阿拉伯(Saudi Post)",
    "southafrican": u"南非（South African Post Office）",
    "ocaargen": u"OCA Argentina",
    "nigerianpost": u"尼日利亚(Nigerian Postal)",
    "chile": u"智利(Correos Chile)",
    "israelpost": u"以色列(Israel Post)",
    "tollpriority": u"Toll Priority(Toll Online)",
    "estafeta": u"Estafeta",
    "gdkd": u"港快速递",
    "mexico": u"墨西哥（Correos de Mexico）",
    "romanian": u"罗马尼亚（Posta Romanian）",
    "tntitaly": u"TNT Italy",
    "multipack": u"Mexico Multipack",
    "portugalctt": u"葡萄牙（Portugal CTT）",
    "interlink": u"Interlink Express",
    "dpduk": u"DPD UK",
    "hzpl": u"华航快递",
    "gatikwe": u"Gati-KWE",
    "redexpress": u"Red Express",
    "mexicodenda": u"Mexico Senda Express",
    "tcixps": u"TCI XPS",
    "hre": u"高铁速递",
    "speedpost": u"新加坡EMS、大包(Singapore Speedpost)",
    "emsinten": u"EMS-国际件-英文",
    "asendiausa": u"Asendia USA",
    "chronopostfren": u"法国大包、EMS-英文(Chronopost France)",
    "italiane": u"意大利(Poste Italiane)",
    "gda": u"冠达快递",
    "chukou1": u"出口易",
    "huangmajia": u"黄马甲",
    "anlexpress": u"新干线快递",
    "shipgce": u"飞洋快递",
    "xlobo": u"贝海国际速递",
    "emirates": u"阿联酋(Emirates Post)",
    "nsf": u"新顺丰（NSF）",
    "pakistan": u"巴基斯坦(Pakistan Post)",
    "shiyunkuaidi": u"世运快递",
    "ucs": u"合众速递(UCS）",
    "afghan": u"阿富汗(Afghan Post)",
    "belpost": u"白俄罗斯(Belpochta)",
    "quantwl": u"全通快运",
    "zhaijibian": u"宅急便",
    "efs": u"EFS Post",
    "tntpostcn": u"TNT Post",
    "gml": u"英脉物流",
    "gtongsudi": u"广通速递",
    "donghanwl": u"东瀚物流",
    "rpx": u"rpx",
    "rrs": u"日日顺物流",
    "yamato": u"黑猫雅玛多",
    "htongexpress": u"华通快运",
    "kyrgyzpost": u"吉尔吉斯斯坦(Kyrgyz Post)",
    "latvia": u"拉脱维亚(Latvijas Pasts)",
    "libanpost": u"黎巴嫩(Liban Post)",
    "lithuania": u"立陶宛（Lietuvos pa?tas）",
    "maldives": u"马尔代夫(Maldives Post)",
    "malta": u"马耳他（Malta Post）",
    "macedonia": u"马其顿(Macedonian Post)",
    "newzealand": u"新西兰（New Zealand Post）",
    "moldova": u"摩尔多瓦(Posta Moldovei)",
    "bangladesh": u"孟加拉国(EMS)",
    "serbia": u"塞尔维亚(PE Post of Serbia)",
    "cypruspost": u"塞浦路斯(Cyprus Post)",
    "tunisia": u"突尼斯EMS(Rapid-Poste)",
    "uzbekistan": u"乌兹别克斯坦(Post of Uzbekistan)",
    "caledonia": u"新喀里多尼亚[法国](New Caledonia)",
    "republic": u"叙利亚(Syrian Post)",
    "haypost": u"亚美尼亚(Haypost-Armenian Postal)",
    "yemen": u"也门(Yemen Post)",
    "india": u"印度(India Post)",
    "england": u"英国(大包,EMS)",
    "jordan": u"约旦(Jordan Post)",
    "vietnam": u"越南小包(Vietnam Posts)",
    "montenegro": u"黑山(Po?ta Crne Gore)",
    "correos": u"哥斯达黎加(Correos de Costa Rica)",
    "xilaikd": u"西安喜来快递",
    "greenland": u"格陵兰[丹麦]（TELE Greenland A/S）",
    "phlpost": u"菲律宾（Philippine Postal）",
    "ecuador": u"厄瓜多尔(Correos del Ecuador)",
    "iceland": u"冰岛(Iceland Post)",
    "emonitoring": u"波兰小包(Poczta Polska)",
    "albania": u"阿尔巴尼亚(Posta shqipatre)",
    "aruba": u"阿鲁巴[荷兰]（Post Aruba）",
    "egypt": u"埃及（Egypt Post）",
    "ireland": u"爱尔兰(An Post)",
    "omniva": u"爱沙尼亚(Eesti Post)",
    "leopard": u"云豹国际货运",
    "sinoairinex": u"中外运空运",
    "hyk": u"上海昊宏国际货物",
    "ckeex": u"城晓国际快递",
    "hungary": u"匈牙利（Magyar Posta）",
    "macao": u"澳门(Macau Post)",
    "postserv": u"台湾（中华邮政）",
    "bjemstckj": u"北京EMS",
    "kuaitao": u"快淘快递",
    "peru": u"秘鲁(SERPOST)",
    "indonesia": u"印度尼西亚EMS(Pos Indonesia-EMS)",
    "kazpost": u"哈萨克斯坦(Kazpost)",
    "lbbk": u"立白宝凯物流",
    "bqcwl": u"百千诚物流",
    "pfcexpress": u"皇家物流",
    "csuivi": u"法国(La Poste)",
    "austria": u"奥地利(Austrian Post)",
    "ukraine": u"乌克兰小包、大包(UkrPoshta)",
    "uganda": u"乌干达(Posta Uganda)",
    "azerbaijan": u"阿塞拜疆EMS(EMS AzerExpressPost)",
    "finland": u"芬兰(Itella Posti Oy)",
    "slovak": u"斯洛伐克(Slovenská Posta)",
    "ethiopia": u"埃塞俄比亚(Ethiopian postal)",
    "luxembourg": u"卢森堡(Luxembourg Post)",
    "mauritius": u"毛里求斯(Mauritius Post)",
    "brunei": u"文莱(Brunei Postal)",
    "quantium": u"Quantium",
    "tanzania": u"坦桑尼亚(Tanzania Posts)",
    "oman": u"阿曼(Oman Post)",
    "gibraltar": u"直布罗陀[英国]( Royal Gibraltar Post)",
    "byht": u"博源恒通",
    "vnpost": u"越南EMS(VNPost Express)",
    "anxl": u"安迅物流",
    "dfpost": u"达方物流",
    "huoban": u"兰州伙伴物流",
    "tianzong": u"天纵物流",
    "bohei": u"波黑(JP BH Posta)",
    "bolivia": u"玻利维亚",
    "cambodia": u"柬埔寨(Cambodia Post)",
    "bahrain": u"巴林(Bahrain Post)",
    "namibia": u"纳米比亚(NamPost)",
    "rwanda": u"卢旺达(Rwanda i-posita)",
    "lesotho": u"莱索托(Lesotho Post)",
    "kenya": u"肯尼亚(POSTA KENYA)",
    "cameroon": u"喀麦隆(CAMPOST)",
    "belize": u"伯利兹(Belize Postal)",
    "paraguay": u"巴拉圭(Correo Paraguayo)",
    "sfift": u"十方通物流",
    "hnfy": u"飞鹰物流",
    "iparcel": u"UPS i-parcel",
    "bjxsrd": u"鑫锐达",
    "mailikuaidi": u"麦力快递",
    "rfsd": u"瑞丰速递",
    "letseml": u"美联快递",
    "cnpex": u"CNPEX中邮快递",
    "xsrd": u"鑫世锐达",
    "chinatzx": u"同舟行物流",
    "qbexpress": u"秦邦快运",
    "idada": u"大达物流",
    "skynet": u"skynet",
    "nedahm": u"红马速递",
    "czwlyn": u"云南中诚",
    "wanboex": u"万博快递",
    "nntengda": u"腾达速递",
    "sujievip": u"郑州速捷",
    "gotoubi": u"UBI Australia",
    "ecmsglobal": u"ECMS Express",
    "fastgo": u"速派快递(FastGo)",
    "ecmscn": u"易客满",
    "eshunda": u"俄顺达",
    "suteng": u"广东速腾物流",
    "gdxp": u"新鹏快递",
    "yundaexus": u"美国云达",
    "toll": u"Toll",
    "szdpex": u"深圳DPEX",
    "baishiwuliu": u"百世物流",
    "postnlpacle": u"荷兰包裹(PostNL International Parcels)",
    "ltexp": u"乐天速递",
    "ztong": u"智通物流",
    "xtb": u"鑫通宝物流",
    "airpak": u"airpak expresss",
    "postnlchina": u"荷兰邮政-中国件",
    "colissimo": u"法国小包（colissimo）",
    "pcaexpress": u"PCA Express",
    "hanrun": u"韩润",
    "tnt": u"TNT",
    "cosco": u"中远e环球",
    "sundarexpress": u"顺达快递",
    "ajexpress": u"捷记方舟",
    "arkexpress": u"方舟速递",
    "adaexpress": u"明大快递",
    "changjiang": u"长江国际速递",
    "bdatong": u"八达通",
    "stoexpress": u"美国申通",
    "epanex": u"泛捷国际速递",
    "shunjiefengda": u"顺捷丰达",
    "nmhuahe": u"华赫物流",
    "deutschepost": u"德国(Deutsche Post)",
    "baitengwuliu": u"百腾物流",
    "pjbest": u"品骏快递",
    "quansutong": u"全速通",
    "zhongjiwuliu": u"中技物流",
    "jiuyescm": u"九曳供应链",
    "tykd": u"天翼快递",
    "dabei": u"德意思",
    "chengji": u"城际快递",
    "chengguangkuaidi": u"程光快递",
    "sagawa": u"佐川急便",
    "lantiankuaidi": u"蓝天快递",
    "yongchangwuliu": u"永昌物流",
    "birdex": u"笨鸟海淘",
    "yizhengdasuyun": u"一正达速运",
    "jdorder": u"京东订单",
    "sdyoupei": u"优配速运",
    "trakpak": u"TRAKPAK",
    "gts": u"GTS快递",
    "aolau": u"AOL澳通速递",
    "yiex": u"宜送物流",
    "tongdaxing": u"通达兴物流",
    "hkposten": u"香港(HongKong Post)英文",
    "suningorder": u"苏宁订单",
    "flysman": u"飞力士物流",
    "zhuanyunsifang": u"转运四方",
    "ilogen": u"logen路坚",
    "dongjun": u"成都东骏物流",
    "japanpost": u"日本郵便",
    "jiajiatong56": u"佳家通货运",
    "jrypex": u"吉日优派",
    "xaetc": u"西安胜峰",
    "doortodoor": u"CJ物流",
    "xintianjie": u"信天捷快递",
    "sd138": u"泰国138国际物流",
    "hjs": u"猴急送",
    "quanxintong": u"全信通快递",
    "amusorder": u"amazon-国际订单",
    "junfengguoji": u"骏丰国际速递",
    "kingfreight": u"货运皇",
    "ycexpress": u"远成快运",
    "subida": u"速必达",
    "sucmj": u"特急便物流",
    "yamaxunwuliu": u"亚马逊中国",
    "jinchengwuliu": u"锦程物流",
    "jgwl": u"景光物流",
    "yufeng": u"御风速运",
    "zhichengtongda": u"至诚通达快递",
    "rytsd": u"日益通速递",
    "hangyu": u"航宇快递",
    "pzhjst": u"急顺通",
    "yousutongda": u"优速通达",
    "qinyuan": u"秦远物流",
    "auexpress": u"澳邮中国快运",
    "zhdwl": u"众辉达物流",
    "fbkd": u"飞邦快递",
    "huada": u"华达快运",
    "fox": u"FOX国际快递",
    "huanqiu": u"环球速运",
    "huilian": u"辉联物流",
    "a2u": u"A2U速递",
    "ueq": u"UEQ快递",
    "scic": u"中加国际快递",
    "yidatong": u"易达通",
    "yisong": u"宜送",
    "ruexp": u"捷网俄全通",
    "htwd": u"华通务达物流",
    "speedoex": u"申必达",
    "lianyun": u"联运快递",
    "jieanda": u"捷安达",
    "shlexp": u"SHL畅灵国际物流",
    "ewe": u"EWE全球快递",
    "abcglobal": u"全球快运",
    "mangguo": u"芒果速递",
    "goldhaitao": u"金海淘",
    "jiguang": u"极光转运",
    "ftd": u"富腾达国际货运",
    "dcs": u"DCS",
    "chengda": u"成达国际速递",
    "zhonghuan": u"中环快递",
    "shunbang": u"顺邦国际物流",
    "qichen": u"启辰国际速递",
    "auex": u"澳货通",
    "aosu": u"澳速物流",
    "aus": u"澳世速递",
    "dangdang": u"当当",
    "tianma": u"天马迅达",
    "mjexp": u"美龙快递",
    "vipshop": u"唯品会(vip)",
    "chunfai": u"香港骏辉物流",
    "zenzen": u"三三国际物流",
    "mxe56": u"淼信快递",
    "hipito": u"海派通",
    "gome": u"国美",
    "pengcheng": u"鹏程快递",
    "guanting": u"冠庭国际物流",
    "yhdshop": u"1号店",
    "jinan": u"金岸物流",
    "haidaibao": u"海带宝",
    "cllexpress": u"澳通华人物流",
    "banma": u"斑马物流",
    "youjia": u"友家速递",
    "buytong": u"百通物流",
    "xingyuankuaidi": u"新元快递",
    "amcnorder": u"amazon-国内订单",
    "quansu": u"全速物流",
    "sunjex": u"新杰物流",
    "lutong": u"鲁通快运",
    "xynyc": u"新元国际",
    "xiaocex": u"小C海淘",
    "airgtc": u"航空快递",
    "dindon": u"叮咚澳洲转运",
    "hqtd": u"环球通达 ",
    "xiaomi": u"小米",
    "sfbest": u"顺丰优选",
    "haoyoukuai": u"好又快物流",
    "yongwangda": u"永旺达快递",
    "mchy": u"木春货运",
    "flyway": u"程光快递",
    "qzx56": u"全之鑫物流",
    "bsht": u"百事亨通",
    "ilyang": u"ILYANG",
    "xianfeng": u"先锋快递",
    "timedg": u"万家通快递",
    "meiquick": u"美快国际物流",
    "tny": u"泰中物流",
    "valueway": u"美通",
    "sunspeedy": u"新速航",
    "bphchina": u"速方",
    "yingchao": u"英超物流",
    "correoargentino": u"阿根廷(Correo Argentina)",
    "vanuatu": u"瓦努阿图(Vanuatu Post)",
    "barbados": u"巴巴多斯(Barbados Post)",
    "samoa": u"萨摩亚(Samoa Post)",
    "fiji": u"斐济(Fiji Post)",
    "edlogistics": u"益递物流",
    "esinotrans": u"中外运",
    "kuachangwuliu": u"跨畅（直邮易）",
    "cnausu": u"中澳速递",
    "gslhkd": u"联合快递",
    "ccd": u"河南次晨达",
    "benteng": u"奔腾物流",
    "mapleexpress": u"今枫国际快运",
    "topspeedex": u"中运全速",
    "yjxlm": u"宜家行",
    "otobv": u"中欧快运",
    "jmjss": u"金马甲",
    "onehcang": u"一号仓",
    "hfwuxi": u"和丰同城",
    "wtdchina": u"威时沛运货运",
    "shunjieda": u"顺捷达",
    "qskdyxgs": u"千顺快递",
    "tlky": u"天联快运",
    "cloudexpress": u"CE易欧通国际速递",
    "speeda": u"行必达",
    "zhongtongguoji": u"中通国际",
    "xipost": u"西邮寄",
    "nle": u"NLE",
    "nlebv": u"亚欧专线",
    "stkd": u"顺通快递",
    "sinatone": u"信联通",
    "auod": u"澳德物流",
    "ahdf": u"德方物流",
    "wzhaunyun": u"微转运",
    "lntjs": u"沈阳特急送",
    "iexpress": u"iExpress",
    "bcwelt": u"BCWELT",
    "euasia": u"欧亚专线",
    "ycgky": u"远成快运"
}

STATE = {'0': 'Transporting', '1': 'Accepted', '2': 'Trouble', '3': 'Delivered', '4': 'Rejected', '5': 'Delivering',
         '6': 'Rejecting'}
