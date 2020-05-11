"""
There are several useful methods and attributes for this.

.head() returns the first few rows (the “head” of the DataFrame).
.info() shows information on each of the columns, such as the data type and number of missing values.
.shape returns the number of rows and columns of the DataFrame.
.describe() calculates a few summary statistics for each column.

.values: A two-dimensional NumPy array of values.
.columns: An index of columns: the column names.
.index: An index for the rows: either row numbers or row names.
"""


""" .sort_values() 
one column --->>> 	df.sort_values("breed")
multiple columns	--->>> df.sort_values(["breed", "weight_kg"])
"""
# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members', ascending=False)

# Print the top few rows
print(homelessness_fam.head())

# Sort homelessness by region(ascending), then descending family members(descending)
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())



""" subsetting 

To select only "col_a" of the DataFrame df, use
df["col_a"]

To select "col_a" and "col_b" of df, use
df[["col_a", "col_b"]]


There are many ways to subset a DataFrame, perhaps the most common is to use relational operators to return True or False for each row, 
then pass that inside square brackets.

dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]

You can filter for multiple conditions at once by using the "logical and" operator, &.

dogs[(dogs["height_cm"] > 60) & (dogs["col_b"] == "tan")]
"""

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members']<1000) & (homelessness['region']=='Pacific')]

# See the result
print(fam_lt_1k_pac)


"""
Subsetting rows by categorical variables

Subsetting data based on a categorical variable often involves using the "or" operator (|) to select rows from multiple categories. 
This can get tedious when you want all states in one of three different regions, for example. 
Instead, use the .isin() method, which will allow you to tackle this problem by writing one condition instead of three separate ones.

colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
"""
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness['region']=='South Atlantic') | (homelessness['region']=='Mid-Atlantic')]

# See the result
print(south_mid_atlantic)


# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)


