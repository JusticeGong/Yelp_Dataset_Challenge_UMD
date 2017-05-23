setwd("D:/Workplace/BigData/DataTrim/Layer3")
rs3 = read.csv("MidOutput37.csv", header = FALSE, col.names = c('Actual','m30','m31','m32','m33','m34','m35','m36','m37'))
library(randomForest)

train = sample(nrow(rs3), 0.8 * nrow(rs3))

rs3_train <- rs3[train, ]
rs3_test <- rs3[-train, ]
rs3_fit <- randomForest(Actual~., data = rs3_train, mtry = 8, importance = TRUE)




rs3_fit <- lm(Actual~., data = rs3_train[,])
summary(rs3_fit)

rs1_pred <- predict(rs1_fit, rs1_test)
rs1_mse <- mean((rs1_pred - rs1_test$Actual)^2)
rs1_mape <- mean(abs(rs1_pred - rs1_test$Actual)/rs1_test$Actual)

rs2_pred <- predict(rs2_fit, rs2_test)
rs2_mse <- mean((rs2_pred - rs2_test$Actual)^2)
rs2_mape <- mean(abs(rs2_pred - rs2_test$Actual)/rs2_test$Actual)

rs3_pred <- predict(rs3_fit, rs3_test)
rs3_mse <- mean((rs3_pred - rs3_test$Actual)^2)
rs3_mape <- mean(abs(rs3_pred - rs3_test$Actual)/rs3_test$Actual)

rs1_mse
rs1_mape
rs2_mse
rs2_mape
rs3_mse
rs3_mape
