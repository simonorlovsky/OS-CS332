
inp = raw_input("enter name of file to copy to out.txt, or q to quit:  ")
while inp.strip()!="q":
    fin = open(inp, 'r')
    fout = open ("out.txt", 'w')
    line = fin.readline()
    while line:
        fout.write(line)
        line = fin.readline()
    fin.close()
    fout.close()
    inp = raw_input("enter name of file to copy to out.txt, or q to quit:  ")

