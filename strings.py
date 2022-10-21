my_string = "Hola mi gente!"
print (my_string)

my_string = 'Hola mi gente "Andry"'
print (my_string)

my_string = """este es una practica\ncon saltos de linea\n quiero ver el resultado"""
print (my_string)

course = "python"
name = "andry"
final_message = course + name
print (final_message)

final_message = "nuevo curso " + course + 'por' + name
print (final_message)

final_message = "NUEVO CURSO %s por%s " % ( course , name )
print (final_message)

final_message = "nuevo curso {} por {}".format (course, name)
print (final_message)

