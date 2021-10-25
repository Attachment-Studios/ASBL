imports = {}
meta = {}
requests = {}

metaf = open('meta.csv', 'r')
for data in metaf.read().split(','):
	dat = data.split(':')
	imports.update({ dat[0] : dat[1] })
metaf.close()

defaults = imports['default'].split(';')
for dat in defaults:
	meta.update({ dat : imports[dat] })
	del imports[dat]
del imports['default']

for data in imports:
	requests.update({ data : imports[data] })

print()
print(f"Establishing {meta['license']}(c) {meta['version']}")
print()

for request in requests:
	requests[request] = input(f'{requests[request]}: ')

basef = open(meta['base'], 'r')
base = basef.read()
basef.close()

for request in requests:
	base = base.replace(f"<x@{request}>", requests[request])

license = base

print()
print('------------------------------------------')
print(license)
print('------------------------------------------')
print()

savename = input('Save Name: ')

print()

licensefile = open(savename, 'w')
licensefile.write(license)
licensefile.close()

print()
print(f'"{savename}" is file containing license.')