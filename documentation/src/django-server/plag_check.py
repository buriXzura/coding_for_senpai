#Imports
import re,os,sys,csv

##assigns numbers to possible characters encountered in the code files inputted
Dictionary = { '=': 0, '!': 1, '%': 2, '^': 4, '&': 5, '*': 6, '+': 7, '-': 8, ':': 9, '|': 10, '\\': 11, '/': 12, '<': 13, '>': 14, '?': 15, '~': 16, '1': 17, '2': 18, '3': 19, '4': 20, '5': 21, '6': 22, '7': 23, '8': 24, '9': 25, '0': 26, '[': 27, ']': 28, '{': 29, '}': 30, '(': 31, ')': 32, '@': 33, '$': 34, '#': 35, 'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61, '_': 3 }

def window (w, has):

    """! This function builds windows and selects fingerprints using hash values passed.
    @param w   size of the window to be formed
    @param has  list of hash values for the file

    Value w functions to check whether the result of window forming is already
    suitable with value w that has been determined.

    Fingerprint selection:
        It is conducted by selecting the minimum hash value of each different window that has been made before.
        If there are similar values in a different window, just choose one of those value to be the fingerprint.
        This process uses the looping function to select the minimum value on each window and
        array_unique function to ensure that there is no similar value on the array as the result of
        fingerprint selection.
    @return  fingerprints dictionary
    """

    #checks for empty file
    if len(has)==0 :
        return {}

    h = [has[0]]*w #INT_MAX
    #to store hash values for a window

    r = 0 #variable saves index of the last selected fingerprint
    Min = 0 #Variable saves the index of minimum hash in the current window

    v = 1
    Fingerprint = {}
    while v!=len(has):
        r = (r+1)%w
        h[r] = has[v] # storing hash values to window
        v += 1  #keeps track of index in the hash list passed

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
    """! This function is for refining the data file passed by the following steps:
    -if the data file given is a cpp file
        *removing the comments(single line & multi lined)
    -if cpp/not cpp
        *replace the strings and variables by X
        *remove punctuations,newline char,spaces and convert all letters to lowercase

    @param file files to be tokenized
    @param cpp boolean value depicting whether passed file is cpp or not
    @param data storing data in single file out of a list of files passed
    @return  tokenized data ie. data free from punctuations, comments, newline char, comments having transformed variables
    """

    with open(file, 'r') as file:
        data = file.read()


    if cpp:
        data = re.sub('//[^\n]+', '', data)
        data = re.sub('\/\*([^\*\/]+|[^\*]+|[^\/]+)\*\/', '', data)
        #removal of comments

    data = re.sub('"+[^"]+"+|\'+[^\']+\'+|`+[^`]+`+', 'x', data)
    data = re.sub(' |;|,|\n|\.', '', data)
    data = re.sub('[A-Z]', lambda pat: pat.group(0).lower(), data)

    return data

def hashing (KGrams, K):

    """! This function maps an arbitrarily large string (KGrams) to hashes which uniquely identify the original string.
    The rolling hash function makes it possible to efficiently compute the current hash of the i th
    k-gram from the preceding hash of the i−1 th k-gram in constant time.

    @param KGrams string whose hash value has to be returned
    @param K  minimum length of kgram beyond which hash value will be computed
    @return  hash of inputted KGram
    """

    Hashes = [0]*len(KGrams)
    #return empty if kgram is empty or length of k garm is less than the passed threshhold
    if len(KGrams)==0 or len(KGrams[0])<K :
        return []
    for i in range(K):
        Hashes[0] += Dictionary[KGrams[0][K-1-i]]*(62**i)

    #print (Dictionary[KGrams[0][0]]*(62**(K-1)))
    for i in range(1,len(KGrams)):
        Hashes[i] = (Hashes[i-1] - Dictionary[KGrams[i-1][0]]*(62**(K-1))) * 62 + Dictionary[KGrams[i][K-1]]

    return Hashes

def hashTable_GST (Hashes):

    """! This function creats a hash table, which maps keys to hash values:
    it appends index i to the key hashes[i] if hashes[i] already exits in the table;
    else creates a new mapping from the key hashes[i] to i

    @param Hashes   list of Hash values to inserted into the hash table
    @return  table created
    """

    Table = {}

    for i in range(len(Hashes)):
        if Hashes[i] in Table:
            Table[Hashes[i]].append(i)
        else:
            Table[Hashes[i]] = [i]

    return Table

def max_match (pattern_hash, index, s, Hashes, string_index, pattern_marks, string_marks) :

    """! This function gives the length of maximum string match at the given starting from the given indices.

    @param pattern_hash list of hash values of string 1
    @param Hashes list of hash values of string 2
    @param index the index for string 1 from where the match is to be found
    @param string_index the index for string 2 from where the match is to be found
    @param s the value of K for the K-gram hashing
    @param pattern_marks the closest index in the right neighbourhood for which a match's already found in string1
    @param pattern_marks the closest index in the right neighbourhood for which a match's already found in string2
    @return returns the size of the match

    """

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

    """! This function implements the running-karp-rabin-greedy-string-tiling strategy.
    It finds the longest common substring(s) in the given 2 strings and then repeats
    the process by selecting the longest common substring(s) in the remaining strings.

    @param File_Hashes list of hashes of string 1
    @param Stub_Hashes list of hashes of string 2
    @param file_data string 1
    @param stub_data string 2
    @param K <he K in K-gram Hashing
    @return string 1 after removal of the common substrings

    """
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

##directory containing files that need to be checked for plagarism
directory = sys.argv[1]

#checks whether input files are of type cpp or not
if sys.argv[2]=="T":
    cpp = True
else:
    cpp = False

##list of files in the selected directory
files = [name for name in os.listdir(directory) if os.path.isfile(directory+"/"+name)]

##list of length equal to number of files; for storing KGram for i th file at the i th index
KGrams = [0]*len(files)
##list of length equal to number of files; for storing Hash Values for i th file at the i th index
Hashes = [0]*len(files)
##list of length equal to number of files; for storing tokenized data for i th file at the i th index
data = [""]*len(files)

##value of K for the KGrams function
K = 10
for i in range(len(files)):
    data[i] = tokenization(directory+"/"+files[i],cpp)
    #print (data[i])
    KGrams[i] = [ data[i][x:x+K] for x in range(len(data[i])-K+1) ]
    Hashes[i] = hashing(KGrams[i], K)

#if user has provided a stub file
if os.path.isdir(directory+"/stub"):
    #print ("hi")
    ##storing path of the stubfile in the directory
    stub = [name for name in os.listdir(directory+"/stub") if os.path.isfile(directory+"/stub/"+name)][0]
    stub = directory+"/stub/"+stub

    #follow similar process of tokenization ,KGram formation and hash value calcultion for the stub file

    ##stores tokenized form of the stub file
    stub_data = tokenization(stub,cpp)

    ##stores the result of performing KGrams on the tokenized stub file
    Stub_KGrams = [ stub_data[x:x+K] for x in range(len(stub_data)-K+1) ]

    ##stores the result of running hashing on Stub_KGrams
    Stub_Hashes = hashing(Stub_KGrams, K)

    #GreedyStringTiling fn called for each file
    for i in range(len(files)):
        data[i] = GreedyStringTiling(Hashes[i],Stub_Hashes,data[i],stub_data,K)
        KGrams[i] = [ data[i][x:x+K] for x in range(len(data[i])-K+1) ]
        Hashes[i] = hashing(KGrams[i], K)

#build windows and select fingerprints

##sets the length of the window for the window function
W = 7
fingerprints = [0]*len(files)

for i in range(len(files)):
    fingerprints[i] = window(W,Hashes[i]) #stores list of fingerprints corresponding to each file

##nxn matrix for storing similarity measures corresponding to each file pair, where n is the number of files
Cov = [list(range(len(files))) for i in range(len(files))]

##list whose ith index stores sum of fingerprints of ith file
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

# similarity measure of file with itself is 1
for i in range(len(files)):
    Cov[i][i] = 1.0

#make directory for results if not already present
if not os.path.exists(directory+"/results"):
    os.makedirs(directory+"/results")

with open(directory+"/results/result.csv","w") as f:
    ##a csv writer for creating the csv files with the result of the plaigarism check
    write = csv.writer(f)
    write.writerow(files)
    write.writerows(Cov)
