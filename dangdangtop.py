import requests,re,json

def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def parse_result(html):
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)

    items = re.findall(pattern,html)

    for item in items:
        yield{
            'rank':item[0],
            'image':item[1],
            'title':item[2],
            'recommend':item[3],
            'author':item[4],
            'times':item[5],
            'price':item[6]
        }

def write_item_to_file(item):
    print('开始写入数据 ===>'+str(item))
    with open('book.txt','a',encoding='UTF-8') as f:
        f.write(json.dumps(item,ensure_ascii=False) + '\n')
        f.close()
def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/1-'+str(page)

    html = request_dandan(url)

    items = parse_result(html)
    print(items)
    # for item in items:
    #     write_item_to_file(item)


if __name__ == "__main__":
    for i in range(1,2):
        main(i)

