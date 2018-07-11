# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_ytd"
app_title = "Salary YTD"
app_publisher = "Alteroo"
app_description = "Employee Salary Year to Date"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "oshane@alteroo.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_ytd/css/erpnext_ytd.css"
# app_include_js = "/assets/erpnext_ytd/js/erpnext_ytd.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_ytd/css/erpnext_ytd.css"
# web_include_js = "/assets/erpnext_ytd/js/erpnext_ytd.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_ytd.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_ytd.install.before_install"
# after_install = "erpnext_ytd.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_ytd.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
  "Salary Slip": {
    "validate": "erpnext_ytd.salary_ytd.ytd.calculate_ytd"
  }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_ytd.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_ytd.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_ytd.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_ytd.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_ytd.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_ytd.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_ytd.event.get_events"
# }

