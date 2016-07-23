#!/system/bin/ash
hos="/sdcard/ba"
whk="$hos/wiki"
err="echo Error!"
fgx="============"
glp(){
[ "$na" == "guest" ]
}
[ -z "$HTTP_HOST" ]&&{
inc="echo Input number or command:"
[ -e "$hos/" ]&&echo 'Welecome to use MaWiki&BBS'||{
echo Installing...
mkdir -p "$hos/main" "$hos/user" "$whk"
touch "$hos/ai"
echo Master name:SYSOP
echo New password:
read mnp
smk="$hos/user/SYSOP"
mkdir -p "$smk/diary" "$smk/mail" "$smk/friend"
touch "$smk/blog"
echo "$mnp">>$smk/pwd
}
slp(){
[ "$na" == "SYSOP" ]
}
fy(){
[ `ls "$1" | wc -l` -ge 10 ]&&sel="$(($sel+10))" 
}
fyx(){
[ `ls "$1" | wc -l` -ge 10 ]&&echo c.Next page
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
chk="`ls "$hos/user" | grep "$nep"`"
[ "$chk" == "$nep" -o "$nep" = "" ]||{
echo Please input verifcation code:
vv="`cat /proc/sys/kernel/random/uuid`"
vv="${vv%%-*}"
echo $vv
read vc
[ "$vc" == "$vv" ]&&{
usk="$hos/user/$nep"
mkdir -p "$usk/diary" "$usk/mail" "$usk/friend"
touch "$usk/blog"
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
read ry
[ "$ry" == "e" ]&&break 1||{
[ -n "$ry" ]&&{
glp&&wblg||{
echo $na  `date` >>$wbb
echo $ry >>$wbb
echo >>$wbb
}
}
}
done
}
pxcx(){
while read nr
do
co=$(($co+1))
[ "$sel" -le "$co" -a "$(($sel+10))" -ge "$co" ]&&echo $co.$nr
done
}
chse(){
glp&&wblg||{
vck="`cat "$wbb/opt/$1" | grep "$na"`"
[ "$na" == "$vck" ]||{
echo $na >> "$wbb/opt/$1"
clear
cat "$wbb/opt/$1"
echo selected it.
sleep 3
}
}
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
cc(){
for lop in `ls "$wbb/opt/"`
do
echo $lop.$1 \(`cat "$wbb/opt/$lop" | wc -l`\)
shift
done
}
na="guest"
sleep 1
while true
do
clear
echo MaWiki  User:$na
echo Total entry:`ls "$whk" | wc -l`
echo $fgx
echo 1.Search
echo 2.Exit
echo 3.Go to MaBBS
echo 4.Random
glp&&echo 5.Login||{
echo 5.Make a new entry
echo 6.Diary 
echo 7.Reset your password
echo 8.Microblog
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
ls "$whk" | grep "$kw" | while read jg
do
echo ${jg%%+*}
done
echo Which one:
read mtt
[ -n "$mtt" ]&&{
tkw=`ls "$whk" | grep "$mtt"`
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
ls "$hos/main" | while read bm
do
co=$(($co+1))
echo $co.$bm \(`ls "$hos/main/$bm/" | wc -l `\)
done
echo $fgx
echo a.Mail box
echo b.Back to MaWiki
slp&&{
echo c.Make a part
echo d.Delete a part
echo e.Release bulletin
}
$inc
read pac
[ -n "$pac" ]||pac="#"
case $pac in
a)
glp&&wblg||{
sel=0
while true
do
clear
echo Mail box
echo $fgx
co="0"
ls "$usv/mail" | pxcx
echo $fgx
echo a.Send mail
echo b.Back
fyx "$usv/mail"
$inc
read int
case $int in
a)
clear
echo From:$na
echo To:
read st
[ -n "$st" -a "$st" == "AI" ]&&{
echo Word:
read swd
[ "$swd" == "study" ]&&{
echo You say:
read ys
echo AI say:
read as
echo $ys-$as >>${hos}/ai
}
ais="`grep "$swd" "$hos/ai"`"
ais=${ais#*-}
[ -z "$swd" -o -z "$ais" ]&&ais="Sorry,I dont know what do you say"
echo Talk AI >>$usv/mail/Talk_AI
date >>$usv/mail/Talk_AI
echo $ais >>$usv/mail/Talk_AI
echo >>$usv/mail/Talk_AI
}
[ -n "$st" -a -e "$hos/user/$st" ]&&{
echo $fgx
echo Title:
read swd
isw="$hos/user/$st/mail/$swd"
[ -z "$swd" -o -e "$isw" ]||{
echo Word:
read iwd
echo From:$na>>$isw
echo To:$st>>$isw
date>>$isw
echo $fgx>>$isw
echo $iwd >>$isw
echo OK!
}
}
sleep 1
;;
b)
break 1
;;
c)
fy "$usv/mail"
;;
*)
clear
wbn="`pdg "$usv/mail"`"
[ -n "$wbn" ]&&{
cat "$usv/mail/$wbn"
echo Press enter to back
echo Input d to delete
read nul
[ "$nul" == "d" ]&&rm -rf "$usv/mail/$wbn"
}
;;
esac
done
}
;;
b)
break
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
echo Which part to delete:
read dpw
rm -rf "$hos/main/$dpw"
}
;;
e)
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
ls "$pcz" | pxcx
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
[ -n "`ls "$pcz" | grep "$tit"`" ]||{
echo Word:
read wod
stt="$pcz/$tit"
echo $tit >>$stt
echo $fgx >>$stt
echo Post master:$na  `date` >>$stt
echo $wod >>$stt
echo >>$stt
}
;;
2)
clear
echo Input the title:
read tit
[ -n "`ls "$pcz" | grep "$tit"`" ]||{
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
[ -e "$wbb/opt/$ry" ]&&chse $ry
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
[ -z "`ls "$whk" | grep "$mt"`" ]&&{
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
jld="`ls "$whk" | wc -l`"
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
ls "$cfd" | pxcx
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
[ -n "`ls "$cfd" | grep "$mt"`" ]||{
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
clear
glp&&wblg||{ 
while true
do
clear
echo Microblog
cat "$usv/blog"
ls "$usv/friend"|while read bl
do
cat "$hos/user/$bl/blog"
done
echo $fgx
echo a.Send Microblog
echo b.Back
echo c.Add friend
echo Input command:
read int
case $int in
a)
clear
echo Word:
read bwd
echo $fgx >>"$usv/blog"
echo $na  `date` >>"$usv/blog" 
echo $bwd >>"$usv/blog"
echo Notify who:
read bwo
[ -n "$bwo" -a -e "$hos/user/$bwo" ]&&{
isw="$hos/user/$bwo/mail/Blog_Notify"
echo From:System>>$isw
echo To:$bwo>>$isw
date>>$isw
echo $fgx>>$isw
echo $na notify you>>$isw
}
;;
b)
break 1
;;
c)
clear
echo Input friend name:
read fnm
[ -n "$fnm" -a -e "$hos/user/$fnm" ]&&touch "$usv/friend/$fnm"
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
echo "<form method=post action=wiki.cgi>"
echo Login:
eco "<input type=text name=lon>"
echo Password:
eco "<input type=password name=pw>"
fmj
$hc
$hc
echo "Dont have?<a href=wiki.cgi?zc>Join us</a>"
}
hcs(){
while read pd
do
eco "$pd"
done
}
fid(){
cat "$rmk"|hcs
echo "<a href=wiki.cgi?main>Press there to back</a>"
}
zxth(){
cat "$rmk"|hcs
glp&&eco "<a href=wiki.cgi?m4>Login</a>"||{
echo "<form method=post action=wiki.cgi?$QUERY_STRING&hfz $ent>"
echo Input reply:
echo "<input type=text name=ry><br>"
fmj
$hc
}
echo "<a href=wiki.cgi?${QUERY_STRING%&m2kk=*}>Press there to back</a>" 
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
cc(){
for lop in `ls "$rmk/opt/"`
do
eco "<a href=wiki.cgi?$QUERY_STRING&jg=$lop&tpa>$lop.$1 (`cat "$rmk/opt/$lop" | wc -l`)</a>"
shift
done
}
fgy(){
read a
read b
read c
}
chse(){
glp&&wblg||{
vck="`cat "$rmk/opt/$1" | grep "$na"`"
[ "$na" == "$vck" ]||{
echo $na >> "$rmk/opt/$1"
cat "$rmk/opt/$1"|hcs
eco selected it.
}
}
}
[ -e "$hos/" ]&&{
eco "<a href=wiki.cgi?main>Welecome to use Mabbs&Wiki</a>"
}||{
echo Installing...
mkdir -p "$hos/main" "$hos/user" "$whk"
touch "$hos/ai"
}
case $QUERY_STRING in
main)
eco "MaWiki  User:$na"
eco "Total entry:`ls "$whk" | wc -l`"
eco "$fgx"
eco "<a href=wiki.cgi?m1>1.Search</a>"
eco "<a href=wiki.cgi?m2>2.Go to MaBBS</a>"
eco "<a href=wiki.cgi?m3>3.Random</a>"
glp&&echo "<a href=wiki.cgi?m4>4.Login</a>"||{
eco "<a href=wiki.cgi?m4>4.Make a new entry</a>"
eco "<a href=wiki.cgi?m5>5.Diary</a>"
eco "<a href=wiki.cgi?m6>6.Reset your password</a>"
echo "<a href=wiki.cgi?m7>7.Microblog</a>"
}
;;
m1)
eco "Input Keyword or tags:"
echo "<form method=post action=wiki.cgi?m1j $ent>"
echo "<input type=text name=kw><br>"
fmj
;;
m1j)
read b
read c
read kk
kw=${kk%?}
[ -n "$kw" ]&&{
eco "Result"
eco "$fgx"
ls "$whk" | grep "$kw" | while read jg
do
eco "<a href=wiki.cgi?m1g=${jg%%+*}>${jg%%+*}</a>"
done
}
;;
m1g=*)
mtt="${QUERY_STRING#*=}"
[ -n "$mtt" ]&&{
tkw="`ls "$whk" | grep "$mtt"`"
[ -n "$tkw" ]&&{
rmk="$whk/$tkw"
fid
}
}
;;
m2)
eco "Welecome,$na"
date
$hc
[ -e "$hos/bul" ]&&eco "Bulletin:`cat "$hos/bul"`"
eco "$fgx"
co=0
ls "$hos/main" | while read bm
do
co=$(($co+1))
eco "<a href=wiki.cgi?m2k=$co>$co.$bm (`ls "$hos/main/$bm/" | wc -l `)</a>"
done
eco "$fgx"
eco "<a href=wiki.cgi?m2a>a.Mail box</a>"
echo "<a href=wiki.cgi?main>b.Back to MaWiki</a>"
;;
m2a)
glp&&wblg||{
sel=0
eco "Mail box"
eco "$fgx"
co="0"
ls "$usv/mail"|while read nr
do
co=$(($co+1))
eco "<a href=wiki.cgi?m2ak=$co>$co.$nr</a>"
done
eco "$fgx"
eco "<a href=wiki.cgi?m2aa>a.Send mail</a>"
echo "<a href=wiki.cgi?m2>b.Back</a>"
}
;;
m2aa)
glp&&wblg||{
echo "<form method=post action=wiki.cgi?m2aas $ent>"
eco "From:$na"
echo To:
echo "<input type=text name=to><br>"
echo Title:
echo "<input type=text name=tit><br>"
echo Word:
echo "<input type=text name=fsw><br>"
fmj
}
;;
m2aas)
glp&&wblg||{
read b
read c
read to
fgy
read tit
fgy
read fsw
to="${to%?}"
tit="${tit%?}"
isw="$hos/user/$to/mail/$tit"
echo From:$na>>$isw
echo To:$to>>$isw
date>>$isw
echo $fgx>>$isw
echo $fsw >>$isw
echo OK!
}
;;
m2ak=*)
glp&&wblg||{
int="${QUERY_STRING#*=}"
wbn="`pdg "$usv/mail"`"
[ -n "$wbn" ]&&{
cat "$usv/mail/$wbn"|hcs
echo "<a href=wiki.cgi?m2a>Back</a>"
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
ls "$pcz" | while read nr
do
co=$(($co+1))
eco "<a href=wiki.cgi?$QUERY_STRING&m2kk=$co>$co.$nr</a>"
done
eco "$fgx"
eco "<a href=wiki.cgi?$QUERY_STRING&m2kk=a>Make a new post</a>"
echo "<a href=wiki.cgi?m2>Back</a>"
}
}
case $cse in
a)
glp&&wblg||{
echo "<form method=post action=wiki.cgi?m2k=$int&m2kk=as $ent>"
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
read wd
tit="${tit%?}"
[ -n "`ls "$pcz" | grep "$tit"`" ]||{
stt="$pcz/$tit"
echo $tit >>$stt
echo $fgx >>$stt
echo Post master:$na  `date` >>$stt
echo $wd >>$stt
echo >>$stt
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
rmk="$pcz/$wbn"
[ -e "$rmk/opt/$ry" ]&&chse $ry
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
echo "<form method=post action=wiki.cgi?m4f $ent>"
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
[ -z "`ls "$whk" | grep "$tit"`" ]&&{
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
m3)
jld="`ls "$whk" | wc -l`"
[ "$jld" == "0" ]&&{
echo Not found...
}||{
int=$((`date +%s`%$jld+1))
rmk="$whk/`pdg "$whk"`"
fid
}
;;
m5)
cfd="$usv/diary"
sel="0"
eco "Welecome,$na"
eco "$fgx"
co="0"
ls "$cfd"|while read nr
do
co=$(($co+1))
eco "<a href=wiki.cgi?m5d=$co>$co.$nr</a>"
done
eco "$fgx"
eco "<a href=wiki.cgi?m5w>Write diary</a>"
eco "<a href=wiki.cgi?main>Back</a>"
;;
m5w)
cfd="$usv/diary"
mt="`date +%y.%m.%d`"
rmk="$cfd/$mt"
[ -n "`ls "$cfd" | grep "$mt"`" ]&&fid||{
echo "<form method=post action=wiki.cgi?m5ws $ent>"
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
echo "<form method=post action=wiki.cgi?m6e>"
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
eco "Microblog"
cat "$usv/blog"|hcs
ls "$usv/friend"|while read bl
do
cat "$hos/user/$bl/blog"|hcs
done
eco "$fgx"
echo "<form method=post action=wiki.cgi?m7e $ent>"
echo Word:
echo "<input type=text name=pw><br>"
fmj
echo "<a href=wiki.cgi?main>Back</a>"
}
;;
m7e)
read b
read c
read bwd
echo $fgx >>"$usv/blog"
echo $na  `date` >>"$usv/blog"
echo $bwd >>"$usv/blog"
;;
zc)
vv="`cat /proc/sys/kernel/random/uuid`"
vv="${vv%%-*}"
echo "<form method=post action=wiki.cgi?zct&vv=$vv>"
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
chk="`ls "$hos/user" | grep "$nep"`"
[ "$chk" == "$nep" -o "$nep" = "" ]||{
usk="$hos/user/$nep"
mkdir -p "$usk/diary" "$usk/mail" "$usk/friend"
touch "$usk/blog"
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
