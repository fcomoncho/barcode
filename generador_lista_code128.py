# from tkinter import *
import barcode
from barcode.writer import ImageWriter

archivo = "lista.txt"

# Autor: francisco.mooncho@discana.es
"""
root = Tk(  )
root.title( "code128 en PNG")
"""
def create_code128(code128_content):
    #bc_content = QrTextBox.get('1.0','end-1c')
    #fn = "{}.png".format(bc_content)
    bc = barcode.get_barcode_class('code128')
    bc.default_writer_options['write_text'] = False
    bc_ = bc(code128_content, writer=ImageWriter()) # PNG
    bc_ = bc(code128_content) # SVG
    bc_.save(code128_content)
    #QrTextBox.delete('1.0',END)
    #QrTextBox.focus_set()
"""
BrowseButton = Button(root,text="Generar QR",command = create_qr)
BrowseButton.grid(row = 0, column = 0, sticky=(W))
QrTextBox = Text(root, height = 2)
QrTextBox.grid(row = 0, column = 1, columnspan=1, sticky=(W))
QrTextBox.focus_set()

root.mainloop()
"""

with open(archivo, 'r') as f:
    data = f.read()

data = data.split('\n')
for code in data:
    print(code)
    create_code128(code)
