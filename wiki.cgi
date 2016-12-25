#!/system/bin/ash
hos="/sdcard/ba"
whk="$hos/wiki"
gly="SYSOP"
err="echo Error!"
fgx="============"
glp(){
[ "$na" == "guest" ]
}
plx(){
stt="$pcz/$tit"
echo $tit >>$stt
echo $fgx >>$stt
echo Post master:$na  `date` >>$stt
echo $wod >>$stt
echo >>$stt
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
*${1}*)
echo $nr
;;
esac
done
}
zcc(){
usk="$hos/user/$nep"
mkdir -p "$usk/diary" "$usk/mail"
>"$usk/chat"
echo $npd>>$usk/pwd
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
wbn=""
co="0"
while read nr
do
co=$(($co+1))
[ "$int" == "$co" ]&&echo "$nr"
done
}
chse(){
glp&&wblg||{
vck="`cat "$wbb/opt/$1"|grp "$na"`"
[ "$na" == "$vck" ]||{
echo $na >> "$wbb/opt/$1"
[ -z "$HTTP_HOST" ]&&{
cat "$wbb/opt/$1"
}||{
cat "$wbb/opt/$1"|hcs
}
echo "selected it."
}
}
}
[ -z "$REMOTE_ADDR" ]&&{
inc="echo Input number or command:"
[ -e "$hos/" ]&&echo 'Welecome to use MaWiki&BBS'||{
echo Installing...
mkdir -p "$hos/main" "$hos/user" "$whk" "$hos/room" "$hos/up"
>"$hos/ip"
nep="$gly"
echo Master name:$gly
echo New password:
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
[ `ls "$1"|wcl` -ge 10 ]&&sel="$(($sel+10))" 
}
fyx(){
[ `ls "$1"|wcl` -ge 10 ]&&echo c.Next page
}
wblg(){
clear
echo Login:
read ua
echo Password:
read pa
[ -z "$ua" ]&&np=0||{
[ -e "$hos/user/$ua" ]&&np="`cat "$hos/user/$ua/pwd"`ck"
}
[ "${pa}ck" == "$np" ]&&{
na="$ua"
usv="$hos/user/$na"
}||{
$err
echo Join us?[Y/N]:
read ju
case $ju in
Y|y)
echo Please input your name:
read nep
echo Please input new password:
read npd
chk="`ls "$hos/user"|grp "$nep"`"
[ "$chk" == "$nep" -o "$nep" = "" ]||{
echo Please input verifcation code:
vv="`cat /proc/sys/kernel/random/uuid`"
vv="${vv%%-*}"
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
}
fid(){
while true
do
clear
cat "$rmk"
echo Press enter to back
glp&&{
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
cat "$wbb"
echo 'Input reply(Input e go back):'
slp&&echo Input d delete the post
[ "$1" == "1" ]&&echo "Input a to add friend:"
read ry
case $ry in
e)
break 1
;;
d)
slp&&rm -rf "$wbb"&break 1
;;
a)
[ "$1" == "1" ]&&{
clear
echo Input friend name:
read fnm
[ -n "$fnm" -a -e "$hos/user/$fnm" ]&&echo "$wbn,$qmz">>"$hos/user/$fnm/chat"
}
;;
*)
[ -n "$ry" ]&&{
glp&&wblg||{
echo $na  `date` >>$wbb
echo $ry >>$wbb
echo >>$wbb
}
}
;;
esac
done
}
pxcx(){
while read nr
do
co=$(($co+1))
[ "$sel" -le "$co" -a "$(($sel+10))" -ge "$co" ]&&echo "$1$co.$nr"
done
}
cc(){
for lop in `ls "$wbb/opt/"`
do
echo $lop.$1 \(`cat "$wbb/opt/$lop"|wcl`\)
shift
done
}
na="guest"
sleep 1
until [ "$cmd" == "2" ]
do
clear
echo "MaWiki User:$na"
echo Total entry:`ls "$whk"|wcl`
echo $fgx
echo 1.Search
echo 2.Exit
echo 3.Go to MaBBS
echo 4.Random
echo 5.Novel Viewer
glp&&echo 6.Login||{
echo 6.Make a new entry
echo 7.Diary 
echo 8.Reset your password
echo 9.Chat Room
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
echo Result
echo $fgx
echo Entry
echo -------
co="0"
ls "$whk"|grp "$kw"|while read jg
do
co=$(($co+1))
echo a$co.${jg%%+*}
done
echo User
echo -------
ls "$hos/user"|grp "$kw"
echo Post
echo -------
ls "$hos/main"|while read nr
do
ls "$hos/main/$nr"|grp "$kw"
done
echo "Novel"
echo "-------"
sel="0"
ls "$hos/up"|grp ".txt"|grp "$kw"|pxcx "b"
echo Which one:
read mtt
case $mtt in
a*)
int="${mtt#a}"
tkw="`ls "$whk"|grp "$kw"|pdg`"
[ -n "$tkw" ]&&{
rmk="$whk/$tkw"
fid
}
;;
b*)
int="${mtt#b}"
tkw="`ls "$hos/up"|grp "$kw"|pdg`"
[ -n "$tkw" ]&&{
clear
more "$hos/up/$tkw"
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
[ -e "$hos/bul" ]&&echo Bulletin:`cat "$hos/bul"`
echo $fgx
co=0
ls "$hos/main"|while read bm
do
co=$(($co+1))
echo $co.$bm \(`ls "$hos/main/$bm/"|wcl`\)
done
echo $fgx
echo a.Back to MaWiki
slp&&{
echo b.Make a part
echo c.Release bulletin
}
$inc
read pac
[ -n "$pac" ]||pac="#"
case $pac in
a)
break 1
;;
b)
clear
slp&&{
echo New part name:
read npn
mkdir "$hos/main/$npn"
}
;;
c)
slp&&{
clear
echo Input bulletin:
read bul
echo "$bul" > $hos/bul
}
;;
*)
int="$pac"
pac="`ls "$hos/main"|pdg`"
[ -n "$pac" ]&&{
sel="0"
while true
do
pcz="$hos/main/$pac"
clear
echo `gaen`   Part:$pac
echo $fgx
co="0"
ls "$pcz"|pxcx
echo $fgx
echo a.Make a new post
bk
fyx "$pcz"
slp&&echo d.Delete the part
$inc
read int
case $int in
a)
glp&&wblg||{
clear
echo 'This is a [1.Post 2.Vote]:'
read cht
case $cht in
1)
clear
echo Input the title:
read tit
[ -n "`ls "$pcz"|grp "$tit"`" ]||{
echo Word:
read wod
plx
}
;;
2)
clear
echo Input the title:
read tit
[ -n "`ls "$pcz"|grp "$tit"`" ]||{
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
echo $tit >>$tsm/main
echo $fgx >>$tsm/main
echo Vote master:$na  `date` >>$tsm/main
echo $wod >>$tsm/main
echo $opt>>$tsm/data
mkdir "$tsm/opt" 
for sle in $oph
do
>"$tsm/opt/$sle"
done
[ "$utk" == "y" ]&&{
echo Talk>>"$tsm/talk"
echo $fgx >>"$tsm/talk"
}
}
;; 
esac
}
;;
b)
break 1
;;
c)
fy "$pcz"
;;
d)
slp&&rm -rf "$pcz"&break 1
;;
*)
wbn="`ls "$pcz"|pdg`"
[ -n "$wbn" ]&&{
wbb="$pcz/$wbn"
[ -f "$wbb" ]&&zxth||{
clear
cat "$wbb/main"
echo $fgx
cc `cat "$wbb/data"`
[ -e "$wbb/talk" ]&&echo Input t to talk,or
echo 'Choose one:'
read ry
[ -n "$ry" ]&&{
[ "$ry" == "t" ]&&{
[ -e "$wbb/talk" ]&&{
wbb="$wbb/talk"
zxth
}
}||{
clear
[ -e "$wbb/opt/$ry" ]&&chse $ry
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
cfd="$hos/up"
sel="0"
while true
do
clear
echo Novel Viewer
echo $fgx
co="0"
ls "$cfd"|grp ".txt"|pxcx
echo $fgx
echo You can Upload novel on Web
bk
fyx "$cfd"
$inc
read int
case $int in
b)
break 1
;;
c)
fy "$cfd"
;;
*)
wbn="`ls "$cfd"|grp ".txt"|pdg`"
[ -n "$wbn" ]&&{
clear
more "$cfd/$wbn"
read nul
}
;;
esac
done
;;
6)
glp&&wblg||{
clear
echo Input Main title:
read mt
[ -z "`ls "$whk"|grp "$mt"`" ]&&{
echo Tags:
read tgs
echo Word:
read wd
mwt="$whk/$mt+$tgs"
echo $mt>>$mwt
echo Made by:$na `date`>>$mwt
echo Tags:$tgs>>$mwt
echo $fgx >>$mwt
echo $wd >>$mwt
rmk="$whk/$mt+$tgs"
fid
}
}
;;
4)
jld="`ls "$whk"|wcl`"
[ "$jld" == "0" ]&&{
echo Not found...
sleep 1
}||{
int=$((`date +%s`%$jld+1))
rmk="$whk/`ls "$whk"|pdg`"
fid
}
;;
7)
glp&&wblg||{
cfd="$usv/diary"
sel="0"
while true
do
clear
gaen
echo $fgx
co="0"
ls "$cfd"|pxcx
echo $fgx
echo a.Write diary
bk
fyx "$cfd"
$inc
read int
case $int in
a)
clear
mt="`date +%y.%m.%d`"
[ -n "`ls "$cfd"|grp "$mt"`" ]||{
echo Word:
read wd
mwt="$cfd/$mt"
echo Diary:$mt>>$mwt
echo $wd >>$mwt
}
rmk="$cfd/$mt"
fid
;;
b)
break 1
;;
c)
fy "$cfd"
;;
*)
wbn="`ls "$cfd"|pdg`"
[ -n "$wbn" ]&&{
rmk="$cfd/$wbn"
fid
}
;;
esac
done
}
;;
8)
glp&&wblg||{
clear
echo Input your new password:
read nrd
[ -n "$nrd" ]&&echo $nrd>$usv/pwd
}
;;
9)
glp&&wblg||{
cfd="$usv/chat"
sel="0"
while true
do
clear
echo Chat Room
gaen
echo $fgx
co="0"
cat "$cfd"|while read nr
do
co=$(($co+1))
echo $co.${nr#*,}
done
echo $fgx
echo a.Make chat room
bk
$inc
read int
case $int in
a)
clear
echo Input Chat room name:
read qmz
wbn="$((`ls "$hos/room"|wcl`+1))"
wbb="$hos/room/$wbn"
echo "Chat Room #$wbn">$wbb
echo "$fgx">>$wbb
echo "$wbn,$qmz">>$cfd
zxth "1"
;;
b)
break 1
;;
*)
wwn="`cat "$cfd"|pdg`"
wbn="${wwn%%,*}"
qmz="${wwn#*,}" 
[ -n "$wbn" ]&&{
wbb="$hos/room/$wbn"
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
qus="$QUERY_STRING"
[ "${qus%%=*}" == "m8d" ]&&{
int="${qus#*=}" 
cfd="$hos/up"
wbn="`ls "$cfd"|pdg`"
[ -f "$cfd/$wbn" ]&&{
[ "${wbn##*.}" == "jpg" ]&&cot="image/jpeg"||cot="application/octet-stream"
echo "Content-type:$cot;charset=utf-8"
echo "Content-Disposition:filename=$wbn"
echo ""
[ -n "$wbn" ]&&cat "$cfd/$wbn"
}
}||{
echo "Content-Encoding:gzip"
echo "Content-type:text/html;charset=utf-8"
read tl
[ "${tl%%=*}" == "lon" ]&&echo "Set-Cookie:$tl;PATH=/"
echo ""
{
echo '<title>Mabbs&Wiki</title>'
hc='echo <br>'
tb="<table border=1><tr>"
thc="</td></tr><tr><td>"
tbo="</tr></table>"
ent="enctype=multipart/form-data"
uma="${HTTP_COOKIE%&pw*}"
ua="${uma#*=}"
pa="${HTTP_COOKIE#*pw=}"
[ -z "$ua" ]&&np=0||{
[ -e "$hos/user/$ua" ]&&np="`cat "$hos/user/$ua/pwd"`ck"
}
[ "${pa}ck" == "$np" ]&&{
na="$ua"
usv="$hos/user/$na"
}||na="guest"
fom(){
echo "<form method=$1 action=$2 $3>"
}
ipt(){
echo "<input type=text name=$1><br>"
}
eco(){
echo "$1<br>"
}
fmj(){
echo "<input type=submit value=Submit>"
echo "</form>"
}
wblg(){
fom post "$0"
echo Login:
eco "<input type=text name=lon>"
echo Password:
eco "<input type=password name=pw>"
fmj
$hc
$hc
echo "Dont have?<a href=$0?zc>Join us</a>"
}
hcs(){
while read pd
do
eco "$pd"
done
}
bk(){
clj "main" "Back"
}
clj(){
echo "<a href=$0?$1>$2</a>"
}
fid(){
[ "$REQUEST_METHOD" == "POST" ]&&{
glp&&wblg||{
read b
read c
read ry
echo "$ry" >>$rmk
}
}
cat "$rmk"|hcs
[ "${qus##*w}" == "s" ]||{
glp&&eco "<a href=$0?m4>Login</a>"||{
fom post "$0?$qus" "$ent"
echo Word:
ipt ry
fmj
$hc
}
}
bk
}
zxth(){
cat "$rmk"|hcs
glp&&eco "<a href=$0?m4>Login</a>"||{
fom post "$0?$qus" "$ent"
echo Input reply:
ipt ry
fmj
$hc
}
int="$(($int+1))"
wbn="`ls "$pcz"|pdg`"
[ -n "$wbn" ]&&{
clj "${qus%=*}=$int" "Next Post $wbn"
$hc
}
clj "${qus%&m2kk=*}" "Press there to back"
}
cc(){
for lop in `ls "$rmk/opt/"`
do
clj "$qus&jg=$lop&tpa" "$lop.$1 (`cat "$rmk/opt/$lop"|wcl`)"
$hc
shift
done
}
fgy(){
read a
read b
read c
}
wpxc(){
echo "$tb"
[ "$2" == "1" ]&&echo "<td>Post</td><td>Reply</td><td>Sender</td><td>Send Time</td>"
while read nr
do
co=$(($co+1))
echo "<tr><td>"
clj "$1=$co" "$co.$nr"
echo "</td>"
[ "$2" == "1" ]&&{
[ -f "$pcz/$nr" ]&&{
ift="$pcz/$nr"
ifo="$ift"
}||{
ift="$pcz/$nr/talk"
ifo="$pcz/$nr/main"
} 
echo "<td>$(((`cat "$ift"|wcl`-2)/3))</td>"
mo=0
cat "$ifo"|while read nc
do
mo=$(($mo+1))
[ $mo == 3 ]&&{
ni="${nc#*:}"
echo "<td>${ni%% *}</td><td>${ni#* }</td>"
break 1
}
done
}
echo "</tr>"
done
echo "$tbo"
}
echo "$tb<td>"
[ -e "$hos/" ]&&{
clj "main" "Welecome to use Mabbs&Wiki"
$hc
}||{
echo "Please run it on shell"
}
echo "$thc"
case $qus in
main)
eco "MaWiki User:$na"
eco "Total entry:`ls "$whk"|wcl`"
[ -e "$hos/bul" ]&&eco "Bulletin:`cat "$hos/bul"`"
jld="`ls "$whk"|wcl`"
[ "$jld" == "0" ]||{
int=$((`date +%s`%$jld+1))
sjs="`ls "$whk"|pdg`"
} 
fom post "$0?m1j" "$ent"
echo "<input type=text name=kw value=${sjs%%+*}>"
fmj
echo "$tb"
echo "<td>MaBBS</td><td>"
co=0
ls "$hos/main"|while read bm
do
co=$(($co+1))
clj "m2k=$co" "$co.$bm (`ls "$hos/main/$bm/"|wcl`)"
$hc
done
echo "${thc}Other</td><td>"
glp&&wblg||{
clj "m4" "1.Make a new entry"
$hc
clj "m5" "2.Diary"
$hc
clj "m6" "3.Reset your password"
$hc
clj "m7" "4.Chat Room"
$hc
clj "m8" "5.File Explorer"
}
echo "</td>$tbo"
;;
m1j)
read b
read c
read kk
kw=${kk%?}
[ -n "$kw" ]&&{
echo "Result$thc"
eco "Entry"
eco "$fgx"
ls "$whk"|while read mr
do
eo=$(($eo+1))
[ -n "`echo "$mr"|grp "$kw"`" ]&&{
clj "m1g=$eo" "${mr%%+*}"
$hc
}
done
eco User
eco "$fgx"
ls "$hos/user"|grp "$kw"|hcs
eco Post
eco "$fgx"
co=0
ls "$hos/main"|while read nr
do
co=$(($co+1))
eo=0
ls "$hos/main/$nr"|while read mr
do
eo=$(($eo+1))
[ -n "`echo "$mr"|grp "$kw"`" ]&&{
clj "m2k=$co&m2kk=$eo" "$mr"
$hc
}
done
done
eco File
eco "$fgx"
ls "$hos/up"|while read mr
do
eo=$(($eo+1))
[ -n "`echo "$mr"|grp "$kw"`" ]&&{
clj "m8d=$eo" "$mr"
$hc
}
done
}
;;
m1g=*)
int="${qus#*=}"
tkw="`ls "$whk"|pdg`"
[ -n "$tkw" ]&&{
rmk="$whk/$tkw"
fid
}
;;
m2k=*)
ind="${qus#*=}"
int="${ind%&m2kk=*}"
pac="`ls "$hos/main"|pdg`"
[ -n "$pac" ]&&{
sel="0"
pcz="$hos/main/$pac"
cze="${qus#*&m2kk=}"
cse=${cze%&hfz}
cse=${cse%&tpa}
[ "$cse" == "$qus" ]&&{
eco "`gaen`   Part:$pac"
co="0"
ls "$pcz"|wpxc "$qus&m2kk" "1"
clj "$qus&m2kk=a" "Make a new post"
$hc
bk
}
}
case $cse in
a)
glp&&wblg||{
fom post "$0?m2k=$int&m2kk=as" "$ent"
echo Input the title:
ipt tit
echo Word:
ipt wd
fmj
}
;;
as)
glp&&wblg||{
read b
read c
read tit
fgy
read wod
tit="${tit%?}"
[ -n "`ls "$pcz"|grp "$tit"`" ]||{
plx
echo "OK!"
}
}
;;
*)
[ "${qus##*&}" == "tpa" ]&&{
glp&&wblg||{
int="${cse%&jg=*}"
wbn="`ls "$pcz"|pdg`"
ry="${cse#*=}"
[ -n "$wbn" ]&&{
wbb="$pcz/$wbn"
[ -e "$wbb/opt/$ry" ]&&chse $ry
}
}
}||{
int="$cse"
wbn="`ls "$pcz"|pdg`"
[ -n "$wbn" ]&&{
rmk="$pcz/$wbn"
[ "$REQUEST_METHOD" == "POST" ]&&{
glp&&wblg||{
[ -f "$rmk" ]||rmk="$pcz/$wbn/talk" 
read b
read c
read ry
echo $na  `date` >>$rmk
echo "$ry" >>$rmk
echo >>$rmk
}
}
[ -f "$rmk" ]&&zxth||{
cat "$rmk/main"|hcs
eco $fgx
cc `cat "$rmk/data"`
eco $fgx
[ -e "$rmk/talk" ]&&{
rmk="$rmk/talk"
zxth
}
}
}
}
;;
esac
;;
m4)
glp&&wblg||{
fom post "$0?m4ws" "$ent"
echo Input Main title:
ipt tit
echo Tags:
ipt tag
echo Word:
ipt wd
fmj
}
;;
m4ws)
glp&&wblg||{
read b
read c
read tit
fgy
read tag
fgy
read wd
tit="${tit%?}"
tag="${tag%?}"
mwt="$whk/$tit+$tag"
[ -z "`ls "$whk"|grp "$tit"`" ]&&{
echo $tit>>$mwt
echo Made by:$na `date`>>$mwt
echo Tags:$tag>>$mwt
echo $fgx >>$mwt
echo "$wd" >>$mwt
rmk="$mwt"
fid
}
}
;;
m5*)
glp&&wblg||{
cfd="$usv/diary"
mt="`date +%y.%m.%d`"
rmk="$cfd/$mt"
case $qus in
m5)
sel="0"
gaen
$hc
co="0"
ls "$cfd"|wpxc "m5d"
clj "m5w" "Write diary"
$hc
bk
$hc
;;
m5w)
[ -n "`ls "$cfd"|grp "$mt"`" ]&&fid||{
fom post "$0?m5ws" "$ent"
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
int="${qus#*=}" 
cfd="$usv/diary"
wbn="`ls "$cfd"|pdg`"
[ -n "$wbn" ]&&{
rmk="$cfd/$wbn"
fid
}
;;
esac
}
;;
m6)
glp&&wblg||{
fom post "$0?m6e"
echo Input your new password:
echo "<input type=password name=pw><br>"
fmj
}
;;
m6e)
nrd="${tl#*=}"
[ -n "$nrd" ]&&echo $nrd>$usv/pwd
echo OK
;;
m7)
glp&&wblg||{
cfd="$usv/chat"
sel="0"
eco "Chat Room"
gaen
$hc
echo $thc
co="0"
cat "$cfd"|while read nr
do
co=$(($co+1))
clj "m7k=$co" "$co.${nr#*,}"
$hc
done
echo $thc
bk
}
;;
m7k=*)
cfd="$usv/chat"
ind="${qus#*=}"
int="${ind%&hfz}"
wwn="`cat "$cfd"|pdg`"
wbn="${wwn%%,*}"
[ -n "$wbn" ]&&{
wbb="$hos/room/$wbn"
[ "$REQUEST_METHOD" == "POST" ]&&{
read b
read c
read ry
echo $na  `date` >>$wbb
echo "$ry" >>$wbb
echo >>$wbb
}
cat "$wbb"|hcs
fom post "$0?m7k=$int" "$ent"
echo "Input reply:<input type=text name=ry><br>"
fmj
$hc
clj "m7" "Press there to back"
}
;;
m8)
sel="0"
eco "File Explorer"
gaen
clj "m8v" "Photo Viewer"
$hc
co="0"
ls "$hos/up"|wpxc "m8d"
eco "Upload Novel:(Upload other use <a href=ftp://$HTTP_HOST>FTP</a>)"
fom post "action=$0?m8u" "$ent" 
echo "<input type=file name=file>"
fmj
$hc
bk
;;
m8u)
read meta
read ct
fnm="${meta#*filename=}"
nu="${fnm#\"*}"
mu="${nu%\"*}"
st="$hos/up/${mu%.txt}.txt"
echo "Uploader:$na">$st
cat >>$st
echo "${mu%.txt}.txt saved."
;;
m8v)
sel="0"
eco "Photo Viewer"
echo "$tb"
co="0"
mo="0"
ls "$hos/up/"|while read nr
do
co=$(($co+1))
[ "${nr##*.}" == "jpg" ]&&{
mo=$(($mo+1))
echo "<td>"
clj "m8x=$co" "<img src=$0?m8d=$co width=80px height=60px />"
echo "</td>"
[ "$mo" == "3" ]&&{
echo "</tr><tr>"
mo="0"
}
}
done
echo "$tbo"
clj "m8" "Back"
;;
m8x=*)
int="${qus#*=}" 
cfd="$hos/up"
eco "<img src=$0?m8d=$int />"
while [ "${wbn##*.}" != "jpg" ]
do
int=$(($int+1))
cfd="$hos/up"
wbn="`ls "$cfd"|pdg`"
[ -z "$wbn" ]&&break 1
[ "${wbn##*.}" == "jpg" ]&&{
clj "m8x=$int" "Next Photo"
break 1
}
done
$hc
clj "m8v" "Back"
;;
zc)
vv="`cat /proc/sys/kernel/random/uuid`"
vv="${vv%%-*}"
fom post "$0?zct&vv=$vv"
echo Please input your name:
ipt name
echo Please input new password:
echo "<input type=password name=pw><br>"
eco "Please input verifcation code:"
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
chk="`ls "$hos/user"|grp "$nep"`"
[ "$chk" == "$nep" -o "$nep" = "" ]||{
zcc
echo OK
}
}
;;
esac
$hc
rip="${REMOTE_ADDR##*:}"
[ -z `cat "$hos/ip"|grp "$rip"` ]&&echo "$rip">>$hos/ip
eco "${thc}Counter:`cat "$hos/ip"|wcl`"
eco "You can use more thing on <a href=telnet://$HTTP_HOST>Telnet Version</a>"
echo "Copyright (C) `date +%Y` by Mayx</td>$tbo"
}|gzip -c
}
}