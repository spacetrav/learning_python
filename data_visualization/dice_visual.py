from die import Die
import pygal

# create two D6 sided dice
die_1 = Die()
die_2 = Die()

# make some rolls and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = []
for value in range(2, max_result+1):
    hist.x_labels.append(value)

print(hist.x_labels)
hist.x_title = "Result"
hist.y_title = "Frequency of the Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')