# THE CHECKER OF MUTATION IN DNA SEQUENCE
a=str(input("ENTER THE NAME OF THE PAITIENT:"))
b= str(input("ENTER THE ORIGNAL SEQ OF DNA:"))
c=str(input("enter the current sequence of dna:"))
print (a,b,c)
print(len(b))
print(len(c))
if b==c:
    print("NOT MUTATED ,")
else :
    print("MUTATION")
DNA= str(input("ENETER DNA SEQUENCE:"))
print (len(DNA))
if set(DNA).issubset(set("ATGC")):
    print("VALID")
else:
    print ("Invalid")
print("Reversed",DNA[::-1])
