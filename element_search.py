arr4=[6,20,15,7,25]
x=int(input("Enter the number u want to find: "))
found=False
for i in arr4:
  if i==x:
    found = True
    break
if found == True:
  print("Element found")
else:
  print("Element not found")
