from ...exceptions import raise_TpE
from ..info.class_name import class_name

__all__ = ["asgmt_brench"]


def asgmt_brench(obj, brench_type: str, brench: dict, *, obj_sig = None):
	def str_brench(obj, brench):
		if type(obj) is not str:
			raise_TpE("obj when brench_type == 'str'", str)

		return brench[obj]

	def type_brench(obj, brench, obj_sig):
		obj_type = class_name(obj)
		
		if obj_type not in brench:
			raise_TpE(obj_sig, *brench.keys())
		
		return brench[obj_type]

	return eval(str_brench(brench_type, {
		"str": "str_brench(obj, brench)",
		"type": "type_brench(obj, brench, obj_sig)"
		}))