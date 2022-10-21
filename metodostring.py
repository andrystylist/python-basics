from itertools import count
from unittest import result


course = 'curso'
my_string = 'codigo facilito'
result = "{} de {}" .format (course, my_string)
print (result)
result = "{a} de {b}" .format ( a= course, b= my_string)
print (result)
result = "{a} de {b}" .format ( b= course, a= my_string)
print (result)
result = result.lower ()
result = "{a} de {b}" .format ( a= course, b= my_string)
print (result)
result = result.lower ()
print (result)
result = result.upper ()
print (result)
result = result.title ()
print (result)
pos = result.find ('codigo')
print (pos)
result = result.lower () #curso de codigo facilito!
print (result)
pos = result.find ("codigo")
print (pos)
count = result.count ('c')
print (count)


new_string = result.replace ('c', 'x')
print (new_string)

new_string = result.split (' ')
print (new_string)

