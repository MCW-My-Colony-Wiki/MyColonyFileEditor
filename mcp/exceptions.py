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
	def raise_error(para, corr):
		if corr is type or corr is None or type(corr) is type:
			corr = class_name(corr)
		elif type(corr) is list:
			#check items in list
			for type_ in corr:
				if type(type_) != type and type_ != type and type_ != None:
					raise_error(type_, type)
			
			if len(corr) < 2:
				corr = class_name(corr[0])
			elif len(corr) == 2:
				corr = f"'{class_name(corr[0])}' or '{class_name(corr[1])}'"
			elif len(corr) > 2:
				corr = str([class_name(type_) for type_ in corr[:-1]])[1:-1] + f" or '{class_name(corr[-1])}'"
		
		raise TypeError(f"the '{para}' must be {corr}, not {class_name(para)}")
		
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
