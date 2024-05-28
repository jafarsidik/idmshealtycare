# Copyright (c) 2024, PT IDMS and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import time_diff

class DoctorSchedule(Document):
	#def autoname(self):
	#	self.name = self.schedule_name

	def validate(self):
		if self.doctor_schedule_time_slots:
			for slots in self.doctor_schedule_time_slots:
				if slots.get("from_time") and slots.get("to_time") and slots.get("duration"):
					time_diff_in_mins = (
						time_diff(slots.get("from_time"), slots.get("to_time")).total_seconds() / 60
					)
					maximum_apps = int(abs(time_diff_in_mins) / slots.get("duration"))
					if slots.get("maximum_appointments") > maximum_apps:
						msg = _("Maximum appointments cannot be more than {0} in row #{1}").format(
							maximum_apps, slots.get("idx")
						)
						frappe.throw(msg)
