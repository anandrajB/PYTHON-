#command line argument argv
from sys import argv
sum1=0

print(type(argv))
print('no of command line Argument:',len(argv))
print('list of clarg:',argv)

print('name',argv[0])
print('arg[1]',argv[1:])
print('command line arg one by one:')
for x in argv[1:]:
    sum1=sum1+int(x)
    print(sum1)


