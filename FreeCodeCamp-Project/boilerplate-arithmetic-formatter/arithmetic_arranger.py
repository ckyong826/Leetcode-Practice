def arithmetic_arranger(problems,display=False):
  #declare variables
  first_line=""
  second_line=""
  dashed_line=""
  answer_line=""

  #catch length of problems error
  if len(problems)>5:
    return "Error: Too many problems."
    
  #loop list of problems
  for problem in problems:
    operator=problem.find("+")
    if operator==-1:
      operator=problem.find("-")
    if operator==-1:
      return "Error: Operator must be '+' or '-'."
    
    #find first operand
    f_op=problem[:operator].replace(" ","")
    
    #find second operand
    s_op=problem[operator+1:].replace(" ","")
    
    #find space
    lenF_op=len(f_op)
    lenS_op=len(s_op)
    space=max(lenF_op,lenS_op)
    
    #check isNum & length
    if not(f_op.isdigit() and s_op.isdigit()):
      return "Error: Numbers must only contain digits."
    if lenF_op > 4 or lenS_op > 4:
      return "Error: Numbers cannot be more than four digits."

    #stringToInteger
    f_INTop=int(f_op)
    S_INTop=int(s_op)
    
    #add space
    f_op=f_op.rjust(space+2," ")
    s_op=s_op.rjust(space," ")

    #add operator into second line
    s_op=problem[operator:operator+1]+" "+s_op

    #produce dashed_line
    dash=""
    dash=dash.rjust(space+2,"-")
    
    #produce answer_line
    if problem[operator:operator+1]=="+":
      answer=f_INTop+S_INTop
    else:
      answer=f_INTop-S_INTop
    answer=str(answer)
    answer=answer.rjust(space + 2 ," ")
    
    #append each line
    if problem==problems[len(problems)-1]:
      first_line+=(f_op)
      second_line+=(s_op)
      dashed_line+=(dash)
      answer_line+=(answer)
    else:
      first_line+=(f_op)+"    "
      second_line+=(s_op)+"    "
      dashed_line+=(dash)+"    "
      answer_line+=(answer)+"    "
    
  #produce arranged_line
  arranged=first_line+"\n"+second_line+"\n"+dashed_line
  if display==True:
    arranged+="\n"+answer_line

  return arranged