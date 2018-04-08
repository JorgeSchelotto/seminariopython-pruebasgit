frase = "Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea"

listaf= frase.split(' ')
print(listaf)
string = input("Ingrese el o los caracter/es a buscar: ")
cont=0
for el in listaf:
	
	if (el.find (string) != -1):
		cont= cont + 1
		
print(cont)
		 
		
