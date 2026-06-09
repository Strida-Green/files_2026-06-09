"""
data = ""
with open('alfa_in.xml', 'r') as file:
    #data = file.read().replace(',', '.').replace(' ', ';')
    data = file.read().replace(',', '.')

with open("alfa_out.xml", "w") as out_file:
    out_file.write(data)
"""

#Пример (открытие всех xml файлов):

import glob

for filename_in in glob.glob('*.xml'):
    with open(filename_in, 'r') as file_in:
        data = file_in.read().replace(',', '.')
    filename_out = filename_in
    with open(filename_out, "w") as file_out:
        file_out.write(data)

print("готово!")