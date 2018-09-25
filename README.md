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
 https://github.com/url2io/url2io-python-sdk/
 - 官网注册，获取token
 http://url2io.applinzi.com/
- 使用
https://github.com/url2io/url2io-python-sdk/

### 抓取结果展示
如下图
![抓取结果](https://img-blog.csdn.net/20180925145654177?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzA5ODc4Nw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
