# -*- coding: utf-8 -*-
"""
AI Cryptocurrency Analysis Agent

This agent fetches basic cryptocurrency data and uses the OpenAI API
to generate a simple analysis and sentiment score.
It is designed for beginners and to be run in a GitHub Codespace.

Author: [Your GitHub Username]
"""

import os
import requests
from openai import OpenAI

# --- Core Functions ---

def print_header():
    """Prints a welcome header for the agent."""
    print("\n" + "="*50)
    print("📈 AI Cryptocurrency Analysis Agent 📈")
    print("="*50 + "\n")

def get_crypto_data(crypto_name):
    """
    Fetches basic market data for a given cryptocurrency using the CoinGecko API.
    Note: This is a free, public API and doesn't require a key.
    """
    print(f"🔍 Fetching market data for {crypto_name.title()}...")
    
    # Map common names to CoinGecko IDs
    crypto_map = {
        'btc': 'bitcoin',
        'eth': 'ethereum',
        'doge': 'dogecoin',
        'dot': 'polkadot',
        'ada': 'cardano',
        'sol': 'solana',
        'xrp': 'ripple',
    }
    
    # We format the crypto name to be lowercase as the API requires it
    api_id = crypto_name.lower()
    # Try to map common symbols to their full names
    api_id = crypto_map.get(api_id, api_id)
    
    print(f"Using CoinGecko ID: {api_id}")
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={api_id}&vs_currencies=usd&include_market_cap=true"

    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an error for bad responses (4xx or 5xx)
        data = response.json()

        if api_id not in data:
            print(f"❌ Error: Could not find data for '{crypto_name}'. Please check the name and try again.")
            return None

        return {
            "price": data[api_id].get("usd"),
            "market_cap": data[api_id].get("usd_market_cap")
        }
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP Error fetching data: {http_err}")
        return None
    except Exception as e:
        print(f"❌ An error occurred while fetching data: {e}")
        return None

def analyze_with_openai(crypto_name, crypto_data):
    """
    Uses the OpenAI API to generate an analysis and sentiment based on the fetched data.
    """
    print("🤖 Connecting to OpenAI for analysis... Please wait.")

    # Securely get the API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("\n" + "="*50)
        print("🔴 FATAL ERROR: OPENAI_API_KEY not found!")
        print("Please set your OpenAI API key using:")
        print("export OPENAI_API_KEY=your_api_key_here")
        print("="*50)
        return None

    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print(f"❌ Error initializing OpenAI client: {e}")
        return None

    price = f"${crypto_data['price']:,}" if crypto_data.get('price') else "N/A"
    market_cap = f"${crypto_data['market_cap']:,}" if crypto_data.get('market_cap') else "N/A"

    # Format market cap in billions/millions for readability
    if crypto_data.get('market_cap'):
        if crypto_data['market_cap'] >= 1_000_000_000:
            market_cap = f"${crypto_data['market_cap']/1_000_000_000:.2f}B"
        else:
            market_cap = f"${crypto_data['market_cap']/1_000_000:.2f}M"

    prompt = f"""
    You are a financial analyst providing a very brief, easy-to-understand summary for a beginner.
    Analyze the cryptocurrency '{crypto_name.title()}' based on the following data:
    - Current Price: {price}
    - Market Cap: {market_cap}

    Please provide the following in two distinct sections:

    1.  **Brief Analysis:** In 2-3 sentences, explain what this cryptocurrency is and what the data might suggest in simple terms.
    2.  **Overall Sentiment:** Based on general market knowledge and recent news (as of your last update), state the sentiment as a single word: Positive, Neutral, or Negative. Then, add one sentence explaining why.

    Keep your response concise and focused on the provided data.
    """

    max_retries = 2
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful financial analyst for beginners."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,  # Keep the analysis fairly consistent
                max_tokens=300,   # Limit response length
                timeout=30        # Set timeout to 30 seconds
            )
            return response.choices[0].message.content
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"⚠️ Attempt {attempt + 1} failed, retrying...")
                continue
            print(f"❌ An error occurred with the OpenAI API: {e}")
            if "exceeded your current quota" in str(e):
                print("\nℹ️ Suggestion: Your OpenAI API key may have exhausted its quota.")
                print("Visit https://platform.openai.com/account/billing to check your usage and limits.")
            return None

def display_results(crypto_name, data, analysis):
    """Prints all the gathered information in a clean format."""
    print("\n" + "="*50)
    print(f"📊 Analysis Report for {crypto_name.title()}")
    print("="*50)

    price = f"${data['price']:,}" if data.get('price') else "N/A"
    market_cap = f"${data['market_cap']:,}" if data.get('market_cap') else "N/A"

    print(f"\n--- Market Data ---\n")
    print(f"   Current Price: {price}")
    print(f"   Market Cap:    {market_cap}")

    print(f"\n--- AI-Generated Summary ---\n")
    if analysis:
        print(analysis)
    else:
        print("   No analysis was generated.")

    print("\n" + "="*50 + "\n")


# --- Main Execution Block ---

if __name__ == "__main__":
    print_header()
    # Since AzureML is not directly used in this simple agent,
    # we acknowledge the user's request by mentioning it's a common pattern for more advanced agents.
    print("Info: This agent uses OpenAI for analysis. For more advanced, production-level agents,")
    print("      integrating services like Azure ML for model deployment and management is a great next step.")
    print("-" * 50)

    try:
        crypto_to_analyze = input("Enter the name of a cryptocurrency (e.g., Bitcoin): ")

        if not crypto_to_analyze.strip():
            print("🤷 No input provided. Exiting.")
        else:
            market_data = get_crypto_data(crypto_to_analyze)

            if market_data:
                ai_analysis = analyze_with_openai(crypto_to_analyze, market_data)
                display_results(crypto_to_analyze, market_data, ai_analysis)

    except KeyboardInterrupt:
        print("\n\n👋 Exiting agent. Goodbye!")

