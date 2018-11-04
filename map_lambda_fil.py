#map,lambda,filter

lst=[1,2,3,4,5,6]
print(list(map(lambda i: i**3,lst)))


#filter

lst=[3,5,7,9]
print(list(filter(lambda i:i**2>50,lst)))
