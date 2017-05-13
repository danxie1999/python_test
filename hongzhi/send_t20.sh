#!/bin/bash
sysdate=`date '+%Y%m%d%H%M%S'`
if [[ -n $1 ]]
then
T20=$1
#echo $T20
T20_change=${T20:0:19}${sysdate}"1234"${T20:37}
#echo $T20_change
cd /opt/nds/emmg/etc
. /opt/nds/emmg/utils/camcenv.sh
T20_sig=`echo $T20_change|/opt/nds/emmg/etc/gen_md5 `
cd - >/dev/null
echo "after signature and change date"
echo $T20_sig
if [[ -n $2 ]]
then
./t20_s.py $T20_sig
else
exit
fi
else
echo "input 1 arg"
exit
fi