#!/system/bin/ash
echo "Content-type:text/html;charset=utf-8"
read tl
[ "${tl%%=*}" == "lon" ]&&echo "Set-Cookie:$tl;PATH=/"
echo ""
echo '<title>Mabbs&Wiki</title>'
hos="/sdcard/ba"
whk="$hos/wiki"
err="echo Error!"
hc='echo <br>'
fgx="============"
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
glp(){
[ "$na" == "guest" ]
}
wblg(){
echo "<form method="post" action="wiki.cgi">"
echo Login:
eco "<input type="text" name="lon">"
echo Password:
eco "<input type="password" name="pw">"
echo "<input type="submit" value="Submit">"
eco "</form>"
$hc
echo "Dont have?<a href="wiki.cgi?zc">Join us</a>"
}
hcs(){
while read pd
do
eco "$pd"
done
}
fid(){
cat "$rmk"|hcs
echo "<a href="wiki.cgi?main">Press there to back</a>"
}
zxth(){
cat "$rmk"|hcs
echo "<form method="post" action="wiki.cgi?$QUERY_STRING\&hfz">"
echo Input reply:
echo "<input type="text" name="ry"><br>"
echo "<input type="submit" value="Submit">"
eco "</form>"
echo "<a href="wiki.cgi?main">Press there to back</a>"
}
chse(){
glp&&wblg||{
vck="`cat "$wbb/opt/$1" | grep "$na"`"
[ "$na" == "$vck" ]||{
echo $na >> "$wbb/opt/$1"
cat "$wbb/opt/$1"
echo selected it.
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
eco "<a href="wiki.cgi?chse&${QUERY_STRING#tk&}">$lop.$1 \(`cat "$wbb/opt/$lop" | wc -l`\)</a>"
shift
done
}
[ -e "$hos/" ]&&{
eco "<a href="wiki.cgi?main">Welecome to use Mabbs&Wiki</a>"
}||{
echo Installing...
mkdir -p "$hos/main" "$hos/user" "$whk"
touch "$hos/ai"
echo
}
case $QUERY_STRING in
main)
eco "MaWiki  User:$na"
eco "Total entry:`ls "$whk" | wc -l`"
eco "$fgx"
eco "<a href="wiki.cgi?m1">1.Search</a>"
eco "<a href="wiki.cgi?m2">2.Go to MaBBS</a>"
eco "<a href="wiki.cgi?m3">3.Random</a>"
glp&&eco "<a href="wiki.cgi?m4">4.Login</a>"||{
eco "<a href="wiki.cgi?m4">4.Make a new entry</a>"
eco "<a href="wiki.cgi?m5">5.Diary</a>"
eco "<a href="wiki.cgi?m6">6.Reset your password</a>"
eco "<a href="wiki.cgi?m7">7.Microblog</a>"
}
;;
m1)
eco "Input Keyword or tags:"
echo "<form method="post" action="wiki.cgi?m1j">"
echo "<input type="text" name="kw"><br>"
echo "<input type="submit" value="Submit">"
echo "</form>"
;;
m1j)
kw="${tl#*=}"
[ -n "$kw" ]&&{
eco "Result"
eco "$fgx"
ls "$whk" | grep "$kw" | while read jg
do
eco "<a href="wiki.cgi?m1g=${jg%%+*}">${jg%%+*}</a>"
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
eco "<a href="wiki.cgi?m2k=$co">$co.$bm (`ls "$hos/main/$bm/" | wc -l `)</a>"
done
eco "$fgx"
eco "<a href="wiki.cgi?m2a">a.Mail box</a>"
eco "<a href="wiki.cgi?main">b.Back to MaWiki</a>"
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
eco "<a href="wiki.cgi?m2ak=$co">$co.$nr</a>"
done
eco "$fgx"
eco "<a href="wiki.cgi?m2aa">a.Send mail</a>"
eco "<a href="wiki.cgi?m2">b.Back</a>"
}
;;
m2aa)
glp&&wblg||{
echo "<form method="post" action="wiki.cgi?m2aas">"
eco "From:$na"
echo To:
echo "<input type="text" name="to"><br>"
echo Title:
echo "<input type="text" name="tit"><br>"
echo Word:
echo "<input type="text" name="fsw"><br>"
echo "<input type="submit" value="Submit">"
echo "</form>"
}
;;
m2aas)
glp&&wblg||{
to="${tl%&tit*}"
tit="${tl%&fsw*}"
fsw="${tl#*&fsw=}"
isw="$hos/user/${to#*=}/mail/${tit##*=}"
echo From:$na>>$isw
echo To:${to#*=}>>$isw
date>>$isw
echo $fgx>>$isw
echo "$fsw" >>$isw
echo OK!
}
;;
m2ak=*)
glp&&wblg||{
int="${QUERY_STRING#*=}"
wbn="`pdg "$usv/mail"`"
[ -n "$wbn" ]&&{
cat "$usv/mail/$wbn"|hcs
echo "<a href="wiki.cgi?m2a">Back</a>"
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
[ "$cse" == "$QUERY_STRING" ]&&{
eco "Welecome,$na   Part:$pac"
eco "$fgx"
co="0"
ls "$pcz" | while read nr
do
co=$(($co+1))
eco "<a href="wiki.cgi?$QUERY_STRING\&m2kk=$co">$co.$nr</a>"
done
eco "$fgx"
eco "<a href="wiki.cgi?$QUERY_STRING\&m2kk=a">Make a new post</a>"
eco "<a href="wiki.cgi?m2">Back</a>"
}
}
case $cse in
a)
glp&&wblg||{
echo "<form method="post" action="wiki.cgi?m2k=$int\&m2kk=as">"
echo Input the title:
echo "<input type="text" name="tit"><br>"
echo Word:
echo "<input type="text" name="wd"><br>"
echo "<input type="submit" value="Submit">"
echo "</form>"
}
;;
as)
glp&&wblg||{
tid="${tl%&wd*}"
tit="${tid#*=}"
wd="${tl#*wd=}"
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
int="$cse"
wbn="`pdg "$pcz"`"
[ -n "$wbn" ]&&{
rmk="$pcz/$wbn"
[ "${QUERY_STRING##*&}" == "hfz" ]&&{
glp&&wblg||{
echo $na  `date` >>$rmk
echo "${tl#*=}" >>$rmk
echo >>$rmk
echo OK
}
}||{
[ -f "$rmk" ]&&zxth||{
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
echo "<form method="post" action="wiki.cgi?m4f">"
echo Input Main title:
echo "<input type="text" name="tit"><br>"
echo Word:
echo "<input type="text" name="wd"><br>"
echo "<input type="submit" value="Submit">"
echo "</form>"
}
;;
m4f)
glp&&wblg||{
tid="${tl%&wd*}"
wd="${tl#*wd=}"
tit="${tid#*=}"
mwt="$whk/$tit"
[ -z "`ls "$whk" | grep "$tit"`" ]&&{
echo $tit>>$mwt
echo Made by:$na `date`>>$mwt
echo Tags:From Web>>$mwt
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
eco "<a href="wiki.cgi?m5d=$co">$co.$nr</a>"
done
eco "$fgx"
eco "<a href="wiki.cgi?m5w">Write diary</a>"
eco "<a href="wiki.cgi?main">Back</a>"
;;
m5w)
cfd="$usv/diary"
mt="`date +%y.%m.%d`"
[ -n "`ls "$cfd" | grep "$mt"`" ]&&fid||{
echo "<form method="post" action="wiki.cgi?m5ws">"
echo "Word:"
echo "<input type="text" name="wd"><br>"
echo "<input type="submit" value="Submit">"
echo "</form>"
}
;;
m5ws)
wd="${tl#*=}"
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
echo "<form method="post" action="wiki.cgi?m6e">"
echo Input your new password:
echo "<input type="text" name="pw"><br>"
echo "<input type="submit" value="Submit">"
echo "</form>"
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
eco "<a href="wiki.cgi?m7w">Send Microblog</a>"
eco "<a href="wiki.cgi?main">Back</a>"
}
;;
m7w)
echo "<form method="post" action="wiki.cgi?m7e">"
echo Word:
echo "<input type="text" name="pw"><br>"
echo "<input type="submit" value="Submit">"
echo "</form>"
;;
m7e)
bwd="${tl#*=}"
echo $fgx >>"$usv/blog"
echo $na  `date` >>"$usv/blog" 
echo $bwd >>"$usv/blog"
;;
zc)
echo "<form method="post" action="wiki.cgi?zct">"
echo Please input your name:
echo "<input type="text" name="name"><br>"
echo Please input new password:
echo "<input type="password" name="pw"><br>"
echo "<input type="submit" value="Submit">"
echo "</form>"
;;
zct)
tid="${tl%&pw*}"
npd="${tl#*pw=}"
nep="${tid#*=}"
chk="`ls "$hos/user" | grep "$nep"`"
[ "$chk" == "$nep" -o "$nep" = "" ]||{
usk="$hos/user/$nep"
mkdir -p "$usk/diary" "$usk/mail" "$usk/friend"
touch "$usk/blog"
echo $npd>>$usk/pwd
echo OK
}
;;
esac
$hc
eco "$fgx"
eco "You can use more thing on Telnet Version"
echo "Copyright (C) 2016 by Mayx"