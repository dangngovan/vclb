from flask import Flask, render_template
import commands
import json
import time
import MySQLdb
"""
BANG PHAN PHOI BANG THONG CUA DICH VU VC
"""

app = Flask(__name__)


#jdata=json.dumps(data)

@app.route('/')
def index():
    conn = MySQLdb.connect(host= "10.5.52.33",
                  user="root",
                  passwd="Ngayconang@123",
                  db="quota")
    x = conn.cursor()

	
    snmp_command = "snmpwalk -v3 -l authNoPriv -u"
    user = "vccloud"
    sw84_pw = "Lq1NIFeOdyXEAFiVHkV1"
    sw85_pw = "aVi2nCZXBib4qDykaJ6w"
    sw1702_pw = "Iz7DFrey19QyXvJNVanP"
    swcorenps_pw = "qP2lXJ1UWDYzibBVZw0F"
    x.execute("select quota,sudung from result  where time in (select max(time) from result group by project) AND project='NPS_LIVETV';")
    data = x.fetchall ()
    for row in data:
        livetv_nps_use = float(row[1])
        livetv_nps_quota = float(row[0])

    x.execute("select quota,sudung from result  where time in (select max(time) from result group by project) AND project='NTL_LIVETV';")
    data = x.fetchall ()
    for row in data:
        livetv_ntl_use = float(row[1])
        livetv_ntl_quota = float(row[0])

    x.execute("select quota,sudung from result  where time in (select max(time) from result group by project) AND project='FPT_LIVETV';")
    data = x.fetchall ()
    for row in data:
        livetv_fpt_use = float(row[1])
        livetv_fpt_quota = float(row[0])

    x.execute(" select quota,sudung from result  where time in (select max(time) from result group by project) AND project='HCM_LIVETV';")
    data = x.fetchall ()
    for row in data:
        livetv_hcm_use = float(row[1])
        livetv_hcm_quota = float(row[0])

    x.execute("select quota,sudung from result  where time in (select max(time) from result group by project) AND project='NPS_CDN';")
    data = x.fetchall ()
    for row in data:
        cdn_nps_use = float(row[1])
        cdn_nps_quota = float(row[0])

    x.execute("select quota,sudung from result  where time in (select max(time) from result group by project) AND project='NTL_CDN';")
    data = x.fetchall ()
    for row in data:
        cdn_ntl_use = float(row[1])
        cdn_ntl_quota = float(row[0])

    x.execute("select quota,sudung from result  where time in (select max(time) from result group by project) AND project='FPT_CDN';")
    data = x.fetchall ()
    for row in data:
        cdn_fpt_use = float(row[1])
        cdn_fpt_quota = float(row[0])

    x.execute(" select quota,sudung from result  where time in (select max(time) from result group by project) AND project='HCM_CDN';")
    data = x.fetchall ()
    for row in data:
        cdn_hcm_use = float(row[1])
        cdn_hcm_quota = float(row[0])
    x.close()	
    data = [{
            "ISP":"NPS",
	    "PROJECT":"LIVETV",
	    "QUOTA":livetv_nps_quota,
	    "USE":"%.2f"%livetv_nps_use,
	    "FREE":"%.2f"%( livetv_nps_quota - livetv_nps_use),
	    "PER(%)":"%.2f"%((livetv_nps_use/livetv_nps_quota)*100)
        },
	{
	    "ISP":"NTL",
            "PROJECT":"LIVETV",
            "QUOTA":livetv_ntl_quota,
            "USE":"%.2f"%livetv_ntl_use,
            "FREE": "%.2f"%(livetv_ntl_quota - livetv_ntl_use),
            "PER(%)":"%.2f"%((livetv_ntl_use/livetv_ntl_quota)*100)
	},
	{
	    "ISP":"FPT",
            "PROJECT":"LIVETV",
            "QUOTA":livetv_fpt_quota,
            "USE":"%.2f"%livetv_fpt_use,
            "FREE": "%.2f"%(livetv_fpt_quota - livetv_fpt_use),
            "PER(%)":"%.2f"%((livetv_fpt_use/livetv_fpt_quota)*100)
	},
	{
	    "ISP":"HCM",
            "PROJECT":"LIVETV",
            "QUOTA":livetv_hcm_quota,
            "USE":"%.2f"%livetv_hcm_use,
            "FREE":"%.2f"%( livetv_hcm_quota - livetv_hcm_use),
            "PER(%)":"%.2f"%((livetv_hcm_use/livetv_hcm_quota)*100)
	},
	{
            "ISP":"NPS",
            "PROJECT":"CDN",
            "QUOTA":cdn_nps_quota,
            "USE":"%.2f"%cdn_nps_use,
            "FREE": "%.2f"%(cdn_nps_quota - cdn_nps_use),
            "PER(%)":"%.2f"%((cdn_nps_use/cdn_nps_quota)*100)
        },
	{
            "ISP":"FPT",
            "PROJECT":"CDN",
            "QUOTA":cdn_fpt_quota,
            "USE":"%.2f"%cdn_fpt_use,
            "FREE":"%.2f"%(cdn_fpt_quota - cdn_fpt_use),
            "PER(%)":"%.2f"%((cdn_fpt_use/cdn_fpt_quota)*100)
        },
	{
            "ISP":"NTL",
            "PROJECT":"CDN",
            "QUOTA":cdn_ntl_quota,
            "USE":"%.2f"%cdn_ntl_use,
            "FREE":"%.2f"% (cdn_ntl_quota - cdn_ntl_use),
            "PER(%)":"%.2f"%((cdn_ntl_use/cdn_ntl_quota)*100)
        },
	{
            "ISP":"HCM",
            "PROJECT":"CDN",
            "QUOTA":cdn_hcm_quota,
            "USE":"%.2f"%cdn_hcm_use,
            "FREE": "%.2f"%(cdn_hcm_quota - cdn_hcm_use),
            "PER(%)":"%.2f"%((cdn_hcm_use/cdn_hcm_quota)*100)
        }
        ]
    # other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
    columns = [
        {
            "field": "ISP",  # which is the field's name of data key
            "title": "ISP",  # display as the table header's name
            "sortable": True,
        },
        {
            "field": "PROJECT",  # which is the field's name of data key
            "title": "PROJECT",  # display as the table header's name
            "sortable": True,
        },
        {
            "field": "QUOTA",
            "title": "QUOTA(Gbps)",
            "sortable": True,
        },
        {
            "field": "USE",
            "title": "USE(Gpbs)",
            "sortable": True,
        },
        {
            "field": "FREE",
            "title": "FREE(Gbps)",
            "sortable": True,
        },
        {
            "field": "PER(%)",
            "title": "PER(%)",
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
