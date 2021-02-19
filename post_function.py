import requests

url = 'http://httpbin.org/post'
#parameted
first_name = 'Dishon'
second_name = 'Kadoh'
age = 29
#create a parameter dictionary
parameters = {'firstname': first_name,'secondname':second_name,'age':age}

x = requests.post(url, data = parameters)

print(x.text)