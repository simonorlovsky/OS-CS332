
inp = raw_input("enter name of file to copy to out.txt, or q to quit:  ")
while inp.strip()!="q":
    fin = open(inp, 'r')
    fout = open ("out.txt", 'w')
    fout.write(fin.read())
    fin.close()
    fout.close()
    inp = raw_input("enter name of file to copy to out.txt, or q to quit:  ")

