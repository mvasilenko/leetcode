# parse facebook open hours to the table
# day[, day...]: open_hours[, open_hours...]
inp = {
     "mon_1_open": "09:00",
     "mon_1_close": "13:00",
     "tue_1_open": "09:00",
     "tue_1_close": "13:00",
     "wed_1_open": "16:00",
     "wed_1_close": "20:00",
     "thu_1_open": "09:00",
     "thu_1_close": "13:00",
     "fri_1_open": "09:00",
     "fri_1_close": "13:00",
     "sat_1_open": "09:00",
     "sat_1_close": "14:00",
     "mon_2_open": "16:00",
     "mon_2_close": "20:00",
     "thu_2_open": "16:00",
     "thu_2_close": "20:00",
}

desired_result = '''Mon, Thu: 09:00-13:00, 16:00-20:00
Tue, Fri: 09:00-13:00
Wed: 16:00-20:00
Sat: 09:00-14:00'''

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

schedule = {}
for key, time in inp.items():
     day = key[0:3]
     day_part = int(key[4])
     oc = key[6:]
     if not schedule.get(day):
         schedule[day] = [{}]
     schedule[day][day_part-1][oc] = time

short_schedule = {}
for day, hours_list in schedule.items():
     key_hours = []
     for hour in hours_list:
         if not hour: continue
         key_hours.append(f"{hour['open']}-{hour['close']}")
     key = ', '.join(key_hours)
     if not short_schedule.get(key):
          short_schedule[key] = []
     short_schedule[key].append(day.capitalize())

result = ''
for hours, days in short_schedule.items():
     result += ', '.join(days) + ': ' + hours + '\n'
result = result.strip()

print(result == desired_result)