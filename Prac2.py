# Checking whether seq is RNA or DNA

RNA= str(input("ENTER THE RNA SEQ:"))
print(len(RNA))
if set(RNA).issubset(set("AUGC")):
    print("RNA")
elif set(RNA).issubset(set("ATGC")):
    print("DNA")
else :
    print("NOT ANY GENOMIC SEQ")