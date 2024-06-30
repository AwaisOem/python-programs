# append any item into 3rd nested list
a=["a","s","d","f","g","h",["q","w","e","r",["z",["x","c"]],"t","y"],"j","k","l"]
b=["v","b","n"]
a[6][4][1].extend(b)
print(a)