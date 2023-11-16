# %%
# df.dropna(inplace=True)

# df.fillna(value, inplace=True)

# df.drop_duplicates(inplace=True)

# df['column_name'] = df['column_name'].astype('desired_data_type')

# df = pd.get_dummies(df, columns=['categorical_column'])

# df.to_csv('cleaned_data.csv', index=False)

# %%
import pandas as pd

# Load the real account dataset
real_account_df = pd.read_csv('df_real.csv')

# Load the fake account dataset
fake_account_df = pd.read_csv('df_fake.csv')


# %%
# Create a new DataFrame to store the merged data
merged_df = pd.DataFrame()

# Concatenate the two DataFrames
merged_df = pd.concat([real_account_df, fake_account_df], ignore_index=True)


# %%
# Relative path (save in the current working directory)
file_path = 'merged.csv'




# %%
merged_df.to_csv(file_path, index=False)


# %%
df = pd.read_csv('merged.csv')

# %%
df.fillna(0)

# %%
import pandas as pd

# Check for null values using either isnull() or isna()
null_values = df.isnull()  # or df.isna()

# Check if any null values are present
if null_values.any().any():
    print("There are null values in the dataset.")
else:
    print("There are no null values in the dataset.")


# %%
import pandas as pd

# Check for null values using either isnull() or isna()
null_values = df.isna()  # or df.isna()

# Check if any null values are present
if null_values.any().any():
    print("There are null values in the dataset.")
else:
    print("There are no null values in the dataset.")


# %%
import pandas as pd

# Check for null values using either isnull() or isna() along columns (axis 0)
null_columns = df.isnull().any()

# Extract the column names with null values
columns_with_null_values = null_columns[null_columns].index

# Print the column names with null values
print("Columns with null values:")
for column in columns_with_null_values:
    print(column)


# %%
columns_to_fill_with_0 = ['userHasProfilPic', 'userIsPrivate', 'isFake','mediaLikeNumbers','mediaCommentNumbers','mediaCommentsAreDisabled','mediaHashtagNumbers','mediaUploadTimes','mediaHasLocationInfo','userHasHighlighReels','userHasExternalUrl','userTagsCount','automatedBehaviour','target']
df[columns_to_fill_with_0] = df[columns_to_fill_with_0].fillna(0)
print(df)

# %%
import pandas as pd

# Check for null values using either isnull() or isna() along columns (axis 0)
null_columns = df.isnull().any()

# Extract the column names with null values
columns_with_null_values = null_columns[null_columns].index

# Print the column names with null values
print("Columns with null values:")
for column in columns_with_null_values:
    print(column)


# %%
from sklearn.model_selection import train_test_split

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df[['userFollowerCount', 'userFollowingCount', 'userBiographyLength', 'userMediaCount', 'userIsPrivate', 'usernameDigitCount', 'usernameLength']],
    df['target'],
    test_size=0.25,
    random_state=42
)


# %%
from sklearn.linear_model import LogisticRegression

# Create a logistic regression classifier
clf = LogisticRegression()

# Train the classifier on the training data
clf.fit(X_train, y_train)


# %%
from sklearn.metrics import accuracy_score

# Predict the labels for the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model on the test data
accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)


# %%
from sklearn.metrics import precision_score, recall_score, f1_score

# Calculate the precision, recall, and F1 score
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1_score = f1_score(y_test, y_pred)

print('Precision:', precision)
print('Recall:', recall)
print('F1 score:', f1_score)



# %%
import numpy as np
from sklearn.linear_model import LogisticRegression


# %%
from sklearn.linear_model import LogisticRegression

# Create a logistic regression classifier
clf = LogisticRegression()

# Train the classifier on the training data
Trained_Model=clf.fit(X_train, y_train)


