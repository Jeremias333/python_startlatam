import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "datas/texts.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#Escrita arquivo
text1 = "Texto da linha 1\n"
text2 = "Texto da linha 2\n"

archive = open(abs_file_path, 'w')
archive.write(text1)
archive.write(text2)

archive.close()

archive = open(abs_file_path, 'r')
for line in archive:
    new_line = line.replace('\n','')
    print(new_line)
    if(new_line == "Texto da linha 1"):
        print("Achou a primeira linha")
archive.close()

