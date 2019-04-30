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
                return a[parameter_begin : parameter_end]
            #begin compiling
            value_size = 0
            for a in command_line:
                values = {}
                length = len(a)
                if "print" in a:
                    print(function_reader(a))
                if "=" in a:
                    x = 0
                    for b in a:
                        if b == "=":
                            values[a[-1:x]] = a[x:(len(a)+1)]
                            break
                        x += 1
                if "make_int" in a:                
                    try:
                        int(function_reader(a))
                    except NameError:
                        print("Value isn't int!")
        #basic terminal
        whattodo = input()
        if whattodo == "code":
            while whattodo != "close":
                in = input()
                command_line.append(in)
                newfile = open(input("File Name:  "), "w+")
        if whattodo == "compile":
            if command_line != []:
                print("Compiling...")
                key_compiler(command_line)
            if command_line == []:
                print("No command line detected.")
            
