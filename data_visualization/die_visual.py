from die import Die
import pygal

# create a D6
die = Die()

# make some rolls and store results in a list
results = []
for roll_num in range(1000000000):
    result = die.roll()
    results.append(result)

# analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 " + str(len(results)) + " times"
hist.x_labels = []
for value in range(1, die.num_sides+1):
    hist.x_labels.append(value)
print(hist.x_labels)
hist.x_title = "Result"
hist.y_title = "Frequency of the Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')