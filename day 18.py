f=open('ABC.txt','r')
x=f.read()


x=x.replace('raj','ram')
print(x)
f=open('ABC.txt','w')
f.write(x)

f.close()


