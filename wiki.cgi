#!/system/bin/ash
m="/sdcard/ba"
n="MaBBS"
t="MaWiki"
zsn="$n&Wiki"
wcm="Welecome to use $zsn"
s="$m/wiki"
wna="Please input your name:"
wnb="Please input new password:"
wnc="Please input verifcation code:"
gly="SYSOP"
j="${0##*/}"
fgx="============"
rip="$REMOTE_ADDR"
fsc(){
echo "$4"
}
pbz(){
[ -n "`ls "$pcz"|grp "$tit"`" ]
}
cpo(){
co=$(($co+1))
}
clj(){
echo "<a href=$j?${yzh}${toa}$1>$2</a>"
}
l(){
[ "$na" == "guest" ]
}
hpd(){
[ "$1" == "1" ]
}
cpd(){
[ "$p" -gt "1" ]
}
opd(){
[ "$p" -lt "$((`ls "$cfd"|wcl`-9))" ]
}
rck(){
[ -n "`echo $nep|grp " "`" -o "$chk" == "$nep" -o -z "$nep" ]
}
uck(){
vv="`cat /proc/sys/kernel/random/uuid`"
vv="${vv%%-*}"
}
ypd(){
[ "$p" -le "$co" -a "$(($p+10))" -gt "$co" ]
}
wjw(){
p="$((`ls "$1"|wcl`-9))"
}
nef(){
nsz="${nr%%-*}"
iao="${nsz% *}"
iob="${nsz#* }"
yti="${nr#*-}"
}
bfx(){
[ -n "$ry" ]&&{
l&&u||{
echo "$na  `date` #$((`cat "$r"|wcl`/3+1))
$ry
">>$r
[ -n "`echo "$ry"|grp @`" -a -z $ckn ]&&{
for snr in ${ry##*@}
do
[ -e "$m/user/$snr" ]&&echo "$inu $i-$na notify you on $w">>$m/user/$snr/noce
done
}
[ -n $ckn -a -n "`echo "$ry"|grp "add friend"`" ]&&{
fnm="${ry##*add friend }"
[ -n "$fnm" -a -e "$m/user/$fnm" ]&&echo "$w,$qmz">>"$m/user/$fnm/chat"
}
[ -n "`echo "$ry"|grp "@ai"`" ]&&{
swd="${ry%@ai}"
[ -n "`echo "$swd"|grp "study"`" ]&&{
echo "${swd##*study }" >>$m/ai
echo "`date`|$rip|$na add AI command">>$m/log
ais="OKay"
}||{
ais="`cat "$m/ai"|while read nr
do
[ "${nr%%-*}" == "$swd" ]&&{
echo "${nr#*-}"
break 1
}
done`"
}
[ -z "$swd" -o -z "$ais" ]&&ais="Sorry,I dont know what do you say"
echo "AI  `date` #$((`cat "$r"|wcl`/3+1))
$ais
">>$r
}
cat "$r"|while read nc
do
ni="${nc#*r:}"
echo "$inu $i-$na reply you on $w">>$m/user/${ni%% *}/noce
break 1
done
}
}
}
plx(){
w="$tit"
r="$pcz/$tit"
echo "Post master:$na  `date` #1
$wod
">>$r
zxth
}
nwe(){
echo "$mt
Made by:$na `date`
Tags:$tgs
$fgx
$wd">$mwt
}
gaen(){
tho=`date +%H`
ztg=night
[ $tho -ge 6 -a $tho -lt 12 ]&&ztg=morning
[ $tho -ge 12 -a $tho -lt 18 ]&&ztg=afternoon
[ $tho -ge 18 -a $tho -lt 21 ]&&ztg=evening
echo "Good ${ztg},$na"
}
grp(){
while read nr
do
case $nr in
*"${1}"*)
echo $nr
;;
esac
done
}
zcc(){
usk="$m/user/$nep"
mkdir -p "$usk/diary"
>"$usk/chat"
>"$usk/noce"
echo "0">"$usk/noct"
echo $npd>>$usk/pwd
echo "`date`|$rip|$nep joined">>$m/log
}
wcl(){
nb="0"
while read nul
do
nb="$(($nb+1))"
done
echo "$nb"
}
pdg(){
w=""
co=0
while read nr
do
cpo
[ "$i" == "$co" ]&&echo "$nr"
done
}
chse(){
l&&u||{
vck="`cat "$r/opt/$1"|grp "$na"`"
[ "$na" == "$vck" ]||{
echo $na >> "$r/opt/$1"
}
cat "$r/opt/$1"
echo "selected it."
}
}
[ -z "$rip" ]&&{
inc="echo Input number or command:"
[ -e "$m/" ]&&echo "$wcm"||{
echo Installing...
mkdir -p "$m/main" "$m/user" "$s" "$m/room" "$m/up/novel"
>"$m/ip"
>$m/ai
nep="$gly"
echo "Master name:$gly"
echo "New password:"
read npd
zcc
}
bk(){
echo b.Back
}
slp(){
[ "$na" == "$gly" ]
}
fy(){
cpd&&p="$(($p-10))" 
}
fyx(){
cpd&&echo r.Next page
}
oy(){
opd&&p="$(($p+10))" 
}
oyx(){
opd&&echo l.Prev page
}
u(){
clear
echo Login:
read ua
echo Password:
read pa
[ -z "$ua" ]&&np=0||{
[ -e "$m/user/$ua" ]&&np="`cat "$m/user/$ua/pwd"`ck"
}
[ "${pa}ck" == "$np" ]&&{
na="$ua"
q="$m/user/$na"
}||{
echo Error!
echo Join us?[Y/N]:
read ju
case $ju in
Y|y)
echo $wna
read nep
echo $wnb
read npd
chk="`ls "$m/user"|grp "$nep"`"
rck||{
echo $wnc
uck
echo $vv
read vc
[ "$vc" == "$vv" ]&&{
zcc
echo OK!
sleep 1
}
}
;;
esac
}
true
}
fid(){
while true
do
clear
cat "$rmk"
echo Press enter to back
l&&{
read nul
break 1
}||{
echo Input c to continue write
read pd
case $pd in
c)
echo Word:
read nw 
echo $nw >>$rmk
[ -n "$ckn" ]&&echo "`date`|$na edited $tkw">>$m/log
;;
*)
break 1
;;
esac
}
done
}
zxth(){
while true
do
clear
hpd $1||{
echo "$w
$fgx"
}
cat "$r"
echo 'Input reply(Input e go back):'
slp&&echo Input d delete the post
hpd $1&&ckn=1
read ry
case $ry in
e)
break 1
;;
d)
slp&&rm -rf "$r"&break 1
;;
*)
bfx
;;
esac
done
}
pxcx(){
while read nr
do
cpo
hpd $2&&{
rg=""
[ -f "$pcz/$nr" ]&&ift="$pcz/$nr"||ift="$pcz/$nr/talk"
[ -e "$ift" ]&&rg="($((`cat "$ift"|wcl`/3)))"
}
ypd&&echo "$1$co.$nr$rg"
done
}
cc(){
for lop in `ls "$r/opt/"`
do
echo $lop.$1 \(`cat "$r/opt/$lop"|wcl`\)
shift
done
}
na="guest"
sleep 1
until [ "$cmd" == "2" ]
do
clear
echo "$t User:$na
Total entry:`ls "$s"|wcl`
$fgx
1.Search
2.Exit
3.Go to $n
4.Random
5.Novel Viewer (`ls "$m/up/novel"|wcl`)"
l&&echo 6.Login||{
echo "6.Make a new entry
7.Diary (`ls "$q/diary/"|wcl`)
8.Reset your password
9.Chat Room (`cat "$q/chat"|wcl`)"
}
echo Input command:
read cmd
case $cmd in
1)
clear
echo Input Keyword or tags:
read kw
[ -n "$kw" ]&&{
clear
echo "Result
$fgx$fgx
Entry
$fgx"
co=0
ls "$s"|grp "$kw"|while read jg
do
cpo
echo a$co.${jg%%+*}
done
echo "User
$fgx"
ls "$m/user"|grp "$kw"
echo "Post
$fgx"
ls "$m/main"|while read nr
do
ls "$m/main/$nr"|grp "$kw"
done
echo "Novel
$fgx"
p="0"
ls "$m/up/novel"|grp "$kw"|pxcx "b"
echo Which one:
read mtt
case $mtt in
a*)
i="${mtt#a}"
tkw="`ls "$s"|grp "$kw"|pdg`"
[ -n "$tkw" ]&&{
rmk="$s/$tkw"
ckn=1
fid
}
;;
b*)
i="${mtt#b}"
tkw="`ls "$m/up/novel"|pdg`"
[ -n "$tkw" ]&&{
clear
more "$m/up/novel/$tkw"
read nul
}
;;
esac
}
;;
3)
while true
do
clear
gaen
date
[ -e "$m/bul" ]&&echo Bulletin:`cat "$m/bul"`
echo $fgx
co=0
ls "$m/main"|while read bm
do
cpo
echo "$co.$bm (`ls "$m/main/$bm/"|wcl`)"
done
echo "$fgx
a.Back to $t"
l||echo "b.Notice ($((`cat "$q/noce"|wcl`-`cat "$q/noct"`)))"
slp&&{
echo c.Make a part
echo d.Release bulletin
}
$inc
read pac
case $pac in
a)
break 1
;;
b)
l&&u||{
[ -e "$q/noce" ]&&{
clear
echo "`cat "$q/noce"|wcl`">"$q/noct"
co=0
cat "$q/noce"|while read nr
do
cpo
echo "$co.${nr#*-}"
done
echo c.Clear
$inc
read i
[ -n "$i" ]&&{
nr="`cat "$q/noce"|pdg`"
[ "$i" == "c" ]&&{
>"$q/noce"
echo "0">"$q/noct"
}||{
[ -n "$nr" ]&&{
nef
inu="$iao"
i="$iao"
pac="`ls "$m/main"|pdg`"
[ -n "$pac" ]&&{
pcz="$m/main/$pac"
i="$iob"
w="`ls "$pcz"|pdg`"
[ -n "$w" ]&&{
r="$pcz/$w"
[ -f "$r" ]&&zxth
}
}
}
}
}
}
}
;;
c)
clear
slp&&{
echo New part name:
read npn
mkdir "$m/main/$npn"
}
;;
d)
slp&&{
clear
echo Input bulletin:
read bul
echo "$bul">$m/bul
}
;;
*)
inu="$pac"
i="$pac"
pac="`ls "$m/main"|pdg`"
[ -n "$pac" ]&&{
pcz="$m/main/$pac"
cfd="$pcz"
wjw "$pcz"
while true
do
clear
echo "`gaen`   Part:$pac
$fgx"
co=0
ls "$pcz"|pxcx "" 1
echo "$fgx"
oyx
fyx
echo "a.Make a new post"
bk
slp&&echo c.Delete the part
$inc
read i
case $i in
a)
l&&u||{
clear
echo 'This is a [1.Post 2.Vote]:'
read cht
case $cht in
1)
clear
echo Input the title:
read tit
pbz||{
echo Word:
read wod
plx
}
;;
2)
clear
echo Input the title:
read tit
pbz||{
echo Main word:
read wod
echo "Option head:"
read oph
echo "Option:"
read opt
echo 'Use talking?[Y/N]:'
read utk
tsm="$pcz/$tit"
mkdir "$tsm"
echo "Vote master:$na  `date`
$wod">>$tsm/main
echo $opt>>$tsm/data
mkdir "$tsm/opt" 
for sle in $oph
do
>"$tsm/opt/$sle"
done
[ "$utk" == "y" ]&&>"$tsm/talk"
}
;; 
esac
}
;;
b)
break 1
;;
l)
oy
;;
r)
fy
;;
c)
slp&&rm -rf "$pcz"&break 1
;;
*)
w="`ls "$pcz"|pdg`"
[ -n "$w" ]&&{
r="$pcz/$w"
[ -f "$r" ]&&zxth||{
clear
cat "$r/main"
echo $fgx
cc `cat "$r/data"`
[ -e "$r/talk" ]&&echo Input t to talk,or
echo 'Choose one:'
read ry
[ -n "$ry" ]&&{
[ "$ry" == "t" ]&&{
[ -e "$r/talk" ]&&{
r="$r/talk"
zxth
}
}||{
clear
[ -e "$r/opt/$ry" ]&&chse $ry
sleep 3
}
}
}
}
;;
esac
done
}
;;
esac
done
;;
5)
cfd="$m/up/novel"
wjw "$cfd"
while true
do
clear
echo "Novel Viewer
$fgx"
co=0
ls "$cfd"|pxcx
echo "$fgx"
oyx
fyx
echo "You can Upload novel on Web"
bk
$inc
read i
case $i in
b)
break 1
;;
l)
oy
;;
r)
fy
;;
*)
w="`ls "$cfd"|pdg`"
[ -n "$w" ]&&{
clear
more "$cfd/$w"
read nul
}
;;
esac
done
;;
6)
l&&u||{
clear
echo Input Main title:
read mt
[ -z "`ls "$s"|grp "$mt"`" ]&&{
echo Tags:
read tgs
echo Word:
read wd
mwt="$s/$mt+$tgs"
nwe
rmk="$mwt"
fid
}
}
;;
4)
jld="`ls "$s"|wcl`"
[ "$jld" == "0" ]&&{
echo Not found...
sleep 1
}||{
i=$((`date +%s`%$jld+1))
rmk="$s/`ls "$s"|pdg`"
fid
}
;;
7)
l&&u||{
cfd="$q/diary"
wjw "$cfd"
while true
do
clear
gaen
echo $fgx
co=0
ls "$cfd"|pxcx
echo "$fgx"
oyx
fyx
echo "a.Write diary"
bk
$inc
read i
case $i in
a)
clear
mt="`date +%y.%m.%d`"
[ -n "`ls "$cfd"|grp "$mt"`" ]||{
echo Word:
read wd
mwt="$cfd/$mt"
echo "Diary:$mt
$wd">>$mwt
}
rmk="$cfd/$mt"
fid
;;
b)
break 1
;;
l)
oy
;;
r)
fy
;;
*)
w="`ls "$cfd"|pdg`"
[ -n "$w" ]&&{
rmk="$cfd/$w"
fid
}
;;
esac
done
}
;;
8)
l&&u||{
clear
echo Input your new password:
read nrd
[ -n "$nrd" ]&&echo $nrd>$q/pwd
}
;;
9)
l&&u||{
cfd="$q/chat"
while true
do
clear
echo Chat Room
gaen
echo $fgx
co=0
cat "$cfd"|while read nr
do
cpo
echo $co.${nr#*,}
done
echo $fgx
echo a.Make chat room
bk
$inc
read i
case $i in
a)
clear
echo Input Chat room name:
read qmz
w="$((`ls "$m/room"|wcl`+1))"
r="$m/room/$w"
echo "Chat Room #$w">$r
echo "$fgx">>$r
echo "$w,$qmz">>$cfd
zxth "1"
;;
b)
break 1
;;
*)
wwn="`cat "$cfd"|pdg`"
w="${wwn%%,*}"
qmz="${wwn#*,}" 
[ -n "$w" ]&&{
r="$m/room/$w"
zxth "1"
}
;;
esac
done
}
;;
esac
done
}||{
ctj(){
echo "Content-type:$1;charset=utf-8"
}
rxh(){
co=0
ls "$m/main"|while read bm
do
cpo
eu="$m/main/$bm"
wjw "$eu"
txc="$co.$bm(`ls "$eu"|wcl`)"
hpd $1&&{
clj "m2k=$co=$p" "$txc"
$hc
}||echo "<item><title>$txc</title><link>${wsf}?m2k=$co=$p</link></item>"
done
}
ndt(){
until [ "$a" == "$1" ]
do
b="${a##*-}"
a="${a%-*}"
o="$b $o"
done
for i in $o
do
nwi="`ls "$m/up/$out"|pdg`"
[ -n "$nwi" ]||break
out="$out/$nwi"
done
}
qua="${QUERY_STRING##*_}"
tok="${qua%token*}"
[ "$tok" == "$qua" ]||toa="${tok}token"
qus="${qua##*token}"
case $qus in
m8d-m8-*)
a="$qus"
ndt "m8d-m8"
cfd="$m/up$out"
[ -f "$cfd" ]&&{
ctj "application/octet-stream"
echo "Content-length:$(fsc `ls -l "$cfd"`)
Content-Disposition:attachment;filename=\"${cfd##*/}\"
"
cat "$cfd"
}||{
wjw "$m/up$out"
[ "${QUERY_STRING%_*}" == "$qua" ]||{
yzz="${QUERY_STRING%_*}"
yzh="${yzz}_"
}
echo "HTTP/1.1 302 Found
Location:$j?${yzh}${toa}${qus#*-}=$p"
}
;;
rss)
ctj "text/xml"
wsf="http://$HTTP_HOST/cgi-bin/$j"
echo '
<?xml version="1.0"?><rss version="2.0"><channel><title>'
echo "$n</title><link>${wsf}?main</link>"
rxh
echo "</channel></rss>"
;;
*)
read tl
[ "${tl%%=*}" == "lon" ]&&{
[ "$tl" == "${tl%&noc=on}" ]&&{
uck
echo "HTTP/1.1 302 Found
Location: $j?${vv}tokenmain
Set-Cookie: ${tl}token${vv};PATH=/;HttpOnly"
}||{
tl="${tl%&noc=on}"
echo "HTTP/1.1 302 Found
Location:$j?${tl}_main"
}
}||{
echo "Content-Encoding:gzip"
ctj "text/html"
}
echo ""
{
echo "<link rel=alternate type=application/rss+xml title=$n href=$j?rss >"
hc='echo <br>'
tb="<table border=1><tr>"
thc="</td></tr><tr><td>"
tbo="</tr></table>"
thq="</td><td>"
spa="echo <input type=password name=pw><br>"
ent="enctype=multipart/form-data"
a="$HTTP_COOKIE"
until [ "$a" == "$b" ]
do
b="${a##*;}"
a="${a%;*}"
o="$b $o"
done
for i in $o
do
[ "${i%%=*}" == "lon" ]&&coke="$i"
done
[ -z "$coke" -o "$tok" == "${coke##*token}" ]&&{
[ "${QUERY_STRING%_*}" == "$qua" ]&&yzz="${coke%token*}"||{
yzz="${QUERY_STRING%_*}"
yzh="${yzz}_"
}
uma="${yzz%&pw*}"
ua="${uma#*=}"
pa="${yzz#*pw=}"
[ -z "$ua" ]&&np=0||{
[ -e "$m/user/$ua" ]&&np="`cat "$m/user/$ua/pwd"`ck"
}
}
[ "${pa}ck" == "$np" ]&&{
na="$ua"
q="$m/user/$na"
cfd="$q/diary"
}||na="guest"
fom(){
echo "<form method=$1 action=$j?${yzh}${toa}$2 $3>"
}
hcs(){
while read pd
do
eco "$pd"
done
}
eco(){
echo "$1<br>"
}
ipt(){
echo "<input type=text name=$1><br>"
}
fmj(){
echo "<input type=submit value=Submit>"
echo "</form>"
}
u(){
fom post
echo Login:
ipt lon
echo Password:
eco "<input type=password name=pw><br> <input name="noc" type="checkbox">Dont Use Cookie"
fmj
$hc
$hc
echo "Dont have?`clj "zc" "Join us"`"
}
bk(){
clj "main" "Back"
}
fid(){
[ "$REQUEST_METHOD" == "POST" ]&&{
l&&u||{
read b
read c
read ry
echo "$ry" >>$rmk
[ -n "$ckn" ]&&echo "`date`|$rip|$na edited $tkw">>$m/log
}
}
cat "$rmk"|hcs
[ "${qus##*w}" == "s" ]||{
l&&clj "m4" "Login"||{
fom post "$qus" "$ent"
echo Word:
ipt ry
fmj
}
$hc
}
bk
}
zxth(){
[ "$REQUEST_METHOD" == "POST" ]&&{
[ -f "$r" ]||r="$pcz/$w/talk"
read b
read c
read ry
ry="${ry%?}"
hpd $1&&ckn=1
bfx
}
hpd $1||{
eco "$w"
echo "$thc"
}
cat "$r"|hcs
[ "$cse" == "as" ]||{
l&&clj "m4" "Login"||{
[ -z $cnk ]&&{
fom post "$qus" "$ent"
echo Input reply:
ipt ry
fmj
}
}
$hc
}
hpd $1&&bkz="m7"||{
i="$(($i+1))"
w="`ls "$pcz"|pdg`"
[ -n "$w" ]&&{
qhn="${qus%=*}"
clj "${qhn%=*}=$i=0" "Next Post $w"
$hc
}
wjw "$pcz"
bkz="${qus%&m2kk=*}=$p"
}
clj "$bkz" "Back"
}
cc(){
for lop in `ls "$r/opt/"`
do
clj "${qus%=0}&jg=$lop&tpa" "$lop.$1 (`cat "$r/opt/$lop"|wcl`)"
$hc
shift
done
}
fgy(){
read a
read b
read c
}
usg(){
fne="User-$nr+User_space"
if [ -e "$s/$fne" ]
then
ls "$s"|while read mr
do
eo=$(($eo+1))
[ "$mr" == "$fne" ]&&{
clj "m1g=$eo" "$nr"
}
done
hpd $1
else
hpd $1&&clj "m4-u" "$na"||echo "$nr"
fi
hpd $1&&{
l||clj "ntf" "Notice($((`cat "$q/noce"|wcl`-`cat "$q/noct"`)))"
}
$hc
}
wpxc(){
echo "$tb"
hpd "$2"&&echo "<td>Post${thq}Reply${thq}Sender${thq}Send Time</td>"||echo "<td>File${thq}Size</td>"
p="${qus##*=}"
while read nr
do
cpo
ypd&&{
echo "<tr><td>"
hpd "$2"&&aw="=0"
clj "$1$co$aw" "$co.$nr"
echo "</td>"
hpd "$2" &&{
[ -f "$pcz/$nr" ]&&{
ift="$pcz/$nr"
ifo="$ift"
}||{
ift="$pcz/$nr/talk"
ifo="$pcz/$nr/main"
}
echo "<td>$((`cat "$ift"|wcl`/3))</td>"
cat "$ifo"|while read nc
do
ni="${nc#*:}"
nl="${ni#* }"
echo "<td>${ni%% *}$thq${nl%%#*}</td>"
break 1
done
}||{
[ -f "$cfd/$nr" ]&&echo "<td>$(fsc `ls -l "$cfd/$nr"`) B</td>"||echo "<td>`ls "$cfd/$nr"|wcl` item</td>"
}
echo "</tr>"
}
done
echo "$tbo"
opd&&clj "${qus%=*}=$(($p+10))" "<--"
cpd&&clj "${qus%=*}=$(($p-10))" "-->"
$hc
}
echo "$tb<td>"
[ -e "$m/" ]&&{
clj "main" "$wcm"
$hc
}||{
echo "Please run it on shell"
}
echo "$thc"
case $qus in
main)
gtn="(`gaen`)"
echo "$t User:"
nr="$na"
usg 1
eco "Total entry:`ls "$s"|wcl`"
[ -e "$m/bul" ]&&eco "Bulletin:`cat "$m/bul"`"
jld="`ls "$s"|wcl`"
[ "$jld" == "0" ]||{
i=$((`date +%s`%$jld+1))
sjs="`ls "$s"|pdg`"
}
fom post "m1j" "$ent"
echo "<input type=text name=kw value=${sjs%%+*}>"
fmj
echo "$tb"
echo "<td>$n$thq"
rxh 1
echo "${thc}Other$thq"
l&&u||{
clj "m4" "1.Make a new entry"
$hc
wjw "$cfd"
clj "m5=$p" "2.Diary (`ls "$q/diary"|wcl`)"
$hc
clj "m6" "3.Reset your password"
$hc
clj "m7" "4.Chat Room (`cat "$q/chat"|wcl`)"
$hc
wjw "$m/up"
clj "m8-=$p" "5.File Explorer(`ls "$m/up"|wcl`)"
}
echo "</td>$tbo"
;;
m1j)
read b
read c
read kk
kw=${kk%?}
[ -n "$kw" ]&&{
gtn="Result for $kw"
pkc(){
[ -n "`echo "$mr"|grp "$kw"`" ]
}
fqc(){
eo=0
while read mr
do
eo=$(($eo+1))
[ -e "$1/$mr" ]&&{
[ -f "$1/$mr" ]&&{
pkc&&{
clj "m8d-m8-$2-$eo" "${1#$m/up}/$mr"
$hc
}
}||{
ls "$1/$mr"|fqc "$1/$mr" "$2-$eo"
}
}
done
}
echo "Result$thc$tb<td>Entry${thq}User${thq}Post${thq}File$thc"
ls "$s"|while read mr
do
eo=$(($eo+1))
pkc&&{
clj "m1g=$eo" "${mr%%+*}"
$hc
}
done
echo "$thq"
ls "$m/user"|grp "$kw"|while read nr
do
usg
done
echo "$thq"
co=0
ls "$m/main"|while read nr
do
cpo
eo=0
ls "$m/main/$nr"|while read mr
do
eo=$(($eo+1))
pkc&&{
clj "m2k=$co&m2kk=$eo=0" "$mr"
$hc
}
done
done
echo "$thq"
ls "$m/up"|fqc "$m/up"
echo "</td>$tbo" 
}
;;
m1g=*)
i="${qus#*=}"
tkw="`ls "$s"|pdg`"
[ -n "$tkw" ]&&{
rmk="$s/$tkw"
gtn="Entry:${tkw%%+*}"
ckn="1"
fid
}
;;
m2k=*)
ind="${qus#m2k=*}"
ine="${ind%=*}"
i="${ine%&m2kk=*}"
inu="$i"
pac="`ls "$m/main"|pdg`"
[ -n "$pac" ]&&{
p="0"
pcz="$m/main/$pac"
cfd="$pcz"
cze="${qus#*&m2kk=}"
cse=${cze%&tpa}
[ "$cse" == "$qus" ]&&{
eco "`gaen`   Part:$pac"
gtn="Part:$pac"
wjs=`ls "$pcz"|wcl`
co=0
ls "$pcz"|wpxc "m2k=$i&m2kk=" "1"
l||{
fom post "m2k=$i&m2kk=as=0" "$ent"
echo Input new post title:
ipt tit
echo Word:
ipt wd
fmj
}
$hc
bk
}
cse=${cse%=0}
}
case $cse in
as)
l&&u||{
read b
read c
read tit
fgy
read wod
tit="${tit%?}"
pbz||plx
}
;;
*)
[ "${qus##*&}" == "tpa" ]&&{
l&&u||{
i="${cse%&jg=*}"
w="`ls "$pcz"|pdg`"
ry="${cse#*=}"
[ -n "$w" ]&&{
r="$pcz/$w"
[ -e "$r/opt/$ry" ]&&chse "$ry"|hcs
}
}
}||{
i="$cse"
w="`ls "$pcz"|pdg`"
[ -n "$w" ]&&{
gtn="Post:$w"
r="$pcz/$w"
[ -f "$r" ]&&zxth||{
cat "$r/main"|hcs
echo $thc
cc `cat "$r/data"`
echo $thc
[ -e "$r/talk" ]&&{
r="$r/talk"
zxth
}
}
}
}
;;
esac
;;
m4*)
l&&u||{
fom post "m4ws" "$ent"
[ "$qus" == "m4ws" ]&&{
l&&u||{
read b
read c
read mt
fgy
read tgs
fgy
read wd
mt="${mt%?}"
tgs="${tgs%?}"
mwt="$s/$mt+$tgs"
[ -z "`ls "$s"|grp "$mt"`" ]&&{ 
nwe
rmk="$mwt"
fid
}
}
}||{
[ "$qus" == "m4-u" ]&&{
echo "<input type=hidden name=tit value=User-$na ><input type=hidden name=tag value=User_space >"
}||{
echo Input Main title:
ipt tit
echo Tags:
ipt tag
}
echo Word:
ipt wd
fmj
}
}
;;
m5*)
l&&u||{
gtn="Diary"
mt="`date +%y.%m.%d`"
rmk="$cfd/$mt"
case $qus in
m5=*)
p="0"
gaen
$hc
co=0
ls "$cfd"|wpxc "m5d="
clj "m5w" "Write diary"
$hc
bk
$hc
;;
m5w)
[ -n "`ls "$cfd"|grp "$mt"`" ]&&fid||{
fom post "m5ws" "$ent"
echo "Word:"
ipt wd
fmj
}
;;
m5ws)
read b
read c
read wd
echo Diary:$mt>>$rmk
echo $wd >>$rmk
fid
;;
m5d=*)
i="${qus#*=}" 
cfd="$q/diary"
w="`ls "$cfd"|pdg`"
[ -n "$w" ]&&{
rmk="$cfd/$w"
fid
}
;;
esac
}
;;
m6)
l&&u||{
fom post "m6e"
echo Input your new password:
$spa
fmj
}
;;
m6e)
nrd="${tl#*=}"
[ -n "$nrd" ]&&echo $nrd>$q/pwd
echo OK
;;
m7)
l&&u||{
cfd="$q/chat"
p="0"
eco "Chat Room"
gtn="Chat Room"
gaen
$hc
echo $thc
co=0
cat "$cfd"|while read nr
do
cpo
clj "m7k=$co" "$co.${nr#*,}"
$hc
done
echo $thc
fom post "m7a" "$ent"
echo Input new room name:
ipt qmz
fmj
bk
}
;;
m7a)
l&&u||{
read b
read c
read qmz
w="$((`ls "$m/room"|wcl`+1))"
r="$m/room/$w"
echo "Chat Room #$w">$r
echo "$fgx">>$r
echo "$w,$qmz">>$m/user/$na/chat
gtn="Room:No.$w"
r="$m/room/$w"
cnk=1
zxth "1"
}
;;
m7k=*)
cfd="$q/chat"
i="${qus#*=}"
wwn="`cat "$cfd"|pdg`"
w="${wwn%%,*}"
qmz="${wwn#*,}"
[ -n "$w" ]&&{
gtn="Room:No.$w"
r="$m/room/$w"
zxth 1
}
;;
m8-*)
a="${qus%=*}"
ndt "m8"
cfd="$m/up$out"
eco "File Explorer"
gtn="Path:/${out#/}"
eco "Path:/${out#/}"
gaen
clj "m8v" "Photo Viewer"
$hc
co=0
a="${qus%=*}"
ls "$cfd"|wpxc "m8d-$a-"
eco "Upload File:"
fom post "m8u-$a" "$ent"
echo "<input type=file name=file>"
fmj
eco "Make new folder name:"
fom post "m8n-$a" "$ent"
ipt nm
fmj
$hc
wjw "$m/up${out%/*}"
[ "$a" == "m8-" ]&&bk||clj "${a%-*}=$p" "Back"
;;
m8u-m8-*)
l&&u||{
a="${qus%=*}"
ndt "m8u-m8"
cfd="$m/up$out"
read meta
read a
read b
fnm="${meta#*filename=}"
nu="${fnm#\"*}"
mu="${nu%\"*}"
echo "`date`|$rip|$na Uploaded $mu">>$m/log
cat >"$cfd/$mu"
echo "$out/$mu saved."
}
;;
m8n-m8-*)
l&&u||{
a="${qus%=*}"
ndt "m8n-m8"
cfd="$m/up$out"
read b
read c
read nm
nm="${nm%?}"
[ -e "$cfd/$nm" ]||{
mkdir "$cfd/$nm"&&echo "OK,$out/$nm Created"||echo "Fail"
}
}
;;
m8v)
p="0"
gtn="Photo Viewer"
eco "Photo Viewer"
echo "$tb"
co=0
mo="0"
ls "$m/up/"|while read nr
do
cpo
[ "${nr##*.}" == "jpg" ]&&{
mo="$(($mo+1))"
echo "<td>"
clj "m8x=$co" "<img src=$j?m8d-m8-$co width=80px height=60px /><br>$nr"
echo "</td>"
[ "$((${mo}%3))" == "0" ]&&{
echo "</tr><tr>"
}
}
done
echo "$tbo"
wjw "$m/up"
clj "m8-=$p" "Back"
;;
m8x=*)
i="${qus#*=}" 
cfd="$m/up"
eco "<img src=$j?m8d-m8-$i />"
while [ "${w##*.}" != "jpg" ]
do
i=$(($i+1))
cfd="$m/up"
w="`ls "$cfd"|pdg`"
[ -z "$w" ]&&break 1
[ "${w##*.}" == "jpg" ]&&{
clj "m8x=$i" "Next Photo"
break 1
}
done
$hc
clj "m8v" "Back"
;;
ntf*)
[ "$qus" == "ntf-c" ]&&{
>"$q/noce"
echo "0">"$q/noct"
}
[ -e "$q/noce" ]&&{
echo "`cat "$q/noce"|wcl`">"$q/noct"
cat "$q/noce"|while read nr
do
nef
clj "m2k=$iao&m2kk=$iob=0" "$yti"
$hc
done
}
clj "ntf-c" "Clear"
bk
;;
zc)
uck
fom post "zct&vv=$vv"
echo $wna
ipt name
echo $wnb
$spa
eco "$wnc"
eco $vv
ipt vv
fmj
;;
zct*)
vs="${qus#*=}"
tid="${tl%&pw*}"
npe="${tl#*pw=}"
npd="${npe%&vv*}"
nep="${tid#*=}"
vv="${tl##*=}"
[ "$vv" == "$vs" ]&&{
chk="`ls "$m/user"|grp "$nep"`"
rck||{
zcc&&{
fom post
echo "OK<br>Onekey Login:<input type=hidden name=lon value=$nep ><input type=hidden name=pw value=$npd >"
fmj
}
}
}
;;
esac
$hc
[ -n "`cat "$m/ip"|grp "$rip"`" ]||echo "$rip">>$m/ip
eco "${thc}`cat "$m/ip"|wcl` people visited the website"
eco "You can use more thing on <a href=telnet://$HTTP_HOST>Telnet Version</a>"
echo "Copyright (C) `date +%Y` by Mayx</td>$tbo <title>$zsn $gtn</title>"
}|while read rot
do
echo "${rot##*<script>*}"
done|gzip -c
;;
esac
}