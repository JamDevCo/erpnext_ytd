## Salary YTD

Employee Salary Year to Date

## Setup Guide

#### Prerequisite

At the moment, we need to manually create a Salary Year to Date table, which is based on the Salary Detail table. Afterwards, we are going to add a table field to the Salary Slip and Salary Structure DocType.

- Create a duplicated version of the Salary Detail and name it Salary Year to Date.
- Remove all fields except the ones listed below or in the screenshot:
  - salary_component
  - abbr
  - amount
<img src="https://image.ibb.co/myU998/salary_year_to_date.png" />

- Customize the Salary Slip DocType and add a table field called Salary Year to Date, which uses the Salary Year to Date Table-DocType as seen in the screenshot below. Repeat this process for the Salary Structure DocType

<img src="https://image.ibb.co/ch9WNT/row_salary_year_to_date.png" />

#### Installing erpnext_ytd

- Clone the repository into your apps folder:

```bash
cd /path/to/frappe-bench/apps/
git clone https://github.com/alteroo/erpnext_ytd.git
```

- Install the app using the following command:

```bash
cd /path/to/frappe-bench/
bench --site <site-id> install-app erpnext_ytd
```



#### License

MIT
