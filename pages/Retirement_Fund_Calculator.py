from datetime import date
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
from collections.abc import Callable
from typing import Any

import streamlit as st


import html
from collections.abc import Callable
from typing import Any

import streamlit as st


def load_thb_input_styles() -> None:
    st.markdown(
        """
        <style>
        /* Entire custom input */
        [class*="st-key-thb_input_"] {
            margin-bottom: 1rem;
        }

        /* Label row */
        [class*="st-key-thb_input_"] .thb-input-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;

            margin-bottom: 0.42rem;
        }

        [class*="st-key-thb_input_"] .thb-input-label {
            color: #f4f8ff;

            font-size: 0.96rem;
            font-weight: 650;
            line-height: 1.35;
        }

        [class*="st-key-thb_input_"] .thb-input-label-hidden {
            visibility: hidden;
        }

        [class*="st-key-thb_input_"] .thb-input-badge {
            padding: 0.15rem 0.48rem;

            border: 1px solid rgba(111, 171, 255, 0.20);
            border-radius: 999px;

            background: rgba(61, 132, 237, 0.10);
            color: #8ebcff;

            font-size: 0.67rem;
            font-weight: 750;
            letter-spacing: 0.08em;
        }

        /* Align input and buttons */
        [class*="st-key-thb_input_"] [data-testid="stHorizontalBlock"] {
            align-items: center;
            gap: 0.42rem;
        }

        /* Remove extra widget spacing */
        [class*="st-key-thb_input_"] [data-testid="stVerticalBlock"] {
            gap: 0;
        }

        [class*="st-key-thb_input_"] .stButton {
            margin: 0;
        }

        /* Minus and plus buttons */
        [class*="st-key-thb_input_"] .stButton > button {
            width: 100%;
            min-width: 0;
            height: 48px;
            min-height: 48px;
            padding: 0;

            border: 1px solid rgba(113, 163, 220, 0.32);
            border-radius: 12px;

            background: #10233b;
            color: #8ebcff;

            box-shadow:
                0 5px 14px rgba(0, 0, 0, 0.16),
                inset 0 1px 0 rgba(255, 255, 255, 0.025);

            font-size: 1.15rem;
            font-weight: 500;

            transition:
                background 140ms ease,
                border-color 140ms ease,
                color 140ms ease,
                transform 100ms ease;
        }

        [class*="st-key-thb_input_"] .stButton > button:hover {
            border-color: rgba(91, 157, 255, 0.72);
            background: #173253;
            color: #ffffff;
        }

        [class*="st-key-thb_input_"] .stButton > button:active {
            transform: scale(0.96);
        }

        [class*="st-key-thb_input_"] .stButton > button:disabled {
            border-color: rgba(113, 163, 220, 0.10);
            background: rgba(16, 35, 59, 0.45);
            color: rgba(142, 188, 255, 0.30);
            opacity: 1;
        }

        /* Input field */
        [class*="st-key-thb_input_"] [data-testid="stTextInput"] {
            margin: 0;
        }

        [class*="st-key-thb_input_"] [data-testid="stTextInput"] > div {
            margin: 0;
        }

        [class*="st-key-thb_input_"] [data-testid="stTextInput"] input {
            height: 48px;
            padding: 0 1rem;

            border: 1px solid rgba(113, 163, 220, 0.34);
            border-radius: 12px;

            background: #10233b;
            color: #f5f8ff;

            box-shadow:
                inset 0 1px 1px rgba(0, 0, 0, 0.18),
                0 5px 14px rgba(0, 0, 0, 0.12);

            font-size: 0.98rem;
            font-weight: 600;
            font-variant-numeric: tabular-nums;
            letter-spacing: 0.01em;

            transition:
                border-color 140ms ease,
                box-shadow 140ms ease,
                background 140ms ease;
        }

        [class*="st-key-thb_input_"]
        [data-testid="stTextInput"]
        input:hover {
            border-color: rgba(113, 174, 255, 0.55);
        }

        [class*="st-key-thb_input_"]
        [data-testid="stTextInput"]
        input:focus {
            border-color: #4f91f7;
            background: #122842;

            box-shadow:
                0 0 0 3px rgba(79, 145, 247, 0.14),
                inset 0 1px 1px rgba(0, 0, 0, 0.14);

            outline: none;
        }

        [class*="st-key-thb_input_"]
        [data-testid="stTextInput"]
        input:disabled {
            color: rgba(245, 248, 255, 0.45);
            background: rgba(16, 35, 59, 0.55);
        }

        /* Help text */
        [class*="st-key-thb_input_"] .thb-input-help {
            margin: 0.38rem 0 0;

            color: #8194ad;

            font-size: 0.76rem;
            line-height: 1.4;
        }

        @media (max-width: 650px) {
            [class*="st-key-thb_input_"]
            .stButton > button {
                height: 45px;
                min-height: 45px;
            }

            [class*="st-key-thb_input_"]
            [data-testid="stTextInput"]
            input {
                height: 45px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


load_thb_input_styles()
def thb_number_input(
    label: str,
    *,
    min_value: int | None = None,
    max_value: int | None = None,
    value: int = 0,
    step: int = 1_000,
    key: str,
    help: str | None = None,
    disabled: bool = False,
    label_visibility: str = "visible",
    on_change: Callable[..., Any] | None = None,
    args: tuple[Any, ...] = (),
    kwargs: dict[str, Any] | None = None,
) -> int:
    """
    Integer input with comma formatting and number-input-style controls.
    """

    if kwargs is None:
        kwargs = {}

    numeric_key = key
    display_key = f"{key}__display"
    minus_key = f"{key}__minus"
    plus_key = f"{key}__plus"
    wrapper_key = f"thb_input_{key}"

    def clamp(number: int) -> int:
        if min_value is not None:
            number = max(number, min_value)

        if max_value is not None:
            number = min(number, max_value)

        return number

    def run_external_callback() -> None:
        if on_change is not None:
            on_change(*args, **kwargs)

    def format_display() -> None:
        raw_value = str(
            st.session_state.get(display_key, "")
        )

        cleaned_value = (
            raw_value
            .replace(",", "")
            .replace("THB", "")
            .replace("฿", "")
            .replace(" ", "")
            .strip()
        )

        try:
            number = int(float(cleaned_value))
            number = clamp(number)

        except (TypeError, ValueError):
            number = int(
                st.session_state.get(
                    numeric_key,
                    value,
                )
            )

        st.session_state[numeric_key] = number
        st.session_state[display_key] = f"{number:,}"

        run_external_callback()

    def decrease_value() -> None:
        current = int(
            st.session_state.get(
                numeric_key,
                value,
            )
        )

        updated = clamp(current - step)

        st.session_state[numeric_key] = updated
        st.session_state[display_key] = f"{updated:,}"

        run_external_callback()

    def increase_value() -> None:
        current = int(
            st.session_state.get(
                numeric_key,
                value,
            )
        )

        updated = clamp(current + step)

        st.session_state[numeric_key] = updated
        st.session_state[display_key] = f"{updated:,}"

        run_external_callback()

    # Initialize the internal numeric value.
    if numeric_key not in st.session_state:
        starting_value = clamp(int(value))
        st.session_state[numeric_key] = starting_value

    # Initialize the visible comma-formatted value.
    if display_key not in st.session_state:
        st.session_state[display_key] = (
            f"{st.session_state[numeric_key]:,}"
        )

    safe_label = html.escape(label)

    with st.container(key=wrapper_key):
        if label_visibility != "collapsed":
            hidden_class = (
                " thb-input-label-hidden"
                if label_visibility == "hidden"
                else ""
            )    
    st.markdown(
                f"""
                <div class="thb-input-header">
                    <span class="thb-input-label{hidden_class}">
                        {safe_label}
                    </span>

                    <span class="thb-input-badge">
                        THB
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )


        minus_column, input_column, plus_column = st.columns(
            [0.72, 5.8, 0.72],
            gap="small",
            vertical_alignment="center",
        )

        with minus_column:
            st.button(
                "−",
                key=minus_key,
                on_click=decrease_value,
                disabled=(
                    disabled
                    or (
                        min_value is not None
                        and st.session_state[numeric_key]
                        <= min_value
                    )
                ),
                use_container_width=True,
            )

        with input_column:
            st.text_input(
                label,
                key=display_key,
                on_change=format_display,
                disabled=disabled,
                label_visibility="collapsed",
                placeholder="0",
            )

        with plus_column:
            st.button(
                "+",
                key=plus_key,
                on_click=increase_value,
                disabled=(
                    disabled
                    or (
                        max_value is not None
                        and st.session_state[numeric_key]
                        >= max_value
                    )
                ),
                use_container_width=True,
            )

        if help:
            st.markdown(
                f"""
                <p class="thb-input-help">
                    {html.escape(help)}
                </p>
                """,
                unsafe_allow_html=True,
            )

    return int(st.session_state[numeric_key])
