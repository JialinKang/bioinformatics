csv_input = read.csv('bioinformatics/hm5/p05pvalues.tsv', header = T, sep='\t')

df = as.data.frame(csv_input)

sorted = sort(df$pvalue)

df$pvalue = sorted

df$qvalue = df$pvalue*length(df$pvalue)/df$index

for (i in 1:length(df$pvalue)){
  if (df$qvalue[i] <= 0.05){
    print(df$qvalue[i])
  }
}

write.table(df, file = './new3.txt', sep= '\t',quote = FALSE, row.names = FALSE, col.names = TRUE)
