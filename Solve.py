import time
start = time.time()
from Constraints import *

opt = SolverFactory("cplex")

results = opt.solve(model, tee=True,options_string="mipgap=0.0005")
end = time.time()
print("User time:", end - start, "s")
results.write()

