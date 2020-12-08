from argparse import *

def give_one_arg(single):
	s1 = "-" + single
	ap = ArgumentParser()
	ap.add_argument(s1,action='store',dest=single,help='supply an input file')
	maroargs = ap.parse_args()
	return maroargs

s2 = "-" + other
s1 = "-" + one
ap = ArgumentParser()
ap.add_argument(s1,action='store',dest=one,help='supply an input file')
ap.add_argument(s2,action='store',dest=other,help='supply an output file')
maroargs = ap.parse_args()

infile = maroargs.inp
outfile = maroargs.out

handle = open(infile)
repl = handle.read()
handle.close()

cancan = list()
abpath = repl.rstrip()
dirs = abpath.split('/')

for address in dirs:
	if address=='.': continue
	elif address=='': continue
	elif address=='..':
		if len(cancan)==0:continue
		else: cancan.pop()
	else: cancan.append(address)

n = len(cancan)
final = "/"
for i in range(n):
	final = final + cancan[i]
	if i!=(n-1):
		final = final + "/"
final += "\n"

nhandle = open(outfile,'w')
nhandle.write(final)
nhandle.close()

quit()
