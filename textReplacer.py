file = input("Which file to modify? ")
replace = input("What phrase would you like replaced? ")
rep_with = input("What would you like that phrase replaced with? ")
try:
    f = open(file, 'r')
    tx = f.read()
    full = ''
    for line in tx.split('\n'):
        new_line = line
        if replace in line:
            split_line = line.split(replace)
            ln = ''
            for chunk in split_line:
                ln += chunk + rep_with
            new_line = ln
        full += new_line + '\n'
    f.close()
    file_write = open(file, mode='w+')
    file_write.write(full)
    file_write.close()
except FileNotFoundError:
    print("sorry, the file could not be found. Please check that all folders are included and that the file name is correct.")

