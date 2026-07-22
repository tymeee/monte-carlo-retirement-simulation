import streamlit as st
import html
from collections.abc import Callable
from typing import Any

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

        /* ======================================================
   MINUS AND PLUS BUTTONS
   ====================================================== */
        
        [class*="st-key-thb_input_"] .stButton {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        [class*="st-key-thb_input_"] .stButton > button {
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        
            width: 100% !important;
            min-width: 0 !important;
            height: 48px !important;
            min-height: 48px !important;
        
            margin: 0 !important;
            padding: 0 !important;
        
            border: 1px solid rgba(113, 163, 220, 0.32) !important;
            border-radius: 12px !important;
        
            /* Original darker color */
            background: #10233b !important;
            background-image: none !important;
            color: #8ebcff !important;
        
            box-shadow:
                0 5px 14px rgba(0, 0, 0, 0.16),
                inset 0 1px 0 rgba(255, 255, 255, 0.025) !important;
        
            font-size: 1.05rem !important;
            font-weight: 500 !important;
            line-height: 1 !important;
        
            transition:
                background 140ms ease,
                border-color 140ms ease,
                color 140ms ease,
                transform 100ms ease !important;
        }
        
        /* Streamlit puts the symbol inside nested div and p elements */
        [class*="st-key-thb_input_"] .stButton > button > div,
        [class*="st-key-thb_input_"] .stButton > button p,
        [class*="st-key-thb_input_"] .stButton > button span,
        [class*="st-key-thb_input_"]
        .stButton
        [data-testid="stMarkdownContainer"] {
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        
            width: 100% !important;
            height: 100% !important;
        
            margin: 0 !important;
            padding: 0 !important;
        
            line-height: 1 !important;
            color: inherit !important;
        }
        
        /* Hover */
        [class*="st-key-thb_input_"] .stButton > button:hover {
            border-color: rgba(91, 157, 255, 0.72) !important;
            background: #173253 !important;
            background-image: none !important;
            color: #ffffff !important;
        }
        
        /* Click */
        [class*="st-key-thb_input_"] .stButton > button:active {
            transform: scale(0.96) !important;
        }
        
        /* Disabled */
        [class*="st-key-thb_input_"] .stButton > button:disabled {
            border-color: rgba(113, 163, 220, 0.12) !important;
            background: rgba(16, 35, 59, 0.55) !important;
            background-image: none !important;
            color: rgba(142, 188, 255, 0.35) !important;
            opacity: 1 !important;
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
            <span class="thb-input-label{hidden_class}">{safe_label}</span>
            <span class="thb-input-badge">THB</span>
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
                dedent(
                    f"""
                    <p class="thb-input-help">
                        {html.escape(help)}
                    </p>
                    """
                    ),
                unsafe_allow_html=True,
            )

    return int(st.session_state[numeric_key])
