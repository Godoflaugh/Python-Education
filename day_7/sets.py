it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")

new_companies = {"Netflix", "Sysco", "Instagram"}

it_companies.update(new_companies)
print(it_companies)

it_companies.remove("Sysco")
print(it_companies)

#remove method will throw an error if the item does not exist in the set, however the discard will not. 

C = A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B))
print(A.isdisjoint(B))