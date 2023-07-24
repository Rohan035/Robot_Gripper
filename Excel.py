import pandas as pd
import numpy as np

# Generate random data
np.random.seed(0)
data = np.random.rand(100, 4)  # Generate 100 rows with 4 columns of random data

# Create a DataFrame
df = pd.DataFrame(data, columns=['Feature1', 'Feature2', 'Feature3', 'Feature4'])

# Add a target column with random labels (0 or 1)
df['Target'] = np.random.choice([0, 1], size=len(df))

# Save the DataFrame to an Excel file
df.to_excel('random_data.xlsx', index=False)
