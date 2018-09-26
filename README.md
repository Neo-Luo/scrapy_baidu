# scrapy_baidu
百度网页搜索爬虫（查询结果列表页和详情页抓取，详情页正文提取）

----

## 爬虫设计
主要python包：requests+BeautifulSoup+jparser+url2io
其中jparser、url2io都用于网页文本正文提取，url2io准确率高，但不稳定，解析错误时则调用jparser。通过两者结合使用来提高正文提取的效果。

### jparser

 - 安装  
`pip install jparser`
- 使用  
可参考官网：https://pypi.org/project/jparser/0.0.10/


### url2io
 - 下载安装  
 即下载本项目中的url2io.py文件。  
 也可以到该其相应github主页下载最新版：https://github.com/url2io/url2io-python-sdk/
 - 官网注册，获取token  
 http://url2io.applinzi.com/
- 使用  
https://github.com/url2io/url2io-python-sdk/

### 运行
` python scrapy_baidu.py `

### 抓取结果展示
record_id,query,title,abstract,link,content    
1,消息面看贸易战进入持久战当下只能说是短暂靴子落地美公布关税豁免程序,贸易战后操作思路_烽火通信(600498)聊吧_赢家聊吧【股吧】,"贸易战既然已经开始,时间上持久战的概率较大。而当下也只能说是短暂的靴子落地,随时还有再起烽火可能,美国公布了个关税豁免程序但那只是正常程序,切勿就...",http://www.baidu.com/link?url=fJ5P3mDdJxPJPBMMaMXI66n0_l72H4Q-ouH3LrM6jwrPW3_Eknpa2LfH_fk3zh_29wqXlDRCR9--xoHr1YMLLa, 周五盘面情绪波动过激主要来源于中美贸易……短线宜做逆风的墙头草，即再跌不悲观，反弹则不能盲目乐观，操作上忌追涨杀跌。把控仓位、跟随市场热点小打小闹为好。
2,消息面看贸易战进入持久战当下只能说是短暂靴子落地美公布关税豁免程序,"保持淡定,为什么说“贸易战”并不可怕?","2018年3月26日 - 既然靴子还没有落地,就不必过于惊慌,意向在落实...周边市场的需求推动下,我认为长期看是利好消息...美商务部长:惩罚关税不会引发贸易战,最终会以谈判...",http://www.baidu.com/link?url=SJ5MEHBKnkWGAdHs_6HCZgjvx1ou6ZVDxEA64Sp_Le5gLoXcyVzn7eL0GDzn4yMi7x5HxOmiMr0jdl_EOtEet_7TGJFxSYnbTIOjdJA81Y_, 霸越英百家号03-2619:31让我们先来回顾下当下热议的贸易战的由来——媒体错误描述贸易战经过3月8日，美国总统特朗普宣布，以损害国家安全为由……另外2017年出口对于GDP的贡献度只有18.5%，即使600亿美元产品征税导致出口额全部取消，对于中国GDP的影响也只有4%*18.5%=0.74%。
