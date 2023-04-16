# imports the iris data set
data(iris)

run <- function(f){
    f()
}

load_iris <- function(){
    iris
}

# packTable   R :: pack   => (["character"], [["character"]]) -> "data.frame"
packTable <- function(x){
    names(x[[2]]) <- x[[1]]
    type.convert(as.data.frame(x[[2]]), as.is=TRUE)
}

# unpackTable R :: unpack => "data.frame" -> (["character"], [["character"]])
unpackTable <- function(df){
    list(names(df), unname(lapply(df, as.character)))
}

#  columnsT :: Table -> [Str]
columnsT <- function(df){
    names(df)
}

# filterOnT :: Str -> (a -> Bool) -> Table -> Table
filterOnT <- function(column, f, table) {
  table[f(table[[column]]), ]
}

#  headT :: Int -> Table -> Table
headT <- function(n, df){
    head(df, n)
}

#  removeColumnsT :: [Str] -> Table -> Table
removeColumnsT <- function(colnames, df){
    df[, !names(df) %in% colnames, drop=FALSE]
}

#  selectColumnsT :: [Str] -> Table -> Table
selectColmnsT <- function(colnames, df){
    df[, colnames, drop=FALSE]
}

#  reverseT :: Table -> Table
reverseT <- function(df){
    if (nrow(df) > 0){
        df[nrow(df):1, ]
    } else {
        df
    }
}

# sortOnT :: [Str] -> Table -> Table
sortOnT <- function(columns, table) {
    table[do.call(order, table[columns]), ]
}

#  writeTsv :: Table -> Filename -> ()
writeTsv <- function(filename, df){
    write.csv(df, file=filename, sep="\t")
}
