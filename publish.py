import os

# create index
os.system('pandoc index.md -o index.html')

# create teaching
os.system('pandoc teaching/index.md -o teaching/index.html')
os.system('pandoc teaching/ds100.md -o teaching/ds100.html')
os.system('pandoc teaching/cs61a.md -o teaching/cs61a.html')
os.system('pandoc teaching/data8.md -o teaching/data8.html')


# create courses
os.system('pandoc courses/index.md -o courses/index.html')

if len(os.sys.argv) > 1:
	arg = os.sys.argv[1]

	if arg == '-c':
		os.system("git add .")
		os.system("git commit -m 'updating site'")
		os.system("git push")