# week 4 class notes rough

# 1 add element to the list
 
li = [1,2,3,4,5]
li.append(6)
li.append('hello')
li.append([7,8,9,11])
print(li)

# 2 add element to the list

li = [1,2,3,4,5]
li.append(6)
li.append('hello')
li.extend([7,8,9,11])
print(li)

# 3  removining the element from the list

li.remove('hello')
print('after removing the element from  the list :',li)

# 4 pop method

rmv_idx = 3
li.pop(rmv_idx)
print('after pop the element the list :',li) 

# 5 slice operator 
# reversing the list 

rev_idx = li[::-1]
print ("revesing the element:",rev_idx) 

print( f'reverse the list:,{li[::-1]}')

rev_li = li[::-1]
print(rev_li)

print( f'reverse the list:,{li[:-1]}')

# 6 accessing the list elements

print(f'accesing element at index 10 is:',{rev_li[3]})

# 7 finding the length of the element  

len_li = len(rev_li)
print(f'length of the list:',{len_li}) 

search_idx = 6
if search_idx<len_li-1:
    print(f'accessing element at idx {search_idx} is {rev_li}')
else:
    print('index not found')


# 8 update the list 

rev_li[search_idx] = 13
print(f'after modifing the list element at pos:',{search_idx})

rev_li[search_idx] = 'world'
print(f'after modifing the list elements at pos:',{search_idx})


# 9 find the index of the list

idx = rev_li.index('world')
print(f'world is found at index:',{idx}) 

# 10 count of elements in the list

cnt_ele_five = rev_li.count(5)
print(f'count of element:',{cnt_ele_five})  
for i in rev_li:
    print(rev_li.count(1))

# 11 get the charater from the input string 
user_input = input("enter a string: ")
for char in user_input:
    print(f'char',{char}) 

# 12 replace the string char in given input sring

updated_str = user_input.replace("","")
print(updated_str)  

# 13 string to list

updated_str = user_input.replace("",";")
li = updated_str.split(";")
print(li)

# 14 list to string

updated_str = ''.join(li)
print(updated_str)

# 15 uppercase to lowercase
# lower to upper
# both cases

print(f'ToUpper:{updated_str.upper()}')
print(f'ToLower:{updated_str.lower()}')
print(f'title:{updated_str.title()}')

# 16 length of the string

len_str = len(updated_str)
print(f'length of thr updated str:',{len_str})

# 17 accessing middle values

print(f'access char from idx 5 to 14 :',{updated_str[5:13]})

# 18 string reverse

print('reversed string:',{updated_str[::-1]})
for i in updated_str.split():
    print(f'reverse sub string is:',{i [::-1]})

# 19 removing trial and error space

print(updated_str.strip())    
