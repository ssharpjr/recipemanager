def ready_in(self):
		prep_time_min = 0
		cook_time_min = 0
		time_uom = 'min'
		hours = 0
		minutes = 0

		# Convert hours to minutes
		if self.prep_time_uom == 'hr':
			prep_time_min = self.prep_time * 60
		else:
			prep_time_min = self.prep_time
		if self.cook_time_uom == 'hr':
			cook_time_min = self.cook_time * 60
		else:
			cook_time_min = self.cook_time
		total_time = prep_time_min + cook_time_min
		# Convert to the most reasonable time
		if total_time >= 60:
			# If gt 1 hour, use hours and minutes
			time_uom = 'hrs'
			hours = total_time // 60
			minutes = total_time % 60
			if hours == 1:
				time_uom = 'hr'
		else:
			time_uom = 'mins'
		# Build the output
		if time_uom == 'hr' or 'hrs':
			time_output = str("{:g}".format(hours)) + ' ' + time_uom + \
				', ' + str("{:g}". format(minutes)) + ' mins'
		else:
			time_output = str("{:g}".format(minutes)) + ' ' + time_uom
		return time_output





# from "moldy" in #django

def ready_in2(self):
    # self.prep_time is a timedelta object.
    if self.prep_time.seconds >= 60 * 60:
        return format_as_hours(self.prep_time)
    if self.prep_time.seconds >= 60:
        return format_as_minutes(self.prep_time)
    return format_as_seconds(self.prep_time)