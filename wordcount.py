#file = open("C:\Users\ramaraj.paulraj\Desktop\Traning Docs\Python\wc.txt", "r")
filename = r'C:\Users\ramaraj.paulraj\Desktop\Traning Docs\Python\wc.txt'
file = open(filename, 'r')
#wordcount = [] this is for interger. not for strings
#wordcount = {} this is for strings.. this is Directories.works with keys and values instead of indexes
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] +=1
print (word,wordcount)
#    for k,v in wordcount.items():
#        print k,v


#this is just count the total words in the program
# filename = r'C:\Users\ramaraj.paulraj\Desktop\Traning Docs\Python\wc.txt'

#words = 0
#textfile = open(filename, 'r')

#for wordcount in textfile.readlines().split(" "):
#    words += 1

# print("counts are" +words)
