# admin 0
self.admin0_text.delete('1.0', END)
if not self.answers[i]["Country"]:
    self.admin0_text.tag_config(background="red")
else:
    self.admin0_text.tag_config(background="white")
    self.admin0_text.insert(INSERT, self.answers[i]["Country"])
# iso
self.iso_text.delete('1.0', END)
if not self.answers[i]["iso"]:
    self.iso_text.tag_config(background="red")
else:
    self.iso_text.tag_config(background="white")
    self.iso_text.insert(INSERT, self.answers[i]["iso"])
# Admin 1
self.admin1_text.delete('1.0', END)
if not self.answers[i]["Admin1"]:
    self.admin1_text.tag_config(background="red")
else:
    self.admin1_text.tag_config(background="white")
    self.admin1_text.insert(INSERT, self.answers[i]["Admin1"])
# Admin 2
self.admin2_text.delete('1.0', END)
if not self.answers[i]["Admin2"]:
    self.admin2_text.tag_config(background="red")
else:
    self.admin2_text.tag_config(background="white")
    self.admin2_text.insert(INSERT, self.answers[i]["Admin2"])
# number
self.operation_number_text.delete('1.0', END)
if not self.answers[i]["OpNum"]:
    self.operation_number_text.tag_config(background="red")
else:
    self.operation_number_text.tag_config(background="white")
    self.operation_number_text.insert(INSERT, self.answers[i]["OpNum"])
# start
self.operation_start_date_text.delete('1.0', END)
if not self.answers[i]["Start"]:
    self.operation_start_date_text.tag_config(background="red")
else:
    self.operation_start_date_text.tag_config(background="white")
    self.operation_start_date_text.insert(INSERT, self.answers[i]["Start"])
# end
self.operation_end_date_text.delete('1.0', END)
if not self.answers[i]["End"]:
    self.operation_end_date_text.tag_config(background="red")
else:
    self.operation_end_date_text.tag_config(background="white")
    self.operation_end_date_text.insert(INSERT, self.answers[i]["End"])
# glide
self.glide_number_text.delete('1.0', END)
if not self.answers[i]["Glide"]:
    self.glide_number_text.tag_config(background="red")
else:
    self.glide_number_text.tag_config(background="white")
    self.glide_number_text.insert(INSERT, self.answers[i]["Glide"])
# affected
self.affected_text.delete('1.0', END)
if not self.answers[i]["Affected"]:
    self.affected_text.tag_config(background="red")
else:
    self.affected_text.tag_config(background="white")
    self.affected_text.insert(INSERT, self.answers[i]["Affected"])
# assisted
self.assisted_text.delete('1.0', END)
if not self.answers[i]["Assisted"]:
    self.assisted_text.tag_config(background="red")
else:
    self.assisted_text.tag_config(background="white")
    self.assisted_text.insert(INSERT, self.answers[i]["Assisted"])
# budget
self.operation_budget_text.delete('1.0', END)
if not self.answers[i]["OpBud"]:
    self.operation_budget_text.tag_config(background="red")
else:
    self.operation_budget_text.tag_config(background="white")
    self.operation_budget_text.insert(INSERT, self.answers[i]["OpBud"])
# host
self.host_national_society_text.delete('1.0', END)
if not self.answers[i]["Host"]:
    self.host_national_society_text.tag_config(background="red")
else:
    self.host_national_society_text.tag_config(background="white")
    self.host_national_society_text.insert(INSERT, self.answers[i]["Host"])