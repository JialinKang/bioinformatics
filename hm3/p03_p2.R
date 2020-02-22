library('e1071');
library('ggplot2');
library('ROCR');


# load the data
mutations_path = 'bioinformatics/hm3/p03_Kato_P53_mutants_200.txt'
mutation = read.table(mutations_path, header = T)
#mutation = mutation[,-1]
#mutation = mutation[-1,]

# shuffle the data
n = nrow(mutation)
shuffle = sample(1:n, n)
mutation_shuffle = mutation[shuffle,]

# creat empty folder
folder_test = vector(mode = 'list')
folder_train = vector(mode = 'list')
predplot = vector(mode = 'list')

j=1

for(i in seq(0, 0.9, 0.33)){
  folder_test[[j]] = mutation_shuffle[(n*i):(n*(i+0.33)-1),]
  folder_train[[j]] = mutation_shuffle[-((n*i):(n*(i+0.33)-1)),]
  
  # train svm mode and test it result
  svm_2 <- svm(ASA.MUT ~., folder_train[[j]])
  pd_scores <- predict(svm_2, folder_test[[j]])
  
  predplot$'predictied'[[j]] = pd_scores
  predplot$'tables'[[j]] = folder_test[[j]]$CLASS
  
  j = j+1
}

pred <- prediction(predplot$predictied, predplot$tables)
perf <- performance(pred,"tpr","fpr")
pdf('./3-corss.pdf')
plot(perf,col="grey82",lty=3)
plot(perf, lwd=3,avg="vertical",spread.estimate="boxplot",add=T)
dev.off()