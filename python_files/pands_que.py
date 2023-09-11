# import pandas as pd


# df = pd.read_excel("myexcel.xlsx")

# print(df,'\n\n')

# import pandas as pd

# df = pd.read_excel('data_excel.xls')
# print(df,'\n\n')

# df_rows,df_columns = df.shape
# print(df_rows,df_columns,'\n\n')

# df_row = df.loc[:].shape[0]
# print(df_row,'==========df_row')

# df_col = df.loc[:].shape[1]
# print(df_col,'==========df_col')

# print("\n")

# df = df[(df['City']=='Delhi') | (df['Country']=='India')] # | (df['Age'] > 23)

# print(df)

# print("\n")

# row_2 = df.loc[:2,['name','Country']]
# print(row_2)

# print("\n")

# subset = df.iloc[1:3, 0:2]  # Access rows 1 and 2, columns 0 and 1
# print(subset)
# import pandas as pd

# data = {
#     'Name': ['John', 'Emma', 'Mike'],
#     'Age': [25, 28, 30],
#     'City': ['New York', 'London', 'Sydney']
# }

# df = pd.DataFrame(data)

# # Get the number of rows and columns using loc
# num_rows = df.loc[:, :].shape[0]  # Select all rows and all columns
# num_columns = df.loc[:, :].shape[1]

# # Get the number of rows and columns using iloc
# num_rows = df.iloc[:, :].shape[0]  # Select all rows and all columns
# num_columns = df.iloc[:, :].shape[1]

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)

# print(df.Name,df.City)
# print('\n\n\n')
# print(df['Name'],df['Age'])

# df_filter_loc = df.loc[(df['Name']=='John') & (df['Age'] <= 28)]
# print(df_filter_loc)

# print('\n\n\n')

# df_filter_loc_shape_row,df_filter_loc_shape_col = df.loc[(df['Name']=='John') & (df['Age'] <= 28)].shape
# print(df_filter_loc_shape_row,'====',df_filter_loc_shape_col)

# print('\n\n\n')

# df_filter_iloc = df.iloc[((df['Name']=='John') & (df['Age'] <= 28)).values]
# print(df_filter_iloc)



# import pandas as pd

# # Sample DataFrames
# data1 = {
#     'ID': [1, 2, 3],
#     'Age' : [20,30,40],
#     'Name': ['John', 'Emma', 'Mike']
# }

# data2 = {
#     'ID': [2, 3, 4],
#     'Age' : [20,30,40],
#     'City': ['New York', 'London', 'Sydney'],
#     'Country' : ['USA','UK','Australia']
# }

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

# # Merge based on the 'ID' column
# merged_df_id = pd.merge(df1, df2, on='ID')

# print(merged_df_id)
# #    ID  Age  Name      City Country
# # 0   2   30  Emma  New York     USA
# # 1   3   40  Mike    London      UK

# merged_df_age = pd.merge(df1, df2, on='Age')

# print(merged_df_age)
# #    ID_x  Age  Name  ID_y      City    Country
# # 0     1   20  John     2  New York        USA
# # 1     2   30  Emma     3    London         UK
# # 2     3   40  Mike     4    Sydney  Australia





# 3rd highest in sql qyuery

# SELECT NAME,EMP_SALARY FROM TABLE_NAME ORDER BY SALARY 
# DESC LIMIT 1 OFFSET 2


# SELECT SALARY,FIELD_NAME FROM TABLENAME WHERE emp_id=2


import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Concatenate them along rows (axis=0) with ignore_index=True
# result_df = pd.concat([df1, df2], axis=0)

# print(result_df)
# sum_df = df1.sum(axis=0)
# print(sum_df)

# sum_df = df1.sum(axis=1)
# print(sum_df)

# df1['C'] = [10,20]

# print('\n\n')

# print(df1)

# data1 = {'name':['vj'],'age':[32]}
# data2 = {'address':['india'],'location':['hyd']}
# newdf1 = pd.DataFrame(data1)
# newdf12 = pd.DataFrame(data2)

# concat_dataframe = pd.concat([newdf1,newdf12],axis=1)
# print(concat_dataframe)


# data1 = {'name':['vj','atul','divya'],'age':[32,25,30],
#          'id':[1,2,3]}
# data2 = {'address':['india','bangla','usa'],
#          'location':['hyd','mirpur','las vegas'],
#          'id':[2,3,4]}

# newdf1 = pd.DataFrame(data1)
# newdf2 = pd.DataFrame(data2)

# merge_dataframe = pd.merge(newdf1,newdf2,on='id',how='inner')
# print(merge_dataframe)
# print("\n\n")

# new_frame = merge_dataframe.dropna()
# print(new_frame)

import pandas as pd
import numpy as np  # Import numpy for generating NaN values

# Create a sample DataFrame with NaN values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan]
}

df = pd.DataFrame(data)
df_filled = df.fillna(0)

df['D'] = [10,20,30,40]
df['D'] =  df['D'].astype(str)
print(df)


# Replace NaN values with a specific value, e.g., 0
# df_filled = df.fillna(0)

# df.at[0, 'A'] = np.nan  # Set cell (row 0, column 'A') to NaN


print(df)

# print(df_filled)

# # Replace NaN values with the mean value of each column
# df_mean_filled = df.fillna(df.mean())
# print(df_mean_filled,'\n\n')

# # Forward fill NaN values (replace with the previous value in the column)
# df_ffill = df.ffill()
# print(df_ffill,'\n\n')

# # Backward fill NaN values (replace with the next value in the column)
# df_bfill = df.bfill()
# print(df_bfill,'=====df_bfill')













































