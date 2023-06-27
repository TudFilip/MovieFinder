import matplotlib.pyplot as plt

train_accuracy = 73.62
validation_accuracy = 74.46
test_accuracy = 69.54

labels = ['Antrenare', 'Validare', 'Testare']
values = [train_accuracy, validation_accuracy, test_accuracy]
colors = ['green', 'blue', 'orange']

plt.barh(labels, values, color=colors)
plt.xlabel('Acuratețea')
plt.title('Acuratețea la antrenare, testare și validare')

plt.show()
