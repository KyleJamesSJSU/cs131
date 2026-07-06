BEGIN {uc = 0}
#/ishigaki/ {uc++}
// {uc++}
END {print uc}

