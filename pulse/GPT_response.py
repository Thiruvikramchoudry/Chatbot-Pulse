import openai

openai.api_key = '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'

def chatgpt_response(message,disease):
  if disease!="":
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt="The skin disease seems to be "+disease+" ."+message,
      temperature=0.5,
      max_tokens=100
    )
  else:
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=message,
      temperature=0.5,
      max_tokens=100
    )

  return response.choices[0].text.strip()