from g4f.client import Client
from insert_questions import add_question
from PyPDF2 import PdfReader
import time

client = Client()
reader = PdfReader("Information_and_Ideas.pdf")


#import prompt for instuctions
promptfile = open("reformat_prompt.txt", "r+").read()

#importfile = open("input.txt", "r+")
outputfile = open("internal_db/Information_and_Ideas.json", "w+")

#auto question converter and exporter
sat_pdf = reader.pages
for page in sat_pdf:
 response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": promptfile + "\n" + page.extract_text()}],
   )
 try:
  outputfile.write(response.choices[0].message.content + ',')
  add_question("sat_database","english",response.choices[0].message.content)
  time.sleep(0.55)
  print("Question Added!")
  print(response.choices[0].message.content)
 except:
  print("Skipped for invalid input or output")  

