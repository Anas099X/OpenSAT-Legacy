from g4f.client import Client
from insert_questions import add_question
from PyPDF2 import PdfReader
import time

client = Client()
reader = PdfReader("test.pdf")


#import prompt for instuctions
promptfile = open("prompt_input.txt", "r+").read()

importfile = open("input.txt", "r+")
outputfile = open("output.json", "w+")

#auto question converter and exporter
page = reader.pages
for x in page:
 response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": promptfile + "\n" + x.extract_text()}],
   )
 
 outputfile.write(response.choices[0].message.content)
 add_question("sat_question_test","questions",response.choices[0].message.content)
 time.sleep(0.55)
 print("Question Added!")
 #print(response.choices[0].message.content)

