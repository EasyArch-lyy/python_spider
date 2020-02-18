import re
import json
import requests
# 乐视网爬取评论
class LetvSpider(object):

    COMMENT_URL='http://d-api-m.le.com/card/dynamic?platform=pc&callback=jQuery191012459755195312594_1580300653189&vid=30744694&cid=2&id=10026177&pagesize=15&type=episode&isvip=0&page=2&_=1580300653190'

    HEADERS={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q = 0.9',
        'Connection': 'keep-alive',
        'Cookie': 'tj_lc = 7a0879bd1891b993c6b7d7b867dc7bfe;ssoCookieSynced = 1;ark_uuid = ck - bfdcb4c3 - f9fc - 4c28 - adf5 - ab1ed4328a9b - 0129 - 125346;tj_v2c = -30744694_2 - 1578861_2 - 67002285_1009 - 67002283_1009;tj_env = 1;language = zh - cn;sso_curr_country = CN;bd_xid = 7a0879bd1891b993c6b7d7b867dc7bfe',
        'Host': 'd-api-m.le.com',
        'Referer': 'http://www.le.com/ptv/vplay/30744694.html?ref=index_focs_1',
        'User-Agent': 'Mozilla/5.0(X11;Linux x86_64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/69.0.3497.100Safari/537.36'
    }

    def __init__(self, url):
        self.necessary_info = {}
        self.url = url
        self.get_necessary_id()
        self.get_comment()

    def get_source(self, url, headers):
        return requests.get(url, headers).content.decode()

    def get_necessary_id(self):
        source = self.get_source(self.url, self.HEADERS)
        vid = re.search('vid:(\d+)', source).group(1)
        pid = re.search('pid:(\d+)', source).group(1)
        self.necessary_info['xid'] = vid
        print("xid"+vid)
        self.necessary_info['pid'] = pid
        print("pid"+pid)
    def get_comment(self):
        url = self.COMMENT_URL.format(xid=self.necessary_info['xid'], pid=self.necessary_info['pid'])
        source = self.get_source(url, self.HEADERS)
        source_json = source[source.find('{"'):-1]
        commit_dict = json.loads(source_json)
        print(commit_dict)
        comments = commit_dict['data']
        print(comments)
        for comment in comments:
            # print(comment['user']['username'])
            # print(comment)
            print(comment['list'])


if __name__ == '__main__':
    spider = LetvSpider('http://www.le.com/ptv/vplay/30744694.html?ref=index_focs_1')