'''
9.4 Write a program to read through the mbox-short.txt and
figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program
creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through
the dictionary using a maximum loop to find the most prolific
committer.
'''

'''name = input('Enter file name: ')
fname = open(name)
counts = []
#counts = dict()
for line in fname :
    if not line.startswith('From') : continue
    sent = line.split(' ')
    #print(sent)
    ssent = sent[1]
    rspc = ssent.rstrip()
    #nsplt = line.find('', asplt)
    #bsplt = line[asplt+ 2 : nsplt]
    counts = counts + rspc
        #print(counts)
    
    print('done')
print('ddone')
''' 
name = input('Enter file name: ')
fname = open(name)
counts = dict()
for line in fname :
    if not line.startswith('From ') : continue
    sent = line.split(' ')
    emailid = sent[1]
    counts[emailid] = counts.get(emailid, 0) + 1
    #print(counts)
#print('done')
##    for word in words:
##        counts[word] = counts.get(word, 0) + 1
        #print(counts[word])
bigcount = None
bigword = None

for emailid,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = emailid
        bigcount = count
print(bigword, bigcount)

        
    
