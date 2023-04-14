import pandas as pd
import io

#  packTable   Py :: pack   => (["str"], [["str"]]) -> ""
def packTable(serial):
    tableStr = "\n".join([",".join(row) for row in serial[1]])
    table = pd.read_csv(io.StringIO(tableStr), header=serial[0])
    return table

#  unpackTable Py :: unpack => "" -> (["str"], [["str"]])
def unpackTable(table):
    columnNames = "[" + ",".join(['"' + c + '"' for c in table.columns]) + "]"
    rows = table.to_json(orient="values")
    return "".join(["[", columnNames, ",", rows, "]"])


# headT :: Int -> Table -> Table
def headT(n, table):
    return table.head(n)

# nrowT :: Table -> Int
def nrowT(table):
    return len(table)

# ncolT :: Table -> Int
def ncolT(table):
    return len(table.columns)

# sortOnT :: [Str] -> Table -> Table
def sortOnT(columns, table):
    return table.sort_values(by=columns)

# reverseT :: Table -> Table
def reverseT(table):
    return table.iloc[::-1]

# columnsT :: Table -> [Str]
def columnsT(table):
    return list(table.columns)

# selectColumnsT :: [Str] -> Table -> Table
def selectColumnsT(columns, table):
    return table[columns]

# removeColumnsT :: [Str] -> Table -> Table
def removeColumnsT(columns, table):
    return table.drop(columns, axis=1)

# filterOnT :: Str -> (a -> Bool) -> Table -> Table
def filterOnT(column, predicate, table):
    return table[table[column].apply(predicate)]



### Additional

# Rename columns in the table
# renameColumnsT :: [(Str, Str)] -> Table -> Table
def renameColumnsT(rename_dict, table):
    return table.rename(columns=rename_dict)

# Add a new column to the table based on a function applied to existing columns
# addColumnT :: Str -> (Row -> a) -> Table -> Table
def addColumnT(column_name, func, table):
    table[column_name] = table.apply(func, axis=1)
    return table

# Group the table by one or more columns, typically followed by an aggregation function
# groupByT :: [Str] -> Table -> GroupedTable
def groupByT(columns, table):
    return table.groupby(columns)

# Apply an aggregation function to each group in a grouped table
# aggregateT :: GroupedTable -> (Group -> a) -> Table
def aggregateT(grouped_table, agg_func):
    return grouped_table.agg(agg_func)

# Perform a join operation between two tables on specified columns
# joinT :: Table -> Table -> Str -> Str -> Table
def joinT(table1, table2, left_on, right_on):
    return pd.merge(table1, table2, left_on=left_on, right_on=right_on)

# Pivot the table to create a wide-format table from a long-format table
# pivotT :: Table -> Str -> Str -> Str -> Table
def pivotT(table, index, columns, values):
    return table.pivot(index=index, columns=columns, values=values)

# Melt the table to create a long-format table from a wide-format table
# meltT :: Table -> [Str] -> Str -> Str -> Table
def meltT(table, id_vars, var_name, value_name):
    return pd.melt(table, id_vars=id_vars, var_name=var_name, value_name=value_name)

# Remove duplicate rows from the table
# dropDuplicatesT :: Table -> Table
def dropDuplicatesT(table):
    return table.drop_duplicates()

# Replace specific values in the table
# replaceValuesT :: a -> a -> Table -> Table
def replaceValuesT(old_value, new_value, table):
    return table.replace(old_value, new_value)
