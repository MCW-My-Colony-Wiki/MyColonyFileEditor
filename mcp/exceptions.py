from .tools.info.class_name import class_name

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

class PageNotWorkError(ConnectionError):
	pass

def raise_TpE(para, *valid_types):
	if not valid_types:
		raise ValueError("the 'valid_types' can't be None")
	
	def raise_error(para, *valid_types):
		valid_types_len = len(valid_types)
		valid_types = [f"'{class_name(Type)}'" if type(Type) != str else f"'{Type}'" for Type in valid_types]
		
		if valid_types_len < 2:
			valid_types = valid_types[0]
		elif valid_types_len >= 2:
			valid_types = ", ".join(valid_types[:-1]) + f' or {valid_types[-1]}'
		
		raise TypeError(f"the '{para}' must be {valid_types}, not {class_name(para)}")
	
	#self check
	if type(para) != str:
		raise_error('para', str)
	
	#raise it as return
	raise_error(para, *valid_types)

def raise_ISE(name):
	raise InvalidSourceError(f"invalid source file '{name}'")

def raise_ICE(name):
	raise InvalidCateError(f"invalid category '{name}'")

def raise_IUE(name):
	raise InvalidUnitError(f"invalid unit '{name}'")
