from ...exceptions import raise_TpE
from ..info.class_name import class_name

__all__ = ["asgmt_branch"]

def asgmt_branch(obj, conditional, branch: dict, *, obj_sig = None, additional = None):
	def str_branch(obj, branch):
		try:
			return branch[obj]
		except KeyError:
			raise_TpE("obj when conditional == 'str'", str)

	def type_branch(obj, branch, *, obj_sig = None):
		try:
			return branch[class_name(obj)]
		except KeyError:
			raise_TpE(obj_sig, *branch.keys())
	
	return eval(type_branch(conditional, {
		"str": """eval(str_branch(conditional, {
			"str": "str_branch(obj, branch)",
			"type": "type_branch(obj, branch, obj_sig = obj_sig)"
		}))""",
		"function": "conditional(obj, branch)"
	}))
