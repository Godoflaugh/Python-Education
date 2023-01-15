#1
lst=[]

#2
five_list =[1, 2, 3, 4, 5]

#3
print(len(five_list))

#4
print(five_list[0])
print(five_list[2])
print(five_list[4])

#5, 6, 7, 8
mixed_data_types = ["Kevin", 31, 180, "Single", "14802 Newport Avenue"]
it_companies = ["Facebook", 'Google', "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)
print(len(it_companies))

#9 show the 1st middle and final item in a list
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

#10 Change an item in an existing list
it_companies[0] = "infosystems"
print(it_companies[0])

#11 Add an item too a list
it_companies.append('Snapchat')
print(it_companies)
print("-------------------------------------------------------------")

#12
it_companies = it_companies[0:len(it_companies) // 2] + ['Dell'] + it_companies[len(it_companies) // 2:]
print(it_companies)

#13
print("-------------------------------------------------------------")
it_companies[0] = it_companies[0].upper()
print(it_companies)

#14
print("-------------------------------------------------------------")
it_companies_hash = '#'.join(it_companies)
print(it_companies_hash)

#15
print("-------------------------------------------------------------")
does_exist = "IBM" in it_companies
print("Does IBM exist in the list?", does_exist)
print("IBM" in it_companies)

# 16
print("-------------------------------------------------------------")
it_companies.sort()
print(it_companies)

#17
print("-------------------------------------------------------------")
it_companies.reverse()
print(it_companies)

# 18
print("-------------------------------------------------------------")
print(it_companies)
print(it_companies[3:])

# 19
print("-------------------------------------------------------------")
print(it_companies)
print(it_companies[:len(it_companies) - 3])

# 20
print("-------------------------------------------------------------")
print(it_companies)
it_companies = it_companies[0:len( it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]
print(it_companies)

# 21
print("-------------------------------------------------------------")
print(it_companies.pop(0))
print(it_companies)

# 22
print("-------------------------------------------------------------")
it_companies.pop(len(it_companies) // 2)
print(it_companies)

#23
print("-------------------------------------------------------------")
it_companies.pop()
print(it_companies)

print("-------------------------------------------------------------")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.append(back_end)
full_stack = front_end
indx = full_stack.index('Redux')
full_stack = full_stack[:indx] + ['Python', 'SQL'] + full_stack[indx:]
print(full_stack)
