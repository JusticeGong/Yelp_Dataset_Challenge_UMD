setwd("D:/Workplace/BigData/DataTrim/Layer3")
rs1 = read.csv("MidOutput13.csv", header = FALSE, col.names = c('Actual','m10','m11','m12','m13'))
rs2 = read.csv("MidOutput25.csv", header = FALSE, col.names = c('Actual','m20','m21','m22','m23','m24','m25'))
rs3 = read.csv("MidOutput37.csv", header = FALSE, col.names = c('Actual','m30','m31','m32','m33','m34','m35','m36','m37'))

train = sample(nrow(rs1), 0.8 * nrow(rs1))

rs1_train <- rs1[train, ]
rs1_test <- rs1[-train, ]
rs1_fit <- lm(Actual~., data = rs1_train)
summary(rs1_fit)

rs2_train <- rs2[train, ]
rs2_test <- rs2[-train, ]
rs2_fit <- lm(Actual~., data = rs2_train)
summary(rs2_fit)

rs3_train <- rs3[train, ]
rs3_test <- rs3[-train, ]
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
