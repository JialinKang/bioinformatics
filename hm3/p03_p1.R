library('kernlab')
library('e1071')
library(ROCR)

# Get the spam database into R
data(spam)
# Split into a training/test set of 80% / 20%
index <- sample(2,nrow(spam),replace = TRUE,prob=c(0.7,0.3))
traindata <- spam[index==1,]
testdata <- spam[index==2,]
# Use SVM with a kernel, Train the SVM on the 80% training set
svm_2 <- svm(make ~., traindata)
pd_scores <- predict(svm_2, testdata)
pred_2 <- prediction(pd_scores, testdata$type)
perf_2 <- performance(pred_2, 'tpr', 'fpr')
pdf('bioinformatics/hm3/svm_8020.pdf')
plot(perf_2)
dev.off()
# shuffle the dataset
shuffle = sample(1:4601, 4601)
spam_shuffle = spam[shuffle,]

# creat empty folder
folder_test = vector(mode = 'list')
folder_train = vector(mode = 'list')
predplot = vector(mode = 'list')

# creat 10 folders
j=1
n = nrow(spam_shuffle)
for(i in seq(0, 0.9, 0.1)){
  folder_test[[j]] = spam_shuffle[(n*i):(n*(i+0.1)-1),]
  folder_train[[j]] = spam_shuffle[-((n*i):(n*(i+0.1)-1)),]
  
  # train svm mode and test it result
  svm_10 <- svm(make ~., folder_train[[j]])
  pd_scores <- predict(svm_2, folder_test[[j]])
  
  predplot$'predictied'[[j]] = pd_scores
  predplot$'tables'[[j]] = folder_test[[j]]$type
  
  # plot the prediction scores
  #pred_2 <- prediction(pd_scores, folder_test[[j]]$type)
  #perf_2 <- performance(pred_2, 'tpr', 'fpr')
  #plot(perf_2)
  
  j = j+1
}

pred <- prediction(predplot$predictied, predplot$tables)
perf <- performance(pred,"tpr","fpr")
pdf('./k-corss.pdf')
plot(perf,col="grey82",lty=3)
plot(perf, lwd=3,avg="vertical",spread.estimate="boxplot",add=T)
dev.off()

