from ..info.class_name import class_name

from ...exceptions import raise_TpE

__all__ = [
    "asgmt_brench"
]

def asgmt_brench(obj, obj_arg_name, valid_obj_type):
	obj_type = class_name(obj)

	if obj_type not in valid_obj_type:
		raise_TpE(obj_arg_name, *valid_obj_type.keys())
	
	return valid_obj_type[obj_type]
