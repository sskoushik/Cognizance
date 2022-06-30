import re,csv

file = open("onelinefile.txt", "w") 
file.write("1Aaa3.5Maths2Bbb4.2Physics3Ccc7.62Chemistry4Ddd9.55Biology5Eee4.0Social6Fff7.6English7Ggg3.111Maths8Hhh9.99Physics9Iii1.23Civics") 
file.close() 

Infile = open("onelinefile.txt")
for i in Infile:
        s = re.findall(r'[+-]?[0-9]+\.[0-9]+', i)
        a = re.findall(r'[a-zA-Z]+', i)
        m = 0
        for p in range(len(s)):
            with open("Filename2.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(p+1), a[m],s[p],a[m+1]])
            m += 2

with open("Filename2.csv", "r",) as file:
    reader = csv.reader(file)
    for row in reader:
        print(','.join(row))
