import argparse

def give_one_arg(single):
	s1 = "-" + single
	ap = argparse.ArgumentParser()
	ap.add_argument(s1,action='store',dest=single,help='supply an input file')
	myargs = ap.parse_args()
	return myargs

def give_two_args(one,other):
	s1 = "-" + one
	s2 = "-" + other
	ap = argparse.ArgumentParser()
	ap.add_argument(s1,action='store',dest=one,help='supply an input file')
	ap.add_argument(s2,action='store',dest=other,help='supply an output file')
	myargs = ap.parse_args()
	return myargs

myargs = give_two_args("inp","out")

infile = myargs.inp
outfile = myargs.out

handle = open(infile, 'r')
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

nhandle = open(outfile,'w')
nhandle.write(final)
nhandle.close()

quit()
