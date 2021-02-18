#!/Bin/Bash
Zoom=5
i="0"

POPUPD="--geometry=80x10+780+900"
APOPUP="--geometry=30x30+10+50"
PODDOWN="--geometry=158x20+0+900"

echo "" >> log

sleep 1
gnome-terminal.real $APOPUP -e "sh -f monitor.sh"
gnome-terminal $PODDOWN -e "journalctl -xf"
gnome-terminal.real $POPUPD -e "python3 Cap-Oigo.py"


while [ $i -lt 4 ]
do
echo "=========================================="
echo "          ESTADO DE CONEXIONES            "
echo "======================================= XF"
echo " "
echo " "
netstat -tun | grep -v "127.0.0.1" | grep --color=always "ESTABLECIDO" ;
sleep 3
clear
done

# https://xfenix652194466.wordpress.com