import re,os,sys,csv,ast,astunparse

Dictionary = { '=': 0, '!': 1, '%': 2, '^': 4, '&': 5, '*': 6, '+': 7, '-': 8, ':': 9, '|': 10, '\\': 11, '/': 12, '<': 13, '>': 14, '?': 15, '~': 16, '1': 17, '2': 18, '3': 19, '4': 20, '5': 21, '6': 22, '7': 23, '8': 24, '9': 25, '0': 26, '[': 27, ']': 28, '{': 29, '}': 30, '(': 31, ')': 32, '@': 33, '$': 34, '#': 35, 'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61, '_': 3 }

def window (w, has):
    if len(has)==0 :
        return {}

    h = [has[0]]*w #INT_MAX
    r = 0
    Min = 0

    v = 1
    Fingerprint = {}
    while v!=len(has):
        r = (r+1)%w
        h[r] = has[v]
        v += 1

        if Min==r :
            i = (r-1)%w
            while i!=r :
                if h[i]<h[Min] :
                    Min = i
                i=(i-1+w)%w
            if h[Min] in Fingerprint:
                Fingerprint[h[Min]] += 1
            else:
                Fingerprint[h[Min]] = 1
        else :
            if h[r]<=h[Min] :
                Min = r
                if h[Min] in Fingerprint:
                    Fingerprint[h[Min]] += 1
                else:
                    Fingerprint[h[Min]] = 1
    
    return Fingerprint

def tokenization(file,cpp):

    with open(file, 'r') as file:
        data = file.read()

    if cpp: 
        tree = ast.parse(data)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                node.id = "x"
            elif isinstance(node, ast.arg):
                node.arg = "x"
            elif isinstance(node, ast.FunctionDef):
                node.name = "x"
            elif isinstance(node,ast.Attribute):
                node.attr = "x"
        data = astunparse.unparse(tree)
        data = re.sub('#[^\n]+', '', data)
        data = re.sub('import[^\n]+')
        #data = re.sub('//[^\n]+', '', data)
        #data = re.sub('\/\*([^\*\/]+|[^\*]+|[^\/]+)\*\/', '', data)
        #comments removal
        #data = re.sub('"+[^"]+"+|\'+[^\']+\'+|`+[^`]+`+', 'x', data)

    #data = re.sub('"+[^"]+"+|\'+[^\']+\'+|`+[^`]+`+', 'x', data)
    data = re.sub(' |;|,|\n|\.|`|\'|"|\t', '', data)
    data = re.sub('[A-Z]', lambda pat: pat.group(0).lower(), data)

    return data

def hashing (KGrams, K):
    Hashes = [0]*len(KGrams)
    if len(KGrams)==0 or len(KGrams[0])<K :
        return [] 
    for i in range(K):
        Hashes[0] += Dictionary[KGrams[0][K-1-i]]*(62**i)

    #print (Dictionary[KGrams[0][0]]*(62**(K-1)))
    for i in range(1,len(KGrams)):
        Hashes[i] = (Hashes[i-1] - Dictionary[KGrams[i-1][0]]*(62**(K-1))) * 62 + Dictionary[KGrams[i][K-1]]

    return Hashes

def hashTable_GST (Hashes):
    Table = {}

    for i in range(len(Hashes)):
        if Hashes[i] in Table:
            Table[Hashes[i]].append(i)
        else:
            Table[Hashes[i]] = [i]
    
    return Table

def max_match (pattern_hash, index, s, Hashes, string_index, pattern_marks, string_marks) :
    
    if index+s>len(pattern_hash) or index+2*s>=pattern_marks or string_index+s>len(Hashes) or string_index+2*s>=string_marks:
        k = min(len(pattern_hash)-index, pattern_marks-index-s+1,len(Hashes)-string_index, string_marks-string_index-s+1)
        
        for i in range(1,k):
            if pattern_hash[index+i] != Hashes[string_index+i]:
                return s+i-1
        
        return s+k-1
    elif pattern_hash[index+s] == Hashes[string_index+s]:
        return s + max_match(pattern_hash, index+s, s, Hashes, string_index+s, pattern_marks, string_marks)
    else:
        for i in range(1,s+1):
            if pattern_hash[index+i] != Hashes[string_index+i]:
                return s+i-1


def GreedyStringTiling(File_Hashes,Stub_Hashes,file_data,stub_data,K):
    File_Table = hashTable_GST(File_Hashes)

    file_markers = [1]*(len(file_data)+1)
    stub_markers = [1]*(len(stub_data)+1)

    file_markers[len(file_data)] = [-1,len(file_data),0]
    stub_markers[len(stub_data)] = [-1,len(stub_data),0]

    file_start = len(file_data)
    stub_start = len(stub_data)
    while True:
        max_length = 0
        positions = []
        file_mark = file_start
        stub_mark = stub_start
        
        i = 0
        while i<len(Stub_Hashes) :
            
            if i+K>stub_mark :
                i = stub_mark+stub_markers[stub_mark][2]
                stub_mark = stub_markers[stub_mark][1]
            else :
                if Stub_Hashes[i] in File_Table:
                    max_of_all = 0
                    index = 0
                    next_tile = 0
                    for k in File_Table[Stub_Hashes[i]] :
                        if file_mark>=k :
                            while file_markers[file_mark][0]>=k:
                                file_mark = file_markers[file_mark][0]
                        else :
                            while file_mark<k:
                                file_mark = file_markers[file_mark][1]
                        
                        prev = file_markers[file_mark][0]
                        if prev!=-1 and file_markers[prev][2]+prev>k :
                            continue
                        elif k+K>file_mark :
                            continue
                        val = max_match(Stub_Hashes,i,K,File_Hashes,k,stub_mark,file_mark)
                        if val>max_of_all:
                            max_of_all = val
                            index = k
                            next_tile = file_mark

                    if max_of_all==0:
                        i += 1
                    else:
                        if max_of_all==max_length:
                            positions.append([i,stub_mark,index,next_tile])
                        elif max_of_all > max_length:
                            positions = [[i,stub_mark,index,next_tile]]
                            max_length = max_of_all
                        i += max_of_all
                else :
                    i += 1

        if max_length==0:
            break
        else :
            for position in positions:

                prev_tile = file_markers[position[3]][0]
                
                if position[2]+max_length>position[3]:
                    continue
                elif prev_tile!=-1 and prev_tile+file_markers[prev_tile][2]>position[2]:
                    continue
                
                file_markers[position[3]][0] = position[2]
                file_markers[position[2]] = [prev_tile,position[3],max_length]
                if prev_tile!=-1:
                    file_markers[prev_tile][1] = position[2]
                else:
                    file_start = position[2]
                
                prev_tile = stub_markers[position[1]][0]
                stub_markers[position[1]][0] = position[0]
                stub_markers[position[0]] = [prev_tile,position[1],max_length]
                if prev_tile!=-1:
                    stub_markers[prev_tile][1] = position[0]
                else:
                    stub_start = position[0]
                

    string = ""
    start = 0           
    while True:
        string += file_data[start:file_start]
        if file_start==len(file_data):
            break
        start = file_start+file_markers[file_start][2]
        file_start = file_markers[file_start][1]

    return string


directory = sys.argv[1]

if sys.argv[2]=="T":
    cpp = True
else:
    cpp = False

files = [name for name in os.listdir(directory) if os.path.isfile(directory+"/"+name)]


KGrams = [0]*len(files)
Hashes = [0]*len(files)
data = [""]*len(files)

K = 10
for i in range(len(files)):
    data[i] = tokenization(directory+"/"+files[i],cpp)
    #print (data[i])
    KGrams[i] = [ data[i][x:x+K] for x in range(len(data[i])-K+1) ]
    Hashes[i] = hashing(KGrams[i], K)

if os.path.isdir(directory+"/stub"):
    print ("hi")
    stub = [name for name in os.listdir(directory+"/stub") if os.path.isfile(directory+"/stub/"+name)][0]
    stub = directory+"/stub/"+stub

    stub_data = tokenization(stub,cpp)
    Stub_KGrams = [ stub_data[x:x+K] for x in range(len(stub_data)-K+1) ]
    Stub_Hashes = hashing(Stub_KGrams, K)

    for i in range(len(files)):
        data[i] = GreedyStringTiling(Hashes[i],Stub_Hashes,data[i],stub_data,K)
        KGrams[i] = [ data[i][x:x+K] for x in range(len(data[i])-K+1) ]
        Hashes[i] = hashing(KGrams[i], K)


W = 7
fingerprints = [0]*len(files)

for i in range(len(files)):
    fingerprints[i] = window(W,Hashes[i])

Cov = [list(range(len(files))) for i in range(len(files))]

sizes = [0]*len(files)
for i in range(len(files)):
    for j in fingerprints[i]:
        sizes[i] += fingerprints[i][j]

for i in range(len(files)):
    for j in range(i+1,len(files)):
        inter = 0
        if sizes[i]>sizes[j]:
            m=j
            n=i
        else:
            m=i
            n=j
        if sizes[m]==0:
            Cov[i][j] = Cov[j][i] = 0
        else:
            for k in fingerprints[m]:
                if k in fingerprints[n]:
                    inter += min(fingerprints[i][k],fingerprints[j][k])
            Ans1 = inter/(sizes[i]+sizes[j]-inter)
            Ans2 = inter/sizes[m]
            Cov[i][j] = Cov[j][i] = (1-Ans2)*Ans1 + Ans2*Ans2

for i in range(len(files)):
    Cov[i][i] = 1.0


if not os.path.exists(directory+"/results"):
    os.makedirs(directory+"/results")
with open(directory+"/results/result.csv","w") as f:
    write = csv.writer(f)
    write.writerow(files)
    write.writerows(Cov)

