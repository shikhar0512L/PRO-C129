import csv , pandas

file1 = "data.csv"
file2 = "data2.csv"

df1=[]
df2=[]

with open(file1,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        df1.append(i)

with open(file2,'r',encoding='utf8') as f:
        csv_reader = csv.reader(f)

        for i in csv_reader:
            df2.append(i)

p_d1 = df1[1:]
p_d2 = df2[1:]

h1 = df1[0]
h2 = df2[0]
h = h1+h2

p_d = []

for i in p_d1:
    p_d.append(i)

for j in p_d2:
    p_d.append(j)

with open("merged_data.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)

df = pandas.read_csv("merged_data.csv")
df.tail(8)