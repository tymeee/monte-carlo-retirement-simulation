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


# =========================================================
# PAGE STYLING
# =========================================================

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


# =========================================================
# SESSION STATE
# =========================================================

if "lifestyle_prompt" not in st.session_state:
    st.session_state["lifestyle_prompt"] = ""

if "lifestyle_result" not in st.session_state:
    st.session_state["lifestyle_result"] = None


def reset_investigator() -> None:
    """Clear the user's input and the previous analysis."""

    st.session_state["lifestyle_prompt"] = ""
    st.session_state["lifestyle_result"] = None


# =========================================================
# API CLIENT
# =========================================================

try:
    api_key = st.secrets["api"]
except KeyError:
    st.error(
        "The Groq API key was not found. Add it to "
        "`.streamlit/secrets.toml` as `api = \"your-key\"`."
    )
    st.stop()

client = Groq(api_key=api_key)


# =========================================================
# HERO
# =========================================================

st.html(
    """
    <section class="lifestyle-hero">
        <div class="lifestyle-eyebrow">
            BLUEBRIDGE RETIREMENT PLANNING
        </div>

        <h1 class="lifestyle-title">
            Design your retirement lifestyle
        </h1>

        <p class="lifestyle-description">
            Describe where you want to live, how frequently you want
            to travel, the type of home you prefer, and how you expect
            to spend your time. The investigator will translate that
            lifestyle into an estimated retirement budget in Thai baht.
        </p>
    </section>
    """
)

st.caption(
    "This tool provides an AI-generated planning estimate rather than "
    "a guaranteed cost forecast or personal financial advice."
)



with st.form(
    key="retirement_lifestyle_form",
    clear_on_submit=False,
):
    prompt = st.text_area(
        "Describe your desired retirement lifestyle",
        key="lifestyle_prompt",
        placeholder=(
            "Example: I want to live in a luxury condominium in central "
            "Bangkok, spend several months each year near the beach in Bali, "
            "eat at high-quality restaurants regularly, own a car, maintain "
            "private health insurance, and travel internationally every "
            "three months."
        ),
        help=(
            "Include your preferred location, housing, travel, transport, "
            "food, hobbies, healthcare, family responsibilities, and other "
            "important lifestyle choices."
        ),
    )

    button_column, reset_column = st.columns([2, 1])

    with button_column:
        submitted = st.form_submit_button(
            "Estimate lifestyle costs",
            type="primary",
            use_container_width=True,
        )

    with reset_column:
        reset_clicked = st.form_submit_button(
            "Reset",
            use_container_width=True,
            on_click=reset_investigator,
        )


