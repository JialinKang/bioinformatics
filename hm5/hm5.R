library(getopt);


command=matrix(c( 
  'input', 'i', 2,'character', '',
  'output', 'o', 2, 'character', ''),byrow=T,ncol=5)
args=getopt(command)
# args <- commandArgs(trailingOnly = TRUE)

csv_input = read.csv(paste("./", args$input, sep = ""), header = T, sep='\t')

df = as.data.frame(csv_input)

sorted = sort(df$pvalue)

df$pvalue = sorted

df$qvalue = df$pvalue*length(df$pvalue)/df$index

j = 0
for (i in 1:length(df$pvalue)){
  if (df$qvalue[i] <= 0.05){
    j = j + 1
  }
}

print(' the count of discoveries is', j)
write.table(df, file = paste("./", args$output, sep = ""), sep= '\t',quote = FALSE, row.names = FALSE, col.names = TRUE)
