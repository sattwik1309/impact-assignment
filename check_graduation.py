import itertools


def allow(attendance_list):
    allow = True
    for i in range(len(attendance_list) - 3):
        if attendance_list[i] == 0 and attendance_list[i+1] == 0 \
                and attendance_list[i+2] == 0 and attendance_list[i+3] == 0:
            allow = False
            break
    return allow


def calculate_probability(total_days):
    absent_present = [0, 1]

    all_attendance = [comb for comb in itertools.product(absent_present, repeat=total_days)]
    graduation_attendance = [a for a in all_attendance if allow(a)]
    graduation_day_missing = [a for a in graduation_attendance if a[-1] == 0]

    return f'{len(graduation_day_missing)}/{len(graduation_attendance)}'


if __name__ == '__main__':
    days = int(input())
    print(calculate_probability(days))
    






