### FILE SELECT


## FILE SELECTOR
def select_file():
    file = input("Select a file by name (No extension) ").split(" ")
    try:
        file = open(file[0])
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
def debug_start(line, mode):
    indents = 0
    linenum = 0
    if line.isspace():
        return
    if line[0] == "/":
        return
    for i in range(len(line)):
        if line[0] == " ":
            
            raise_error(2, linenum)
#    for i in range(4):
#        if line[i] == " ":
#            indents += 1
    if indents != 4:
        error = 2
    if mode == "p":
        print(line)


## DEBUGGER - INVOKER
def debugger(file, mode):
    for line in (file):
        debug_start(line, mode)


### CODE OUTPUTTING
## INTERPRETER
def interpret(file):
    code = ""
    code = code + "print(\"hello world\")\n"
    code = code + "print(\"{to_print}\".format(to_print = 2))\n"
    return code


## COMPILER
def compile(file):
    code = ""
    code += "this = 2\n"
    code += "print(\"hello world\")\n"
    code += "print(\"{to_print}\".format(to_print = sol_file_out.this))\n"
    return code