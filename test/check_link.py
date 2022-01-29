"""リンクにアクセスできるかを確認するスクリプト
"""

import requests
import bs4

TARGET_LINK = 'https://masatakashiwagi.github.io/mlops-practices/knowledge/'


def check_link(target_link: str) -> None:
    """URL Linkの生存を確認する

    Args:
        target_link (str): 調査するサイトのURL
    """

    res = requests.get(target_link)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # contentのclass属性を対象とする
    elems = soup.select('.content')

    href_list = []
    for i in elems[0].find_all("a"):
        if str(i).find("https") > 0:
            val_href = i.get("href")
            href_list.append(val_href)

    for i, href in enumerate(href_list):
        res_href = requests.get(href, allow_redirects=False)
        if res_href.status_code != 200:
            raise ValueError(f"status code is {res_href.status}, check the URL link.")
        else:
            print(f'href {i}, {res_href}: OK')


if __name__ == '__main__':
    check_link(TARGET_LINK)
