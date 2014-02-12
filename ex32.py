the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']
# this first kind of for-loop goes through a list

for number in the_count:
    print "the number is %d" % number

for fruit in fruits:
    print "the fruit is %s " % fruit

for mix in change:
    print "the content is %r" % mix

# we can also build lists,first start with an empty one
'''
elements=[]
for i in range(0,6):
    print "Adding %d to the list"%i
    elements.append(i)

for i in elements:
    print "element was :%r"%i

'''
elements = range(0,6)

print elements

def append_num(num):
    i=0
    numbers=[]
    while i<num:
        print "the num is %i" %i
        numbers.append(i)
        i=i+1
    return numbers
num=6
element=append_num(num)
print element
