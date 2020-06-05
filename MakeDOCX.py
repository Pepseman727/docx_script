import os
import click
from docx import Document
from docx.shared import Cm

@click.command()
@click.option('--name', prompt="Введите имя для файла")
def Make(name):
    CreateFile(name)

def CreateFile(fileName):
    document = Document()
    files = os.listdir()
    pictures = list(filter(lambda x: x.endswith('.jpg'), files))
    for pic in pictures:
        document.add_picture(pic,  width=Cm(18))
    document.save(fileName + ".docx")
    print("Готово!!!")

if __name__ == '__main__':
    Make()