data(iris)
boxplot(Sepal.Length~Species, data=iris)
pairs(iris[1:4], main = 'Iris Data', pch = 21, bg = c("red", "green3","blue")[unclass(iris$Species)])
testidx <- which(1:length(iris[,1])%%5 == 0)
iristrain <- iris[-testidx,]
iristest <- iris[testidx,]
library('klaR')
nbmodel <- NaiveBayes(Species~., data=iristrain)
prediction <- predict(nbmodel, iristest[,-5])
table(prediction$class, iristest[,5])
iristest
