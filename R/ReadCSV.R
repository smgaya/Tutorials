# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

# Read CSV file
getwd()
setwd("C:/Software_Development/Tutorials/R")
getwd()
data <- read.csv("owls15.csv", TRUE, ",")
data
head(data)
tail(data)