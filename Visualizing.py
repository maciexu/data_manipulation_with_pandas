# Example 1
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size').nb_sold.sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar', x='size', y='nb_sold_by_size')

# Show the plot
plt.show()


# Example 2
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date').nb_sold.sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind='line', x='date', y='nb_sold_by_date')

# Show the plot
plt.show()


# Example 3
# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x='nb_sold', y='avg_price', kind='scatter', title='Number of avocados sold vs. average price')

# Show the plot
plt.show()


# Example 4 --->>> Price of conventional vs. organic avocados
# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()


""" missing values 
1. find missing values --->>> 
.isna()
.isna.any()
.isna.sum()

2. to do with missing values: 
remove or replace
.dropna()
.fillna(0)

"""
# Example 1
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Create a bar plot of the total number of missing values in each column.
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()


# Example 2 --->>> dropna
# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())


# Example 3 --->>> You can plot histograms for multiple variables at a time as follows:
# dogs[["height_cm", "weight_kg"]].hist()
# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()

