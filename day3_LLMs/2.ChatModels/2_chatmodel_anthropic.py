
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='Claude-3-5-Sonnet-20241022')

result = model.invoke('What is the capital of India')

print(result.content)