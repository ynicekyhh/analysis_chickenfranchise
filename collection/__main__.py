import crawler


def proc_bbq(html):
    pass


def store_bbq(data):
    pass


if __name__ == '__main__':

    # collection
    crawler.crawling(
        url='https://www.bbq.co.kr/shop/shop_ajax.asp?page=1&pagesize=2000&gu=&si=',
        proc=proc_bbq,
        store=store_bbq)
