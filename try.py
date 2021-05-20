import google_trans_new
dict1 = google_trans_new.LANGUAGES
dict2 = {}
count = 0
for i in dict1.items(): 
    dict2[i[1]] = i[0]
print(dict2)    
