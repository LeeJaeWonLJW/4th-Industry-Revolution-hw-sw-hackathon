getwd()
data <- read.csv("food.csv")
ddata <- data[, -1]

dist.ddata <- dist(ddata)
dist.ddata.mds <- cmdscale(dist.ddata)
plot(dist.ddata.mds)
text(dist.ddata.mds, c("apple", "pear", "peach", "mango", "melon"))

t.ddata <- t(ddata)
dist.t.ddata <- dist(t.ddata)
dist.t.ddata.mds <- cmdscale(dist.t.ddata)
plot(dist.t.ddata.mds)
text(dist.t.ddata.mds, c("one", "two", "three", "four", "five"))