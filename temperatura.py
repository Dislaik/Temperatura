from datetime import date
from statistics import mode
 
def days_between(d1, d2):
    return abs(d1 - d2).days

def get_data(lista):
	file = open('temp.txt', 'r')
	for x in file.readlines():
		lista.append(x)
	file.close()
	lista = ''.join(lista)
	lista = lista.split()
	return lista

def data_to_list(lista):
	j = 0
	for i in lista:
		lista[j] = i.rstrip("\n")
		j += 1

def temperature():
	i = 0
	while i < total_elementos:
		dates[i] = dates[i].split(" ")
		dates[i][1] = int(dates[i][1])
		only.append(dates[i][1])
		i+= 1

def separate_date():
	j = 0
	while j < total_elementos:
		dates[j][0] = dates[j][0].replace('-', '')
		print(dates[j])
		if dates[j][1] == find:
			testing.append(dates[j])
			testing.append(dates[j+1])
		j+= 1

def reorder_list(x):
	for i in testing:
		if i not in x:
			new_dates.append(i)

def set_data(x, y):
	file = open('estable.txt', 'w')
	file.write(str(x) + " " + str(y))
	file.close()

if __name__ == '__main__':
	dates = []
	only = []
	new_dates = []
	testing = []
	get_data(dates)
	data_to_list(dates)
	total_elementos = len(dates)
	temperature()
	find = mode(only)
	lenfind = only.count(find)
	separate_date()
	reorder_list(new_dates)
	print(new_dates)
	date_1 = date(int(new_dates[0][0][4:8]), int(new_dates[0][0][2:4]), int(new_dates[0][0][:2]))
	print("Fecha de inicio:", date_1)
	date_2 = date(int(new_dates[lenfind][0][4:8]), int(new_dates[lenfind][0][2:4]), int(new_dates[lenfind][0][:2]))
	print("Fecha de termino", date_2)
	print("Longitud en días:", days_between(date_2, date_1))
	print("Temperatura:", find)
	write = days_between(date_2, date_1)
	set_data(write, find)
