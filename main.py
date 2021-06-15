from hello import Hello
from algorithms import powList as pL


print('Main begins')
def testing(number):
	if number > 15:
		print('number is too big')
	else:
		l = [x for x in range(number)]
		print('testing algorithms')
		print(pL(l, 2))

if __name__ == '__main__':
	h = Hello()
	h.printHello()
	h.printValue()
	print('These are the new changes'.upper())
	
