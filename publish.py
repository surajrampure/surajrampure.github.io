import os

# create index
os.system('pandoc index.md -o index.html')

# create teaching
os.system('pandoc teaching.md -o teaching.html')

if len(os.sys.argv) > 1:
	arg = os.sys.argv[1]

	if arg == '-c':
		os.system("git add .")
		os.system("git commit -m 'updating site'")
		os.system("git push")