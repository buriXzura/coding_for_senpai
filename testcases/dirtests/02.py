import argparse as parso

def doublearg(one,other):
	s1 = "-" + one
	s2 = "-" + other
	ap = parso.ArgumentParser()
	ap.add_argument(s1,action='store',dest=one,help='supply input file')
	ap.add_argument(s2,action='store',dest=other,help='supply output file')
	mereargs = ap.parse_args()
	return mereargs

mereargs = doublearg("inp","out")

file1 = mereargs.inp
file2 = mereargs.out

handle = open(file1)
abpath = handle.read().rstrip()
handle.close()

dirs = abpath.split('/')
canpath = list()

for address in dirs:
	if address=='': continue
	elif address=='.': continue
	elif address=='..':
		if len(canpath)==0:continue
		else: canpath.pop()
	else: canpath.append(address)

final = "/"
n = len(canpath)
for i in range(n):
	final = final + canpath[i]
	if i!=(n-1):
		final = final + "/"
final += "\n"

nhandle = open(file2,'w')
nhandle.write(final)
nhandle.close()

quit()
