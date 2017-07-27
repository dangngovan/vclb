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
    vc_snmp_user = "ccloud"
    sw84_snmp_pw = "L1q1NIFeOdyXEAFiVHkV1"
    sw85_snmp_pw = "a1Vi2nCZXBib4qDykaJ6w"
    sw1702_snmp_pw = "I1z7DFrey19QyXvJNVanP"
    oid_bw_quota = "1.3.6.1.2.1.2.2.1.5"
    oid_bw_curent = "1.3.6.1.2.1.2.2.1.16"
    # sw85 (Po5) -> Core
    sw85_to_swcore_quota = commands.getoutput("snmpwalk -v3 -l authNoPriv -u %s -a MD5 -A %s \
    123.31.8.5 %s.5005"%(vc_snmp_user,sw85_snmp_pw,oid_bw_quota)).split(": ")[1]
    sw85_to_swcore_curent = commands.getoutput("snmpwalk -v3 -l authNoPriv -u %s -a MD5 -A %s \
    123.31.8.5 %s.5005"%(vc_snmp_user,sw85_snmp_pw,oid_bw_curent)).split(": ")[1]

    # sw1702 (Po1)-> swcore
    sw1702_to_swcore_quota = commands.getoutput("snmpwalk -v3 -l authNoPriv -u %s -a MD5 -A %s \
    123.30.170.2 %s.5001"%(vc_snmp_user,sw1702_snmp_pw,oid_bw_quota)).split(": ")[1]
    sw1702_to_swcore_curent = commands.getoutput("snmpwalk -v3 -l authNoPriv -u %s -a MD5 -A %s \
    123.30.170.2 %s.5001"%(vc_snmp_user,sw1702_snmp_pw,oid_bw_curent)).split(": ")[1]

    # sw84 (Po1) -> sw85
    sw84_to_sw85_quota = commands.getoutput("snmpwalk -v3 -l authNoPriv -u %s -a MD5 -A %s \
    123.31.8.4 %s.5001"%(vc_snmp_user,sw84_snmp_pw,oid_bw_quota)).split(": ")[1]
    sw1702_to_sw85_curent = commands.getoutput("snmpwalk -v3 -l authNoPriv -u %s -a MD5 -A %s \
    123.31.8.4 %s.5001"%(vc_snmp_user,sw84_snmp_pw,oid_bw_curent)).split(": ")[1]

    #sw85  (Po4) -> svr27126
    sw85_to_svr27126_quota = commands.getoutput("snmpwalk -v3 -l authNoPriv -u %s -a MD5 -A %s \
    123.31.8.5 %s.5004"%(vc_snmp_user,sw85_snmp_pw,oid_bw_quota)).split(": ")[1]
    sw85_to_svr27126_curent = commands.getoutput("snmpwalk -v3 -l authNoPriv -u %s -a MD5 -A %s \
    123.31.8.5 %s.5004"%(vc_snmp_user,sw85_snmp_pw,oid_bw_curent)).split(": ")[1]

    data = [{
            "Dich Vu":"CND",
            "Duong Truyen": "8.5 to core",
            "Bang Thong (MB)":float(sw85_to_swcore_quota)/100000,
            "Bang Thong Hien Tai (MB)":float(sw85_to_swcore_curent)/1000000,
            "Ty Le(%)": float(sw85_to_swcore_curent)/float(sw85_to_swcore_quota)* 100
        },
        {
            "Dich Vu": "CND",
            "Duong Truyen": "170.2 to core",
            "Bang Thong (MB)":float(sw1702_to_swcore_quota)/1000000,
            "Bang Thong Hien Tai (MB)":float(sw1702_to_swcore_curent)/100000,
            "Ty Le(%)": float(sw1702_to_swcore_curent)/float(sw1702_to_swcore_quota)* 100
        },
        {
            "Dich Vu": "CND",
            "Duong Truyen": "8.4 to 8.5",
            "Bang Thong (MB)":float(sw84_to_sw85_quota)/100000,
            "Bang Thong Hien Tai (MB)":float(sw84_to_sw85_curent)/100000,
            "Ty Le(%)": float(sw84_to_sw85_curent)/float(sw84_to_sw85_quota)* 100,
            "May chu1":float(sw85_to_svr27126_curent)/10000

        }]
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
  app.run(debug=True)