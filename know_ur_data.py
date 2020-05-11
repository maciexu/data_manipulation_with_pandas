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
"""







