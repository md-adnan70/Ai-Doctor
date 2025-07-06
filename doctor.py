import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", groq_api_key = os.getenv("GROQ_API_KEY"))

#Convert image to required format
import base64 

def encode_img(img_path):
  img_file = open(img_path,'rb')
  return base64.b64encode(img_file.read()).decode('utf-8')
  
#Setup Multimodel LLM

query = 'Is there something wrong with my face?'
model="meta-llama/llama-4-scout-17b-16e-instruct"
def analyze_img(query,encoded_img,model):
  client = Groq()
  messages=[
    {
      'role':'user',
      'content':[
        {
          'type':'text',
          'text':query
        },
        {
          'type':'image_url',
          'image_url':{
            'url':f"data:image/jpeg;base64,{encoded_img}",
          },
        },
      ],
    }
  ]

  chat_completion = client.chat.completions.create(
    messages=messages,
    model=model
  )

  return chat_completion.choices[0].message.content