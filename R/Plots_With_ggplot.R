# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

# Plots with ggplot
library(ggplot2)
head(diamonds)

qplot(diamonds$carat, diamonds$price, color=diamonds$clarity)