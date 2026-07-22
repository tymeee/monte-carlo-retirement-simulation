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



st.html(
    """
    <style>
    :root {
        --page-background: #050b18;
        --surface: rgba(13, 31, 55, 0.90);
        --surface-light: rgba(18, 42, 73, 0.92);
        --border: rgba(140, 180, 235, 0.18);
        --primary: #4f8cff;
        --primary-bright: #79a8ff;
        --text-main: #f1f6ff;
        --text-secondary: #a8bad4;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 12% 0%,
                rgba(38, 91, 168, 0.24),
                transparent 34%
            ),
            linear-gradient(
                145deg,
                #040914,
                #071121 48%,
                #050b18
            );

        color: var(--text-main);
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    .lifestyle-hero {
        padding: 3rem 3.2rem;
        margin-bottom: 1.5rem;

        border: 1px solid var(--border);
        border-radius: 26px;

        background:
            radial-gradient(
                circle at 90% 20%,
                rgba(56, 155, 235, 0.17),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                rgba(14, 35, 63, 0.97),
                rgba(5, 16, 32, 0.95)
            );

        box-shadow: 0 28px 70px rgba(0, 0, 0, 0.38);
    }

    .lifestyle-eyebrow {
        margin-bottom: 0.85rem;
        color: var(--primary-bright);

        font-size: 0.78rem;
        font-weight: 750;
        letter-spacing: 0.13em;
    }

    .lifestyle-title {
        max-width: 800px;
        margin: 0;

        color: var(--text-main);

        font-size: clamp(2.3rem, 5vw, 4rem);
        line-height: 1.05;
        letter-spacing: -0.045em;
    }

    .lifestyle-description {
        max-width: 760px;
        margin: 1.25rem 0 0;

        color: var(--text-secondary);

        font-size: 1.05rem;
        line-height: 1.7;
    }

    [data-testid="stForm"] {
        padding: 1.6rem 1.7rem;

        border: 1px solid var(--border);
        border-radius: 20px;

        background:
            linear-gradient(
                145deg,
                rgba(13, 31, 55, 0.88),
                rgba(7, 18, 35, 0.88)
            );

        box-shadow: 0 20px 55px rgba(0, 0, 0, 0.28);
    }

    [data-testid="stTextArea"] textarea {
        min-height: 180px;

        background: rgba(8, 23, 43, 0.95);
        color: var(--text-main);

        border: 1px solid var(--border);
        border-radius: 14px;

        font-size: 1rem;
        line-height: 1.55;
    }

    [data-testid="stTextArea"] textarea:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(79, 140, 255, 0.15);
    }

    .stButton > button,
    [data-testid="stFormSubmitButton"] > button {
        width: 100%;
        min-height: 50px;

        border: 1px solid rgba(133, 178, 255, 0.30);
        border-radius: 13px;

        font-weight: 700;
    }

    .st-key-results_card {
        margin-top: 1.5rem;
        padding: 1.8rem 2rem;

        border: 1px solid var(--border);
        border-radius: 20px;

        background:
            linear-gradient(
                145deg,
                rgba(13, 31, 55, 0.92),
                rgba(7, 18, 35, 0.90)
            );

        box-shadow: 0 22px 60px rgba(0, 0, 0, 0.32);
    }

    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.8rem;
            padding-right: 0.8rem;
        }

        .lifestyle-hero {
            padding: 2.1rem 1.5rem;
        }

        [data-testid="stForm"] {
            padding: 1.2rem;
        }
    }
    </style>
    """
)
st.title("Retirement Funds Calculator")
col1, col2, col3 = st.columns(3)
st.write("ประเมินค่าใช้จ่ายแต่ละประเภทต่อเดือน")
with col1:
    household = st.number_input("ค่าใช้จ่ายเกี่ยวกับบ้าน", min_value = 1000)
    bills = st.number_input ("ค่าสาธารณูปโภค (ค่าไฟฟ้า, ค่าน้ำประปา, อื่น ๆ)" , min_value = 1000)
    leisure = st.number_input ("ค่าท่องเที่ยว/สันทนาการ", min_value = 1000)
    other = st.number_input("ค่าใช้จ่ายอื่น ๆ", min_value = 1000)
with col2:
    Food_and_dining = st.number_input ("ค่าใช้จ่ายเกี่ยวกับอาหาร", min_value = 1000)
    clothes = st.number_input ("ค่าเสื้อผ้า เครื่องแต่งกาย", min_value = 1000)
    travel = st.number_input ("ค่าเดินทาง", min_value = 1000)
    donate = st.number_input("ค่าบริจาค/ทำบูญ", min_value = 1000)
with col3:
    hospital = st.number_input ("ค่าใช้จ่ายเกี่ยวกับสุขภาพ",min_value = 1000)
    rent = st.number_input ("ค่าผ่อนบ้าน/ผ่อนรถ", min_value = 1000)
    child = st.number_input("ค่าเลี้ยงลูกหลาน", min_value =1000)

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
