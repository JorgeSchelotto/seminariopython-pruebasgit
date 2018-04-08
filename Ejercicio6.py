#String a trabajar.
frase = "Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple."

#Limpio puntos y comas.
frase = frase.replace(',','')
frase = frase.replace('.','')


#Paso a minuscula.
frase = frase.lower()

#Paso de string a lista.
listaFrase = frase.split(' ')

#Paso de lista a conjunto (limpia repetidos).
setFrase = set(listaFrase)

#Paso a lista.
frase = list(setFrase)
frase.sort(reverse=True)
nueva = []


diccioFrases = {}
for i in frase:
    diccioFrases[len(i)]= []

for i in frase:
    diccioFrases[len(i)].append(i)



print(diccioFrases)






