list= ['Lorem', 'ele', 'sit', 'incididunt', 'a', 'su', 'dom', 'ouch', 'ipsum']
d={}
for word in list:
    d.setdefault(len(word), []).append(word)

result=[d[n] for n in sorted(d)]

print (result)