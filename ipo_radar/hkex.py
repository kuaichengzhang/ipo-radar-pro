import requests
from bs4 import BeautifulSoup

HKEX_URL = "https://www.hkexnews.hk/new-listings/prospectuses-and-listing-documents?sc_lang=zh-HK"


def fetch_hkex_items():
    headers = {
        "User-Agent": "Mozilla/5.0 IPO-Radar-Pro"
    }

    items = []

    try:
        response = requests.get(
            HKEX_URL,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        links = soup.find_all("a")

        for link in links:

            title = link.get_text(strip=True)

            href = link.get("href")

            if not title:
                continue

            if any(
                keyword in title
                for keyword in [
                    "申请版本",
                    "聆讯后资料集",
                    "招股章程",
                    "上市文件"
                ]
            ):
                items.append({
                    "source": "HKEX",
                    "market": "港股",
                    "status": "递表/更新",
                    "title": title,
                    "url": href
                })

        return items[:30]

    except Exception as e:

        return [{
            "source": "HKEX",
            "market": "港股",
            "status": "抓取失败",
            "title": str(e),
            "url": HKEX_URL
        }]
