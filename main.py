import os
import sys
from dotenv import load_dotenv
from google import genai


def handle_arg():
    if len(sys.argv) < 2:
        print("Usage: main.py <prompt>")
        sys.exit(1)
    if len(sys.argv) == 2:
        return sys.argv[1]
    return sys.argv[1], sys.argv[2]


def main():
    prompt = handle_arg()[0]
    verbose_set = True if handle_arg()[1] is not None else False
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[prompt],
    )
    print(response.text)
    if verbose_set:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
