import argparse
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    args = parser.parse_args()

    with open(args.file, "r") as f:
        source_code = f.read()

    print(f"🔁 Converting to {args.to}...\n")
    converted = convert_code(source_code, args.to)
    print("✅ Conversion complete:\n")
    print(converted)

if __name__ == "__main__":
    main()
