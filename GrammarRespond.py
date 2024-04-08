from openai import OpenAI
client = OpenAI()

text = input("Enter your text here: ")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    { 
    "role": "system", "content": "You will be provided with statements, and your task is to convert them to standard English." 
    },
    {
    "role": "user", "content": text
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
print(response.choices[0].message.content)