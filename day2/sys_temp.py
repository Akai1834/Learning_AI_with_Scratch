import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY set kro phle")
client = Groq(api_key=my_api_key)
model= "openai/gpt-oss-20b"
role='user'
prompt='suggest the brand name for my clothing company and give only one name. And name should be in one word.'

message_system=[{"role": "system", "content": "You are my brand manager who suggest the brand name for my clothing brand and name should be in one word."}]
message=[{"role": role, "content": prompt}]
response = client.chat.completions.create(model=model, messages=message_system + message,temperature=0.2)
# print(response)
print(response.choices[0].message.content) 