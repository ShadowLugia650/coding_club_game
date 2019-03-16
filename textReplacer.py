import os

def runReplacement(file, replace, rep_with):
    try:
        f = open(file, 'r')
        tx = f.read()
        full = ''
        if ' ; ' in replace and ' ; ' in rep_with:
            reps = replace.split(' ; ')
            repws = rep_with.split(' ; ')
            for line in tx.split('\n'):
                new_line = line
                if [phr in line for phr in reps] == [True]*len(reps):
                    for phr in reps:
                        split_line = new_line.split(phr)
                        ln = ''
                        for chunk in split_line:
                            ln += chunk
                            if split_line.index(chunk) != len(split_line)-1:
                                ln += repws[reps.index(phr)]
                        new_line = ln
                full += new_line + '\n'
        else:
            for line in tx.split('\n'):
                new_line = line
                if replace in line:
                    split_line = line.split(replace)
                    ln = ''
                    for chunk in split_line:
                        ln += chunk
                        if split_line.index(chunk) != len(split_line)-1:
                            ln += rep_with
                    new_line = ln
                full += new_line + '\n'
        f.close()
        file_write = open(file, mode='w+')
        file_write.write(full)
        file_write.close()
    except FileNotFoundError:
        print("sorry, the file could not be found. Please check that all folders are included and that the file name is correct.")
        input()


if __name__ == "__main__":
    file = input("Which file to modify? ")
    replace = input("What phrase would you like replaced? ")
    rep_with = input("What would you like that phrase replaced with? ")
    if file.lower() != "all":
        runReplacement(file, replace, rep_with)
    else:
        folder = [None, 'dependencies', 'Rooms\Intros', 'Rooms\Easy', 'Rooms\Medium', 'Rooms\Hard', 'Rooms\Impossible']
        for folderset in folder:
            for filename in os.listdir(folderset):
                if filename.endswith('.py') and filename != 'textReplacer.py':
                    name = filename
                    if folderset is not None: name = "{}\{}".format(folderset, filename)
                    runReplacement((name), replace, rep_with)



