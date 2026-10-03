import os
import google.generativeai as genai

def run_ai_assistant():
    # Retrieve API key from environment variable or user prompt
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        api_key = input("Enter your Gemini API Key: ").strip()

    genai.configure(api_key=api_key)

    print("==================================================")
    print("      Welcome to Karim's AI Customer Assistant    ")
    print("==================================================")

    model_name = 'gemini-3.8-flash'

    try:
        model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=(
                "You are an AI customer support assistant built for Karim's Freelance Services. "
                "Provide concise, helpful, and professional responses."
            )
        )

        user_prompt = (
            "Hello! Briefly introduce yourself as Karim's AI assistant "
            "and explain how you help businesses with AI integration."
        )

        print(f"\n[Sending Request for Karim] >>> {user_prompt}\n")

        response = model.generate_content(user_prompt)

        print("--- [AI Response Output] ---")
        print(response.text)
        print("----------------------------")
        print("\n[SUCCESS] AI Integration Service completed successfully!")

    except Exception as e:
        print(f"\n[ERROR] Execution failed: {e}")

if __name__ == "__main__":
    run_ai_assistant()