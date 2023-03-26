import pandas as pd
import io

#  packTable   Py :: pack   => (["str"], [["str"]]) -> ""


def packTable(serial):
    tableStr = "\n".join([",".join(row) for row in serial[1]])
    table = pd.read_csv(io.StringIO(tableStr), header=serial[0])
    return table

#  unpackTable Py :: unpack => "" -> (["str"], [["str"]])
def unpackTable(table):
    pass

#  columnsT :: Table -> [Str]

#  filterOnT :: Str -> (a -> Bool) -> Table -> Table

#  headT :: Int -> Table -> Table

#  ncolT :: Table -> Int

#  nrowT :: Table -> Int

#  removeColumnsT :: [Str] -> Table -> Table

#  reverseT :: Table -> Table

#  selectColumnsT :: [Str] -> Table -> Table

#  sortOnT :: [Str] -> Table -> Table

#  writeTsv :: Table -> Filename -> ()
