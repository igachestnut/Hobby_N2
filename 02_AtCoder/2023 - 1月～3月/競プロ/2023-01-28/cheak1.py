s = "atcoder"
t = "????"
#print(s[3:5])

#print(s[-2:])
print(s[7:])

def remove_str(s, start, end):
    return s[:start] + s[end:]

for i in range(len(t)+1) :
    print(remove_str(s, i, len(s)-len(t)+i))
