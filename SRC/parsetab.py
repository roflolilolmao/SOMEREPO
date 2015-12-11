
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'C093F183D2371809097A1CDCAFA19738'
    
_lr_action_items = {'IS':([5,],[7,]),'$end':([1,3,4,8,9,10,16,17,18,19,21,],[-3,-1,0,-2,-4,-5,-6,-9,-8,-7,-10,]),'DOT':([1,3,9,10,16,17,18,19,21,],[-3,6,-4,-5,-6,-9,-8,-7,-10,]),'PLUS':([9,10,16,17,18,19,21,],[14,-5,-6,14,14,14,14,]),'NUMBER':([7,12,13,14,20,],[10,10,10,10,10,]),'BY':([9,10,16,17,18,19,21,],[12,-5,-6,12,12,12,12,]),'VAR':([2,11,],[5,16,]),'OF':([15,],[20,]),'MINUS':([9,10,16,17,18,19,21,],[13,-5,-6,13,13,13,13,]),'SOMETHING':([0,6,7,12,13,14,20,],[2,2,11,11,11,11,11,]),'OUT':([9,10,16,17,18,19,21,],[15,-5,-6,15,15,15,15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'EXPRESSION':([7,12,13,14,20,],[9,17,18,19,21,]),'ASSIGNMENT':([0,6,],[1,1,]),'PROGRAM':([0,6,],[4,8,]),'STATEMENT':([0,6,],[3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> STATEMENT','PROGRAM',1,'p_PROGRAM_STATEMENT','PARSER.PY',38),
  ('PROGRAM -> STATEMENT DOT PROGRAM','PROGRAM',3,'p_PROGRAM_STATEMENT','PARSER.PY',39),
  ('STATEMENT -> ASSIGNMENT','STATEMENT',1,'p_STATEMENT_EXP','PARSER.PY',47),
  ('ASSIGNMENT -> SOMETHING VAR IS EXPRESSION','ASSIGNMENT',4,'p_ASSIGNEMENT','PARSER.PY',53),
  ('EXPRESSION -> NUMBER','EXPRESSION',1,'p_EXPRESSION_NUM','PARSER.PY',58),
  ('EXPRESSION -> SOMETHING VAR','EXPRESSION',2,'p_EXPRESSION_NUM','PARSER.PY',59),
  ('EXPRESSION -> EXPRESSION PLUS EXPRESSION','EXPRESSION',3,'p_EXPRESSION_PLUS','PARSER.PY',68),
  ('EXPRESSION -> EXPRESSION MINUS EXPRESSION','EXPRESSION',3,'p_EXPRESSION_PLUS','PARSER.PY',69),
  ('EXPRESSION -> EXPRESSION BY EXPRESSION','EXPRESSION',3,'p_EXPRESSION_PLUS','PARSER.PY',70),
  ('EXPRESSION -> EXPRESSION OUT OF EXPRESSION','EXPRESSION',4,'p_EXPRESSION_PLUS','PARSER.PY',71),
]