def log(file, msg):
	# Example: log("test.log", "testing")
	log_file = open(file, "w")
	log_file.write(msg)
	log_file.close()

def read_log(file):
	log_file = open(file, "r")
	data = log_file.read()
	print(data)

def sleep(num):
	snum = int(num)
	time.sleep(snum)

def exit(code):
	exit_code = int(code)
	curses.endwin()
	sys.exit(exit_code)