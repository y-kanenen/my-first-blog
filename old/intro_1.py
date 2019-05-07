print('hello world!')

if 3 > 2:
	print('3 is indeed greater than 2')
else:
	print('3 is not greater than 2')


#name = 'Sonja'
def hi(name):
	if name == 'Ola':
		print('Hey Ola')
	elif name == 'Sonja':
		print('Hey Sonja!')
	else:
		print('Hey anonymous!')


def hi2(name):
	print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
	hi2(name)
	print('Next girl\n ')

#name2 = 'Rachel'
#hi2(name2)