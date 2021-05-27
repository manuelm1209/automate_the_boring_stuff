#! python3
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?           # area code
    (\s|-|\.)?                  # separator
    \d{3}                       # first 3 digits
    (\s|-|\.)                   # separator
    \d{4}                       # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?# extension
    )''', re.VERBOSE)
texto = 'Mi numero de telefono es 415-555-4242 y vivo con'\
        'batwowowoman en un batmobil y el numero del trabajo es: 222-345-8787' \
        'y secuntadio 111-234-6555 ext 120'
print(phoneRegex.findall(texto))


# Combinar re.IGNORECASE, re.DOTALL Y re.VERBOSE
print('--- re.VERBOSE re.DOTALL re.IGNORECASE ---')
someTegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
