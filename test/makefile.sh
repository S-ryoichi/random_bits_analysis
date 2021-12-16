#!/bin/sh

n=1
e=100

while [ ${n} -le ${e} ] ; do
    echo "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF" > test_${n}.txt
    n=`expr $n + 1`
done

exit 0