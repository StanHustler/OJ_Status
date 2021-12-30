import requests
from bs4 import BeautifulSoup


class setting:
    calendar_url = "https://contests.sdutacm.cn/contests.json"
    atcoder_rank = "https://atcoder.jp/ranking"
    wlacm_rank = "http://wlacm.com/ranklist.php"
    nowcoder_rank = "https://ac.nowcoder.com/acm/contest/rating-index"


def getHTMLText(url):
    try:
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.baidu.com/link?url=nV__VLzaxpWPJBmpmsyh_0ZOHmnauP8Qm4cDGfbb0Um3COrclHlbrr4FDfBJBzqU_bbMhuUsRpC7iqjskDMbkq&wd=&eqid=e43c8e050005decb0000000561cc5120',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "connect error"


def isChinese(str):
    for i in str:
        if i >= '\u4e00' and i <= '\u9fa5':
            return True
    return False


def getCalendar():
    ls = eval(getHTMLText(setting.calendar_url))
    return ls


def getRanking(OJ="wlacm"):
    ls = []
    if OJ == "atcoder":
        html = getHTMLText(setting.atcoder_rank)
        soup = BeautifulSoup(html, "html.parser")
        for i in range(len(soup.tbody("tr"))):
            frag = soup.tbody("tr")[i]("td")
            ls.append(
                [
                    frag[0].text,
                    frag[1]("a")[1].text,
                    frag[1]("a")[2].text,
                    frag[3].text
                ]
            )
    elif OJ == "wlacm":
        html = getHTMLText(setting.wlacm_rank)
        soup = BeautifulSoup(html, "html.parser")
        for i in range(len(soup.tbody("tr"))):
            frag = soup.tbody("tr")[i]("td")
            ls.append(
                [
                    frag[0].text.strip(),
                    frag[1].text,
                    frag[2].text,
                    frag[3].text
                ]
            )
    elif OJ=="nowcoder":
        html = getHTMLText(setting.nowcoder_rank)
        soup = BeautifulSoup(html, "html.parser")
        for i in range(len(soup.tbody("tr"))):
            frag = soup.tbody("tr")[i]("td")
            ls.append(
                [
                    frag[0].text.strip(),
                    frag[1].span.text,
                    frag[2].text.strip("\n"),
                    frag[4].text
                ]
            )

    return ls


# print(getRanking("nowcoder"))
