# from "moldy" in #django

def ready_in(self):
    # self.prep_time is a timedelta object.
    if self.prep_time.seconds >= 60 * 60:
        return format_as_hours(self.prep_time)
    if self.prep_time.seconds >= 60:
        return format_as_minutes(self.prep_time)
    return format_as_seconds(self.prep_time)