import frappe

def calculate_ytd(doc, method):
  gp_to_date = 101
  np_to_date = 101

  salaries = frappe.get_all("Salary Slip", fields=["*"], filters={'employee': 'EMP/0001', 'status': 'Submitted', 'start_date': (">=", "2018-01-01"), 'end_date': ("<", "2018-07-01")}, order_by='end_date')

  salary_structure = frappe.get_doc('Salary Structure', doc.salary_structure)
  salary_year_to_date = salary_structure.salary_year_to_date
  salary_structure_dict = {}

  for item in salary_year_to_date:
    salary_structure_dict[item.salary_component] = {
      'abbr': item.abbr,
      'salary_component': item.salary_component,
      'amount': 0.0
    }

  if len(salaries) > 0:
    prev_salary = salaries[-1]
    prev_salary_db = frappe.get_doc('Salary Slip', prev_salary.get('name'))

    if len(prev_salary_db.salary_year_to_date) > 0:
      for item in prev_salary_db.salary_year_to_date:
        if item.salary_component in salary_structure_dict:
          salary_structure_dict[item.salary_component]['amount'] += item.amount
    else:
      for item in prev_salary_db.earnings:
        if item.salary_component in salary_structure_dict:
          salary_structure_dict[item.salary_component]['amount'] += item.amount

      for item in prev_salary_db.deductions:
        if item.salary_component in salary_structure_dict:
          salary_structure_dict[item.salary_component]['amount'] += item.amount

  for item in doc.earnings:
    if item.salary_component in salary_structure_dict:
      salary_structure_dict[item.salary_component]['amount'] += item.amount

  for item in doc.earnings:
    if item.salary_component in salary_structure_dict:
      salary_structure_dict[item.salary_component]['amount'] += item.amount

  for item in salary_structure_dict.values():
    doc.append('salary_year_to_date', item)

