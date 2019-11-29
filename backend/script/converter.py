import pandas
from scipy.spatial.distance import pdist, squareform
from sklearn.manifold import MDS
import matplotlib.pylab as plt


data = pandas.read_csv("food.csv")

print(data)
ddata = data.drop(['name'], axis=1)
# x <-> y
#ddata = pandas.DataFrame(ddata.transpose())

print(data.get(['name']))

# x<->y
print(list(data.columns))
print(ddata)

d = squareform(pdist(ddata, 'euclidean'))

df_dist = pandas.DataFrame(d)
print(df_dist)
pdata = pandas.DataFrame(MDS(n_components=2).fit_transform(df_dist))
print("result-MDS")
print(pdata)

pdata.insert(0, "name", data.get(['name'])['name'].tolist(), True)
# x <-> y
#print(len(data.columns[1:]))
#pdata.insert(0, "name", list(data.columns[1:]), True)


print(pdata)

pdata.plot(kind='scatter',x=0, y=1, color='red')
for name, x, y in pdata.values.tolist():
    plt.text(x, y, name, fontsize=12)
plt.show()



"""
dist_ddata = dist(ddata)
dist_ddata_mds = cmdscale(dist_ddata)
plot(dist_ddata_mds)
text(dist_ddata_mds, make_tuple("apple", "pear", "peach", "mango", "melon"))
t_ddata = t(ddata)
dist_t_ddata = dist(t_ddata)
dist_t_ddata_mds = cmdscale(dist_t_ddata)
plot(dist_t_ddata_mds)
text(dist_t_ddata_mds, make_tuple("gyuwon", "junyoung", "dog", "jaewon", "junsung"))
"""