st.html("style.css")
st.title("Retirement Funds Calculator")
col1, col2, col3 = st.columns(3)
st.write("ประเมินค่าใช้จ่ายแต่ละประเภทต่อเดือน")
with col1:
    household = thb_number_input(label = "ค่าใช้จ่ายเกี่ยวกับบ้าน", min_value = 0, key = "household")
    bills = thb_number_input (label = "ค่าสาธารณูปโภค (ค่าไฟฟ้า, ค่าน้ำประปา, อื่น ๆ)" , min_value = 0, key = "bills")
    leisure = thb_number_input (label = "ค่าท่องเที่ยว/สันทนาการ", min_value = 0, key = "leisure")
    other = thb_number_input(label = "ค่าใช้จ่ายอื่น ๆ", min_value = 0, key = "other")
with col2:
    Food_and_dining = thb_number_input (label = "ค่าใช้จ่ายเกี่ยวกับอาหาร", min_value = 0, key = "Food_and_dining" )
    clothes = thb_number_input (label = "ค่าเสื้อผ้า เครื่องแต่งกาย", min_value = 0, key = "clothes" )
    travel = thb_number_input (label = "ค่าเดินทาง", min_value = 0, key = "travel" )
    donate = thb_number_input(label = "ค่าบริจาค/ทำบูญ", min_value = 0, key = "donate" )
with col3:
    hospital = thb_number_input (label = "ค่าใช้จ่ายเกี่ยวกับสุขภาพ",min_value = 0, key = "hospital" )
    rent = thb_number_input (label = "ค่าผ่อนบ้าน/ผ่อนรถ", min_value = 0, key = "rent")
    child = thb_number_input(label = "ค่าเลี้ยงลูกหลาน", min_value =0, key = "child" )

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
