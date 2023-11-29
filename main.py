import sol_lib as sol
print('{{to_print}}'.format(to_print = 2))
def main():
    sol_selected_file = sol.select_file()
    sol.debugger(sol_selected_file, "p")
#    if selected_file[2] == "-c":
#        file_out = sol.compile(selected_file)
#    elif selected_file[2] == "-i":
    sol_file_out = sol.interpret(sol_selected_file)
    exec(sol_file_out)


if __name__ == "__main__":
    main()
