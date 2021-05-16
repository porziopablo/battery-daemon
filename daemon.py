import sys, os, time, atexit, signal

class Daemon:
	"""A generic daemon class. Usage: subclass the `Daemon` class and override the `run()` method."""

	def __init__(self, pidfile):
		self.pidfile = pidfile

	def fork(self, forkID):
		try: 
			pid = os.fork() 
			if pid > 0:
				sys.exit(0) # exit parent process 
		except OSError: 
			sys.stderr.write('fork #{0} failed: {1}\n'.format(forkID, OSError))
			sys.exit(1)
	
	def daemonize(self):
		"""Deamonize class. UNIX double fork mechanism."""

		# first fork
		self.fork(1)
	
		# decouple from parent environment
		os.chdir('/') 
		os.setsid() 
		os.umask(0) # all files to be created as 0666 or world-writable  
	
		# second fork
		self.fork(2)
	
		# redirect standard file descriptors
		sys.stdout.flush()
		sys.stderr.flush()
		si = open(os.devnull, 'r')
		so = open(os.devnull, 'a+')
		se = open(os.devnull, 'a+')

		os.dup2(si.fileno(), sys.stdin.fileno())
		os.dup2(so.fileno(), sys.stdout.fileno())
		os.dup2(se.fileno(), sys.stderr.fileno())

		# upon normal termination, the pidfile is deleted
		atexit.register(self.delpid)

		# write pidfile
		pid = str(os.getpid())
		with open(self.pidfile,'w+') as f:
			f.write(pid + '\n')
	
	def delpid(self):
		"""Deletes pidfile."""
		os.remove(self.pidfile)

	def start(self):
		"""Starts daemon."""

		# check for a pidfile to see if the daemon already runs
		try:
			with open(self.pidfile,'r') as pf:

				pid = int(pf.read().strip())
		except IOError:
			pid = None
	
		if pid:
			message = "pidfile {0} already exist. Daemon already running?\n"
			sys.stderr.write(message.format(self.pidfile))
			sys.exit(1)
		
		# starts daemon
		self.daemonize()
		self.run()

	def stop(self):
		"""Stops daemon."""

		# get the pid from the pidfile
		try:
			with open(self.pidfile,'r') as pf:
				pid = int(pf.read().strip())
		except IOError:
			pid = None
	
		if not pid:
			message = "pidfile {0} does not exist. Daemon not running?\n"
			sys.stderr.write(message.format(self.pidfile))
			return # not an error in a restart

		# try gracefully killing daemon process	
		try:
			while 1:
				os.kill(pid, signal.SIGTERM)
				time.sleep(0.1)
		except OSError as err:
			e = str(err.args)
			if e.find("No such process") > 0:
				if os.path.exists(self.pidfile):
					os.remove(self.pidfile)
			else:
				print (str(err.args))
				sys.exit(1)

	def restart(self):
		"""Restarts daemon."""
		self.stop()
		self.start()

	def run(self):
		"""Method to be overwritten with `Daemon` subclass.
		
		It will be called after the process has been daemonized by `start()` or `restart()`."""
