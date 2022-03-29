sentence = 'hi, how are you?'
print(sentence.split())
print(sentence.split(','))

def add(a,b,c):
    result = a*b*c
    print(result)
    
add(2,4,6)

def wordCount():
    file = input('Enter file name: ')
    f = open(file,'r')
    count = 0
    for i in f:
        words = i.split()
        count = count+len(words)
    
    print(count)

wordCount()
    