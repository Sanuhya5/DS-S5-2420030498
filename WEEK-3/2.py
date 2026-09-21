#THIS IS ALL WEEK 3
# 
# #hamming distance

def hamming_distance(str1,str2):
    #strings of not same length
    if len(str1) !=len(str2):
        raise ValueError("Strings must be of equal length")
  
    #count differing positions
    return sum (ch1 != ch2 for ch1,ch2 in zip(str1,str2))

#ex usage 1
s1="Karolin"
s2="kathrin"
dist=hamming_distance(s1,s2)
print(f"Hamming Distance between '{s1}' and '{s2}':{dist}")
 
print()
 
#ex usage 2
s3="My name is Sanuhya"
s4="My name is Nimisha"
dist=hamming_distance(s3,s4)
print(f"Hamming Distance between '{s3}' and '{s4}':{dist}")
