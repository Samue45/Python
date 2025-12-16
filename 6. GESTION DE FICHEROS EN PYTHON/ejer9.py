import shutil
import os

shutil.copy("texto.txt","nuevo.txt")

shutil.move("texto.txt","hola.txt")

os.mkdir("nuevo_direct")

with open(os.path.join("nuevo_direct","archivo1"), 'w', encoding='utf-8') as f:
    f.write("Hola")

shutil.rmtree("nuevo_direct")

