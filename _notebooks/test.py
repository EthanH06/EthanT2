import seaborn as sns

# Load the titanic dataset
titanic_data = sns.load_dataset('titanic')

print("Titanic Data")


print(titanic_data.columns) # titanic data set
display(titanic_data[['survived','pclass', 'sex', 'age', 'sibsp', 'parch', 'class', 'fare', 'embark_town', 'alone']]) # look at selected columns