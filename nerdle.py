import enum
import re

 #[   1,2,3,4,5,6,7,8,9,                   ], #0
 #[ 0,1,2,3,4,5,6,7,8,9,'+','-','*','/',   ], #1
 #[ 0,1,2,3,4,5,6,7,8,9,'+','-','*','/',   ], #2
 #[ 0,1,2,3,4,5,6,7,8,9,'+','-','*','/','='], #3
 #[ 0,1,2,3,4,5,6,7,8,9,'+','-','*','/','='], #4
 #[ 0,1,2,3,4,5,6,7,8,9,'+','-','*','/','='], #5
 #[ 0,1,2,3,4,5,6,7,8,9,'+','-','*','/','='], #6
 #[ 0,1,2,3,4,5,6,7,8,9,                   ], #7
spots = [
  [   1,            8,                     ], #0
  [ 0,1,2,            9,    '-',           ], #1
  [ 0,1,            8,                     ], #2
  [                         '-',           ], #3
  [ 0,  2,          8,9,    '-',           ], #4
  [                 8                      ], #5
  [                                     '='], #6
  [   1,2,          8,                     ], #7
]

#chars_not_in : 7 5 3 6 + 4 / *
#correct :      

#chars_in : 9 8 - = 2 1 0
inchar_patterns = [
   '.*0.*',
   '.*1.*',
   '.*2.*',
 # '.*3.*',
 # '.*4.*',
 # '.*5.*',
 # '.*6.*',
 # '.*7.*',
   '.*8.*',
   '.*9.*',
]

bad_patterns = [
    '++',    # WORKS
    '//',    # WORKS
    '///',    # WORKS
    '+++',    # WORKS
    '--',    # WORKS
    '=.*=',    # WORKS
]


for i,spot_opts in enumerate(spots):
    print(f'{i} = {spot_opts}')



opts_0 = spots[0]
opts_1 = spots[1]
opts_2 = spots[2]
opts_3 = spots[3]
opts_4 = spots[4]
opts_5 = spots[5]
opts_6 = spots[6]
opts_7 = spots[7]

idx = 200

def report_chars(expr_str):
    expr_list = [ c for c in expr_str]

    set_list = set(expr_list)
    return sorted(list(set(expr_list)))

def has_opchars(instr):
    opchars = [ '+', '-', '*', '/']

    for c in instr:
      if c in opchars:
        return True

    return False

def go_run(go_print=True):
  for o0 in opts_0:
    for o1 in opts_1:
      for o2 in opts_2:
        for o3 in opts_3:
          for o4 in opts_4:
            for o5 in opts_5:
              for o6 in opts_6:
                for o7 in opts_7:

                  expr_list = [ str( o0),str( o1),str( o2),str( o3),str( o4),str( o5),str( o6),str( o7), ]
                  expr_str = ''.join(expr_list)
                  expr_split = expr_str.split("=")
                  if len(expr_split) == 2:
                    beg_str = expr_str.split('=')[0]
                    end_str = expr_str.split('=')[1]
                  else:
                    continue

                  still_valid = True
                  for bp in bad_patterns:
                    if expr_str.find(bp) != -1:
                      still_valid = False
                      global idx
                      if idx > 0:
                        #print(f'bp: {bp:20s} for expr: {expr_str:20s}')
                        idx -= 1
                  
                  if has_opchars(end_str):
                    continue

                  for ip in inchar_patterns:
                    if re.match(ip, expr_str) == None:
                      still_valid = False
                      continue

                  if still_valid:
                    #potentially valid
                    #beg_str = ''.join(expr_list[0:5])
                    #end_str = str(o6) + str(o7)
                    try:
                       beg_expr = eval(beg_str)
                       end_expr = eval(end_str)

                       if beg_expr == end_expr:
                          #pass
                          full_eqn = beg_str+'='+end_str
                          sorted_list = report_chars(full_eqn)

                          if go_print:
                            print(f'match for : {beg_str} == {end_expr} | {sorted_list} | {full_eqn}')
                    except:
                       continue

#go_run(False)
go_run(True)


