import pickle
import pandas as pd
df = pd.read_csv('data//books.csv', usecols=['title', 'authors', 'average_rating', 'isbn13', '  num_pages', 'publication_date', 'publisher'])
with open("data//dictionary", "rb") as fp:
    dict = pickle.load(fp)
search = "potter"
#print(dict)
#print(dict[search])
#print(type(df['title'][0]))
'''
search1 = dict["potter"][0]+"|"+dict["potter"][1]+"|"+dict["potter"][2]+"|"+dict["potter"][3]+"|"+dict["potter"][4]+"|"+dict["potter"][5]+"|"+dict["potter"][6]+"|"+dict["potter"][7]+"|"+dict["potter"][8]+"|"+dict["potter"][9]
print((df.loc[df['title'].str.contains(search+"|"+search1, case=False)]))
print(dict.values())'''


'''for book_name in df['title']:
    if entry in (book_name.lower()):
        for letter in book_name.lower():
            if letter == ' ':
                count += 1
            text = text + letter
            print(text)
            if(count==space):
                break
print(text)'''

'''for book_name in df['title']:
    if "harry" in book_name.lower():

        print(book_name)'''

'''entry = "harry potter".lower()
space = entry.count(' ')+1
for book_name in df['title']:
    if entry in book_name.lower():
        text = ""
        count = 0
        for letter in book_name.lower():
            if letter == ' ':
                count += 1
            text = text + letter
            if count == space:
                break
print(text)'''

st = "harry"
ptr = []
length = len(st)
for i in range(length):
    count = 0
    nw=""
    if(st[i]==st[i-1]):
        continue
    for letter in st:
        if count == i:
            count = count + 1
            continue
        count = count + 1
        nw+=letter
    ptr.append(nw)
print(ptr)

result = df.loc[df['title'].str.contains("harry potter")]
print(df['title'])