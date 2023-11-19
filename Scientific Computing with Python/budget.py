class Category:
  # Instantiate objects
  def __init__(self, name):
    self.name = name
    self.ledger = []

  # Methods
  def deposit(self, amount, desciption = ""):
    self.ledger.append({"amount": amount, "description": desciption})

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    return False
    
  def check_funds(self, amount):
    # Check if amount smaller than available balance
    # Return True if smaller, indicating sufficient funds
    # Return False if bigger, indicaitng insufficient funds
    return amount <= self.get_balance()

  # Define how object should be printed when print() is called
  def __str__(self):
    # Print title line
    # Center object and pad with * characters
    title = f"{self.name:*^30}\n"
    # Ilitrate through ledger and make into items
    # Description until 23rd char and has 23 width
    # Amount max 7 chars and has 2 decimal places
    items = "".join(f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
                    for item in self.ledger)
    total = f"Total: {self.get_balance()}"
    return title + items + total

def create_spend_chart(categories):
  spend_amount = []
  for category in categories:
    spend_amount.append(round(sum(item["amount"] 
    for item in category.ledger if item["amount"] < 0),2))

  total_spending = sum(spend_amount)
  percentages = [(amount/total_spending)*100 for amount in spend_amount]

  graph = "Percentage spent by category\n"
  for i in range(100, -10, -10):
    graph += f"{i:3d}|"
    for percentage in percentages:
      if percentage >= i:
        graph += " o "
      else:
        graph += "   "
    graph += " \n"
  graph += "    " + "---"*len(categories) + "-\n"

  max_length = max(len(category.name) for category in categories)
  for i in range(max_length):
    graph += "     "
    for category in categories:
      if i < len(category.name):
        graph += f"{category.name[i]}  "
      else:
        graph += "   "

    if i < max_length - 1:
      graph += "\n"
  print(graph)
  return graph