#! python3
import re

# Nongreedy se usa con signo "?" ::: Para uso del .* (El "." reemplaza todos
# los simbolos excepto "\n" new line.
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyTegex = re.compile(r'<.*>')
mo = greedyTegex.search('<To serve man> for dinner>.')
print(mo.group())

# Para que el signo "." tome tambien "\n" se debe gregar "re.DOTALL" en el re.compile
print('--- Sin: re.DOTALL ---')
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('texto de primera linea.\ntexto de segunda linea.\ntercera.').group())

print('--- Con: re.DOTALL ---')
NewlineRegex = re.compile('.*', re.DOTALL)
print(NewlineRegex.search('texto de primera linea.\ntexto de segunda linea.\ntercera.').group())


# Ignorar mayusculas y minusculas con re.I como parametro de re.compile
print('--- Ignorar mayus y minus ---')
robocop = re.compile(r'robocop', re.I)
print(robocop.findall('RoboCop, ROBOCOP, RoBoCoP'))


# Sustituir con sub()
print('--- Sustituir ---')
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the documents to Agent Bob.'))
print('--- Sustituir dejando ver la primera letra ---')
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'\1****', 'Agent Alicentriva gave the documents to Agent Bob.'))

