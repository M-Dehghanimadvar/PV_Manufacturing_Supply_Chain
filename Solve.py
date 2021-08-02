import time
start = time.time()
from Constraints import *

opt = SolverFactory("cplex")

results = opt.solve(model)
end = time.time()
print("User time:", end - start, "s")
results.write()

