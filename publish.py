import os

os.system("rm -r resources")
os.system("rm -r posts")
os.system("markdown-folder-to-html src")
os.system("cp -a _src/ .")
os.system("rm -r _src")

if len(os.sys.argv) > 1:
	arg = os.sys.argv[1]

	if arg == '-c':
		os.system("git add .")
		os.system("git commit -m 'updating book'")
		os.system("git push")