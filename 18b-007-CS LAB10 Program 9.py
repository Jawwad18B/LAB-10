print('Jawwad 18b-007-CS(A)')
print('lab 10 Program no 9')
dict = {'Name' : 'Jibran', 'Age': 12, 'Class':'Sixth', 'DOB':'16 April 2006', 'School' : 'The Seeds School', 'Friend1':'Mohib', 'Friend2':'Akbar', 'Friend3':'Jazil'}
print(dict)
for x, y in dict.items():
    print(x,y)
dict.popitem()
print("After poping from the dictionary the remaining elements are: ",dict)
