# open file for reading and suck them in
with open('file_path', 'r') as file:
    lines = file.readlines()


# open file for writing
with open('file_path', 'w') as file:
    file1.writelines(lines)
