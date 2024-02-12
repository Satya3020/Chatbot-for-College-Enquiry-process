import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
data = pd.read_csv('course_suggestions.csv')

# Calculate the total count for each course preference
counts = data[['Course Preference 1', 'Course Preference 2']].stack().value_counts()

# Create a pie chart
plt.pie(counts.values, labels=counts.index.tolist(), autopct='%1.1f%%')
plt.title('Course Preference Distribution')
plt.show()
