
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTION_KEY AND_KEY DEFINE_KEY DOMAIN_KEY EFFECT_KEY EQUALITY_KEY EQUALS GOAL_KEY HYPHEN INIT_KEY LPAREN NAME NOT_KEY OBJECTS_KEY PARAMETERS_KEY PRECONDITION_KEY PREDICATES_KEY PROBLEM_KEY REQUIREMENTS_KEY RPAREN STRIPS_KEY TYPES_KEY TYPING_KEY VARIABLEpddl : domain\n            | problemdomain : LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPARENproblem : LPAREN DEFINE_KEY problem_def domain_def objects_def init_def goal_def RPARENdomain_def : LPAREN DOMAIN_KEY NAME RPARENproblem_def : LPAREN PROBLEM_KEY NAME RPARENobjects_def : LPAREN OBJECTS_KEY typed_constants_lst RPARENinit_def : LPAREN INIT_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN\n                | LPAREN INIT_KEY ground_predicates_lst RPARENgoal_def : LPAREN GOAL_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPARENrequire_def : LPAREN REQUIREMENTS_KEY require_key_lst RPARENrequire_key_lst : require_key require_key_lst\n                       | require_keyrequire_key : STRIPS_KEY\n                   | EQUALITY_KEY\n                   | TYPING_KEYtypes_def : LPAREN TYPES_KEY names_lst RPARENpredicates_def : LPAREN PREDICATES_KEY predicate_def_lst RPARENpredicate_def_lst : predicate_def predicate_def_lst\n                         | predicate_defpredicate_def : LPAREN NAME typed_variables_lst RPAREN\n                     | LPAREN NAME RPARENaction_def_lst : action_def action_def_lst\n                      | action_defaction_def : LPAREN ACTION_KEY NAME parameters_def action_def_body RPARENparameters_def : PARAMETERS_KEY LPAREN typed_variables_lst RPAREN\n                      | PARAMETERS_KEY LPAREN RPARENaction_def_body : precond_def effects_defprecond_def : PRECONDITION_KEY LPAREN AND_KEY literals_lst RPAREN\n                   | PRECONDITION_KEY literaleffects_def : EFFECT_KEY LPAREN AND_KEY literals_lst RPAREN\n                   | EFFECT_KEY literalliterals_lst : literal literals_lst\n                    | literalliteral : LPAREN NOT_KEY predicate RPAREN\n               | predicateground_predicates_lst : ground_predicate ground_predicates_lst\n                             | ground_predicatepredicate : LPAREN NAME variables_lst RPAREN\n                 | LPAREN EQUALS VARIABLE VARIABLE RPAREN\n                 | LPAREN NAME RPARENground_predicate : LPAREN NAME constants_lst RPAREN\n                        | LPAREN NAME RPARENtyped_constants_lst : constants_lst HYPHEN type typed_constants_lst\n                           | constants_lst HYPHEN typetyped_variables_lst : variables_lst HYPHEN type typed_variables_lst\n                           | variables_lst HYPHEN typeconstants_lst : constant constants_lst\n                     | constantvariables_lst : VARIABLE variables_lst\n                     | VARIABLEnames_lst : NAME names_lst\n                 | NAMEtype : NAMEconstant : NAME'
    
