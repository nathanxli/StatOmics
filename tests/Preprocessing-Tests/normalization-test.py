from rpy2.robjects import DataFrame, FloatVector
from StatOmics.Preprocessing import call

reference = DataFrame({
    "Val1": FloatVector([2.0, 4.0]),
    "Val2": FloatVector([10.0, 20.0])
})

to_normalize = DataFrame({
    "Val1": FloatVector([4.0, 8.0]),
    "Val2": FloatVector([20.0, 40.0])
})

result = call("reference_normalization", reference, to_normalize)

print("Normalized Data:\n", result)
