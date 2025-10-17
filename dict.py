grocery={"veggie":"tomato","fruits":"apple","snacks":"chips"}
print(grocery)
#accessing
print(grocery["fruits"])
print(grocery.get("snacks"))
#update
grocery["dairy"]="milk"
print(grocery)
#deleting
del grocery["veggie"]
print(grocery)
print(grocery.pop("fruits"))
#membership
print("snacks" in grocery)