_lr_action_items = {'LPAREN':([0,5,7,8,12,14,19,21,22,23,31,34,35,39,42,47,50,54,58,63,64,67,72,74,79,83,87,88,89,94,97,100,102,105,108,113,114,119,122,126,131,132,135,],[4,6,11,13,18,20,30,33,-5,-6,40,48,-11,52,40,61,-17,52,-7,76,77,-18,76,-9,-22,95,-43,76,-21,103,-42,-25,111,-36,-8,120,123,120,120,-41,-35,-39,-40,]),'$end':([1,2,3,56,65,],[0,-1,-2,-3,-4,]),'DEFINE_KEY':([4,],[5,]),'DOMAIN_KEY':([6,13,],[9,9,]),'PROBLEM_KEY':([6,],[10,]),'NAME':([9,10,29,32,38,45,46,52,55,59,61,70,71,73,76,90,103,111,120,123,],[15,16,38,46,38,46,-55,66,69,71,73,46,-54,46,73,71,115,115,115,115,]),'REQUIREMENTS_KEY':([11,],[17,]),'RPAREN':([15,16,24,25,26,27,28,36,37,38,41,42,43,45,46,49,51,53,54,57,60,62,63,66,68,70,71,73,75,78,79,81,84,85,86,87,89,91,92,95,96,97,98,99,100,101,105,106,109,110,112,115,118,121,122,124,125,126,128,130,131,132,133,134,135,],[22,23,35,-13,-14,-15,-16,-12,50,-53,56,-24,58,-49,-55,65,-52,67,-20,-23,-48,74,-38,79,-19,-45,-54,87,-37,89,-22,-51,-44,96,97,-43,-21,-50,100,107,108,-42,109,-47,-25,-28,-36,117,118,-46,-32,126,-10,129,-34,131,132,-41,134,-33,-35,-39,135,-31,-40,]),'STRIPS_KEY':([17,25,26,27,28,],[26,26,-14,-15,-16,]),'EQUALITY_KEY':([17,25,26,27,28,],[27,27,-14,-15,-16,]),'TYPING_KEY':([17,25,26,27,28,],[28,28,-14,-15,-16,]),'TYPES_KEY':([18,],[29,]),'OBJECTS_KEY':([20,],[32,]),'PREDICATES_KEY':([30,],[39,]),'INIT_KEY':([33,],[47,]),'ACTION_KEY':([40,],[55,]),'HYPHEN':([44,45,46,60,80,81,91,],[59,-49,-55,-48,90,-51,-50,]),'GOAL_KEY':([48,],[64,]),'AND_KEY':([61,77,103,111,],[72,88,113,119,]),'VARIABLE':([66,71,81,95,99,115,116,127,],[81,-54,81,81,81,81,127,133,]),'PARAMETERS_KEY':([69,],[83,]),'PRECONDITION_KEY':([82,107,117,],[94,-27,-26,]),'EFFECT_KEY':([93,104,105,126,129,131,132,135,],[102,-30,-36,-41,-29,-35,-39,-40,]),'NOT_KEY':([103,111,120,],[114,114,114,]),'EQUALS':([103,111,120,123,],[116,116,116,116,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'pddl':([0,],[1,]),'domain':([0,],[2,]),'problem':([0,],[3,]),'domain_def':([5,8,],[7,14,]),'problem_def':([5,],[8,]),'require_def':([7,],[12,]),'types_def':([12,],[19,]),'objects_def':([14,],[21,]),'require_key_lst':([17,25,],[24,36,]),'require_key':([17,25,],[25,25,]),'predicates_def':([19,],[31,]),'init_def':([21,],[34,]),'names_lst':([29,38,],[37,51,]),'action_def_lst':([31,42,],[41,57,]),'action_def':([31,42,],[42,42,]),'typed_constants_lst':([32,70,],[43,84,]),'constants_lst':([32,45,70,73,],[44,60,44,86,]),'constant':([32,45,70,73,],[45,45,45,45,]),'goal_def':([34,],[49,]),'predicate_def_lst':([39,54,],[53,68,]),'predicate_def':([39,54,],[54,54,]),'ground_predicates_lst':([47,63,72,88,],[62,75,85,98,]),'ground_predicate':([47,63,72,88,],[63,63,63,63,]),'type':([59,90,],[70,99,]),'typed_variables_lst':([66,95,99,],[78,106,110,]),'variables_lst':([66,81,95,99,115,],[80,91,80,80,125,]),'parameters_def':([69,],[82,]),'action_def_body':([82,],[92,]),'precond_def':([82,],[93,]),'effects_def':([93,],[101,]),'literal':([94,102,113,119,122,],[104,112,122,122,122,]),'predicate':([94,102,113,114,119,122,],[105,105,105,124,105,105,]),'literals_lst':([113,119,122,],[121,128,130,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> pddl","S'",1,None,None,None),
  ('pddl -> domain','pddl',1,'p_pddl','parser.py',100),
  ('pddl -> problem','pddl',1,'p_pddl','parser.py',101),
  ('domain -> LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPAREN','domain',8,'p_domain','parser.py',106),
  ('problem -> LPAREN DEFINE_KEY problem_def domain_def objects_def init_def goal_def RPAREN','problem',8,'p_problem','parser.py',111),
  ('domain_def -> LPAREN DOMAIN_KEY NAME RPAREN','domain_def',4,'p_domain_def','parser.py',116),
  ('problem_def -> LPAREN PROBLEM_KEY NAME RPAREN','problem_def',4,'p_problem_def','parser.py',121),
  ('objects_def -> LPAREN OBJECTS_KEY typed_constants_lst RPAREN','objects_def',4,'p_objects_def','parser.py',126),
  ('init_def -> LPAREN INIT_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN','init_def',7,'p_init_def','parser.py',131),
  ('init_def -> LPAREN INIT_KEY ground_predicates_lst RPAREN','init_def',4,'p_init_def','parser.py',132),
  ('goal_def -> LPAREN GOAL_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN','goal_def',7,'p_goal_def','parser.py',140),
  ('require_def -> LPAREN REQUIREMENTS_KEY require_key_lst RPAREN','require_def',4,'p_require_def','parser.py',145),
  ('require_key_lst -> require_key require_key_lst','require_key_lst',2,'p_require_key_lst','parser.py',150),
  ('require_key_lst -> require_key','require_key_lst',1,'p_require_key_lst','parser.py',151),
  ('require_key -> STRIPS_KEY','require_key',1,'p_require_key','parser.py',159),
  ('require_key -> EQUALITY_KEY','require_key',1,'p_require_key','parser.py',160),
  ('require_key -> TYPING_KEY','require_key',1,'p_require_key','parser.py',161),
  ('types_def -> LPAREN TYPES_KEY names_lst RPAREN','types_def',4,'p_types_def','parser.py',166),
  ('predicates_def -> LPAREN PREDICATES_KEY predicate_def_lst RPAREN','predicates_def',4,'p_predicates_def','parser.py',171),
  ('predicate_def_lst -> predicate_def predicate_def_lst','predicate_def_lst',2,'p_predicate_def_lst','parser.py',176),
  ('predicate_def_lst -> predicate_def','predicate_def_lst',1,'p_predicate_def_lst','parser.py',177),
  ('predicate_def -> LPAREN NAME typed_variables_lst RPAREN','predicate_def',4,'p_predicate_def','parser.py',185),
  ('predicate_def -> LPAREN NAME RPAREN','predicate_def',3,'p_predicate_def','parser.py',186),
  ('action_def_lst -> action_def action_def_lst','action_def_lst',2,'p_action_def_lst','parser.py',194),
  ('action_def_lst -> action_def','action_def_lst',1,'p_action_def_lst','parser.py',195),
  ('action_def -> LPAREN ACTION_KEY NAME parameters_def action_def_body RPAREN','action_def',6,'p_action_def','parser.py',203),
  ('parameters_def -> PARAMETERS_KEY LPAREN typed_variables_lst RPAREN','parameters_def',4,'p_parameters_def','parser.py',208),
  ('parameters_def -> PARAMETERS_KEY LPAREN RPAREN','parameters_def',3,'p_parameters_def','parser.py',209),
  ('action_def_body -> precond_def effects_def','action_def_body',2,'p_action_def_body','parser.py',217),
  ('precond_def -> PRECONDITION_KEY LPAREN AND_KEY literals_lst RPAREN','precond_def',5,'p_precond_def','parser.py',222),
  ('precond_def -> PRECONDITION_KEY literal','precond_def',2,'p_precond_def','parser.py',223),
  ('effects_def -> EFFECT_KEY LPAREN AND_KEY literals_lst RPAREN','effects_def',5,'p_effects_def','parser.py',231),
  ('effects_def -> EFFECT_KEY literal','effects_def',2,'p_effects_def','parser.py',232),
  ('literals_lst -> literal literals_lst','literals_lst',2,'p_literals_lst','parser.py',240),
  ('literals_lst -> literal','literals_lst',1,'p_literals_lst','parser.py',241),
  ('literal -> LPAREN NOT_KEY predicate RPAREN','literal',4,'p_literal','parser.py',249),
  ('literal -> predicate','literal',1,'p_literal','parser.py',250),
  ('ground_predicates_lst -> ground_predicate ground_predicates_lst','ground_predicates_lst',2,'p_ground_predicates_lst','parser.py',258),
  ('ground_predicates_lst -> ground_predicate','ground_predicates_lst',1,'p_ground_predicates_lst','parser.py',259),
  ('predicate -> LPAREN NAME variables_lst RPAREN','predicate',4,'p_predicate','parser.py',267),
  ('predicate -> LPAREN EQUALS VARIABLE VARIABLE RPAREN','predicate',5,'p_predicate','parser.py',268),
  ('predicate -> LPAREN NAME RPAREN','predicate',3,'p_predicate','parser.py',269),
  ('ground_predicate -> LPAREN NAME constants_lst RPAREN','ground_predicate',4,'p_ground_predicate','parser.py',279),
  ('ground_predicate -> LPAREN NAME RPAREN','ground_predicate',3,'p_ground_predicate','parser.py',280),
  ('typed_constants_lst -> constants_lst HYPHEN type typed_constants_lst','typed_constants_lst',4,'p_typed_constants_lst','parser.py',288),
  ('typed_constants_lst -> constants_lst HYPHEN type','typed_constants_lst',3,'p_typed_constants_lst','parser.py',289),
  ('typed_variables_lst -> variables_lst HYPHEN type typed_variables_lst','typed_variables_lst',4,'p_typed_variables_lst','parser.py',297),
  ('typed_variables_lst -> variables_lst HYPHEN type','typed_variables_lst',3,'p_typed_variables_lst','parser.py',298),
  ('constants_lst -> constant constants_lst','constants_lst',2,'p_constants_lst','parser.py',306),
  ('constants_lst -> constant','constants_lst',1,'p_constants_lst','parser.py',307),
  ('variables_lst -> VARIABLE variables_lst','variables_lst',2,'p_variables_lst','parser.py',315),
  ('variables_lst -> VARIABLE','variables_lst',1,'p_variables_lst','parser.py',316),
  ('names_lst -> NAME names_lst','names_lst',2,'p_names_lst','parser.py',324),
  ('names_lst -> NAME','names_lst',1,'p_names_lst','parser.py',325),
  ('type -> NAME','type',1,'p_type','parser.py',335),
  ('constant -> NAME','constant',1,'p_constant','parser.py',340),
]