count = 0;  
word = "";  
maxCount = 0;  
words = []; 

file = open("about.txt", "w") 
file.write("Python has tools for almost every aspect of scientific computing. The Bank of America uses Python to crunch its financial data and Facebook looks upon the Python library Pandas for its data analysis. While there are many libraries available to perform data analysis in Python, here are a few: NumPy, SciPy, Pandas and Matplotlib.") 
file.close() 
  
file = open("about.txt", "r")  

for line in file:  
    string = line.lower().replace(',','').replace('.','').split(" ");
 
    for a in string: 
        if len(a) == 6:
            words.append(a);

for i in range(0, len(words)):  
    count = 1;  

    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;
            
    if(count > maxCount):  
        maxCount = count;  
        word = words[i];
        
print("most frequently used word - " + word);  
file.close();
