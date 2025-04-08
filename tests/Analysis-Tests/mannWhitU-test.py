from StatOmics.Analysis import call
from rpy2.robjects import DataFrame, FloatVector, StrVector

data = DataFrame({
    "Gene": StrVector(["P1", "P2", "P3"]),
    "A_1": FloatVector([1.2, 2.3, 3.4]),
    "A_2": FloatVector([1.1, 2.2, 3.3]),
    "B_1": FloatVector([2.0, 3.0, 4.0]),
    "B_2": FloatVector([2.1, 3.1, 4.1])
})
groups = StrVector(["A", "A", "B", "B"])

result = call("run_mannWhitU_test", data, groups)
print(result)