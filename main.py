
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='diabetes', version=1, as_frame=True)

print(data.DESCR)

df = data.frame

df.sample(5)
df.describe()
df.dtypes

features = df.columns
selected_features = [features[1], features[2], features[4], features[5], features[6]]

features = list(df.columns)
print("Available features:", features)
selected_features = [features[1], features[2], features[4], features[5], features[6]]
print("Selected features: ", selected_features)


selected_features
data = df[selected_features[0]]

data.hist(bins=5, edgecolor = "black", figsize =(10,5))
plt.title("Plasma glucose concentration") 
plt.show()



selected_features
data = df[selected_features[1]]

data.hist(bins=5, edgecolor = "black", figsize = (10,5))
plt.title("Diastolic blood pressure")
plt.show()



selected_features
data = df[selected_features[2]]

data.hist(bins=5, edgecolor = "black", figsize=(10,5))
plt.title("Serum insulin concentration")
plt.show()



selected_features
data = df[selected_features[3]]

data.hist(bins=5, edgecolor = "black", figsize=(10, 5))
plt.title("Body mass index (weight in kg/(height in m)^2)")
plt.show()



selected_features
data = df[selected_features[4]]

data.hist(bins=5,edgecolor = "black", figsize=(10, 5))
plt.title("Diabetes pedigree function")
plt.show()




fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)



reference_feature = selected_features[4]  # The reference feature
y = df[reference_feature]

fig, axs = plt.subplots(1, len(selected_features), figsize=(20, 3))

for ax, f in zip(axs, selected_features):  # Use selected_features
    ax.scatter(df[f], y, color='blue', alpha=0.5)
    ax.set_xlabel(f)

plt.show()




reference_feature = selected_features[4]  # The reference feature
comparison_feature = selected_features[0]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()
