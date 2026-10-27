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
#three prompts to test the model

prompt1="Hi"
prompt2="Explain time travelling in simple words"
prompt3="write 1000 word eassay on machine learning"
promtps=[prompt1, prompt2, prompt3]
for prompt in promtps:
    message={"role": role, "content": prompt}
    messages=[message]
    response = client.chat.completions.create(model=model, messages=messages,max_tokens=50)
    usage = response.usage
    print(f"Prompt: {prompt}--> your tokens:{usage.prompt_tokens} completion tokens used: {usage.completion_tokens} total tokens used: {usage.total_tokens} Finish Reason:{response.choices[0].finish_reason}")
    # print(response)
    # print(response.choices[0].message.content)

# prompt='Do you know about padho with pratyush?'
# message=[{"role": role, "content": prompt}]
# response = client.chat.completions.create(model=model, messages=message)
# print(response)
# print(response.choices[0].message.content) 
# when you cut/limit the tokens then ----> answer -->lenght
#when prompt full fill it token then----->answer ---> stop