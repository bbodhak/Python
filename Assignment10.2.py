'''
10.2
Write a program to read through the mbox-short.txt and
figure out the distribution by hour of the day for each
of the messages. You can pull the hour out from the 'From '
line by finding the time and then splitting the string a second
time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print
out the counts, sorted by hour as shown below.

ans:

04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

Thought my answer is right and will be graded and will give you the right answer, but I suggest to follow Dr.chucks answer. I know there is something I
am missing.

'''

name = input("Enter file: ")
handle = open(name)
counts = dict()
for line in handle :
    #print(line)
    if not line.startswith('From ') : continue
##    print(line)
    sent = line.split(' ')
    #print(sent)
    hrs = sent[6]
    ffnd = hrs.split(':')
    fhrs = ffnd[0]
    #ffhrs = float(fhrs)
    counts[fhrs] = counts.get(fhrs, 0) + 1
    #intcounts = int[counts]
    #print(counts)
##    counts[emailid] = counts.get(emailid, 0) + 1
##    words = line.strip()
lst = list()
for key,val in sorted(counts.items()) :
    ntup = (val, key)
    #print(ntup)
    lst.append(ntup)
    print(key, val)
    #lst = sorted(lst, reverse = False)
    #print(key,val)
##    for key,val in lst :
##        print(key, val)
        
    #print(kay,valu)
                      
##    print(val, key)
##    
##
##print('done')
