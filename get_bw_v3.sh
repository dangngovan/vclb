check () {
#INTNUMBER=403701791
ifOutOctets=1.3.6.1.2.1.2.2.1.16
ifInOctets=1.3.6.1.2.1.2.2.1.10
ifSpeed=1.3.6.1.2.1.2.2.1.5
#snmpget -v3 -l authNoPriv -u vccloud -a MD5 -A aVi2nCZXBib4qDykaJ6w 123.31.8.5 1.3.6.1.2.1.2.2.1.16.12623
OUT=$(snmpget -v3 -l authNoPriv -u vccloud -a MD5 -A $community_string $hostname $ifOutOctets.$INTNUMBER | awk '{print $4}')
IN=$(snmpget -v3 -l authNoPriv -u vccloud -a MD5 -A $community_string $hostname $ifInOctets.$INTNUMBER | awk '{print $4}')
SPEED=$(snmpget -v3 -l authNoPriv -u vccloud -a MD5 -A $community_string $hostname $ifSpeed.$INTNUMBER | awk '{print $4}')
TIME=5
SPEED=$speed
PIPE=10000
echo "OUT1:" $OUT
echo "IN1": $IN
        if [ -z "$OUT" ] || [ -z "$IN" ]; then
                msg="Unable to retrieve SNMP info."
                state=CRITICAL
                echo $state $msg
                exit 2

        else
                #wait $TIME before running the same check, this way we can confirm how much the data has changed in two periods.
                sleep $TIME
                OUT2=$(snmpget -v3 -l authNoPriv -u vccloud -a MD5 -A $community_string $hostname $ifOutOctets.$INTNUMBER | awk '{print $4}')
                IN2=$(snmpget -v3 -l authNoPriv -u vccloud -a MD5 -A $community_string $hostname $ifInOctets.$INTNUMBER | awk '{print $4}')
		echo "OUT2" $OUT2
		echo "IN2" $IN2
                DELTAOUT=$(( $OUT2 - $OUT +1))
                DELTAIN=$(( $IN2 - $IN +1))
                #Value is in octets so will need to be divided by 8 to get bytes, this is then divided by 1024 to give kilobytes.
                INPUTBW=$(((($DELTAIN)/$TIME)*8/1024))
                OUTPUTBW=$(((($DELTAOUT)/$TIME)*8/1024))
		msg="Inbound: $INPUTBW  Outbound: $OUTPUTBW"
		echo $msg

                #For percentage usage we do 100/(total possible bandwidth – current bandwidth).
#                percentage_use=$(echo "scale=9; $PIPE/$INPUTBW" | bc)
#                PRCNTIN=$(echo "scale=0; 100/$percentage_use/1000" | bc)
#                percentage_use=$(echo "scale=9; $PIPE/$OUTPUTBW" | bc)
#                PRCNTOUT=$(echo "scale=0; 100/$percentage_use/1000" | bc)
                #Bash hates decimals, so take the number and remove the decimal point and then compare this to speed (another none decimal).
#                PRCNTIN_IF=$(echo $PRCNTIN | tr -d ".")
#                PRCNTOUT_IF=$(echo $PRCNTOUT | tr -d ".")
#                if [ "$PRCNTIN_IF" -gt $SPEED ] || [ "$PRCNTOUT_IF" -gt $SPEED ]; then
#                        msg="Inbound: $INPUTBW"kbps" ($PRCNTIN% Used), Outbound: $OUTPUTBW"kbps" ($PRCNTOUT% Used)."
#                        msg="Inbound: $INPUTBW ($PRCNTIN% Used), Outbound: $OUTPUTBW ($PRCNTOUT% Used)."
#                        state=CRITICAL
#                        echo $state $msg
#                        exit 2
#                else
#                        #msg="Inbound: $INPUTBW"kbps" ($PRCNTIN% Used), Outbound: $OUTPUTBW"kbps" ($PRCNTOUT% Used)."
#                        msg="Inbound: $INPUTBW ($PRCNTIN% Used), Outbound: $OUTPUTBW ($PRCNTOUT% Used)."
#                        state=OK
#                        echo $state $msg
#                        exit 0
#                fi
        fi
}

while getopts "i:b:s:h:" option
do
case $option in
i)INTNUMBER=$OPTARG
;;
b)speed=$OPTARG
;;
s)community_string=$OPTARG
;;
h)hostname=$OPTARG
;;
*) echo "Syntax is $usage -h <hostname> -s <snmpstring> -b <bandwidth> -i <interface>"
exit 1;;
esac
done

if [ -z "$hostname" ]; then
        echo "-h) IP address required."
        exit 1
elif [ -z "$community_string" ]; then
        echo "-s) snmp string needs to be specified."
        exit 1
elif [ -z "$speed" ]; then
        echo "-b) bandwidth percentage used before flagging alerts (e.g 50)"
        exit 1
elif [ -z "$INTNUMBER" ]; then
        echo "-i) interface switch id"
        exit 1
else
        check
fi
