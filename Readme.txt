Capabilities should include:

- ability to show:
  - income, expenses, savings & expendable income for both Jacco & Marjolein seperately and simultaneously
  - ability to show required amount to be paid monthly to joint bank account, per month.
- Edit:
  - Add additional income / expenses
  - Edit prices for expenses, income and savings
  - ability to enter changes to the above to be performed in a future month (selectable)


Optionally:

- Ability to calculate a savings goal and perpetually track it across the months

Needed pages:

- Home
 - Quick overview of both Jacco & Marjolein containing:
  - Sum of income
  - Sum of expenses
  - Predicted savings
  - expendable income
  - necessary amount to transfer to joint bank account
  - (optional) savings goal

- Jacco
  - Elaborate overview of every expense and income + calculation of expendable income
  - Graphs at the top to show:
    1) expenses vs income (bar graph)
    2) expenses category (% per category, pie chart)
- Marjolein
  - Elaborate overview of every expense and income + calculation of expendable income
  - Graphs at the top to show:
    1) expenses vs income (bar graph)
    2) expenses category (% per category, pie chart)
- changes
 - Ability to enter changes to income/expenses for future months

Needed database:
 - Table: expenses
  - fields:
    1) id
    2) Category
    3) name
    4) amount
    5) person (J, M or Joint)
 - Table: income
  - fields:
    1) id
    2) Category
    3) name
    4) amount
    5) person (J, M or Joint)
- Table: changes
  - fields:
    1) id
    2) Category (income or expense)
    3) amount
    4) month
    5) person
