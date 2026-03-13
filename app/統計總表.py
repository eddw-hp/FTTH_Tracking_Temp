import streamlit as st

st.set_page_config(page_title="追蹤表", layout="wide")
st.title("資料截至: 2026/03/12")

months = ["3月", "4月", "5月"]

month_header = '<tr><th class="left-col"></th>'
for m in months:
    month_header += f'<th colspan="5" class="month">{m}</th>'
month_header += '</tr>'

plan_header = '<tr><th class="left-col"></th>'
for _ in months:
    plan_header += '<th colspan="2">預計</th><th colspan="3">已完成</th>'
plan_header += '</tr>'

sub_header = '<tr class="subhead"><th class="left-col">地區</th>'
for _ in months:
    sub_header += '<th>棟數</th><th>戶數</th><th>棟數</th><th>戶數</th><th>完成率</th>'
sub_header += '</tr>'

header_html = month_header + plan_header + sub_header

data = [
    {"area": "全區", "3月": [100, 10000, 80, 8000, 80], "4月": [100, 10000, 80, 8000, 80], "5月": [100, 10000, 80, 8000, 80]},
    {"area": "北一", "3月": [25, 2500, 10, 1000, 40], "4月": [25, 2500, 10, 1000, 40], "5月": [25, 2500, 10, 1000, 40]},
    {"area": "北二", "3月": [25, 2500, 15, 1500, 60], "4月": [25, 2500, 15, 1500, 60], "5月": [25, 2500, 15, 1500, 60]},
    {"area": "南區", "3月": [50, 5000, 40, 4000, 80], "4月": [50, 5000, 40, 4000, 80], "5月": [50, 5000, 40, 4000, 80]},
]

rows_html = ''
for row in data:
    rows_html += f'<tr><td class="left-col">{row["area"]}</td>'
    for m in months:
        planned_build, planned_house, done_build, done_house, rate = row[m]
        color = 'red' if rate < 50 else 'black'
        rows_html += (
            f'<td>{planned_build}</td>'
            f'<td>{planned_house}</td>'
            f'<td>{done_build}</td>'
            f'<td>{done_house}</td>'
            f'<td style="color:{color}; font-weight:bold;">{rate}%</td>'
        )
    rows_html += '</tr>'

table_html = f"""
<style>
.report-table {{
    border-collapse: collapse;
    width: 100%;
    text-align: center;
    font-size: 18px;
}}
.report-table th, .report-table td {{
    border: 1px solid black;
    padding: 6px 10px;
}}
.report-table th {{
    background-color: #f2f2f2;
    font-weight: bold;
}}
.report-table .left-col {{
    min-width: 80px;
    font-weight: bold;
}}
.report-table .month {{
    font-size: 24px;
}}
.report-table tr.subhead th {{
    background-color: #fafafa;
}}
</style>

<table class="report-table">
{header_html}
{rows_html}
</table>
"""

st.markdown(table_html, unsafe_allow_html=True)