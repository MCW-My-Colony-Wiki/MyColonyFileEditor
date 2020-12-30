from .tools.data import class_name

__all__ = [
	'InvalidSourceError',
	'InvalidCateError',
	'InvalidUnitError',
	'raise_TpE',
	'raise_ISE',
	'raise_ICE',
	'raise_IUE'
]

class InvalidSourceError(LookupError):
	pass

class InvalidCateError(LookupError):
	pass

class InvalidUnitError(LookupError):
	pass

def raise_TpE(para, corr):
	def raise_error(parameter, correct_type):
		if correct_type is type or type(correct_type) is type:
			correct_type = class_name(correct_type)
		elif type(correct_type) is list:
			#check items in list
			for type_ in correct_type:
				if type(type_) != type and type_ != type:
					raise_error(type_, type)
			
			if len(correct_type) < 2:
				correct_type = class_name(correct_type[0])
			elif len(correct_type) == 2:
				correct_type = f"'{class_name(correct_type[0])}' or '{class_name(correct_type[1])}'"
			elif len(correct_type) > 2:
				correct_type = str([class_name(type_) for type_ in correct_type[:-1]])[1:-1] + f" or '{class_name(correct_type[-1])}'"
		
		raise TypeError(f"the '{parameter}' must be {correct_type}, not {class_name(parameter)}")
	
	#Self check
	if type(para) != str:
		raise_error('para', str)
	
	#corr must == 'type' or list of type(int, float, list, tuple, dict....)
	if type(corr) != type and type(corr) != list:
		raise_error('corr', [type, list])
	
	#raise as return
	raise_error(para, corr)

def name_check(name):
	if type(name) != str:
		raise_TpE('name', str)

def raise_ISE(name):
	name_check(name)
	raise InvalidSourceError(f"invalid source file '{name}'")

def raise_ICE(name):
	name_check(name)
	raise InvalidCateError(f"invalid category '{name}'")

def raise_IUE(name):
	name_check(name)
	raise InvalidUnitError(f"invalid unit '{name}'")
