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


#  columnsT :: Table -> [Str]
def columnsT(table):
    return list(table.columns)

#  filterOnT :: Str -> (a -> Bool) -> Table -> Table

#  headT :: Int -> Table -> Table
def headT(n, table):
    return table.head(n)

#  ncolT :: Table -> Int
def ncolT(table):
    return table.shape[1]

#  nrowT :: Table -> Int
def nrowT(table):
    return table.shape[0]

#  removeColumnsT :: [Str] -> Table -> Table

#  reverseT :: Table -> Table

#  selectColumnsT :: [Str] -> Table -> Table

#  sortOnT :: [Str] -> Table -> Table

#  writeTsv :: Table -> Filename -> ()
