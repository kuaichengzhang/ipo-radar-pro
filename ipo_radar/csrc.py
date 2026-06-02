import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

CSRC_URL = "https://www.csrc.gov.cn/csrc/c100098/common_list.shtml"

KEYWORDS = [
    "境外发行上市备案",
    "境外上市备案",
    "备案通知书",
    "补充材料",
    "许可反馈意见"
]

def fetch_csrc_items():
    headers = {
        "User-Agent": "Mozilla/5.0 IPO-Radar-Pro"
    }

    response = requests.get(CSRC_URL, headers=headers, timeout=20)
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "lxml")
    items = []

    for a in soup.find_all("a"):
        title = a.get_text(strip=True)
        href = a.get("href")

        if not title or not href:
            continue

        if any(keyword in title for keyword in KEYWORDS):
            items.append({
                "source": "证监会境外上市备案",
                "title": title,
                "url": urljoin(CSRC_URL, href),
                "market": "境外上市",
                "status": guess_status(title)
            })

    return items


def guess_status(title):
    if "备案通知书" in title:
        return "备案通过/备案通知书"
    if "补充材料" in title:
        return "补充材料要求"
    if "许可反馈" in title:
        return "反馈意见"
    return "备案动态"
