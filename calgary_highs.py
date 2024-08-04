import csv
import matplotlib.pyplot as plt

# Check if a given string is a number or not
# Reference for this method: 
# https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-represents-a-number-float-or-int
def is_number(t):
    try:
        float(t)
        return True
    except ValueError:
        return False

# Open file containing Calgary data information
filename = 'data/calgary-climate-daily.csv'
with open(filename) as f:

    # Read the header information
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Print the headers and their positions so we don't forget
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get the daily max temps
    highs = []
    for row in reader:
        if not is_number(row[3]):
            continue
        high = float(row[3])
        highs.append(high)

print(highs)

# Plot the extracted max temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='pink')

# Format the plot
plt.title("Daily high temperatures, June-July 2024", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Display the plot
plt.show()