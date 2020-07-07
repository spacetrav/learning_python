from die import Die
import pygal

# create two D6 sided dice
die_1 = Die(12)
die_2 = Die(12)

# make some rolls and store results in a list
results = []
for roll_num in range(1000000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides

for value in range(1, max_result+1):
    frequency = results.count(value)
    if frequency != 0:
        frequencies.append(frequency)

# print(frequencies)
all_values = []
all_possibilities = []

for value in range(1,die_1.num_sides+1):
    for value2 in range(1,die_2.num_sides+1):
        all_value = value*value2
        all_possibilities.append(all_value)
        if all_value not in all_values:
            all_values.append(value*value2)

all_possibilities.sort()
# print(all_possibilities)
all_values.sort()

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice " + str(len(results)) + " times and multiplying result"
hist.x_labels = all_values
# print(hist.x_labels)
# print(len(frequencies))
# print(len(hist.x_labels))
# print(hist.x_labels)
hist.x_title = "Result"
hist.y_title = "Frequency of the Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_multiply12.svg')