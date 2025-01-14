
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightPOWERleftLPARENRPARENDATATYPE DIVIDE EQ GE GT IDENTIFIER LE LPAREN LT MINUS NE NO NUMBER OUTPUT PLUS POWER RPAREN SET TEXT TIMES TO TYPE YES\n    statement : OUTPUT expression\n    \n    type_statement : TYPE DATATYPE\n    \n    var_assignment : SET IDENTIFIER\n    \n    statement : var_assignment TO expression\n              | var_assignment type_statement\n              | var_assignment TO expression type_statement\n    \n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | expression POWER expression\n    expression : LPAREN expression RPAREN\n    expression : YES\n               | NO\n    \n    expression : expression EQ expression\n               | expression GT expression\n               | expression LT expression\n               | expression GE expression\n               | expression LE expression\n               | expression NE expression\n    expression : NUMBERexpression : IDENTIFIER'
    
_lr_action_items = {'OUTPUT':([0,],[2,]),'SET':([0,],[4,]),'$end':([1,5,7,8,9,10,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,],[0,-1,-13,-14,-21,-22,-5,-4,-2,-7,-8,-9,-10,-11,-15,-16,-17,-18,-19,-20,-12,-6,]),'LPAREN':([2,6,11,15,16,17,18,19,20,21,22,23,24,25,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'YES':([2,6,11,15,16,17,18,19,20,21,22,23,24,25,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'NO':([2,6,11,15,16,17,18,19,20,21,22,23,24,25,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'NUMBER':([2,6,11,15,16,17,18,19,20,21,22,23,24,25,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'IDENTIFIER':([2,4,6,11,15,16,17,18,19,20,21,22,23,24,25,],[10,14,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'TO':([3,14,],[11,-3,]),'TYPE':([3,7,8,9,10,14,27,29,30,31,32,33,34,35,36,37,38,39,40,],[13,-13,-14,-21,-22,-3,13,-7,-8,-9,-10,-11,-15,-16,-17,-18,-19,-20,-12,]),'PLUS':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[15,-13,-14,-21,-22,15,15,-7,-8,-9,-10,-11,15,15,15,15,15,15,-12,]),'MINUS':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[16,-13,-14,-21,-22,16,16,-7,-8,-9,-10,-11,16,16,16,16,16,16,-12,]),'TIMES':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[17,-13,-14,-21,-22,17,17,17,17,-9,-10,-11,17,17,17,17,17,17,-12,]),'DIVIDE':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[18,-13,-14,-21,-22,18,18,18,18,-9,-10,-11,18,18,18,18,18,18,-12,]),'POWER':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[19,-13,-14,-21,-22,19,19,19,19,19,19,19,19,19,19,19,19,19,-12,]),'EQ':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[20,-13,-14,-21,-22,20,20,-7,-8,-9,-10,-11,20,20,20,20,20,20,-12,]),'GT':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[21,-13,-14,-21,-22,21,21,-7,-8,-9,-10,-11,21,21,21,21,21,21,-12,]),'LT':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[22,-13,-14,-21,-22,22,22,-7,-8,-9,-10,-11,22,22,22,22,22,22,-12,]),'GE':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[23,-13,-14,-21,-22,23,23,-7,-8,-9,-10,-11,23,23,23,23,23,23,-12,]),'LE':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[24,-13,-14,-21,-22,24,24,-7,-8,-9,-10,-11,24,24,24,24,24,24,-12,]),'NE':([5,7,8,9,10,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[25,-13,-14,-21,-22,25,25,-7,-8,-9,-10,-11,25,25,25,25,25,25,-12,]),'RPAREN':([7,8,9,10,26,29,30,31,32,33,34,35,36,37,38,39,40,],[-13,-14,-21,-22,40,-7,-8,-9,-10,-11,-15,-16,-17,-18,-19,-20,-12,]),'DATATYPE':([13,],[28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'var_assignment':([0,],[3,]),'expression':([2,6,11,15,16,17,18,19,20,21,22,23,24,25,],[5,26,27,29,30,31,32,33,34,35,36,37,38,39,]),'type_statement':([3,27,],[12,41,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> OUTPUT expression','statement',2,'p_statement_output','parser.py',15),
  ('type_statement -> TYPE DATATYPE','type_statement',2,'p_statement_type','parser.py',21),
  ('var_assignment -> SET IDENTIFIER','var_assignment',2,'p_statement_var_assignment','parser.py',27),
  ('statement -> var_assignment TO expression','statement',3,'p_statement_assignment','parser.py',53),
  ('statement -> var_assignment type_statement','statement',2,'p_statement_assignment','parser.py',54),
  ('statement -> var_assignment TO expression type_statement','statement',4,'p_statement_assignment','parser.py',55),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser.py',67),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser.py',68),
  ('expression -> expression TIMES expression','expression',3,'p_expression','parser.py',69),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser.py',70),
  ('expression -> expression POWER expression','expression',3,'p_expression','parser.py',71),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',76),
  ('expression -> YES','expression',1,'p_expression_boolean','parser.py',81),
  ('expression -> NO','expression',1,'p_expression_boolean','parser.py',82),
  ('expression -> expression EQ expression','expression',3,'p_expression_comparison','parser.py',88),
  ('expression -> expression GT expression','expression',3,'p_expression_comparison','parser.py',89),
  ('expression -> expression LT expression','expression',3,'p_expression_comparison','parser.py',90),
  ('expression -> expression GE expression','expression',3,'p_expression_comparison','parser.py',91),
  ('expression -> expression LE expression','expression',3,'p_expression_comparison','parser.py',92),
  ('expression -> expression NE expression','expression',3,'p_expression_comparison','parser.py',93),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',98),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',102),
]
