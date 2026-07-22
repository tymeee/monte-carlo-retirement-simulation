from datetime import date

from groq import Groq
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Retirement Lifestyle Investigator",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="auto",
)

st.html("style.css")
st.title("Retirement Funds Calculator")
col1, col2, col3 = st.columns(3)
st.write("ประเมินค่าใช้จ่ายแต่ละประเภทต่อเดือน")
with col1:
    household = st.number_input("ค่าใช้จ่ายเกี่ยวกับบ้าน", min_value = 0)
    bills = st.number_input ("ค่าสาธารณูปโภค (ค่าไฟฟ้า, ค่าน้ำประปา, อื่น ๆ)" , min_value = 0)
    leisure = st.number_input ("ค่าท่องเที่ยว/สันทนาการ", min_value = 0 )
    other = st.number_input("ค่าใช้จ่ายอื่น ๆ", min_value = 0)
with col2:
    Food_and_dining = st.number_input ("ค่าใช้จ่ายเกี่ยวกับอาหาร", min_value = 0 )
    clothes = st.number_input ("ค่าเสื้อผ้า เครื่องแต่งกาย", min_value = 0 )
    travel = st.number_input ("ค่าเดินทาง", min_value = 0 )
    donate = st.number_input("ค่าบริจาค/ทำบูญ", min_value = 0 )
with col3:
    hospital = st.number_input ("ค่าใช้จ่ายเกี่ยวกับสุขภาพ",min_value = 0 )
    rent = st.number_input ("ค่าผ่อนบ้าน/ผ่อนรถ", min_value = 0)
    child = st.number_input("ค่าเลี้ยงลูกหลาน", min_value =0 )

inf_rate = st.slider(
    "Inflation Rate",
    0.0,
    0.15,
    0.02)
years = st.slider(
    "Years Until Retirement",
    0,
    100,
    15)
sum = (household + bills + leisure +other + Food_and_dining + clothes + travel + donate + hospital + rent + child) * 12
inf_sum = sum * ((1+inf_rate) **years)
c1,c2 = st.columns(2)
c1.metric("ค่าใช้จ่ายต่อปี (Nominal)", value = f"THB{sum:,}")

c2.metric("ค่าใช้จ่ายต่อปี(Inflation Adjusted)", value=f"THB{inf_sum:,.0f}") 
