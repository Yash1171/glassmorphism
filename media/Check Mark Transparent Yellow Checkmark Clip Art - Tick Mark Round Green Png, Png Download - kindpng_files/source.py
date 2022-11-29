import random

with open("flag.txt", "rb") as filp:
    flag = filp.read().strip()
    
key = [random.randint(1, 256) for _ in range(len(flag))]

ct = [1, 6, 29, 85, 95, 60, 190, 180, 153, 185, 198, 186, 219, 14, 195, 145, 194, 131, 93, 184, 70, 139, 4, 144, 180, 109, 73, 23, 117, 38, 7, 227, 37, 61, 135, 155, 202, 238, 177, 56, 89, 139, 254, 116, 107]
enc = [179, 52, 88, 28, 76, 24, 227, 85, 93, 17, 17, 31, 9, 138, 253, 52, 12, 57, 177, 151, 161, 160, 187, 255, 23, 170, 123, 109, 20, 54, 83, 157, 178, 112, 139, 114, 54, 123, 61, 186, 21, 166, 70, 248, 98]
for i, v in enumerate(key):
    k = 1
    for j in range(i, 0, -1):
        k ^= key[j]
    ct.append(k)
    enc.append(flag[i] ^ v)

with open("output.txt", "w") as filp:
    filp.write(f"ct={ct}\n")
    filp.write(f"enc={enc}\n")