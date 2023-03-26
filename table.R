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

#  filterOnT :: Str -> (a -> Bool) -> Table -> Table
filterOnT <- function(colname, f, df){
    df[sapply(df[[colname]], f), ]
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
    df[, colnames]
}

#  reverseT :: Table -> Table
reverseT <- function(df){
    if (nrow(df) > 0){
        df[rev(1:nrow(df)), ]
    } else {
        df
    }
}

#  sortOnT :: [Str] -> Table -> Table
sortOnT <- function(colnames, df){
    df[do.call(order, lapply(colanmes, function(n) df[[n]])), ]
}

#  writeTsv :: Table -> Filename -> ()
writeTsv <- function(df, filename){
    write.csv(df, file=filename, sep="\t")
}
