from die import Die
import pygal

# create a D6 and D10 sided dice
die_1 = Die()
die_2 = Die(10)

# make some rolls and store results in a list
results = []
for roll_num in range(50000):
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
hist.x_labels = []
hist.title = "Results of rolling a D6 and D10 dice 50000 times"
for num in range(2,max_result+1):
    hist.x_labels.append(str(num))

hist.x_title = "Result"
hist.y_title = "Frequency of the Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_6-10_visual.svg')