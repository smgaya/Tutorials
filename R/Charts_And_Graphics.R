# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

sample <- read.csv("sample.csv", TRUE, ",")
head(sample)
# Histogram
hist(sample$age, main="Ages of Users", ylab="Users", xlab="Ages")
# Scatter plot
plot(sample$age, sample$income, ylab="Age", xlab="Income")
# Box plot
boxplot(sample$age)
install.packages("ggplot")