print('Jawwad 18b-007-CS(A)')
print('Lab 10 Program no 7')
dict = {'Name' : 'Jibran', 'Age': 12, 'Class':'Sixth', 'DOB':'16 April 2006', 'School' : 'The Seeds School', 'Friend1':'Mohib', 'Friend2':'Akbar', 'Friend3':'Jazil'}
for x, y in dict.items():
    print(x,y)
dict.pop('Friend1')
print(dict)