if submitted:
    cleaned_prompt = prompt.strip()

    if not cleaned_prompt:
        st.warning(
            "Describe your desired retirement lifestyle before "
            "generating an estimate."
        )

    else:
        current_year = date.today().year

        system_prompt = f"""
You are a retirement lifestyle cost investigator.

Your task is to translate a person's desired retirement lifestyle into a
clear and detailed spending estimate.

The current year is {current_year}.

PRIMARY OBJECTIVE

Estimate how much the described lifestyle would cost using current purchasing
power. The main output must focus on expenses rather than long-term inflation.

CURRENCY RULES

- Express every monetary value in Thai baht.
- Use the format "THB 120,000 per month".
- Never use the dollar-sign currency symbol.
- Do not display USD, IDR, EUR, or another foreign currency.
- When an expense occurs overseas, convert and present the estimate only in THB.
- Clearly label all figures as estimates.

LANGUAGE RULES

- If any meaningful part of the user's description is written in Thai,
  respond entirely in Thai.
- Otherwise, respond entirely in English.

ESTIMATION RULES

- Interpret the lifestyle realistically rather than taking vague words
  literally without explanation.
- When the user uses terms such as "luxurious", "comfortable", or "lavish",
  state what you assume those terms mean.
- State uncertain assumptions explicitly.
- Do not invent personal facts that were not supplied.
- Do not provide investment, tax, legal, or product-purchasing advice.
- Avoid double-counting expenses between categories.
- Separate recurring monthly costs from annual, irregular, and one-time costs.
- Check that monthly and annual totals are arithmetically consistent.
- Emphasize the user's expected lifestyle rather than allowing inflation to
  dominate the analysis.
- Keep the main estimates in today's THB.
- Do not create future nominal projections unless specifically requested.

REQUIRED OUTPUT FORMAT

## Lifestyle interpreted

Summarize the lifestyle you understood from the user's description.

## Key assumptions

List the assumptions required because the user did not provide enough detail.
Include assumptions about household size, housing arrangement, travel style,
transportation, healthcare, and location when relevant.

## Detailed monthly expenses

Create a Markdown table with these columns:

| Category | What the category includes | Lower estimate | Expected estimate | Higher estimate |

Use relevant categories such as:

- Housing or rent
- Utilities and internet
- Groceries
- Dining and entertainment
- Transportation
- Domestic help or household services
- Healthcare and insurance
- Personal care and shopping
- Hobbies and memberships
- Regular travel savings
- Family support
- Miscellaneous and contingency

Only include categories that reasonably apply.

## Annual and irregular expenses

Create a separate table for costs that do not occur evenly every month, such as:

- International trips
- Accommodation while travelling
- Major medical costs
- Vehicle maintenance
- Visa or residency costs
- Home maintenance
- Technology replacement
- Special events

Show both annual totals and monthly equivalents.

## Progressive lifestyle ranges

Provide three complete spending levels:

1. **Practical baseline**
   The least expensive version that still broadly preserves the lifestyle.

2. **Expected lifestyle**
   The most realistic interpretation of what the user described.

3. **High-comfort buffer**
   A more expensive version allowing for premium choices and unexpected costs.

For each level, provide:

- Total monthly cost in THB
- Total annual cost in THB
- A one-sentence explanation of what changes between levels

## Main cost drivers

Explain the three to five categories that have the greatest effect on the
estimated budget.

## Uncertainties

Explain which missing details could materially change the result.

## Suggested simulator input

End with one clearly labeled figure:

**Suggested current annual retirement spending input: THB X,XXX,XXX**

Use the expected-lifestyle annual total for this figure.

STYLE RULES

- Use clean Markdown.
- Be detailed but easy for someone without financial knowledge to understand.
- Do not use LaTeX.
- Do not use mathematical notation unnecessarily.
- Do not describe the result as guaranteed.
Cost-control and double-counting rules:

- Do not assume the user maintains two full-time residences unless they
  explicitly say so.
- Identify one location as the primary residence.
- Treat other locations as temporary travel unless the user clearly asks
  for a second home.
- Do not count travel twice through both a monthly travel reserve and
  separate annual trip expenses.
- Do not count accommodation under both housing and travel.
- Calculate the expected annual total as:
  recurring monthly expenses multiplied by 12,
  plus annual irregular expenses.
- Verify that all totals match the listed categories.
- If the lifestyle description is ambiguous, state two scenarios rather
  than silently choosing the more expensive interpretation.
"""

        user_message = (
            "Estimate the cost of the following desired retirement "
            "lifestyle:\n\n"
            f"{cleaned_prompt}"
        )

        try:
            with st.spinner(
                "Investigating the cost of your retirement lifestyle..."
            ):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt,
                        },
                        {
                            "role": "user",
                            "content": user_message,
                        },
                    ],
                    temperature=0.2,
                )

            result = response.choices[0].message.content

            if result:
                st.session_state["lifestyle_result"] = result
            else:
                st.error(
                    "The model returned an empty response. Please try again."
                )

        except Exception as error:
            st.error(
                "The lifestyle estimate could not be generated. "
                f"Details: {error}"
            )




result = st.session_state.get("lifestyle_result")

if result:
    with st.container(key="results_card"):
        st.subheader("Estimated retirement lifestyle budget")

        # Prevent an unexpected dollar symbol from being interpreted
        # as Markdown/LaTeX.
        clean_result = result.replace("$", r"\$")

        st.markdown(clean_result)

        st.caption(
            "The estimate is based on generalized assumptions and current "
            "purchasing power. Actual retirement expenses may differ."
        )
