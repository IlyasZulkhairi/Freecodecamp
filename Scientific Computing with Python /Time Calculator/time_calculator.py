def add_time(start, duration, day = None):
  # Create list of days
  days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  days_count = 0

  # Split start time, duration time and AM PM
  start_time, period = start.split()
  start_hours, start_mins = map(int, start_time.split(":"))
  duration_hours, duration_mins = map(int, duration.split(":"))

  # Sum the hours and mins
  total_hours = start_hours + duration_hours
  total_mins = start_mins + duration_mins

  # Convert excess minutes to hours
  if total_mins >= 60:
    total_hours = total_hours + total_mins // 60
    total_mins = total_mins % 60

  # Make minute into 2 digits
  total_mins = total_mins if total_mins > 9 else "0" + str(total_mins)

  # Handle AM PM
  while total_hours >= 12:
    total_hours -= 12
    # Check if PM flip to AM, add days count
    if period == "PM":
        days_count += 1
    # Flip AM PM
    period = "AM" if period == "PM" else "PM"
  
  # If total hours = 0, change total hours = 12
  if total_hours == 0: total_hours = 12

  end_time = f"{total_hours}:{total_mins} {period}"

  # Check for day
  if day:
    day = day.lower().title()
    end_day_index = int((days_of_the_week.index(day) + days_count) % 7)
    end_day = days_of_the_week[end_day_index]
    end_time += f", {end_day}"
    
  if days_count == 1:
    return f"{end_time} (next day)"
  elif days_count > 1:
    return f"{end_time} ({days_count} days later)"
  else:
    return end_time