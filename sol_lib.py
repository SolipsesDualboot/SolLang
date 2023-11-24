### FILE SELECT


## FILE SELECTOR
def select_file():
    file = input("Select a file by name (No extension) ").split(" ")
    try:
        file = open(file[0] + ".sol")
    except FileNotFoundError: # If file is not found, exit
        print("File not found:", "\"{filename}\"".format(filename = file[0]))
        exit()
    return file

### DEBUGGER

## ERROR INDEX
def raise_error(error, line):
    match error: # Give error number, line where error occured, give details
        case 1:
            print("At line", line, "(ERROR 1) - Whitespace at line start")
            exit()
        case 2:
            print("At line", line, "ERROR 2) - Unexpected indentation")
            exit()


## DEBUGGER - FIRST PASS
def debug_start(file, mode):
    indents = 0
    linenum = 0
    for line in (file):
        if line.isspace():
            continue
        if line[0] == "/":
            continue
#        if line[0] == " ":
#            raise_error(2, linenum)
#    for i in range(4):
#        if line[i] == " ":
#            indents += 1
#    if indents != 4:
#        error = 2
        if mode == "p":
            print(line)


## DEBUGGER - INVOKER
def debugger(file, mode):
    for line in (file):
        debug_start(file, "r")


## INTERPRETER
def interpret():
    pass


## COMPILER
def compile(file):
    code = ""
    return code
