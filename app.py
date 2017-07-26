from flask import Flask, render_template
import commands
import json

"""
BANG PHAN PHOI BANG THONG CUA DICH VU CDN & LIVETV
"""

app = Flask(__name__)


#jdata=json.dumps(data)

@app.route('/')
def index():
    data = [{
        "Duong Truyen": "CDN CORE_TO_8.5",
        "Bang Thong Cho Phep (MB)":
            float(commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 iso.3.6.1.2.1.2.2.1.5.10148").split(": ")[1])/100000,
        "Bang Thong Hien Tai (MB)":
            float(commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 IF-MIB::ifOutOctets.10148").split(": ")[1])/1000000,
        "Ty Le(%)": float(commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 IF-MIB::ifOutOctets.10148").split(": ")[1]) / \
                    float(commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 iso.3.6.1.2.1.2.2.1.5.10148").split(": ")[1]) \
                    * 100
        },
        {
            "Duong Truyen": "CDN CORE_TO_170.2",
            "Bang Thong Cho Phep (MB)":
                float(commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 iso.3.6.1.2.1.2.2.1.5.10202").split(": ")[1])/1000000,
            "Bang Thong Hien Tai (MB)":
                float(commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 IF-MIB::ifOutOctets.10202").split(": ")[1])/100000,
            "Ty Le(%)": float(
                commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 IF-MIB::ifOutOctets.10202").split(": ")[1]) / \
                        float(commands.getoutput(
                            "snmpwalk -c public -v2c 192.168.51.224 iso.3.6.1.2.1.2.2.1.5.10202").split(": ")[1]) \
                        * 100
        }, {
            "Duong Truyen": "CDN 8.5_TO_8.4",
            "Bang Thong Cho Phep (MB)":
                float(commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 iso.3.6.1.2.1.2.2.1.5.10103").split(": ")[1])/100000,
            "Bang Thong Hien Tai (MB)":
                float(commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 IF-MIB::ifOutOctets.10103").split(": ")[1])/100000,
            "Ty Le(%)": float(
                commands.getoutput("snmpwalk -c public -v2c 192.168.51.224 IF-MIB::ifOutOctets.10103").split(": ")[1]) / \
                        float(commands.getoutput(
                            "snmpwalk -c public -v2c 192.168.51.224 iso.3.6.1.2.1.2.2.1.5.10103").split(": ")[1]) \
                        * 100,
            "May Chu1":"27.160: %s"%(1000/4),
            "May Chu2":"27.127: %s"%(1000/4),
            "May Chu3":"27.84: %s"%(1000/4),
            "May Chu4":"27.150: %s"%(1000/4)
        }]
    # other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
    columns = [
        {
            "field": "Duong Truyen",  # which is the field's name of data key
            "title": "Duong Truyen",  # display as the table header's name
            "sortable": True,
        },
        {
            "field": "Bang Thong Cho Phep (MB)",
            "title": "Bang Thong Cho Phep (MB)",
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
      title='BANG PHAN PHOI BANG THONG DICH VU CDN & LIVETV')


if __name__ == '__main__':
	#print jdata
  app.jinja_env.auto_reload = True
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run(debug=True)