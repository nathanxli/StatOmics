# from StatOmics.Preprocessing import call
# from StatOmics.Analysis import call
from StatOmics.Test import call
from rpy2.robjects import FloatVector

# Example: Call count_chars from test1.R
result = call("count_chars", "hello")
print(result)  # Output: 5

# Example: Call say_hi from test1.R
result = call("say_hi")
print(result)  # Output: "hi"

# Example: Call echo from test2.R
result = call("echo", "Test String")
print(result)  # Output: "Test String"

# Example: Testing usage of package
result = call("get_top_table")
print(result)

# Example: Testing package with input & output
# first convert input to R type (in this case, numeric vector)
vec = FloatVector([1, 2, 3, 4, 5])
result = call("summarize_vector", vec)
# rpy2 returns a ListVector - convert to dict
summary_dict = {name: result.rx2(name)[0] for name in result.names}
print(summary_dict)