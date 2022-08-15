import requests
import argparse
from bs4 import BeautifulSoup
from prettytable import PrettyTable

parser = argparse.ArgumentParser(description ='Enter state name to get covid 19 data.',epilog='Program to display covid 19 data of state')

parser.add_argument('-s',help="Enter state")

args = parser.parse_args()

state = args.s

URL = "https://prsindia.org/covid-19/cases"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('table', attrs = {'class':'table table-striped table-bordered'})
D={}
count = 0
for row in table.tbody.findAll('tr',attrs = {}):
	#print(row)
	L = []
	for column in row.findAll('td',attrs = {}):
		L.append(column.get_text())
	D[count] = L
	count+=1

L = []
for row in table.tfoot.tr.findAll('td',attrs = {}):
	#print(row)
	

	L.append(row.get_text())
D[count] = L
#print(D)

state_list = []

for i in D.values():
	state_list.append(i[1])

#print(state_list)

data = []
if(state==None):
	'''
	data.append(D[len(D)-1][1])
	data.append(D[len(D)-1][2])
	data.append(D[len(D)-1][3])
	data.append(D[len(D)-1][4])
	data.append(D[len(D)-1][5])
	t = PrettyTable(['Country','Confirmed Cases','Active Cases','Recovered cases','Death'])
	t.add_row(['{}'.format(data[0]),'{}'.format(data[1]),'{}'.format(data[2]),'{}'.format(data[3]),'{}'.format(data[4])])
	print(t)
	'''
else:
	URL = r"https://www.google.com/search?q={}+state+india".format(state)
	#print(URL)
	google = requests.get(URL)
	soup = BeautifulSoup(google.content, 'html5lib')
	#print(soup)
	g_str = soup.find('div', attrs = {'class':'BNeawe vvjwJb AP7Wnd'})
	
	#print(g_str.get_text())
	for i in state_list:
		if(g_str.get_text().find(i) != -1):
			final_state = i
			L = final_state.split()
				
			URL = 'https://www.google.com/search?q=covid+{}'.format('+'.join(L))
			print(URL)
			
			google= requests.get(URL)
			soup = BeautifulSoup(google.content, 'html5lib')
			
			
			'''
			for j in range(0,len(D)):
				if(D[j][1] == final_state):
					data.append(D[j][1])
					data.append(D[j][2])
					data.append(D[j][3])
					data.append(D[j][4])
					data.append(D[j][5])
					t = PrettyTable(['Country','Confirmed Cases','Active Cases','Recovered cases','Death'])
					t.add_row(['{}'.format(data[0]),'{}'.format(data[1]),'{}'.format(data[2]),'{}'.format(data[3]),'{}'.format(data[4])])
					print(t)
					break
			'''
			break;
	else:
		print("Please Enter a valid state")
	
	
			
	
