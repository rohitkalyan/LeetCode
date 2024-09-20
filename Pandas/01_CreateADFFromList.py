import pandas as pd


student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

df1 = pd.DataFrame(student_data, columns = ["Roll_Number", "Marks"])
print(df1)