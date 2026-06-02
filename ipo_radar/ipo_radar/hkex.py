import requests

def fetch_hkex_items():
    """
    港交所IPO监控（第一版测试）
    先验证系统流程是否正常
    """

    items = []

    try:
        response = requests.get(
            "https://www.hkex.com.hk",
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0 IPO-Radar"
            }
        )

        items.append({
            "source": "HKEX",
            "title": f"HKEX Website Status {response.status_code}",
            "market": "港股",
            "status": "测试连接成功",
            "url": "https://www.hkex.com.hk"
        })

    except Exception as e:
        items.append({
            "source": "HKEX",
            "title": str(e),
            "market": "港股",
            "status": "测试连接失败",
            "url": ""
        })

    return items
