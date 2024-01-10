import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm

# Load data from CSV
data = pd.read_csv('data2-1.csv', names = ['Salary'])
salary_values = data['Salary']

# Calculate mean and standard deviation
mean_salary = np.mean(salary_values)
std_dev = np.std(salary_values)

# Create a probability density function
xmin , xmax = min(salary_values) , max(salary_values)
x_values = np.linspace(xmin , xmax , 100)
pdf_values = norm.pdf(x_values , mean_salary , std_dev)

# Plot histogram and probability density function
plt.hist(salary_values , bins=20 , density=True , alpha=0.5 ,
         color='b' , label='Histogram')
plt.plot(x_values , pdf_values , 'r-' , lw=2 , label='PDF')

# Calculate X (e.g., 5th percentile)
percentile_5 = np.percentile(salary_values , 5)

# Add mean and X values to the plot
plt.axvline(mean_salary , color='k' , linestyle='dashed' ,
            linewidth=2 , label='Mean Salary = '+str(mean_salary))
plt.axvline(percentile_5 , color='g', linestyle='dashed' , linewidth=2 ,
            label='X (5th Percentile)='+str(percentile_5))

# Display mean and X values on the graph
plt.text(mean_salary + 5000 , 0.00012 , '$\~{{W}}$: {:.2f}'.format(mean_salary) ,
         verticalalignment='bottom' , horizontalalignment='left' ,
         color='black' , fontsize=10)
plt.text(percentile_5 + 5000, 0.00015, 'X: {:.2f}'.format(percentile_5),
         verticalalignment='bottom' , horizontalalignment='left',
         color='green' , fontsize=10)

# Set labels and title
plt.xlabel('Annual Salary')
plt.ylabel('Probability Density')
plt.title('Probability Density Function and Histogram of Annual Salaries')
plt.legend()

# Display the plot
plt.show()

# Print the values
print("Mean Salary: {:.2f}".format(mean_salary))
print("X (5th Percentile): {:.2f}".format(percentile_5))
