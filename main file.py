#!usr\bin\python
def key_main() :
    while True:
        command_line = []
        def key_compiler(command_line):
            def function_reader(a):
                x = 0
                    for b in a:
                        if b == "(":
                            parameter_begin = x
                        if b == ")":
                            try:
                                parameter_begin
                            except NameError:
                                print("""SyntaxError:  parameter beginning not found:""", a)
                                print("""                                        """
                                   
                            parameter_end = x  
                        x += 1
            x = 0
            for a in command_line:
                length = 0
                for b in a:
                    length += 1
                if "print" in a:
                    x = 0
                    for b in a:
                        if b == "(":
                            parameter_begin = x
                        if b == ")":
                            try:
                                if parameter_begin > 10:
                                    pass
                            except NameError:
                                print("""SyntaxError:  parameter beginning not found:""", a)
                            else:
                                parameter_end = x
                        
                        x += 1
                x += 1
        in = input()
        if in == "code":
            while in != "close":
                in = input()
                command_line.append(in)
        if in == "compile":
            if command_line != []:
                print("Compiling...")
                key_compiler(command_line)
            if command_line == []:
                print("No command line detected.")
            
