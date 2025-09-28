def time_converter(minutes):
    if minutes <= 0:
        return "00:00"
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

def main():
    minutes = 235
    correct_time = time_converter(minutes)
    print(correct_time)

main()