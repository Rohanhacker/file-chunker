import os
print "press j if you want to join files and d for dividing \n"
ip = raw_input()
if ip == 'd':
    n = "part"
    print "enter path and file should be atleast 5 mb  \n"
    path = raw_input()
    f = open(path,"r+b")
    sc = os.path.getsize(path)
    print (sc >> 20 )
    print "enter size of chunk in megabytes"
    chunk = input()
    kilobytes = 1024
    megabytes = kilobytes * 1000
    chunk = chunk*megabytes
    r = sc%chunk
    noofchunks = int(sc)/chunk
    for i in range(noofchunks):
        name = n + str(i)
        s = open(name,'w+b')
        data = f.read(int(chunk))
        s.write(data)
        lst = i
    if r!=0:
        name = n + str(lst+1)
        s = open(name,'w+b')
        data = f.read(int(r))
        s.write(data)
    s.close()
    f.close()
elif ip == 'j':
    print "enter no. of chunks (parts)"
    no = input()
    n = "part"
    print "extension of file "
    ex = raw_input()
    c = open("nf.{}".format(ex),"w+b")
    for i in range(no):
        f = open((n+str(i)),"rb")
        data = f.read()
        c.write(data)
        f.close()
    c.close()
