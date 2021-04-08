import json
jfin = []
data = open('mepointize.data','r')
x = []
y = []
unparseddata = data.readlines()

for datalet in unparseddata:
    try:
        i,j = datalet.split(',')
        x.append(float(i))
        y.append(float(j))
    except:
        print("MESSED" , datalet)
print(type(i))

for _ in range(len(x)):
    a,b = x[_],y[_]
    jdat = json.dumps({
       'x':a ,
       'y':b
    })
    jfin.append(jdat)

print(jfin[0])
jfile = open("jsondata.json",'w')

jfile.write('{')
c = 0;
for jl in jfin:
    jfile.write(f'"{c}":')
    jfile.write(jl)
    jfile.write(',')
    c+=1
jfile.write('}')