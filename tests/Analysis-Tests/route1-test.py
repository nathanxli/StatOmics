import numpy as np
from rpy2.robjects import DataFrame, FloatVector, StrVector
from rpy2.robjects.vectors import FactorVector
from StatOmics.Analysis import call


# Create small fake normalized+imputed plasma data
norm_imputed_plasma = DataFrame({
    "Protein": StrVector(["P1", "P2", "P3"]),
    "Sample1": FloatVector([1.2, 2.1, 3.4]),
    "Sample2": FloatVector([1.5, 2.2, 3.5]),
    "Sample3": FloatVector([1.3, 2.0, 3.6]),
    "Sample4": FloatVector([1.0, 2.3, 3.7])
})

# Create case_control vector (needs to match Samples)
# 4 samples => 4 labels
case_control = StrVector(["Case", "Case", "Control", "Control"])

# Create protein_gene mapping
protein_gene = DataFrame({
    "Protein": StrVector(["P1", "P2", "P3"]),
    "Gene": StrVector(["G1", "G2", "G3"])
})

# Call final_data_r1 from Python
result = call(
    "final_data_r1",
    norm_imputed_plasma,
    case_control,
    protein_gene
)

print("T-test Results:\n", result)
