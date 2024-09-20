import pandas as pd


student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

df1 = pd.DataFrame(student_data, columns = ["Roll_Number", "Marks"])
dim = list(df1.shape)
print(dim[0])
print(type([dim[0], dim[1]]))