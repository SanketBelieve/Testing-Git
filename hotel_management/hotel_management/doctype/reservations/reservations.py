# Copyright (c) 2024, admin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Reservations(Document):
	def validate(self):
		room=self.room_no
		# print(room)
		room_booked = frappe.get_all(
            'Reservations',
            filters={'room_no':room },
            fields=['name']
        )
		# print(room_booked)
		# if room_booked:
		# 	frappe.throw("the room is already booked")
		# else:
		# 	self.available()
		self.check()
		self.dt_check()

	def available(self):
		room = frappe.get_doc("Managing Hotel  Rooms",self.room_no)
		room.room_availability = 'No'
		room.save()

	def check(self):
		check_out=self.check_out
		print(check_out)
		if check_out:
			room=frappe.get_doc("Managing Hotel  Rooms",self.room_no)
			print(room.room_availability)
			if room.room_availability == 'No':
				room.room_availability = 'Yes'
			print(room.room_availability)
			room.save(ignore_permissions=True)

	def dt_check(self):
		st_date=self.start_date
		room=self.room_no
		room_booked = frappe.get_all(
			'Reservations',
			filters={'room_no': room, 'start_date': st_date},
			fields=['name']
		)
		if room_booked:
			frappe.throw("Room is not available on this date") 

	def availb(self):
		room = frappe.get_doc("Managing Hotel  Rooms",self.room_no)
		room.room_availability = 'No'
		room.save()

				