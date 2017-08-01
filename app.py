from flask import Flask, render_template
import commands
import json

"""
BANG PHAN PHOI BANG THONG CUA DICH VU VC
"""

app = Flask(__name__)


#jdata=json.dumps(data)

@app.route('/')
def index():
    snmp_command = "snmpwalk -v3 -l authNoPriv -u"
    user = "vccloud"
    sw84_pw = "Lq1NIFeOdyXEAFiVHkV1"
    sw85_pw = "aVi2nCZXBib4qDykaJ6w"
    sw1702_pw = "Iz7DFrey19QyXvJNVanP"
    swcorenps_pw = "qP2lXJ1UWDYzibBVZw0F"


    oid_bw_quota = "1.3.6.1.2.1.2.2.1.5"
    oid_bw_curent_out = "1.3.6.1.2.1.2.2.1.16"
    oid_bw_curent_in = "1.3.6.1.2.1.2.2.1.10"
    # sw85 (Po2) -> Core
    sw85_to_swcore_quota = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.5 %s.5002"%(snmp_command,user,sw85_pw,oid_bw_quota)).split(": ")[1]
    sw85_to_swcore_curent = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.5 %s.5002"%(snmp_command,user,sw85_pw,oid_bw_curent_out)).split(": ")[1]

    # sw1702 (Po1)-> swcore
    sw1702_to_swcore_quota = commands.getoutput("%s %s -a MD5 -A %s 123.30.170.2 %s.5001"%(snmp_command,user,sw1702_pw,oid_bw_quota)).split(": ")[1]
    sw1702_to_swcore_curent = commands.getoutput("%s %s -a MD5 -A %s 123.30.170.2 %s.5001"%(snmp_command,user,sw1702_pw,oid_bw_curent_out)).split(": ")[1]

    # sw1702 -> svr170126 Gi0/27 28 29 30
    sw1702_to_svr170126_curent = commands.getoutput("%s %s -a MD5 -A %s 123.30.170.2 %s.10127"%(snmp_command,user,sw1702_pw,oid_bw_curent_in)).split(": ")[1]

    # sw84 (Po1) -> sw85
    sw84_to_sw85_quota = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.4 %s.5001"%(snmp_command,user,sw84_pw,oid_bw_quota)).split(": ")[1]
    sw84_to_sw85_curent = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.4 %s.5001"%(snmp_command,user,sw84_pw,oid_bw_curent_out)).split(": ")[1]

    #sw85  (gi2/0/42-43-44-45) -> svr27126
    sw85_to_svr27126_quota = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.5 %s.10642"%(snmp_command,user,sw85_pw,oid_bw_quota)).split(": ")[1]
    sw85_to_svr27126_curent = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.5 %s.10642"%(snmp_command,user,sw85_pw,oid_bw_curent_in)).split(": ")[1]
    # sw84 (gi0/3-4 12 13) -> svr27160
    sw84_to_svr27160_curent = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.4 %s.10103"%(snmp_command,user,sw84_pw,oid_bw_curent_in)).split(": ")[1]
    # sw84 (gi0/1 2 14 15) svr27127
    sw84_to_svr27127_curent = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.4 %s.10101"%(snmp_command,user,sw84_pw,oid_bw_curent_in)).split(": ")[1]
    # sw84 (gi0/10 19 22 23) svr2784
    sw84_to_svr2784_curent = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.4 %s.10110"%(snmp_command,user,sw84_pw,oid_bw_curent_in)).split(": ")[1]
    # sw84 (g0/7 8 24 25) svr27150
    sw84_to_svr27150_curent = commands.getoutput("%s %s -a MD5 -A %s 123.31.8.4 %s.10107"%(snmp_command,user,sw84_pw,oid_bw_curent_in)).split(": ")[1]

    #   swfptwan_to_core
    swfptwan_to_core_quota = commands.getoutput("snmpwalk -c monitor -v2c 42.112.37.1 1.3.6.1.2.1.2.2.1.5.61").split(": ")[1]
    swfptwan_to_core_curent = commands.getoutput("snmpwalk -c monitor -v2c 42.112.37.1 1.3.6.1.2.1.2.2.1.16.61").split(": ")[1]
    #swfptwan_to_svr3742 ten 1/1
    swfptwan_to_svr3742_curent = commands.getoutput("snmpwalk -c monitor -v2c 42.112.37.1 1.3.6.1.2.1.2.2.1.10.1").split(": ")[1]
    #swfptwan_to_svr3741 ten 1/2
    swfptwan_to_svr3741_curent = commands.getoutput("snmpwalk -c monitor -v2c 42.112.37.1 1.3.6.1.2.1.2.2.1.10.2").split(": ")[1]

    # sw274 to swcorenps po3
    sw274_to_swcorenps_quota = commands.getoutput("snmpwalk -c monitor -v2c 172.31.1.223 1.3.6.1.2.1.2.2.1.5.403701791").split(": ")[1]
    sw274_to_swcorenps_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.31.1.223 1.3.6.1.2.1.2.2.1.16.403701791").split(": ")[1]

    sw274_to_svr2789_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.31.1.223 1.3.6.1.2.1.2.2.1.10.403472408").split(": ")[1]
    sw274_to_svr2746_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.31.1.223 1.3.6.1.2.1.2.2.1.10.403505177").split(": ")[1]
    sw274_to_svr2748_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.31.1.223 1.3.6.1.2.1.2.2.1.10.403734560").split(": ")[1]
    sw274_to_svr579r_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.31.1.223 1.3.6.1.2.1.2.2.1.10.402849797").split(": ")[1]

    # swcorenps to vnpt po1
    swcorenps_to_vnpt_quota = commands.getoutput("%s %s -a MD5 -A %s 123.30.232.84 %s.41"%(snmp_command,user,swcorenps_pw,oid_bw_quota)).split(": ")[1]
    swcorenps_to_vnpt_curent = commands.getoutput("%s %s -a MD5 -A %s 123.30.232.84 %s.41"%(snmp_command,user,swcorenps_pw,oid_bw_curent_out)).split(": ")[1]
    # swcorenps to viettel te1/4 te1/8
    swcorenps_to_viettel1_quota = commands.getoutput("%s %s -a MD5 -A %s 123.30.232.84 %s.4"%(snmp_command,user,swcorenps_pw,oid_bw_quota)).split(": ")[1]
    swcorenps_to_viettel1_curent = commands.getoutput("%s %s -a MD5 -A %s 123.30.232.84 %s.4"%(snmp_command,user,swcorenps_pw,oid_bw_curent_out)).split(": ")[1]
    swcorenps_to_viettel2_quota = commands.getoutput("%s %s -a MD5 -A %s 123.30.232.84 %s.8"%(snmp_command,user,swcorenps_pw,oid_bw_quota)).split(": ")[1]
    swcorenps_to_viettel2_curent = commands.getoutput("%s %s -a MD5 -A %s 123.30.232.84 %s.8"%(snmp_command,user,swcorenps_pw,oid_bw_curent_out)).split(": ")[1]

    # swntl01_02 to vnptntl
    swntl01_to_vnptntl_quota = commands.getoutput("snmpwalk -c monitor -v2c 172.18.255.6 1.3.6.1.2.1.2.2.1.5.369098899").split(": ")[1]
    swntl01_to_vnptntl_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.18.255.6 1.3.6.1.2.1.2.2.1.16.369098899").split(": ")[1]
    # swntl01 to svr3223 eth1/4
    swntl01_to_svr3223_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.18.255.6 1.3.6.1.2.1.2.2.1.10.436209152").split(": ")[1]
    # swntl01 to svr3221 eth1/5
    swntl01_to_svr3221_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.18.255.6 1.3.6.1.2.1.2.2.1.10.436209664").split(": ")[1]

    # swntl02 to vnptntl
    swntl02_to_vnptntl_quota = commands.getoutput("snmpwalk -c monitor -v2c 172.18.255.9 1.3.6.1.2.1.2.2.1.16.369098899").split(": ")[1]
    swntl02_to_vnptntl_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.18.255.9 1.3.6.1.2.1.2.2.1.16.369098899").split(": ")[1]
    # swntl02 to svr3222
    swntl02_to_svr3222_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.18.255.9 1.3.6.1.2.1.2.2.1.10.436213248").split(": ")[1]
    # swntl02 to svr3224
    swntl02_to_svr3224_curent = commands.getoutput("snmpwalk -c monitor -v2c 172.18.255.9 1.3.6.1.2.1.2.2.1.10.436207616").split(": ")[1]

    data = [{
            "Dich Vu":"VC_CDN_Backend",
            "Duong Truyen": "8.5 to core",
            "Bang Thong (MB)":float(sw85_to_swcore_quota)/1000000,
            "Bang Thong Hien Tai (MB)":float(sw85_to_swcore_curent)/1000000,
            "Ty Le(%)": float(sw85_to_swcore_curent)/float(sw85_to_swcore_quota)* 100,
            "May Chu1": float(sw85_to_svr27126_curent) * 4 / 100000000
        },
        {
            "Dich Vu": "VC_CDN_Backend",
            "Duong Truyen": "170.2 to core",
            "Bang Thong (MB)":float(sw1702_to_swcore_quota)/1000000,
            "Bang Thong Hien Tai (MB)":float(sw1702_to_swcore_curent)/1000000,
            "Ty Le(%)": float(sw1702_to_swcore_curent)/float(sw1702_to_swcore_quota)* 100,
            "May Chu1": "170.126: %s"%(float(sw1702_to_svr170126_curent) * 4 / 100000000)
        },
        {
            "Dich Vu": "VC_CDN_Backend",
            "Duong Truyen": "8.4 to 8.5",
            "Bang Thong (MB)":float(sw84_to_sw85_quota)/1000000,
            "Bang Thong Hien Tai (MB)":float(sw84_to_sw85_curent)/1000000,
            "Ty Le(%)": float(sw84_to_sw85_curent)/float(sw84_to_sw85_quota)* 100,
            "May Chu1": "27.160: %s"%(float(sw84_to_svr27160_curent) * 4 / 100000000),
            "May Chu2": "27.127: %s"%(float(sw84_to_svr27127_curent) * 4 / 100000000),
            "May Chu3": "27.84: %s"%(float(sw84_to_svr2784_curent) * 4 / 100000000),
            "May Chu4": "27.150: %s"%(float(sw84_to_svr27150_curent) * 4 / 100000000)

        },
        {
            "Dich Vu": "LiveTV",
            "Duong Truyen": "FPT WAN TO CORE",
            "Bang Thong (MB)": float(swfptwan_to_core_quota) / 1000000,
            "Bang Thong Hien Tai (MB)": float(sw274_to_swcorenps_curent) / 1000000,
            "Ty Le(%)": float(sw274_to_swcorenps_curent) / float(swfptwan_to_core_quota) * 100,
            "May Chu1": "37.42: %s" % (float(swfptwan_to_svr3742_curent)/ 100000000),
            "May Chu2": "37.41: %s" % (float(swfptwan_to_svr3741_curent)/ 100000000)

        },
        {
            "Dich Vu": "LiveTV",
            "Duong Truyen": "SW27.4 To CORENPS",
            "Bang Thong (MB)": float(sw274_to_swcorenps_quota) / 1000000,
            "Bang Thong Hien Tai (MB)": float(swfptwan_to_core_curent) / 1000000,
            "Ty Le(%)": float(swfptwan_to_core_curent) / float(swfptwan_to_core_quota) * 100,
            "May Chu1": "27.89: %s" % (float(sw274_to_svr2789_curent) / 100000000),
            "May Chu2": "27.46: %s" % (float(sw274_to_svr2746_curent) / 100000000),
            "May Chu3": "27.48: %s" % (float(sw274_to_svr2748_curent) / 100000000),
            "May Chu4": "svr579r: %s" % (float(sw274_to_svr579r_curent) / 100000000)
        },
        {
            "Dich Vu": "LiveTV",
            "Duong Truyen": "CORE NPS TO VNPT",
            "Bang Thong (MB)": float(swcorenps_to_vnpt_quota) / 1000000,
            "Bang Thong Hien Tai (MB)": float(swcorenps_to_vnpt_curent) / 1000000,
            "Ty Le(%)": float(swcorenps_to_vnpt_curent) / float(swcorenps_to_vnpt_quota) * 100
        },
        {
            "Dich Vu": "LiveTV",
            "Duong Truyen": "CORE NPS TO VT1",
            "Bang Thong (MB)": float(swcorenps_to_viettel1_quota) / 1000000,
            "Bang Thong Hien Tai (MB)": float(swcorenps_to_viettel1_curent) / 1000000,
            "Ty Le(%)": float(swcorenps_to_viettel1_curent) / float(swcorenps_to_viettel1_quota) * 100
        },
        {
            "Dich Vu": "LiveTV",
            "Duong Truyen": "CORE NPS TO VT2",
            "Bang Thong (MB)": float(swcorenps_to_viettel2_quota) / 1000000,
            "Bang Thong Hien Tai (MB)": float(swcorenps_to_viettel2_curent) / 1000000,
            "Ty Le(%)": float(swcorenps_to_viettel2_curent) / float(swcorenps_to_viettel1_quota) * 100
        },
        {
            "Dich Vu": "LiveTV",
            "Duong Truyen": "NTL01 TO VNPT NTL",
            "Bang Thong (MB)": float(swntl01_to_vnptntl_quota) / 1000000,
            "Bang Thong Hien Tai (MB)": float(swntl01_to_vnptntl_curent) / 1000000,
            "Ty Le(%)": float(swntl01_to_vnptntl_curent) / float(swntl01_to_vnptntl_quota) * 100,
            "May Chu1": "31.21: %s" % (float(swntl01_to_svr3221_curent) / 100000000),
            "May Chu2": "31.23: %s" % (float(swntl01_to_svr3223_curent) / 100000000)
        },
        {
            "Dich Vu": "LiveTV",
            "Duong Truyen": "NTL02 TO VNPT NTL",
            "Bang Thong (MB)": float(swntl02_to_vnptntl_quota) / 1000000,
            "Bang Thong Hien Tai (MB)": float(swntl02_to_vnptntl_curent) / 1000000,
            "Ty Le(%)": float(swntl02_to_vnptntl_curent) / float(swntl02_to_vnptntl_quota) * 100,
            "May Chu1": "31.22: %s" % (float(swntl02_to_svr3222_curent) / 100000000),
            "May Chu2": "31.24: %s" % (float(swntl02_to_svr3224_curent) / 100000000)
        }
        ]
    # other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
    columns = [
        {
            "field": "Dich Vu",  # which is the field's name of data key
            "title": "Dich Vu",  # display as the table header's name
            "sortable": True,
        },
        {
            "field": "Duong Truyen",  # which is the field's name of data key
            "title": "Duong Truyen",  # display as the table header's name
            "sortable": True,
        },
        {
            "field": "Bang Thong (MB)",
            "title": "Bang Thong (MB)",
            "sortable": True,
        },
        {
            "field": "Bang Thong Hien Tai (MB)",
            "title": "Bang Thong Hien Tai (MB)",
            "sortable": True,
        },
        {
            "field": "Ty Le(%)",
            "title": "Ty Le(%)",
            "sortable": True,
        },
        {
            "field": "May Chu1",
            "title": "May Chu1",
            "sortable": True,
        },
        {
            "field": "May Chu2",
            "title": "May Chu2",
            "sortable": True,
        },
        {
            "field": "May Chu3",
            "title": "May Chu3",
            "sortable": True,
        },
        {
            "field": "May Chu4",
            "title": "May Chu4",
            "sortable": True,
        }
    ]
    return render_template("table.html",
      data=data,
      columns=columns,
      title='BANG PHAN PHOI BANG THONG DICH VU VC')


if __name__ == '__main__':
	#print jdata
  app.jinja_env.auto_reload = True
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run( host='10.3.26.7',debug=True)
