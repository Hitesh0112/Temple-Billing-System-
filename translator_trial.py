import time
import pandas as pd
start = time.time()
df = pd.read_csv('tamil trans.csv')
print(df.to_string())
end = time.time()
print(end-start)

