from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# Define the output schema
class Review(TypedDict):
    summary: str
    sentiment: str

# ✅ Add a docstring to describe what the function does
def review_schema(summary: str, sentiment: str) -> Review:
    """
    Extracts a summary and sentiment from the user's product review.
    """
    return {
        "summary": summary,
        "sentiment": sentiment,
    }

# Now it works!
structured_model = model.with_structured_output(review_schema)

result = structured_model.invoke("""
The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands.
Hoping for a software update to fix this.
""")

# print(result)
# print(result['summary'])
# print(result['sentiment'])

item = result[0]
print(item['args']['summary'])
print(item['args']['sentiment'])
