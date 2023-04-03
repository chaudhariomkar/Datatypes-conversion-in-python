#Zip and Typecasting
x = [10,20,30]
y = ['python','java','c++']
print(zip(x,y)) #When output is in the form of object to see the result , do the type casting
print(list(zip(x,y))) #Typecast into list
print(dict(zip(x,y))) #Typecast into dict
print(dict(zip(x,y)).items()) #Dict items
#Typecasting - Typecasting is also known as type conversion. Converting a data/object from one from to other
a = 10
print(a)
print(type(a)) #Type of a = int
print(str(a)) #convert to str
print(float(a)) #convert to float
print(complex(a)) #convert to complex
print(bool(a)) #convert to boolean - everything except (None,0,'') is True
print(bool(None)) #False
print(bool(0)) #False
print(bool('')) #False
print(bool(12.3)) #True
print(bool([1,2,3])) #True
print(bool('rajesh')) #True
#Convert to a list
#print(list(a)) --->TypeError - 'int' object is not iterable
#if we supply 10 instead of '10'
print(list('10'))
#Convert to a tuple
print(a)
#print(tuple(a)) --->TypeError - 'int' object is not iterable
#Convert to set
#print(set(a)) --->TypeError - 'int' object is not iterable
#Convert to dict
#print(dict(a)) --->TypeError - 'int' object is not iterable
print('100'*5) #5times 100 concatenate
print(int('100')*5) #500
#Input function is used to collect values from users
age = input('Enter your age:')
print(age)
print(type(age))
#print(age+10) TypeError: can only concatenate str (not "int") to str
print(int(age)+10)
#Binary Conversion - Convert decimal(base-10) to binary(base-2)
print(a)
print(bin(a))
#Octal Conversion - Convert decimal to octal(base-8)
print(oct(a))
#Hex Conversion - Convert decimal to hex(base-16)
print(hex(a))
#python default uses decimal number system. It is of base 10(0-9).
#Typecasting is of 2 types
#Implicit Typecasting - It is performed by Python itself
print(12+12.0)
print(10/2)
#Data Structure priorty - Numeric -> Int -> Float -> Complex
#Explicit Typecasting - It is performed by users as per requirements
print(1+(2+4j))
print(str(1+(2+4j)))
p = '23.4'
print(float(p))
q = 'twenty'
#print(float(q)) ValueError: could not convert string to float
r = ['a','b','c']
print(set(r))
