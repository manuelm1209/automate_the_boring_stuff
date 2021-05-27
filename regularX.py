#! python3
import re

phoneTex = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')
texto = 'Mi numero de telefono es (415)555-4242 y vivo con batman, batwoman,\
batwowowoman en un batmobil'
mo = phoneTex.search(texto)
print('Código de área: ' + mo.group(1))
print('Número de telefono: ' + mo.group(2))

# Encontrar números sin código de áres.
print('\n---Con y sin código de area---')
phoneTex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
texto1 = 'Mi numero de telefono es 415-555-4242.'
texto2 = 'Mi numero de telefono es 555-4242.'
mo2 = phoneTex.search(texto1)
mo3 = phoneTex.search(texto2)
print('Con código de area: ' + mo2.group())
print('Sin código de area: ' + mo3.group())

batTex = re.compile(r'bat(man|copter|mobil)')
mo1 = batTex.search(texto)
print('Palabras que empiezan con bat: ' + mo1.group() + '\n parte de busqueda: ' + mo1.group(1))

# Varias veces del termino opcional en la busqueda
print('\n---Varias repeticiones de (wo)---')
texto3 = 'Mi numero de telefono es (415)555-4242 y vivo con\
batwowowoman en un batmobil'
batTex = re.compile(r'bat(wo)*?man')
mo4 = batTex.search(texto3)
print('Palabras con bat y opcional wo en la mitad: ' + mo4.group())

# Varias veces en el texto y no solo la primera como los ejemplos anteriores
print('\n---Varias repeticiones del termino de busqueda---')
texto4 = 'Mi numero de telefono es 415-555-4242 y vivo con\
batwowowoman en un batmobil y el numero del trabajo es: 222-345-8787'
phoneTex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')
mo5 = phoneTex.findall(texto4)
print('Lista: ')
print(mo5)

# Ejemplo con grupos para respuesta en tuples y no en lista.
phoneTex = re.compile(r'((\d\d\d)-(\d\d\d)-(\d\d\d\d))')
mo6 = phoneTex.findall(texto4)
print('Tuples: ')
print(mo6)
