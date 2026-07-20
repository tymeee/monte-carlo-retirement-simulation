import json
from google import genai
from google.genai import types
import numpy as np
import pandas as pd
from typing import Any

def make_json_safe(value: Any) -> Any:
    """Convert pandas and NumPy objects into JSON-compatible values."""

    if isinstance(value, pd.DataFrame):
        return value.to_dict(orient="records")

    if isinstance(value, pd.Series):
        return value.to_dict()

    if isinstance(value, np.ndarray):
        return value.tolist()

    if isinstance(value, np.generic):
        return value.item()

    if isinstance(value, dict):
        return {
            str(key): make_json_safe(item)
            for key, item in value.items()
        }

    if isinstance(value, (list, tuple)):
        return [
            make_json_safe(item)
            for item in value
        ]

    return value

def explain_results(api_key,model,input_data,allocation_data,results_data):
  payload = {
        "investor_inputs": make_json_safe(input_data),
        "portfolio_allocation": make_json_safe(allocation_data),
        "simulation_results": make_json_safe(results_data),
    }
  prompt = ( 
    "You are to act as a financial guide for individuals who have very little degree of finance basics. Your job is to explain to them why the results of their Monte Carlo came out the way it did. Some facts about the monte carlo, the simulation runs from the starting age till age 85(for all simulations) as that is the Thai median death age, so keep that in mind. "
    "Things you must fulfill are 3 fold: 1. What their strategy does well and how it leads to success (talk about diversification, DCA models, etc.) 2. What their strategy lacks in and why it is sometimes dangerous (too much reliance on one market, etc.)"
    "3. How much does their simulation results match them as an investor based on their input data"
    "You are to not overstep and claim things that don't make sense based on the data. Do not pull from outside information that may be baseless"
    "Try to talk less about initial capital as that varies a lot by person, instead focus a lot more on strategy, risk, and allocations. If allocations aren't present, explain why that is a risk too."
    " If we are talking about mutual funds (the allocation is specific fund names), the listed funds for the investors to choose from are as follows: KKP Cash, KKP Plus, KFAFIX-A, UGISFX-N, ES-GCORE, ES-GQG, ES-GTECH, KT-HEALTHCARE-A, SCBS&P500A, ES-EAE, KT-PRECIOUS, KKP-GNP-H, KFG-PROP-A"
    "Remember again to try to base it off their simulation results as much as possible and explain with understandable financial logic. Don't add recommendations of financial advice as this is not the point of this."
    """ Lastly,
        Write the financial analysis in clean Markdown.
        
        Formatting rules:
        - Never use LaTeX or mathematical notation.
        - Never use the $ currency symbol.
        - Write currency as "USD 2,089.00" or "THB 2,089.00".
        - Put a space between numbers and surrounding words.
        - Use Markdown bold only for headings and important values.
        - Do not place Markdown formatting inside currency values.
        """
    + json.dumps(payload)
  )
  with genai.Client(api_key=api_key) as client:
    response = client.models.generate_content(
      model = model,
      contents = prompt,
      config=types.GenerateContentConfig(temperature=0.2),
    )
  return response.text or "No Analysis was Returned." 
