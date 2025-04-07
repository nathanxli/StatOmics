from rpy2.robjects import DataFrame, FloatVector
from StatOmics.Preprocessing import call

data = DataFrame({
    "Val1": FloatVector([1.0, 2.0, 4.0]),
    "Val2": FloatVector([8.0, 16.0, 32.0])
})

result = call("transformation_log2", data)

print("Log2 Transformed Data:\n", result)
