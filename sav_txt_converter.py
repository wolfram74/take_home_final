from scipy import io
import re
import os

def make_text_file(address, values):
    new_file = open(address, 'w')
    for value in values:
        # print(value)
        new_file.write('%f\n'%value)
    return

files = os.listdir('./')
sav_extension = re.compile('.*\.sav$')
sav_files = filter(sav_extension.match, files)

print('found idl sav files')
print(sav_files)
for save in sav_files:
    data = io.readsav(save)
    prefix = save.split('.')[0]
    variables = data.keys()
    print(variables)
    for variable in variables:
        make_text_file(
            '%s_%s.txt' % (prefix, variable),
            data[variable]
            )
