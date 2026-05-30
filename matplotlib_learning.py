import matplotlib.pyplot as plt

x = ['Ali', 'Hassan', 'Hussain', 'Abbas', 'Umar']
y = [20, 25, 30, 40, 50]

plt.plot(x,y, color = "red", linestyle = "dashed") #Draw the line graph 
#plt.show() #This function is used to show/print the graph
plt.title("Name Age Graph") # This function set the title(name) of the graph
#plt.show()

plt.scatter(x, y) # Scatter plot
plt.show()


