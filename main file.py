#!usr\bin\python
dir = "C:/%USERNAME%/Downloads/"
def key_main(dir) :
    while True:
        def key_compiler(command_line):
            def function_reader(a):
                x = 0
                for b in a:
                    if b == "(":
                        parameter_begin = x
                    if b == ")":
                        try:
                            parameter_end = x
                            if parameter_begin > 10:
                                pass
                            return a[parameter_begin + 1 : parameter_end]
                        except NameError:
                            print("""SyntaxError:  parameter beginning not found:""", a)
                    x += 1
            #begin compiling
            value_size = 0
            for a in command_line:
                #setting up vital variables
                for b in a:
                    if x == len(a):
                        if b != ";":
                            
                values = {}
                length = len(a)
                if "print" in a:
                    user_input = function_reader(a)
                    if user_input in values:
                        print(values.get(user_input))
                    else:
                        print(user_input)
                elif "=" in a:
                    x = 0
                    for b in a:
                        if b == "=":
                            values[a[-1:x]] = a[x:(length+1)]
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
            command_line = []
            code = ""
            while code != "close":
                import os.path
                code = input()
                if code != "close":
                    command_line.append(code)
        if whattodo == "compile":
            print("Compiling...")
            key_compiler(command_line)
