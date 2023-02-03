# path = "C:/Users/sweet/OneDrive/Desktop/composer.txt"
# with open(path, 'r') as newFile:
#     line = newFile.read().replace('\n', '')
#     print(line)
#     line = newFile.readline()
#     print(line)

path = "C:/Users/sweet/OneDrive/Desktop/composer.csv"
header = 'person,work\n'
line1 = 'Smetana, Ma Vlast\n'
line2 = 'Shostakovich,no5\n'
with open(path, 'w', encoding = 'utf8') as newFile:
    newFile.write(header)
    newFile.write(line1)
    newFile.write(line2)
