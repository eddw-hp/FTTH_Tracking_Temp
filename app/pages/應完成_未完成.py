import streamlit as st
st.title("應完成/未完成")

months = ["3月", "4月", "5月"]
district = ['全區', '北一', '北二', '南區']

col1, col2 = st.columns([1,1])

with col1:
    st.subheader("月份")
    selected_month = st.selectbox("", months)

with col2:
    st.subheader("平台")
    selected_district = st.selectbox("", district)
    
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
.report-table .grey {{
    min-width: 80px;
    font-weight: bold;
    color: #FFFFFF;
    background-color: #666666;
}}
.report-table .red {{
    min-width: 80px;
    font-weight: bold;
    color: #FFFFFF;
    background-color: #FF0000; 
}}
.report-table .brown {{
    min-width: 80px;
    font-weight: bold;
    color: #FFFFFF;
    background-color: #800000; 
}}
.report-table .yellow {{
    min-width: 80px;
    font-weight: bold;
    color: #FF0000;
    background-color: #EEEE00; 
}}
.report-table .green {{
    min-width: 80px;
    font-weight: bold;
    color: #FFFFFF;
    background-color: #008866; 
}}
</style>

<table class="report-table">
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
    <tr>
        <td>範例1</td>
        <td>N1</td>
        <td>220</td>
        <td>中山區</td>
        <td>XXX</td>
        <td>123</td>
        <td>3</td>
        <td>2026/03/28</td>
        <td>3</td>
        <td>台北業務四部</td>
        <td>王小明</td>
        <td>8.施工中</td>
        <td>2026/03/30</td>
        <td></td>
    </tr>
    <tr>
        <td>範例2</td>
        <td>S1</td>
        <td>710</td>
        <td>中山區</td>
        <td>XXX</td>
        <td>222</td>
        <td>3</td>
        <td></td>
        <td></td>
        <td>高雄業務部</td>
        <td>王大明</td>
        <td>5.待簽進線同意書</td>
        <td>2026/04/05</td>
        <td>同意書待用印</td>
    </tr>
</table>
"""

st.markdown(table_html, unsafe_allow_html=True)