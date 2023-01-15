empty_tple = ()

brother_tuple = ("Kevin", "Mike", "Lorenzo")
brother2_tuple = ("Paul", "Alex", "Krishna")

brothers_tuple = brother_tuple + brother2_tuple

print(len(brothers_tuple))
print(brothers_tuple)
      
family_members = brothers_tuple + ("Ian", "Danny")
brothers_tuple, white, asian = family_members
print(brothers_tuple)
print(white)
print(asian)
