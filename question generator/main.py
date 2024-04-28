from g4f.client import Client
import g4f
from insert_questions import add_question
from PyPDF2 import PdfReader
import time

client = Client()
reader = PdfReader("main_input.pdf")


#import prompt for instuctions
promptfile = open("question generator/reformat_prompt.txt", "r+").read()

#importfile = open("input.txt", "r+")
outputfile = open("internal_db/SAT_database.json", "w+")

#auto question converter and exporter
sat_pdf = reader.pages
for page in sat_pdf:
 response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": promptfile + "\n" + page.extract_text()}],
    provider=g4f.Provider.Ecosia
   )
 try:
  add_question("sat_database","english",response.choices[0].message.content)
  outputfile.write(response.choices[0].message.content + ',')
  time.sleep(0.55)
  print("Question Added!")
  print(response.choices[0].message.content)
 except:
  print("Skipped for invalid input or output")  

