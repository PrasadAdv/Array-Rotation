print('Enter array')
array=[]
num=0
while(num!='q'):
    num=(input('\t'))
    if(num!='q'):
        array.append(num)
   
temp=[]
d=int(input('Enter rotation moves'))
p=str(input('Enter rotation direction (C/AC)'))

if p=='C':
    temp[:]=temp[:]+array[d:]
    i=0
    temp[:]=temp[:]+array[i:d]

if p=='AC':
    i=len(array)-d
    temp[:]=temp[:]+array[i:len(array)]
    temp[:]=temp[:]+array[:i]
print(temp)
