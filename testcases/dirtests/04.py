import argparse as hehe

tumtum = list()

t2 = "-" + other
l1 = "-" + one
ap = hehe.ArgumentParser()
ap.add_argument(l1,action='store',dest=one,help='supply an input file')
ap.add_argument(t2,action='store',dest=other,help='supply an output file')
myargs = ap.parse_args()

infile = myargs.inp
outfile = myargs.out

handle = open(infile, 'r')
lala = handle.read()
handle.close()

abpath = lala.rstrip()
dirs = abpath.split('/')
counter = 0
dirlen = len(dirs)

while counter < dirlen:
	if address=='..':
		if len(tumtum)==0:
			counter = counter + 1
			continue
		else: tumtum.pop()
	elif address=='.':
		counter = counter + 1
		continue
	elif address=='':
		counter = counter + 1
		continue
	else:
		tumtum.append(address)
		counter = counter + 1
		continue

n = len(tumtum)
final = "/"
for i in range(n):
	final = final + tumtum[i]
	if i!=(n-1):
		final = final + "/"
	else:
		final += "\n"

whan = open(outfile,'w')
whan.write(final)
whan.close()
