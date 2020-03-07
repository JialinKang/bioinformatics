args <- commandArgs(trailingOnly = TRUE)

csv_input = read.csv(paste("./", args[2], sep = ""), header = T, sep='\t')

df = as.data.frame(csv_input)

sorted = sort(df$pvalue)

df$pvalue = sorted

df$qvalue = df$pvalue*length(df$pvalue)/df$index

for (i in 1:length(df$pvalue)){
  if (df$qvalue[i] <= 0.05){
    print(df$qvalue[i])
  }
}

write.table(df, file = paste("./", args[4], sep = ""), sep= '\t',quote = FALSE, row.names = FALSE, col.names = TRUE)

# print(args[1])
