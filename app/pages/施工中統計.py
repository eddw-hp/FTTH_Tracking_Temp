import streamlit as st
st.title("#8 施工中統計")

data = [
    {"area": "全區", "3月": [100, 10000], "4月": [100, 10000], "5月": [100, 10000]},
    {"area": "北一", "3月": [25, 2500], "4月": [25, 2500], "5月": [25, 2500]},
    {"area": "北二", "3月": [25, 2500], "4月": [25, 2500], "5月": [25, 2500]},
    {"area": "南區", "3月": [50, 5000], "4月": [50, 5000], "5月": [50, 5000]},
]

months = ["3月", "4月", "5月"]

month_header = '<tr><th class="left-col"></th>'
for m in months:
    month_header += f'<th colspan="2" class="month">{m}</th>'
month_header += '</tr>'

sub_header = '<tr class="subhead"><th class="left-col">地區</th>'
for _ in months:
    sub_header += '<th>棟數</th><th>戶數</th>'
sub_header += '</tr>'

header_html = month_header + sub_header

rows_html = ''
for row in data:
    rows_html += f'<tr><td class="left-col">{row["area"]}</td>'
    for m in months:
        ongoing_build, ongoing_house = row[m]
        rows_html += (
            # f'<td>{ongoing_build}</td>'
            # f'<td><a href="/施工中清單">{ongoing_build}</a></td>'
            f'<td><a href="?area={row["area"]}&month={m}" target="_self">{ongoing_build}</a></td>'
            f'<td>{ongoing_house}</td>'
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

# =========================
# 讀取點擊條件
# =========================
params = st.query_params
selected_area = params.get("area")
selected_month = params.get("month")

st.divider()

# =========================
# 假明細資料
# =========================
detail_data = [
    {
        "項次": "範例1", "平台": "N2", "SO": "230", "行政區": "大安區", "大樓": "XXX", "戶數": "100",
        "升級月": "3", "完工日期": "", "完工年月": "", "執行中單位": "台北業務四部", "承辦人": "王小明",
        "進度": "8.施工中", "預計完成日期": "2026/03/30", "備註說明": "", "地區": "全區", "月份": "3月"
    },
    {
        "項次": "範例2", "平台": "S1", "SO": "710", "行政區": "中山區", "大樓": "XXX", "戶數": "222",
        "升級月": "3", "完工日期": "", "完工年月": "", "執行中單位": "高雄業務部", "承辦人": "王大明",
        "進度": "8.施工中", "預計完成日期": "2026/04/05", "備註說明": "", "地區": "北一", "月份": "3月"
    },
    {
        "項次": "範例3", "平台": "N2", "SO": "310", "行政區": "中和區", "大樓": "XXX", "戶數": "344",
        "升級月": "3", "完工日期": "", "完工年月": "", "執行中單位": "台北業務部", "承辦人": "吳大明",
        "進度": "8.施工中", "預計完成日期": "2026/04/05", "備註說明": "", "地區": "北二", "月份": "3月"
    },
    {
        "項次": "範例4", "平台": "S1", "SO": "710", "行政區": "中山區", "大樓": "XXX", "戶數": "222",
        "升級月": "5", "完工日期": "", "完工年月": "", "執行中單位": "高雄業務部", "承辦人": "王大明",
        "進度": "8.施工中", "預計完成日期": "2026/04/05", "備註說明": "", "地區": "南區", "月份": "5月"
    },
]

# =========================
# 若有點擊，顯示下方彩色明細表
# =========================
if selected_area and selected_month:
    st.subheader(f"施工中清單｜{selected_area}｜{selected_month}")

    filtered = [
        x for x in detail_data
        if x["地區"] == selected_area and x["月份"] == selected_month
    ]

    if filtered:
        detail_rows_html = ""
        for row in filtered:
            detail_rows_html += (
                f"<tr>"
                f"<td>{row['項次']}</td>"
                f"<td>{row['平台']}</td>"
                f"<td>{row['SO']}</td>"
                f"<td>{row['行政區']}</td>"
                f"<td>{row['大樓']}</td>"
                f"<td>{row['戶數']}</td>"
                f"<td>{row['升級月']}</td>"
                f"<td>{row['完工日期']}</td>"
                f"<td>{row['完工年月']}</td>"
                f"<td>{row['執行中單位']}</td>"
                f"<td>{row['承辦人']}</td>"
                f"<td>{row['進度']}</td>"
                f"<td>{row['預計完成日期']}</td>"
                f"<td>{row['備註說明']}</td>"
                f"</tr>"
            )
        detail_table_html = f"""
        <style>
        .detail-table {{
            border-collapse: collapse;
            width: 100%;
            text-align: center;
            font-size: 16px;
        }}
        .detail-table th, .detail-table td {{
            border: 1px solid black;
            padding: 6px 10px;
        }}
        .detail-table .grey {{
            min-width: 80px;
            font-weight: bold;
            color: #FFFFFF;
            background-color: #666666;
        }}
        .detail-table .red {{
            min-width: 80px;
            font-weight: bold;
            color: #FFFFFF;
            background-color: #FF0000;
        }}
        .detail-table .brown {{
            min-width: 80px;
            font-weight: bold;
            color: #FFFFFF;
            background-color: #800000;
        }}
        .detail-table .yellow {{
            min-width: 80px;
            font-weight: bold;
            color: #FF0000;
            background-color: #EEEE00;
        }}
        .detail-table .green {{
            min-width: 80px;
            font-weight: bold;
            color: #FFFFFF;
            background-color: #008866;
        }}
        </style>
        <table class="detail-table">
            <tr>
                <th class="grey">項次</th>
                <th class="grey">平台</th>
                <th class="grey">SO</th>
                <th class="grey">行政區</th>
                <th class="grey">大樓</th>
                <th class="grey">戶數</th>
                <th class="red">升級月</th>
                <th class="red">完工日期</th>
                <th class="red">完工年月</th>
                <th class="brown">執行中單位</th>
                <th class="brown">承辦人</th>
                <th class="yellow">進度</th>
                <th class="yellow">預計完成日期</th>
                <th class="green">備註說明</th>
            </tr>
            {detail_rows_html}
        </table>
        """

        st.markdown(detail_table_html, unsafe_allow_html=True)
    else:
        st.info("目前沒有符合條件的施工中清單。")
