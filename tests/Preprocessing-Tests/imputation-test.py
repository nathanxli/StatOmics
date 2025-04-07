import numpy as np
from rpy2.robjects import DataFrame, FloatVector, StrVector
from StatOmics.Preprocessing import call

# Simulated expression-like data with missing values
data = DataFrame({
    "ProteinID": StrVector(["P1", "P2", "P3"]),
    "Sample1": FloatVector([1.2, np.nan, 3.4]),
    "Sample2": FloatVector([1.5, 2.1, np.nan]),
    "Sample3": FloatVector([np.nan, 2.2, np.nan]),
    "Sample4": FloatVector([1.0, 2.3, 3.7])
})

result = call("imputation_with_normal", data)

print("Imputed Data:\n", result)
