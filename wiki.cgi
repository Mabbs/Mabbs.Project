#!/system/bin/ash
hos="/sdcard/ba"
bsn="MaBBS"
wsn="MaWiki"
zsn="$bsn&Wiki"
wcm="Welecome to use $zsn"
whk="$hos/wiki"
wna="Please input your name:"
wnb="Please input new password:"
wnc="Please input verifcation code:"
gly="SYSOP"
j="${0##*/}"
err="echo Error!"
fgx="============"
rip="$REMOTE_ADDR"
pbz(){
[ -n "`ls "$pcz"|grp "$tit"`" ]
}
cpo(){
co=$(($co+1))
}
clj(){
echo "<a href=$j?$1>$2</a>"
}
glp(){
[ "$na" == "guest" ]
}
hpd(){
[ "$1" == "1" ]
}
cpd(){
[ "$sel" -gt "1" ]
}
rck(){
[ -n "`echo $nep|grp " "`" -o "$chk" == "$nep" -o -z "$nep" ]
}
uck(){
vv="`cat /proc/sys/kernel/random/uuid`"
vv="${vv%%-*}"
}
ypd(){
[ "$sel" -le "$co" -a "$(($sel+10))" -gt "$co" ]
}
wjw(){
sel="$((`ls "$1"|wcl`-9))"
}
bfx(){
[ -n "$ry" ]&&{
glp&&wblg||{
echo "$na  `date` #$((`cat "$wbb"|wcl`/3+1))
$ry
">>$wbb
cat "$wbb"|while read nc
do
ni="${nc#*r:}"
echo "$na reply you on `clj "m2k=$inu&m2kk=$int=0" "$wbn"`">>$hos/user/${ni%% *}/noce
break 1
done
}
}
}
plx(){
wbn="$tit"
wbb="$pcz/$tit"
echo "Post master:$na  `date` #1
$wod
">>$wbb
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
usk="$hos/user/$nep"
mkdir "$usk/diary"
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
co=0
while read nr
do
cpo
[ "$int" == "$co" ]&&echo "$nr"
done
}
chse(){
glp&&wblg||{
vck="`cat "$wbb/opt/$1"|grp "$na"`"
[ "$na" == "$vck" ]||{
echo $na >> "$wbb/opt/$1"
}
cat "$wbb/opt/$1"
echo "selected it."
}
}
[ -z "$rip" ]&&{
inc="echo Input number or command:"
[ -e "$hos/" ]&&echo "$wcm"||{
echo Installing...
mkdir -p "$hos/main" "$hos/user" "$whk" "$hos/room" "$hos/up"
>"$hos/ip"
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
cpd&&sel="$(($sel-10))" 
}
fyx(){
cpd&&echo c.Next page
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
echo $wna
read nep
echo $wnb
read npd
chk="`ls "$hos/user"|grp "$nep"`"
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
hpd $1||{
echo "$wbn
$fgx"
}
cat "$wbb"
echo 'Input reply(Input e go back):'
slp&&echo Input d delete the post
hpd $1&&echo "Input a to add friend:"
read ry
case $ry in
e)
break 1
;;
d)
slp&&rm -rf "$wbb"&break 1
;;
a)
hpd $1&&{
clear
echo Input friend name:
read fnm
[ -n "$fnm" -a -e "$hos/user/$fnm" ]&&echo "$wbn,$qmz">>"$hos/user/$fnm/chat"
}
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
ypd&&echo "$1$co.$nr"
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
echo "$wsn User:$na
Total entry:`ls "$whk"|wcl`
$fgx
1.Search
2.Exit
3.Go to $bsn
4.Random
5.Novel Viewer"
glp&&echo 6.Login||{
echo "6.Make a new entry
7.Diary
8.Reset your password
9.Chat Room"
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
ls "$whk"|grp "$kw"|while read jg
do
cpo
echo a$co.${jg%%+*}
done
echo "User
$fgx"
ls "$hos/user"|grp "$kw"
echo "Post
$fgx"
ls "$hos/main"|while read nr
do
ls "$hos/main/$nr"|grp "$kw"
done
echo "Novel
$fgx"
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
cpo
echo $co.$bm \(`ls "$hos/main/$bm/"|wcl`\)
done
echo "$fgx
a.Back to $wsn"
glp||echo "b.Notice"
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
glp&&wblg||{
clear
cat "$usv/noce"
read nul
}
;;
c)
clear
slp&&{
echo New part name:
read npn
mkdir "$hos/main/$npn"
}
;;
d)
slp&&{
clear
echo Input bulletin:
read bul
echo "$bul">$hos/bul
}
;;
*)
inu="$pac"
int="$pac"
pac="`ls "$hos/main"|pdg`"
[ -n "$pac" ]&&{
pcz="$hos/main/$pac"
wjw "$pcz"
while true
do
clear
echo "`gaen`   Part:$pac
$fgx"
co=0
ls "$pcz"|pxcx
echo "$fgx
a.Make a new post"
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
wjw "$cfd"
while true
do
clear
echo "Novel Viewer
$fgx"
co=0
ls "$cfd"|grp ".txt"|pxcx
echo "$fgx
You can Upload novel on Web"
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
nwe
rmk="$mwt"
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
wjw "$cfd"
while true
do
clear
gaen
echo $fgx
co=0
ls "$cfd"|pxcx
echo "$fgx
a.Write diary"
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
echo "Diary:$mt
$wd">>$mwt
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
ctj(){
echo "Content-type:$1;charset=utf-8"
}
rxh(){
co=0
ls "$hos/main"|while read bm
do
cpo
eu="$hos/main/$bm"
wjw "$eu"
txc="$co.$bm(`ls "$eu"|wcl`)"
hpd $1&&{
clj "m2k=$co=$sel" "$txc"
$hc
}||echo "<item><title>$txc</title><link>${wsf}?m2k=$co=$sel</link></item>"
done
} 
qus="$QUERY_STRING"
case $qus in
m8d=*)
int="${qus#*=}" 
cfd="$hos/up"
wbn="`ls "$cfd"|pdg`"
[ -f "$cfd/$wbn" ]&&{
ctj "application/octet-stream"
co=0
for fcl in `ls -l "$cfd/$wbn"`
do
cpo
[ $co == 4 ]&&echo "Content-length:$fcl
Content-Disposition:attachment;filename=\"$wbn\"
"
done
[ -n "$wbn" ]&&cat "$cfd/$wbn"
}
;;
rss)
ctj "text/xml"
wsf="http://$HTTP_HOST/cgi-bin/$j"
echo '
<?xml version="1.0"?><rss version="2.0"><channel><title>'
echo "$bsn</title><link>${wsf}?main</link>"
rxh
echo "</channel></rss>"
;;
*)
read tl
[ "${tl%%=*}" == "lon" ]&&{
echo "HTTP/1.1 302 Found
Location:$j?main
Set-Cookie:$tl;PATH=/"
}||{
echo "Content-Encoding:gzip"
ctj "text/html"
}
echo ""
{
echo "<title>$zsn</title><link rel="alternate" type="application/rss+xml" title="$bsn" href="$j?rss" >"
hc='echo <br>'
tb="<table border=1><tr>"
thc="</td></tr><tr><td>"
tbo="</tr></table>"
thq="</td><td>"
spa="echo <input type=password name=pw><br>"
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
cfd="$usv/diary"
}||na="guest"
fom(){
echo "<form method=$1 action=$j?$2 $3>"
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
wblg(){
fom post
echo Login:
ipt lon
echo Password:
eco "<input type=password name=pw>"
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
glp&&wblg||{
read b
read c
read ry
echo "$ry" >>$rmk
}
}
cat "$rmk"|hcs
[ "${qus##*w}" == "s" ]||{
glp&&clj "m4" "Login"||{
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
[ -f "$wbb" ]||wbb="$pcz/$wbn/talk"
read b
read c
read ry
ry="${ry%?}"
bfx
}
hpd $1||{
eco "$wbn"
echo "$thc"
}
cat "$wbb"|hcs
[ "$cse" == "as" ]||{
glp&&clj "m4" "Login"||{
hpd $1&&hyt="m7k=$int"||hyt="$qus"
fom post "$hyt" "$ent"
echo Input reply:
ipt ry
fmj
}
$hc
}
hpd $1&&bkz="m7"||{
int="$(($int+1))"
wbn="`ls "$pcz"|pdg`"
[ -n "$wbn" ]&&{
qhn="${qus%=*}"
clj "${qhn%=*}=$int=0" "Next Post $wbn"
$hc
}
wjw "$pcz"
bkz="${qus%&m2kk=*}=$sel"
}
clj "$bkz" "Back"
}
cc(){
for lop in `ls "$wbb/opt/"`
do
clj "${qus%=0}&jg=$lop&tpa" "$lop.$1 (`cat "$wbb/opt/$lop"|wcl`)"
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
fne="User-$nr+User space"
if [ -e "$whk/$fne" ]
then
ls "$whk"|while read mr
do
eo=$(($eo+1))
[ "$mr" == "$fne" ]&&{
clj "m1g=$eo" "$nr"
}
done
hpd $1&&clj "cop" "Rewrite"
else
hpd $1&&clj "cop" "$na"||echo "$nr"
fi
glp||clj "ntf" "Notice"
$hc
}
wpxc(){
echo "$tb"
hpd "$2"&&echo "<td>Post${thq}Reply${thq}Sender${thq}Send Time</td>"
sel="${qus##*=}"
while read nr
do
cpo
ypd&&{
echo "<tr><td>"
hpd "$2"&&a="=0"
clj "$1=$co$a" "$co.$nr"
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
}
echo "</tr>"
}
done
echo "$tbo"
cpd&&clj "${qus%=*}=$(($sel-10))" "Next page"
$hc
}
echo "$tb<td>"
[ -e "$hos/" ]&&{
clj "main" "$wcm"
$hc
}||{
echo "Please run it on shell"
}
echo "$thc"
case $qus in
main)
echo "$wsn User:"
nr="$na"
usg 1
eco "Total entry:`ls "$whk"|wcl`"
[ -e "$hos/bul" ]&&eco "Bulletin:`cat "$hos/bul"`"
jld="`ls "$whk"|wcl`"
[ "$jld" == "0" ]||{
int=$((`date +%s`%$jld+1))
sjs="`ls "$whk"|pdg`"
}
fom post "m1j" "$ent"
echo "<input type=text name=kw value=${sjs%%+*}>"
fmj
echo "$tb"
echo "<td>$bsn$thq"
rxh 1
echo "${thc}Other$thq"
glp&&wblg||{
clj "m4" "1.Make a new entry"
$hc
wjw "$cfd"
clj "m5=$sel" "2.Diary"
$hc
clj "m6" "3.Reset your password"
$hc
clj "m7" "4.Chat Room"
$hc
wjw "$hos/up"
clj "m8=$sel" "5.File Explorer"
}
echo "</td>$tbo"
;;
m1j)
read b
read c
read kk
kw=${kk%?}
[ -n "$kw" ]&&{
pkc(){
[ -n "`echo "$mr"|grp "$kw"`" ]
}
echo "Result$thc$tb<td>Entry${thq}User${thq}Post${thq}File$thc"
ls "$whk"|while read mr
do
eo=$(($eo+1))
pkc&&{
clj "m1g=$eo" "${mr%%+*}"
$hc
}
done
echo "$thq"
ls "$hos/user"|grp "$kw"|while read nr
do
usg
done
echo "$thq"
co=0
ls "$hos/main"|while read nr
do
cpo
eo=0
ls "$hos/main/$nr"|while read mr
do
eo=$(($eo+1))
pkc&&{
clj "m2k=$co&m2kk=$eo=0" "$mr"
$hc
}
done
done
echo "$thq"
ls "$hos/up"|while read mr
do
eo=$(($eo+1))
pkc&&{
clj "m8d=$eo" "$mr"
$hc
}
done
echo "</td>$tbo" 
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
ind="${qus#m2k=*}"
ine="${ind%=*}"
int="${ine%&m2kk=*}"
inu="$int"
pac="`ls "$hos/main"|pdg`"
[ -n "$pac" ]&&{
sel="0"
pcz="$hos/main/$pac"
cze="${qus#*&m2kk=}"
cse=${cze%&tpa}
[ "$cse" == "$qus" ]&&{
eco "`gaen`   Part:$pac"
wjs=`ls "$pcz"|wcl`
co=0
ls "$pcz"|wpxc "m2k=$int&m2kk" "1"
clj "m2k=$int&m2kk=a=0" "Make a new post"
$hc
bk
}
cse=${cse%=0}
}
case $cse in
a)
glp&&wblg||{
fom post "m2k=$int&m2kk=as=0" "$ent"
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
pbz||plx
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
[ -e "$wbb/opt/$ry" ]&&chse "$ry"|hcs
}
}
}||{
int="$cse"
wbn="`ls "$pcz"|pdg`"
[ -n "$wbn" ]&&{
wbb="$pcz/$wbn"
[ -f "$wbb" ]&&zxth||{
cat "$wbb/main"|hcs
echo $thc
cc `cat "$wbb/data"`
echo $thc
[ -e "$wbb/talk" ]&&{
wbb="$wbb/talk"
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
fom post "m4ws" "$ent"
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
read mt
fgy
read tgs
fgy
read wd
mt="${mt%?}"
tgs="${tgs%?}"
mwt="$whk/$mt+$tgs"
[ -z "`ls "$whk"|grp "$mt"`" ]&&{ 
nwe
rmk="$mwt"
fid
}
}
;;
m5*)
glp&&wblg||{
mt="`date +%y.%m.%d`"
rmk="$cfd/$mt"
case $qus in
m5=*)
sel="0"
gaen
$hc
co=0
ls "$cfd"|wpxc "m5d"
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
fom post "m6e"
echo Input your new password:
$spa
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
co=0
cat "$cfd"|while read nr
do
cpo
clj "m7k=$co" "$co.${nr#*,}"
$hc
done
echo $thc
bk
}
;;
m7k=*)
cfd="$usv/chat"
int="${qus#*=}"
wwn="`cat "$cfd"|pdg`"
wbn="${wwn%%,*}"
[ -n "$wbn" ]&&{
wbb="$hos/room/$wbn"
zxth 1
}
;;
m8=*)
eco "File Explorer"
gaen
clj "m8v" "Photo Viewer"
$hc
co=0
ls "$hos/up"|wpxc "m8d"
eco "Upload File:"
fom post "m8u" "$ent" 
echo "<input type=file name=file>"
fmj
$hc
bk
;;
m8u)
read meta
read a
read b
fnm="${meta#*filename=}"
nu="${fnm#\"*}"
mu="${nu%\"*}"
st="$hos/up/$mu"
cat >$st
echo "$mu saved."
;;
m8v)
sel="0"
eco "Photo Viewer"
echo "$tb"
co=0
mo="0"
ls "$hos/up/"|while read nr
do
cpo
[ "${nr##*.}" == "jpg" ]&&{
echo "<td>"
clj "m8x=$co" "<img src=$j?m8d=$co width=80px height=60px />"
echo "</td>"
[ "$((${co}%3))" == "0" ]&&{
echo "</tr><tr>"
mo="0"
}
}
done
echo "$tbo"
clj "m8=0" "Back"
;;
m8x=*)
int="${qus#*=}" 
cfd="$hos/up"
eco "<img src=$j?m8d=$int />"
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
cop)
glp&&wblg||{
fom post "cows" "$ent"
echo Word:
ipt wd
fmj
}
;;
cows)
glp&&wblg||{
read b
read c
read wd
mt="User-$na"
tgs="User space"
mwt="$whk/$mt+$tgs"
nwe
rmk="$mwt"
fid
}
;;
ntf)
cat "$usv/noce"|hcs
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
chk="`ls "$hos/user"|grp "$nep"`"
rck||{
zcc
echo OK
}
}
;;
esac
$hc
[ -n "`cat "$hos/ip"|grp "$rip"`" ]||echo "$rip">>$hos/ip
eco "${thc}Counter:`cat "$hos/ip"|wcl`"
eco "You can use more thing on <a href=telnet://$HTTP_HOST>Telnet Version</a>"
echo "Copyright (C) `date +%Y` by Mayx</td>$tbo"
}|gzip -c
;;
esac
}