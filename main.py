from datetime import datetime
from pathlib import Path

from ipo_radar.csrc import fetch_csrc_items
from ipo_radar.hkex import fetch_hkex_items

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def generate_report(items):
    now = datetime.now()
    filename = REPORT_DIR / f"report_{now.strftime('%Y%m%d_%H%M%S')}.md"

    lines = [
        "# IPO Radar Daily Report",
        "",
        f"生成时间：{now.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 抓取结果",
        "",
    ]

    if not items:
        lines.append("暂无抓取到相关IPO动态。")
    else:
        lines.append(f"共抓取到 {len(items)} 条动态。")
        lines.append("")

        for idx, item in enumerate(items, start=1):
            lines.append(f"### {idx}. {item.get('title', '')}")
            lines.append("")
            lines.append(f"- 来源：{item.get('source', '')}")
            lines.append(f"- 市场：{item.get('market', '')}")
            lines.append(f"- 状态：{item.get('status', '')}")
            lines.append(f"- 链接：{item.get('url', '')}")
            lines.append("")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("Report generated:", filename)


def main():
    print("========== IPO RADAR START ==========")

    all_items = []

    try:
        print("Fetching HKEX data...")
        hkex_items = fetch_hkex_items()
        print(f"HKEX items fetched: {len(hkex_items)}")
        all_items.extend(hkex_items)
    except Exception as e:
        print("HKEX fetch failed:")
        print(str(e))

    try:
        print("Fetching CSRC data...")
        csrc_items = fetch_csrc_items()
        print(f"CSRC items fetched: {len(csrc_items)}")
        all_items.extend(csrc_items)
    except Exception as e:
        print("CSRC fetch failed:")
        print(str(e))

    generate_report(all_items)

    print("========== IPO RADAR END ==========")


if __name__ == "__main__":
    main()
