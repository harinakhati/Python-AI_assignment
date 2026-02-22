#10. Write a program that collects daily screen-time data per app and reports which app consumes the most total time. 

#Screen Time Tracker

screen_time = {}

while True:
    app = input("App name:")
    if app == "done":
        break

    time = float(input("Time spent:"))

    screen_time[app] = screen_time.get(app, 0)+time

most_used = max(screen_time, key=screen_time.get)

print("Most used app:", most_used)
print("Total time:", round(screen_time[most_used]/60,2) )