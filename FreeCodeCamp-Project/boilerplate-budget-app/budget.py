class Category:

  def __init__(self,name):
    self.name=name
    self.ledger=[]

  def __str__(self):
    printed_name=self.name.center(30,"*")+'\n'
    for i in range(len(self.ledger)):
      s = f"{self.ledger[i]['description'][:23]:<23}{self.ledger[i]['amount']:>7.2f}" +'\n'
      printed_name+=s
    printed_name+=f"Total: {self.get_balance():.2f}"
    return printed_name 

  def check_funds(self,amount):
    if self.ledger[0]["amount"]>=amount:
      return True
    else:
      return False
    
  def deposit(self,amount,description=""):
    dep={"amount":amount, "description":description}
    self.ledger.append(dep)

  def withdraw(self,amount,description=""):
    if self.check_funds(amount):
      dep={"amount":-amount, "description":description}
      self.ledger.append(dep)
      return True
    else:
      return False

  def get_balance(self):
    if self.ledger!=[]:
      return sum(entry["amount"] for entry in self.ledger)
    else:
      return 0
    
  def transfer(self,amount,category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to " + category.name)
      category.deposit(amount,"Transfer from " + self.name)
      return True
    else:
      return False
  
def create_spend_chart(categories):
  #delcare variables
  length=len(categories)
  totalWD=[0]*length
  total=0
  percentage={
    100:"",90:"",80:"",70:"",60:"",50:"",40:"",30:"",20:"",10:"",0:"",
  }

  #find percentage
  for i in range(length):
    totalWD[i]+=(categories[i].ledger[0]["amount"]-categories[i].get_balance())
    total+=totalWD[i]
  for i in range(length):
    totalWD[i]=totalWD[i]/total*100
    totalWD[i]=(totalWD[i]//10)*10
    value=0
    while value<=totalWD[i]:
      percentage[value]+=" o "
      value+=10
    while value<=100:
      percentage[value]+="   "
      value+=10
  for i in range(11):
    percentage[i*10]+=" "

  #print chart
  chart="Percentage spent by category"+'\n'
  
  #print percentage
  for i in percentage:
    chart+=f"{i:>3}|"+percentage[i]+'\n'
  chart+="    "
  
  #print "-"
  for i in range(length):
    chart+="---"
  chart+='-\n'
    
  #find longest length of category name
  maxNameLength = max(len(category.name) for category in categories)

  #print row
  for i in range(maxNameLength):
    row=["    "]*maxNameLength
    for j in range(length):
      if i<len(categories[j].name):
        row[i]+=f" {categories[j].name[i]} "
      else:
        row[i]+="   "
    if i==(maxNameLength-1):
      row[i]+=' '
    else:
      row[i]+=' \n'
    chart+=row[i] 
  return chart
      