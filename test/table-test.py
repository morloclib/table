import pyarrow as pa

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RESET='\033[0m'


def good(msg):
    return f"{GREEN}{msg}{RESET}"

def bad(msg):
    return f"{RED}{msg}{RESET}"

def info(msg):
    return f"{BLUE}{msg}{RESET}"


# Render a RecordBatch as a column-keyed dict for human-readable failure
# messages. pyarrow's default repr is verbose and hides the values.
def _show(v):
    if isinstance(v, pa.RecordBatch):
        return {name: v.column(i).to_pylist() for i, name in enumerate(v.column_names)}
    return v


# Structural equality for the values that flow through the test harness.
# RecordBatches compare on ordered column names plus per-column to_pylist();
# this matches morloc Table semantics (column order is part of the schema)
# and is robust to chunking/back-end differences (numpy vs python ints, etc).
# Falls through to recursive list/tuple/dict comparison otherwise.
def _deep_equal(x, y):
    if isinstance(x, pa.RecordBatch) and isinstance(y, pa.RecordBatch):
        if list(x.column_names) != list(y.column_names):
            return False
        if x.num_rows != y.num_rows:
            return False
        for i in range(x.num_columns):
            if x.column(i).to_pylist() != y.column(i).to_pylist():
                return False
        return True
    if isinstance(x, (tuple, list)) and isinstance(y, (tuple, list)):
        if len(x) != len(y):
            return False
        return all(_deep_equal(a, b) for a, b in zip(x, y))
    if isinstance(x, dict) and isinstance(y, dict):
        if x.keys() != y.keys():
            return False
        return all(_deep_equal(x[k], y[k]) for k in x)
    return x == y


def testEqual(msg, x, y, results):
    (nfails, ntests) = results
    if _deep_equal(x, y):
        print(f"  {msg} ... {good('PASS')}")
        return (nfails, ntests + 1)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        print(f"    expected: {_show(y)}")
        print(f"    got:      {_show(x)}")
        return (nfails + 1, ntests + 1)


def printMsg(msg, x):
    print(info(msg))
    return x


def printResult(x):
    if x[0] == 0:
        print(good(f"All {x[1]!s} tests pass"))
    else:
        print(bad(f"{x[0]!s}/{x[1]!s} tests failed"))
    return x
