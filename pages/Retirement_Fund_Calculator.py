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
    Number-input-style THB field with comma formatting.

    Returns an integer, just like thb_number_input configured with integers.
    """

    if kwargs is None:
        kwargs = {}

    numeric_key = key
    display_key = f"{key}__display"
    minus_key = f"{key}__minus"
    plus_key = f"{key}__plus"

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

    # Initialize both the actual numeric value and formatted display value.
    if numeric_key not in st.session_state:
        starting_value = clamp(int(value))
        st.session_state[numeric_key] = starting_value

    if display_key not in st.session_state:
        st.session_state[display_key] = (
            f"{st.session_state[numeric_key]:,}"
        )

    st.markdown(
        f"<div class='thb-input-label'>{label}</div>",
        unsafe_allow_html=True,
    )

    if help:
        st.caption(help)

    minus_column, input_column, plus_column = st.columns(
        [1, 6, 1],
        gap="small",
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

    return int(st.session_state[numeric_key])
st.html("style.css")
st.title("Retirement Funds Calculator")
col1, col2, col3 = st.columns(3)
st.write("ประเมินค่าใช้จ่ายแต่ละประเภทต่อเดือน")
with col1:
    household = thb_number_input("ค่าใช้จ่ายเกี่ยวกับบ้าน", min_value = 0)
    bills = thb_number_input ("ค่าสาธารณูปโภค (ค่าไฟฟ้า, ค่าน้ำประปา, อื่น ๆ)" , min_value = 0)
    leisure = thb_number_input ("ค่าท่องเที่ยว/สันทนาการ", min_value = 0 )
    other = thb_number_input("ค่าใช้จ่ายอื่น ๆ", min_value = 0)
with col2:
    Food_and_dining = thb_number_input ("ค่าใช้จ่ายเกี่ยวกับอาหาร", min_value = 0 )
    clothes = thb_number_input ("ค่าเสื้อผ้า เครื่องแต่งกาย", min_value = 0 )
    travel = thb_number_input ("ค่าเดินทาง", min_value = 0 )
    donate = thb_number_input("ค่าบริจาค/ทำบูญ", min_value = 0 )
with col3:
    hospital = thb_number_input ("ค่าใช้จ่ายเกี่ยวกับสุขภาพ",min_value = 0 )
    rent = thb_number_input ("ค่าผ่อนบ้าน/ผ่อนรถ", min_value = 0)
    child = thb_number_input("ค่าเลี้ยงลูกหลาน", min_value =0 )

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
