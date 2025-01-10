from datetime import datetime

current_time = datetime.now()
timestamp = current_time.timestamp()

print("Seconds since January 1, 1970:", "{:,.4f}".format(timestamp), "or", "{:.3}".format(timestamp), "in scientific notation")
print(current_time.strftime("%b %d %Y"))
