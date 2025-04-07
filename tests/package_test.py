# from StatOmics.Preprocessing import call
# from StatOmics.Analysis import call
from StatOmics.Test import call

# Example: Call count_chars from test1.R
result = call("count_chars", "hello")
print(result)  # Output: 5

# Example: Call say_hi from test1.R
result = call("say_hi")
print(result)  # Output: "hi"

# Example: Call echo from test2.R
result = call("echo", "Test String")
print(result)  # Output: "Test String"

