from functools import reduce
numbers = [90,80,74,76]
avg = reduce(lambda x,y: x+y, numbers) / len(numbers)


def lowercase_decorator(func):
	def wrapper(*args, **kwargs):
		result = func()
		return result.lower()
	return wrapper

@lowercase_decorator
def greet():
	return f"YOUR AVERAGE IS, {avg}!"

print(greet("average"))