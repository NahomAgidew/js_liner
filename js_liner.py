import optparse
import os

VERSION = "0.1"
source = ""
output = ""

def info():
    print("\njs_liner.py condenses JS code to one line. Useful for obfuscating code in the browser.\n")
    print("Version: " + VERSION + "\n")

def main():
    inp = open(source)
    lines = 0
    ls = []

    #counting lines and appending statements to a list
    for i in inp.readlines():
        ls.append(i.strip("\n"))
        lines += 1

    print(str(lines)+" lines found.")

    print("Writing changes...")

    #write all statements into one line
    final = ""
    for x in ls:
        final += x

    open(output, "w").write(final)

    print("Done!")
        

if __name__ == '__main__':
    info()
    
    parser = optparse.OptionParser('usage%prog ' + '-i <input> -o <output>')
    parser.add_option('-i', dest='source')
    parser.add_option('-o', dest='output')
    (options, args) = parser.parse_args()
    source = options.source
    output = options.output

    if(not os.path.isfile(source)):
        print(source + " doesn't exists.")
        exit()

    print("Source File: " + source)
    print("Output File: " + output)
        
    main()
