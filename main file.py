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
                            if parameter_begin > 10:
                                pass
                        except NameError:
                            print("""SyntaxError:  parameter beginning not found:""", a)
                        else:     
                            parameter_end = x  
                return a[parameter_begin + 1, parameter_end - 1]
            #begin compiling
            for a in command_line:
                values = {}
                length = len(a)
                if "print" in a:
                    print(function_reader(a))
                if "make_int" in a:
                    try:
                        int(function_reader(a))
                    except NameError:
                        print("Value isn't int!", a)
                if "=" in a:
                    
                        
        #basic terminal
        in = input()
        if in == "code":
            while in != "close":
                in = input()
                command_line.append(in)
                newfile = open(input("File Name:  "), "w+")
                for a in command_line:
                    
        if in == "compile":
            if command_line != []:
                print("Compiling...")
                key_compiler(command_line)
            if command_line == []:
                print("No command line detected.")
            
