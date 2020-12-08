import argparse as vahh
ap = vahh.ArgumentParser()
tumtum = list()

t2 = "-" + other
l1 = "-" + one
ap.add_argument(l1,action='store',dest=one,help='supply an input file')
ap.add_argument(t2,action='store',dest=other,help='supply an output file')

myargs = ap.parse_args()
outfile = myargs.out
infile = myargs.inp

handle = open(infile)
lala = handle.read()

abpath = lala.rstrip()
dirs = abpath.split('/')

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
oke = 0

while oke<n:
	final = final + tumtum[oke]
	if oke!=(n-1):
		final = final + "/"
	else:
		final += "\n"
	oke = oke + 1

handle.close()
whan = open(outfile,'w')
whan.write(final)
whan.close()

quit()
quit()
