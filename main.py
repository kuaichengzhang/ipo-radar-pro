from datetime import datetime
from pathlib import Path

from ipo_radar.csrc import fetch_csrc_items

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def generate_report(items):
    now = datetime.now()
    filename = REPORT_DIR / f"report_{now.strftime('%Y%m%d_%H%M%S')}.md"

    lines = []
    lines.append("# IPO Radar Daily Report")
    lines.append("")
    lines.append(f"生成时间：{now.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## 今日监控源")
    lines.append("")
    lines.append("- 证监会境外上市备案")
    lines.append("")
    lines.append("## 抓取结果")
    lines.append("")

    if not items:
        lines.append("暂无抓取到相关IPO备案动态。")
    else:
        lines.append(f"共抓取到 {len(items)} 条相关动态。")
        lines.append("")

        for idx, item in enumerate(items, start=1):
            lines.append(f"### {idx}. {item['title']}")
            lines.append("")
            lines.append(f"- 来源：{item['source']}")
            lines.append(f"- 市场：{item['market']}")
            lines.append(f"- 状态：{item['status']}")
            lines.append(f"- 链接：{item['url']}")
            lines.append("")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("Report generated:", filename)


def main():
    print("========== IPO RADAR START ==========")

    all_items = []

    try:
        print("Fetching CSRC data...")

        csrc_items = fetch_csrc_items()

        print(f"CSRC items fetched: {len(csrc_items)}")

        all_items.extend(csrc_items)

    except Exception as e:
        print("CSRC fetch failed:")
        print(str(e))

    generate_report(all_items)

    print("Report generated.")
    print("========== IPO RADAR END ==========")


if __name__ == "__main__":
    main()
