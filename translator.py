import argparse
import openai
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def convert_code_gemini(code: str, target_lang: str) -> str:
    """Converts code to the target language using Google Gemini API."""
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "Error: GOOGLE_API_KEY not found in environment variables."
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Convert the following code to {target_lang}:\n\n{code}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during Gemini API call: {e}"

def convert_code(code: str, target_lang: str) -> str:
    prompt = f"Convert the following code to {target_lang}:\n\n{code}"

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a code converter that rewrites code from one language to another."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()

def main():
    parser = argparse.ArgumentParser(description="Codex-style code converter.")
    parser.add_argument("--file", type=str, help="Path to source code file", required=True)
    parser.add_argument("--to", type=str, help="Target language (e.g., python, java, c++)", required=True)
    parser.add_argument("--api", type=str, choices=["openai", "gemini"], default="openai", help="API to use for conversion (openai or gemini)")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        source_code = f.read()

    print(f"🔁 Converting to {args.to} using {args.api.upper()} API...\n")
    if args.api == "gemini":
        converted = convert_code_gemini(source_code, args.to)
    else:
        converted = convert_code(source_code, args.to)
    
    print("✅ Conversion complete:\n")
    print(converted)

if __name__ == "__main__":
    main()
