#!/system/bin/ash
hos="/sdcard/ba"
whk="$hos/wiki"
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
ls "$1"|while read nr
do
co=$(($co+1))
[ "$int" == "$co" ]&&echo "$nr"
done
}
chse(){
glp&&wblg||{
vck="`cat "$wbb/opt/$1"|grep "$na"`"
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
[ -z "$HTTP_HOST" ]&&{
inc="echo Input number or command:"
[ -e "$hos/" ]&&echo 'Welecome to use MaWiki&BBS'||{
echo Installing...
mkdir -p "$hos/main" "$hos/user" "$whk" "$hos/room"
echo Master name:SYSOP
echo New password:
read mnp
smk="$hos/user/SYSOP"
mkdir -p "$smk/diary" "$smk/mail" "$smk/chat"
echo "$mnp">>$smk/pwd
}
slp(){
[ "$na" == "SYSOP" ]
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
chk="`ls "$hos/user"|grep "$nep"`"
[ "$chk" == "$nep" -o "$nep" = "" ]||{
echo Please input verifcation code:
vv="`cat /proc/sys/kernel/random/uuid`"
vv="${vv%%-*}"
echo $vv
read vc
[ "$vc" == "$vv" ]&&{
usk="$hos/user/$nep"
mkdir -p "$usk/diary" "$usk/mail" "$usk/chat"
echo $npd>>$usk/pwd
na="$nep"
usv="$hos/user/$na"
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
echo Input e to insert a new paragraph
echo Input c to continue write
read pd
case $pd in
e)
clear
echo Input title:
read tt
echo Word:
read nwd
echo >>$rmk
echo $tt >>$rmk
echo -------- >>$rmk
echo $nwd >>$rmk
;;
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
[ "$1" == "1" ]&&echo "Input a to add friend:"
read ry
case $ry in
e)
break 1
;;
a)
[ "$1" == "1" ]&&{
clear
echo Input friend name:
read fnm
[ -n "$fnm" -a -e "$hos/user/$fnm" ]&&touch "$hos/user/$fnm/chat/${wbb##*/}"
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
[ "$sel" -le "$co" -a "$(($sel+10))" -ge "$co" ]&&echo $co.$nr
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
while true
do
clear
echo MaWiki  User:$na
echo Total entry:`ls "$whk"|wcl`
echo $fgx
echo 1.Search
echo 2.Exit
echo 3.Go to MaBBS
echo 4.Random
glp&&echo 5.Login||{
echo 5.Make a new entry
echo 6.Diary 
echo 7.Reset your password
echo 8.Chat Room
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
ls "$whk"|grep "$kw"|while read jg
do
echo ${jg%%+*}
done
echo User
echo -------
ls "$hos/user"|grep "$kw"
echo Post
echo -------
ls "$hos/main"|while read nr
do
ls "$hos/main/$nr"|grep "$kw"
done
echo Which one:
read mtt
[ -n "$mtt" ]&&{
tkw=`ls "$whk"|grep "$mtt"`
[ -n "$tkw" ]&&{
rmk="$whk/$tkw"
fid
}
}
}
;;
2)
echo Bye
break
;;
3)
while true
do
clear
echo Welecome,$na
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
echo c.Delete a part
echo d.Release bulletin
}
$inc
read pac
[ -n "$pac" ]||pac="#"
case $pac in
a)
break
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
echo Which part to delete:
read dpw
rm -rf "$hos/main/$dpw"
}
;;
d)
slp&&{
clear
echo Input bulletin:
read bul
echo "$bul" > $hos/bul
}
;;
*)
int="$pac"
pac="`pdg "$hos/main"`"
[ -n "$pac" ]&&{
sel="0"
while true
do
pcz="$hos/main/$pac"
clear
echo Welecome,$na   Part:$pac
echo $fgx
co="0"
ls "$pcz"|pxcx
echo $fgx
echo a.Make a new post
echo b.Back
fyx "$pcz"
slp&&echo d.Delete a post
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
[ -n "`ls "$pcz"|grep "$tit"`" ]||{
echo Word:
read wod
plx
}
;;
2)
clear
echo Input the title:
read tit
[ -n "`ls "$pcz"|grep "$tit"`" ]||{
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
touch "$tsm/opt/$sle"
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
slp&&{
echo Which post delete:
read tdw
rm -rf "$pcz/$tdw"
}
;;
*)
wbn="`pdg "$pcz"`"
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
glp&&wblg||{
clear
echo Input Main title:
read mt
[ -z "`ls "$whk"|grep "$mt"`" ]&&{
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
rmk="$whk/`pdg "$whk"`"
fid
}
;;
6)
glp&&wblg||{
cfd="$usv/diary"
sel="0"
while true
do
clear
echo Welecome,$na
echo $fgx
co="0"
ls "$cfd"|pxcx
echo $fgx
echo a.Write diary
echo b.Back
fyx "$cfd"
$inc
read int
case $int in
a)
clear
mt="`date +%y.%m.%d`"
[ -n "`ls "$cfd"|grep "$mt"`" ]||{
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
wbn="`pdg "$cfd"`"
[ -n "$wbn" ]&&{
rmk="$cfd/$wbn"
fid
}
;;
esac
done
}
;;
7)
glp&&wblg||{
clear
echo Input your new password:
read nrd
[ -n "$nrd" ]&&echo $nrd>$usv/pwd
}
;;
8)
glp&&wblg||{
cfd="$usv/chat"
sel="0"
while true
do
clear
echo Chat Room
echo Welecome,$na
echo $fgx
co="0"
ls "$cfd"|pxcx
echo $fgx
echo a.Make chat room
echo b.Back
fyx "$cfd"
$inc
read int
case $int in
a)
clear
chz="$((`ls "$hos/room"|wcl`+1))"
wbb="$hos/room/$chz"
echo "Chat Room #$chz">$wbb
echo "$fgx">>$wbb
touch "$cfd/$chz"
zxth "1"
;;
b)
break 1
;;
c)
fy "$cfd"
;;
*)
wbn="`pdg "$cfd"`"
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
echo "Content-type:text/html;charset=utf-8"
read tl
[ "${tl%%=*}" == "lon" ]&&echo "Set-Cookie:$tl;PATH=/"
echo ""
echo '<title>Mabbs&Wiki</title>'
hc='echo <br>'
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
eco(){
echo "$1<br>"
}
fmj(){
echo "<input type=submit value=Submit>"
echo "</form>"
}
wblg(){
echo "<form method=post action=$0>"
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
clj(){
echo "<a href=$0?$1>$2</a>"
}
fid(){
cat "$rmk"|hcs
clj "main" "Press there to back"
}
zxth(){
cat "$rmk"|hcs
glp&&eco "<a href=$0?m4>Login</a>"||{
[ "${QUERY_STRING##*&}" == "hfz" ]||zhy="&hfz"
echo "<form method=post action=$0?$QUERY_STRING$zhy $ent>"
echo Input reply:
echo "<input type=text name=ry><br>"
fmj
$hc
}
clj "${QUERY_STRING%&m2kk=*}" "Press there to back" 
}
cc(){
for lop in `ls "$rmk/opt/"`
do
clj "$QUERY_STRING&jg=$lop&tpa" "$lop.$1 (`cat "$rmk/opt/$lop"|wcl`)"
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
while read nr
do
co=$(($co+1))
clj "$1=$co" "$co.$nr"
$hc
done
eco "$fgx"
}
[ -e "$hos/" ]&&{
clj "main" "Welecome to use Mabbs&Wiki"
$hc
}||{
echo "Please run it on shell"
}
case $QUERY_STRING in
main)
eco "MaWiki  User:$na"
eco "Total entry:`ls "$whk"|wcl`"
[ -e "$hos/bul" ]&&eco "Bulletin:`cat "$hos/bul"`"
jld="`ls "$whk"|wcl`"
[ "$jld" == "0" ]||{
int=$((`date +%s`%$jld+1))
sjs="`pdg "$whk"`"
} 
echo "<form method=post action=$0?m1j $ent>"
echo "<input type=text name=kw value=${sjs%%+*}>"
fmj
echo "<table border=1><tr>"
echo "<td>MaBBS</td><td>"
co=0
ls "$hos/main"|while read bm
do
co=$(($co+1))
clj "m2k=$co" "$co.$bm (`ls "$hos/main/$bm/"|wcl`)"
$hc
done
echo "</td></tr><tr>"
echo "<td>Other</td><td>"
glp&&wblg||{
clj "m4" "1.Make a new entry"
$hc
clj "m5" "2.Diary"
$hc
clj "m6" "3.Reset your password"
$hc
clj "m7" "4.Chat Room"
}
echo "</td></tr></table>"
;;
m1j)
read b
read c
read kk
kw=${kk%?}
[ -n "$kw" ]&&{
eco "Result"
eco "$fgx"
eco "Entry"
eco "-------"
ls "$whk"|grep "$kw"|while read jg
do
clj "m1g=${jg%%+*}" "${jg%%+*}"
$hc
done
eco User
eco -------
ls "$hos/user"|grep "$kw"|hcs
eco Post
eco -------
co=0
ls "$hos/main"|while read nr
do
co=$(($co+1))
eo=0
ls "$hos/main/$nr"|while read mr
do
eo=$(($eo+1))
[ -n "`echo "$mr"|grep "$kw"`" ]&&{
clj "m2k=$co&m2kk=$eo" "$mr"
$hc
}
done
done
}
;;
m1g=*)
mtt="${QUERY_STRING#*=}"
[ -n "$mtt" ]&&{
tkw="`ls "$whk"|grep "$mtt"`"
[ -n "$tkw" ]&&{
rmk="$whk/$tkw"
fid
}
}
;;
m2k=*)
ind="${QUERY_STRING#*=}"
int="${ind%&m2kk=*}"
pac="`pdg "$hos/main"`"
[ -n "$pac" ]&&{
sel="0"
pcz="$hos/main/$pac"
cze="${QUERY_STRING#*&m2kk=}"
cse=${cze%&hfz}
cse=${cse%&tpa}
[ "$cse" == "$QUERY_STRING" ]&&{
eco "Welecome,$na   Part:$pac"
eco "$fgx"
co="0"
ls "$pcz"|wpxc "$QUERY_STRING&m2kk"
clj "$QUERY_STRING&m2kk=a" "Make a new post"
$hc
clj "m2" "Back"
}
}
case $cse in
a)
glp&&wblg||{
echo "<form method=post action=$0?m2k=$int&m2kk=as $ent>"
echo Input the title:
echo "<input type=text name=tit><br>"
echo Word:
echo "<input type=text name=wd><br>"
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
[ -n "`ls "$pcz"|grep "$tit"`" ]||{
plx
echo "OK!"
}
}
;;
*)
[ "${QUERY_STRING##*&}" == "tpa" ]&&{
glp&&wblg||{
int="${cse%&jg=*}"
wbn="`pdg "$pcz"`"
ry="${cse#*=}"
[ -n "$wbn" ]&&{
wbb="$pcz/$wbn"
[ -e "$wbb/opt/$ry" ]&&chse $ry
}
}
}||{
int="$cse"
wbn="`pdg "$pcz"`"
[ -n "$wbn" ]&&{
rmk="$pcz/$wbn"
[ "${QUERY_STRING##*&}" == "hfz" ]&&{
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
echo "<form method=post action=$0?m4f $ent>"
echo Input Main title:
echo "<input type=text name=tit><br>"
echo Tags:
echo "<input type=text name=tag><br>"
echo Word:
echo "<input type=text name=wd><br>"
fmj
}
;;
m4f)
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
[ -z "`ls "$whk"|grep "$tit"`" ]&&{
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
m5)
cfd="$usv/diary"
sel="0"
eco "Welecome,$na"
eco "$fgx"
co="0"
ls "$cfd"|wpxc "m5d"
clj "m5w" "Write diary"
$hc
clj "main" "Back"
$hc
;;
m5w)
cfd="$usv/diary"
mt="`date +%y.%m.%d`"
rmk="$cfd/$mt"
[ -n "`ls "$cfd"|grep "$mt"`" ]&&fid||{
echo "<form method=post action=$0?m5ws $ent>"
echo "Word:"
echo "<input type=text name=wd><br>"
fmj
}
;;
m5ws)
read b
read c
read wd
mt="`date +%y.%m.%d`"
cfd="$usv/diary"
mwt="$cfd/$mt"
echo Diary:$mt>>$mwt
echo $wd >>$mwt
rmk="$cfd/$mt"
fid
;;
m5d=*)
int="${QUERY_STRING#*=}" 
cfd="$usv/diary"
wbn="`pdg "$cfd"`"
[ -n "$wbn" ]&&{
rmk="$cfd/$wbn"
fid
}
;;
m6)
glp&&wblg||{
echo "<form method=post action=$0?m6e>"
echo Input your new password:
echo "<input type=text name=pw><br>"
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
eco Chat Room
eco Welecome,$na
eco $fgx
co="0"
ls "$cfd"|wpxc "m7k"
clj "m7a" "a.Make chat room"
$hc
clj "main" "b.back"
}
;;
m7a)
glp&&wblg||{
chz="$((`ls "$hos/room"|wcl`+1))"
wbb="$hos/room/$chz"
echo "Chat Room #$chz">$wbb
echo "$fgx">>$wbb
touch "$usv/chat/$chz"
echo OK,Chat Room ID:$chz
clj "m7" "Back"
}
;;
m7k=*)
cfd="$usv/chat"
ind="${QUERY_STRING#*=}"
int="${ind%&hfz}"
wbn="`pdg "$cfd"`"
[ -n "$wbn" ]&&{
wbb="$hos/room/$wbn"
[ "${QUERY_STRING##*&}" == "hfz" ]&&{
read b
read c
read ry
echo $na  `date` >>$wbb
echo "$ry" >>$wbb
echo >>$wbb
}
cat "$wbb"|hcs
echo "<form method=post action=$0?m7k=$int&hfz $ent>"
echo Input reply:
echo "<input type=text name=ry><br>"
fmj
$hc
clj "m7" "Press there to back"
}
;;
zc)
vv="`cat /proc/sys/kernel/random/uuid`"
vv="${vv%%-*}"
echo "<form method=post action=$0?zct&vv=$vv>"
echo Please input your name:
echo "<input type=text name=name><br>"
echo Please input new password:
echo "<input type=password name=pw><br>"
eco "Please input verifcation code:"
eco $vv
echo "<input type=text name=vv><br>"
fmj
;;
zct*)
vs="${QUERY_STRING#*=}"
tid="${tl%&pw*}"
npe="${tl#*pw=}"
npd="${npe%&vv*}"
nep="${tid#*=}"
vv="${tl##*=}"
[ "$vv" == "$vs" ]&&{
chk="`ls "$hos/user"|grep "$nep"`"
[ "$chk" == "$nep" -o "$nep" = "" ]||{
usk="$hos/user/$nep"
mkdir -p "$usk/diary" "$usk/mail" "$usk/chat"
echo $npd>>$usk/pwd
echo OK
}
}
;;
esac
$hc
eco "$fgx"
eco "You can use more thing on Telnet Version"
echo "Copyright (C) 2016 by Mayx"
}
