import string
vocales="aeiouAEIOUáíóúé"
consonantes=[x for x in string.ascii_letters if x not in vocales]
numeros=string.digits;signosP=string.punctuation
e_numeros=[];e_signosP=[]
e_vocales=[];e_consonantes=[]

msg='''Los corchetes indican subíndices de matrices uni y multi dimensionales.
        char ch, str[] = "Cadena de caracteres";
        int mat[][]; // Matriz de  x 
        ch = str[]; // cuarto elemento'''

e_vocales=[x for x in msg if x in vocales]
e_consonantes=[x for x in msg if x in consonantes]
e_numeros=[x for x in msg if x in numeros]
e_signosP=[x for x in msg if x in signosP]

print(len(e_vocales)," Vocales extraidos:", e_vocales if e_vocales else "N/A")
print(len(e_consonantes)," Consonantes extraidos:", e_consonantes if e_consonantes else "N/A")
print(len(e_numeros)," Numeros extraidos:", e_numeros)
print(len(e_signosP)," Signos de puntuación extraidos:", e_signosP if e_signosP else "N/A")
