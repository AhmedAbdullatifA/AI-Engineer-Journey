import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Initialize the OpenAI client configured for Groq
groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_API_BASE_URL")
)

def llm_query(prompt: str) -> str:
    """Sends the prompt to Llama 3.1 via Groq and returns the response."""
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as error:
        return f"An error occurred: {error}"

# EPL 2025-2026 Final Standings data used as context
PREMIER_LEAGUE_TABLE = """
You are a football expert. I will provide you with the final table of the English Premier League 
for the 2025-2026 season. Your task is to analyze the table then answer the question: 
    
Arsenal – 38 played, 26 wins, 7 draws, 5 losses, 71 GF, 27 GA, +44 GD, 85 points (Champions)
Manchester City – 38 played, 23 wins, 9 draws, 6 losses, 77 GF, 35 GA, +42 GD, 78 points (Champions League)
Manchester United – 38 played, 20 wins, 11 draws, 7 losses, 69 GF, 50 GA, +19 GD, 71 points (Champions League)
Aston Villa – 38 played, 19 wins, 8 draws, 11 losses, 56 GF, 49 GA, +7 GD, 65 points (Champions League)
Liverpool – 38 played, 17 wins, 9 draws, 12 losses, 63 GF, 53 GA, +10 GD, 60 points (Champions League)
Bournemouth – 38 played, 13 wins, 18 draws, 7 losses, 58 GF, 54 GA, +4 GD, 57 points (Europa League)
Sunderland – 38 played, 14 wins, 12 draws, 12 losses, 42 GF, 48 GA, -6 GD, 54 points (Europa League)
Brighton & Hove Albion – 38 played, 14 wins, 11 draws, 13 losses, 52 GF, 46 GA, +6 GD, 53 points (Conference League Playoff)
Brentford – 38 played, 14 wins, 11 draws, 13 losses, 55 GF, 52 GA, +3 GD, 53 points
Chelsea – 38 played, 14 wins, 10 draws, 14 losses, 58 GF, 52 GA, +6 GD, 52 points
Fulham – 38 played, 15 wins, 7 draws, 16 losses, 47 GF, 51 GA, -4 GD, 52 points
Newcastle United – 38 played, 14 wins, 7 draws, 17 losses, 53 GF, 55 GA, -2 GD, 49 points
Everton – 38 played, 13 wins, 10 draws, 15 losses, 47 GF, 50 GA, -3 GD, 49 points
Leeds United – 38 played, 11 wins, 14 draws, 13 losses, 49 GF, 56 GA, -7 GD, 47 points
Crystal Palace – 38 played, 11 wins, 12 draws, 15 losses, 41 GF, 51 GA, -10 GD, 45 points
Nottingham Forest – 38 played, 11 wins, 11 draws, 16 losses, 48 GF, 51 GA, -3 GD, 44 points
Tottenham Hotspur – 38 played, 10 wins, 11 draws, 17 losses, 48 GF, 57 GA, -9 GD, 41 points
West Ham United – 38 played, 10 wins, 9 draws, 19 losses, 46 GF, 65 GA, -19 GD, 39 points (Relegated)
Burnley – 38 played, 4 wins, 10 draws, 24 losses, 38 GF, 75 GA, -37 GD, 22 points (Relegated)
Wolverhampton Wanderers – 38 played, 3 wins, 11 draws, 24 losses, 27 GF, 68 GA, -41 GD, 20 points (Relegated)
"""

# Main execution block
if __name__ == "__main__":
    print("--- Premier League 2025-2026 AI Analyst ---")
    
    # Get user question from terminal
    user_question = input("Enter your question about the Table of the Premier League 2025-2026 season: ")
    
    if user_question.strip():
        # Combine the context table with the user's question
        final_prompt = f"{PREMIER_LEAGUE_TABLE}\n\nQuestion: {user_question}\n\nAnswer:"
        
        print("\nThinking...")
        ai_response = llm_query(final_prompt)
        
        print("\n" + "="*40 + "\nAI Response:\n" + "="*40)
        print(ai_response)
    else:
        print("Please enter a valid question.")