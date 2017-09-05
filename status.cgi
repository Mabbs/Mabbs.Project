#!/system/bin/sh
zhc(){
while read nr
do
echo "$nr<br>"
done
}
jcg(){
echo "</td></tr><tr><td>$1</td><td>"
}
dsk(){
echo "$3/$2"
}
cpc(){
tot="$(($2+$3+$4+$5+$6+$7+$8+$9+${10}))"
idt="$5"
}
ncc(){
upl="${10}"
dol="$2"
}
echo "Content-type:text/html;charset=utf-8"
echo ""
echo '<meta name="viewport" content="width=device-width,minimum-scale=1.2,maximum-scale=1.2,user-scalable=no" /><h1>Server Status</h1><hr>'
date
echo '<br><title>Server Status</title><table border=1><tr><td>OS</td><td>'
uname
uname -r
echo "</td><td>Memory</td></tr><tr><td>Disk</td><td>"
dsk `df|grep "/storage/emulated/0"`
echo "</td><td rowspan=4>`cat "/proc/meminfo"|zhc`</td></tr><tr><td>Battery</td><td>"
cat "/sys/class/power_supply/dollar_cove_battery/capacity"
echo "% "
[ `cat "/sys/class/power_supply/dollar_cove_charger/online"` == "1" ]&&echo Charging
jcg CPU
cpc $(
cat "/proc/stat"|while read ni
do
echo "$ni"
break 1
done
)
sleep 0.1
tut="$tot"
idu="$idt"
cpc $(
cat "/proc/stat"|while read ni
do
echo "$ni"
break 1
done
)
tto="$(($tot-$tut))"
ito="$(($idt-$idu))"
echo "$((100*($tto-$ito)/$tto))%"
jcg Network
ncc `cat /proc/net/dev|grep wlan0`
upw="$upl"
dow="$dol"
sleep 1
ncc `cat /proc/net/dev|grep wlan0`
rup="$(($upl-$upw))"
rdo="$(($dol-$dow))"
echo "↑$(($rup/1024))KiB/s  ↓$(($rdo/1024))KiB/s"
echo "</td></tr></table>"