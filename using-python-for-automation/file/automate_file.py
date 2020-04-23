f = open('inputFile.txt', 'r')
fp = open('pFile.txt', 'w')
ff = open('fFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        fp.write(line)
    else:
        ff.write(line)
f.close()
fp.close()
ff.close()