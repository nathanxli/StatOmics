import numpy as np
from rpy2.robjects import DataFrame, StrVector, FloatVector
from StatOmics.Preprocessing import call

# Build a case where some rows don't meet threshold in all groups
data = DataFrame({
    "Gene": StrVector(["g1", "g2", "g3", "g4"]),
    "A_1": FloatVector([1.0, 2.0, np.nan, 4.0]),
    "A_2": FloatVector([1.0, np.nan, np.nan, 4.0]),
    "B_1": FloatVector([np.nan, 2.0, np.nan, 4.0]),
    "B_2": FloatVector([np.nan, np.nan, np.nan, 4.0])
})

groups = StrVector(["A", "A", "B", "B"])  # corresponds to A_1, A_2, B_1, B_2

result = call("filter_missing_byPct", data, 0.6, "all", groups)

filtered_data = result.rx2("filtered_data")
indexes = list(result.rx2("filtered_out_indexes"))
group_info = list(result.rx2("group_info"))

print("Filtered Data:\n", filtered_data)
print("Filtered out row indexes:", indexes)
print("Group Info:", group_info)
