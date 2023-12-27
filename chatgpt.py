#! /usr/bin/python

import openai   

print("Content-type: text/html")
print("")

openai.api_key = "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"

model_engine = "gpt-3.5-turbo" #"text-davinci-003"

prompt = "Hello, how are you today?"

completion = openai.completions.create(
    model=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)