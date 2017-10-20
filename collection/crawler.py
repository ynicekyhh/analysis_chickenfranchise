from datetime import datetime
from urllib.request import Request, urlopen
import sys


def crawling(
        url='',
        encoding='utf-8',
        proc=lambda html: html,
        store=lambda p: None,
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)

        html = resp.read().decode(encoding)
        print('%s : success for request [%s]' % (datetime.now(), url))

        store(proc(html))
    except Exception as e:
        err(e)
