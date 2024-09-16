import matplotlib.pyplot as mt
import pandas as pd
import seaborn as s
heart=pd.read_csv("heart.csv")
print(heart.head(5))  #top 5 rows
print(heart.tail(5))  #last 5 rows
print(heart.shape)   #shape of data set
print(heart.isnull())
print(heart.duplicated())
print(heart.describe())
b=heart.corr()
s.heatmap(b)
mt.show()
disease=heart['target'].value_counts()
print(disease)
s.barplot(x=disease.index, y=disease.values)
mt.show()
s.scatterplot(data=heart,x='target',hue='sex')
mt.show()
sex=heart['sex'].value_counts()
s.barplot(x=sex.index,y=sex.values)
mt.show()
s.countplot(x='target', hue='sex', data=heart, palette='Set1')
mt.show()
s.countplot(x='age', data=heart, palette='Set1') 
mt.show()
s.histplot(x='age', data=heart, palette='Set1')  #age distribution
mt.title("age distribution")
mt.show()
s.histplot(x='cp', data=heart, palette='Set1')   #chest pain type
mt.show()
s.histplot(x='target', hue='cp', data=heart, palette='Set1')   #chest pain distribution
mt.title("chest pain distribution")
mt.show()
s.histplot(x='target', hue='restecg', data=heart, palette='Set1')  #bp distribution as per target
mt.title("bp distribution as per target")
mt.show()
s.histplot(x='restecg', data=heart, palette='Set1')  #bp distribution
mt.show()
s.histplot(x='sex', hue='restecg', data=heart, palette='Set1')  #bp distribution as per age
mt.show()
s.histplot(heart['age'], bins=30, kde=True, color='blue')
mt.title("bp distribution as per age")
mt.show()
s.histplot(x='chol',data=heart, palette='Set1')
mt.show()

