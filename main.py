from datetime import datetime
from pathlib import Path

# 创建 reports 目录
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)

# 当前时间
now = datetime.now()

# 生成日报内容
report_content = f"""
# IPO Radar Daily Report

生成时间：{now.strftime("%Y-%m-%d %H:%M:%S")}

## 系统状态

✅ GitHub Actions 运行成功

## 后续计划

- 港交所递表监控
- 上交所IPO审核监控
- 深交所IPO审核监控
- 证监会境外备案监控
- 医疗IPO分类
- AI IPO分类
- 半导体IPO分类
- 风险信号扫描

---

IPO Radar Pro v1.0
"""

# 保存文件
filename = REPORT_DIR / f"report_{now.strftime('%Y%m%d_%H%M%S')}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(report_content)

print("Report generated:", filename)
