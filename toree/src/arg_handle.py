import utils

lay_opts = ["--layout", "-l", "layout"]
help_opts = ["--help", "-h", "help"]
ver_opts = ["--version", "-v", "version"]

def help_msg():
    print("""toree - directory tree viewer:
        Usage:
           toree [LAYOUT_(1..3)] [PATH]

        Layouts:
           1: normal layout
           2: tree-style layout
           3: xml layout


        ['--help', '-h', 'help'] = help_msg
        ['--version', '-v', 'version'] = see version of toree""")

def arg_handle(args, ctx):
    i = 0
    n_args = []

    while i < len(args):
        arg = args[i]

        if arg in lay_opts:
            try:
                ctx.layout = int(args[i + 1])
                if i+1 == "1":
                    ctx.layout = 1
                elif i+1 == "2":
                    ctx.layout = 2
                elif i+1 == "3":
                    ctx.layout = 3
                i += 2
                continue
            except:
                print("layout mode from 1..3 only")
                exit(1)

        if arg in help_opts: 
            utils.help_msg()
            i += 1
            continue

        if arg in ver_opts:
            print(f"toree: {utils.Prog_ver}")
            i += 1
            continue

        n_args.append(arg)
        i += 1

    return n_args
