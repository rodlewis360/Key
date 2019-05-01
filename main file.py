#!usr\bin\python
dir = "C:/%USERNAME%/Downloads/"
def key_main(dir) :
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
                #setting up vital variables
                values = {}
                length = len(a)
                if "print" in a:
                    print(function_reader(a))
                elif "=" in a:
                    x = 0
                    for b in a:
                        if b == "=":
                            values[a[-1:x]] = a[x:(len(a)+1)]
                            break
                        x += 1
                elif "make_int" in a:                
                    try:
                        int(function_reader(a))
                    except NameError:
                        print("Value isn't int!")
        #basic terminal
        whattodo = input()
        if whattodo == "code":
            while whattodo != "close":
                import os.path
                code = input()
                command_line.append(code)
                newfile = open(os.path.join(dir + input("File Name:  ") + ".txt"), "w+")
        if whattodo == "compile":
            if command_line != []:
                print("Compiling...")
                key_compiler(command_line)
            else:
                print("No command line detected.")
            
