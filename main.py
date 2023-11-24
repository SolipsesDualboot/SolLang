import sol_lib as sol

def main():
    selected_file = sol.select_file()
    print(selected_file.read())
    sol.debugger(selected_file[0], "r")
#    if selected_file[2] == "-c":
#        file_out = sol.compile(selected_file)
#    elif selected_file[2] == "-i":
#        file_out = sol.interpret(selected_file)
#    exec(file_out)


if __name__ == "__main__":
    main()
