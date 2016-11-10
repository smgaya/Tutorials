# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

# Vectors
id <- 1:10
age <- c(12, 43, 56, 4, 59, 90, 21, 29, 34, 81)
name <- c("Jeff", "Thomas", "Aoife", "Rachel", "Neil", "Beeeaaan", "Greg", "Geraldine", "Martin", "Jim")
# Data frame
df <- data.frame(id, age, name)
df
# Data frame operations
nrow(df)
ncol(df)
dim(df)
names(df)[2]
head(df)
tail(df)
df$ids
df[2]
df[7, 1:3]
df[ , 2]