def uppercase(str):
    uppercase=""
    for i in str:
        if ord(i) >=97 and ord(i) < 123:
            uppercase+=chr(ord(i)-32)
        else:
            uppercase+=i
    print(uppercase)


"""
string1="every charaCter is in uppercase"
string2="everyBody"
new_string1="" 
new_string2=""
for i in string1 and string2: 
   # 'ord' is used to find the ascii value 
   if ord(i) >=97 and ord(i)< 123: 
       #'chr' used to find the character from ascii value 
        new_string1+=chr(ord(i)-32) 
        new_string2+=chr(ord(i)-32)
   else: 
        new_string1+=i 
        new_string2+=i 
print(new_string1)
print(new_string2)  
"""
"""
def uppercase(str):
    ascii=[]
    for i in str:
        #ascii.append(ord(i))
        ascii+=chr(ord(i)-32)
        #ascii+=i
    print(str)
"""