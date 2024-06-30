cube=int(input("Enter any value to check approx cube root:  "))
ep=0.01
count=0
s=0.0
e=cube
guess=(s+e)/2.0
while abs(guess**3-cube)>=ep:
    if (guess**3)<cube:
        s=guess
    else:
        e=guess
    guess=(s+e)/2.0
    count+=1

print ('num_guesses =', count)
print( guess, 'is close to the cube root of', cube)

