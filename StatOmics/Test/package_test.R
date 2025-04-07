# package_test.R

library(limma)

get_top_table <- function() {
  # Create dummy data
  design <- model.matrix(~ 0 + factor(c(1,1,2,2)))
  colnames(design) <- c("Group1", "Group2")
  fit <- lmFit(matrix(rnorm(100), nrow=10), design)
  contrast.matrix <- makeContrasts(Group2 - Group1, levels=design)
  fit2 <- contrasts.fit(fit, contrast.matrix)
  fit2 <- eBayes(fit2)
  topTable(fit2)
}