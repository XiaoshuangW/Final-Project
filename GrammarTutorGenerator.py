from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a web developer who provides templates for well-structured websites. Provide an HTML file as requested."},
    {"role": "user", "content": "Create a web application that corrects text grammar submitted bu user. The header should say GrammarTutor and the body of the website must include a paragraph explaining the site, a section with a user-side text input box, and a section with a button that user can submit texts and get grammar-corrected text."}
  ]
)

print(completion.choices[0].message.content)