#!/usr/bin/env python
import sys, random
categories={}
current=None
fname=sys.argv[0].replace('.py','')+'.txt'
with open(fname) as ifile:
	for l in ifile:
		lstripped = l.strip()
		if lstripped.endswith(':'):
			current=categories[lstripped]=[]
		elif lstripped:
			current.append(l)
if len(sys.argv) > 1:
	if sys.argv[1] == '--shuffle':
		with open(fname,"w") as ofile:
			for c in categories.keys():
				random.shuffle(categories[c])
				ofile.write(c+"\n"+"".join(categories[c])+"\n")
	else: print("Usage: "+ sys.argv[0] + " [--shuffle]")
else:
	deals_count = int(raw_input('Enter deals count:'))
	people_count = int(raw_input('Enter people count:'))
	statefname = fname+".state.ini"
	try:
		with open(statefname) as istatef:
			state = int(istatef.read())
	except:
		state = 0
	
	deals=[]
	for i in range(deals_count*people_count):
		state+=1
		categ_name = sorted(categories.keys())[state%len(categories)]
		categ = categories[categ_name]
		deals.append(categ_name.strip()+" "+categ[(state//len(categories)) % len(categ)])
	random.shuffle(deals)
	for p in range(people_count):
		sys.stdout.write("\n")
		map(sys.stdout.write,deals[p::people_count])
	with open(statefname, "w") as ostatef:
		ostatef.write(str(state))
