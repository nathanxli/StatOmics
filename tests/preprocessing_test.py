import numpy as np
from rpy2.robjects import DataFrame, StrVector, FloatVector
from StatOmics.Preprocessing import call

# Use np.nan instead of None
data = DataFrame({
    "Gene": StrVector(["gene1", "gene2", "gene3"]),
    "A_1": FloatVector([1.0, np.nan, 3.0]),
    "A_2": FloatVector([2.0, np.nan, np.nan]),
    "B_1": FloatVector([1.5, 2.5, np.nan]),
    "B_2": FloatVector([1.2, np.nan, np.nan])
})

# Corresponding group labels for A_1, A_2, B_1, B_2
groups = StrVector(["A", "A", "B", "B"])

result = call("filter_missing_byPct", data, 0.5, "either", groups)

# Unpack result
filtered_data = result.rx2("filtered_data")
indexes = result.rx2("filtered_out_indexes")
group_info = result.rx2("group_info")

print("Filtered data:\n", filtered_data)
print("Filtered out indexes:", list(indexes))
print("Group info:", list(group_info))
