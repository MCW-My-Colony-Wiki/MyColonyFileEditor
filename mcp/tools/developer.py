import time

def used_time(func):
	def warper(*args):
		start_time = time.time()
		func_return = func(*args)
		end_time = time.time()
		print(f"function '{func.__name__}' took about {round(end_time - start_time, 5)} seconds")
		return func_return
	return warper
