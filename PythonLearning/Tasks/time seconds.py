all_sec = int(input())
sec = all_sec % 60
minute = all_sec // 60
hour = all_sec // 3600

if all_sec < 60:
    print(f"{sec:02d}")
elif all_sec < 3600:
    print(f"{minute:02d}:{sec:02d}")
else:
    minute = minute - hour * 60
    print(f"{hour:02d}:{minute:02d}:{sec:02d}")
