import PyPDF2
import os
import sys
import smtplib
from PIL import Image
from email.message import EmailMessage
from string import Template
from pathlib import Path


def resize_image():  # making a thumbnail of every picture (instead of resize, as it can result in 'bad' proportions)
    image_folder = sys.argv[1]  # via cmd
    resized_folder = sys.argv[2]

    if not os.path.exists(resized_folder):  # create folder if it doesn't yet exist
        os.makedirs(resized_folder)

    for input_image in os.listdir(image_folder):  # loop through images
        image = Image.open(f'{image_folder}\\{input_image}')    # open via its absolute path
        image.thumbnail((200, 200))
        image.save(f'{resized_folder}\\{input_image}')  # save at absolute path in other folder


def convert_image_type():  # convert from .jpg to .pdf
    resized_folder = sys.argv[2]
    pdf_folder = sys.argv[3]

    if not os.path.exists(pdf_folder):  # create the output folder if non-existant
        os.makedirs(pdf_folder)

    for input_image in os.listdir(resized_folder):  # for loop needs an iterable
        image = Image.open(f'{resized_folder}\\{input_image}')
        split_name = os.path.splitext(input_image)  # to convert: split between 'name image' and 'extension'
        # print(split_name) # checking

        first_name = split_name[0]  # get image name (part before extension) to change the extension afterwards
        # print(first_name) # checking

        image.save(f'{pdf_folder}\\{first_name}.pdf', 'pdf')  # convert to pdf


def merge_pdf():
    pdf_merger = PyPDF2.PdfFileMerger()
    pdf_folder = sys.argv[3]

    pdfs = [f'{pdf_folder}\\bulbasaur.pdf',
            f'{pdf_folder}\\charmander.pdf',
            f'{pdf_folder}\\squirtle.pdf']

    for pdf in pdfs:
        # print(pdf)    # checking
        pdf_merger.append(pdf)  # appending files in pdfs (above) with a for loop to pdf_merger

    pdf_merger.write('C:\\Users\\Nicola\\Pictures\\merged_PDF.pdf')  # output location
    pdf_merger.close()


def watermark_pdf():
    pdf_file = PyPDF2.PdfFileReader(open('C:\\Users\\Nicola\\Pictures\\merged_PDF.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('C:\\Users\\Nicola\\Pictures\\wtr.pdf', 'rb'))
    watermarked_pdf = PyPDF2.PdfFileWriter()

    for i in range(pdf_file.getNumPages()):  # loop through all the pages of the pdf_file (to watermark every page)
        page = pdf_file.getPage(i)  # get every page
        page.mergePage(watermark.getPage(0))  # each page: watermark (and: my watermark PDF only has 1 page)
        watermarked_pdf.addPage(page)  # add each merged (watermarked) page to output file

        with open('C:\\Users\\Nicola\\Pictures\\watermarked_PDF.pdf', 'wb') as file:    # output location absolute path
            watermarked_pdf.write(file)


def send_email():
    html = Template(Path('C:\\Users\\Nicola\\PycharmProjects\\PycharmProject1\\user_notification.html').read_text())
    email = EmailMessage()  # instantiate class object
    email['from'] = 'Nicolas Lintermans'
    email['to'] = 'email@gmail.com'  # fill in the email address of who you are sending it to
    email['subject'] = "Your PDF is ready!"
    email.set_content(html.substitute({'name': 'Nicolas'}), 'html')  # in HTML file: "Dear $name, your PDF is ready!"

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  # Googling around was really my friend here (when not?)
        smtp.ehlo()  # ehlo (hello!) server, I'm introducing myself
        smtp.starttls()  # for a secure SMTP session (or a negative response)
        smtp.login('email2@gmail.com', 'email2_password')  # log in remotely (fill in your email account and password)
        smtp.send_message(email)
        print('Finished sending email.')


resize_image()
convert_image_type()
merge_pdf()
watermark_pdf()
send_email()  # For this to work with gmail, you have to unblock the "Less secured apps" within Google user settings

# cmd: python Project2_scripting1.py
# C:\Users\Nicola\Pictures\Pokedex C:\Users\Nicola\Pictures\Pokedex_resized C:\Users\Nicola\Pictures\Pokedex_resized_PDF
