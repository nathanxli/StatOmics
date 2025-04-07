import numpy as np
from rpy2.robjects import DataFrame, FloatVector, StrVector
from StatOmics.Preprocessing import call

data = DataFrame({
    "Gene": StrVector(["g1", "g2"]),
    "Sample1": FloatVector([1.0, np.nan]),
    "Sample2": FloatVector([np.nan, 2.0])
})

result = call("imputation_with_normal", data)

print("Imputed Data:\n", result)
