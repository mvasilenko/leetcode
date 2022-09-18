# design meeting scheduler
# inputs - meetings list, rooms count

meetings = [
    {"id": 1, "start": "10:00", "end": "10:30"},  # 1st room
    {"id": 2, "start": "10:00", "end": "10:15"},  # overlap, should go to 2nd room
    {"id": 3, "start": "10:00", "end": "10:30"},  # overlap, should go to 3rd room
    {"id": 4, "start": "10:15", "end": "11:00"},  # should go to 2nd room
    {"id": 5, "start": "10:30", "end": "11:30"},  # should go to 1st room
    {"id": 6, "start": "10:00", "end": "10:30"},  # 4th room
    {"id": 7, "start": "10:00", "end": "10:30"},  # 5th room
    {"id": 8, "start": "10:00", "end": "10:30"},  # cannot be scheduled
]

work_time_bitmask = ((1 << (10 * 4)) - 1)  # start at 10:00, 1 bit per 15 min interval
work_time_bitmask = work_time_bitmask << (8 * 4)  # end at 18:00, 1 bit per 15 min interval
rooms_count = 5


def time2bin(meeting_time):
    hour_str, minute_str = meeting_time.split(':')
    if minute_str == '00':
        minute = 0
    if minute_str == '15':
        minute = 1
    if minute_str == '30':
        minute = 2
    if minute_str == '45':
        minute = 3
    hour = int(hour_str) * 4
    result = hour + minute
    return result


def meet2bin(meeting):
    start = time2bin(meeting['start'])
    end = time2bin(meeting['end'])
    duration = end-start
    meet_mask = 2**duration - 1  # generate 1 for every 15 min in meeting
    result = (meeting['id'], start, duration)
    return result


def schedule_meeting(meetings, rooms_count):
    rooms = [[] for x in range(rooms_count)]
    rooms_mask = [0 for x in range(rooms_count)]
    rooms_bitpos = [40 for x in range(rooms_count)]

    for meeting in meetings:
        (meeting_id, start_pos, duration) = meet2bin(meeting)  # id, start_position in day bitmask, meet_bitmask
        scheduled = False
        for i, room in enumerate(rooms):
            # check if meeting fits room i
            if (rooms_mask[i] & work_time_bitmask) & ((2**duration-1) << start_pos) != 0:
                continue
            # if yes, add it to i's room_mask by or-ing shifted by start_pos
            rooms_mask[i] |= ((2**duration-1) << rooms_bitpos[i])
            rooms_bitpos[i] += duration
            rooms[i].append(meeting)
            scheduled = True
            break

        if not scheduled:
            print("meeting cannot be scheduled:", meeting)

    return rooms


if __name__ == "__main__":
    rooms_meeting_schedule = schedule_meeting(meetings, rooms_count)
    for room_id, schedule in enumerate(rooms_meeting_schedule):
        print(f"Schedule for room {room_id+1}: {schedule}")
