f1 = open('myfile1.txt','r')
f2 = open('myfile2.txt','w')

for line in f1.readlines():
    if not (line.startswith('TextGenerator')):
      
        print(line, end=' ')
        f2.write(line)

f2.close()
f1.close()