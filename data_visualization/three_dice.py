from die import Die
import pygal

# create two D6 sided dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# make some rolls and store results in a list
results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice " + str(len(results)) + " times"
hist.x_labels = []
for value in range(3, max_result+1):
    hist.x_labels.append(value)

print(hist.x_labels)
hist.x_title = "Result"
hist.y_title = "Frequency of the Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual3.svg')