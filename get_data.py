import commands
import json
import time
import datetime
import MySQLdb
conn = MySQLdb.connect(host= "10.5.52.33",
                  user="root",
                  passwd="Ngayconang@123",
                  db="quota")
x = conn.cursor()
livetv_nps_quota = 20
livetv_ntl_quota = 20
livetv_fpt_quota = 20
livetv_hcm_quota = 20
cdn_nps_quota = 20
cdn_ntl_quota = 20
cdn_fpt_quota = 20
cdn_hcm_quota = 20

#jdata=json.dumps(data)
livetv_fpt_use_41 = commands.getoutput("sh get_bw_v2.sh -h 42.112.37.1 -s monitor -b 50 -i 2")
livetv_fpt_use_42 = commands.getoutput("sh get_bw_v2.sh -h 42.112.37.1 -s monitor -b 50 -i 1")
livetv_fpt_use = (float(livetv_fpt_use_41.split()[1]) + float(livetv_fpt_use_42.split()[1]))/1000000
x.execute (" INSERT INTO result VALUES ('%s','%s','%s', '%s','%s','%s','%s')"%(datetime.datetime.utcnow(),'FPT','FPT_LIVETV', livetv_fpt_quota,livetv_fpt_use,livetv_fpt_quota - livetv_fpt_use, livetv_fpt_use/livetv_fpt_quota*100,))


# LIVETV NPS = 27.46 + 27.48 + SVR579R
livetv_nps_use_46 = commands.getoutput("sh get_bw_v2.sh -h 172.31.1.223 -s monitor -b 50 -i 403505177")
livetv_nps_use_48 = commands.getoutput("sh get_bw_v2.sh -h 172.31.1.223 -s monitor -b 50 -i 403734560")
livetv_nps_use_579r = commands.getoutput("sh get_bw_v2.sh -h 172.31.1.223 -s monitor -b 50 -i 402849797")
livetv_nps_use = (float(livetv_nps_use_46.split()[1]) + float(livetv_nps_use_48.split()[1]) + float(livetv_nps_use_579r.split()[1]))/1000000
x.execute (" INSERT INTO result VALUES ('%s','%s','%s', '%s','%s','%s','%s')"%(datetime.datetime.utcnow(),'NPS','NPS_LIVETV', livetv_nps_quota,livetv_nps_use,livetv_nps_quota - livetv_nps_use, livetv_nps_use/livetv_nps_quota*100,))

# LIVETV NTL = 32.23 + 32.21 + 32.22 + 32.24
livetv_ntl_use_21 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.6 -s monitor -b 50 -i 436209664")
livetv_ntl_use_22 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.9 -s monitor -b 50 -i 436213248")
livetv_ntl_use_23 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.6 -s monitor -b 50 -i 436209152")
livetv_ntl_use_24 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.9 -s monitor -b 50 -i 436207616")
livetv_ntl_use = (float(livetv_ntl_use_21.split()[1]) + float(livetv_ntl_use_22.split()[1]) + float(livetv_ntl_use_23.split()[1]) + float(livetv_ntl_use_24.split()[1]))/1000000
x.execute (" INSERT INTO result VALUES ('%s','%s','%s', '%s','%s','%s','%s')"%(datetime.datetime.utcnow(),'NTL','NTL_LIVETV', livetv_ntl_quota,livetv_ntl_use,livetv_ntl_quota - livetv_ntl_use, livetv_ntl_use/livetv_ntl_quota*100,))

# LIVETV HCM = 215.65 + 215.43 + 215.47
livetv_hcm_use_65 = commands.getoutput("sh get_bw_v2.sh -h 123.30.215.1 -s monitor -b 50 -i 436244480")
livetv_hcm_use_43 = commands.getoutput("sh get_bw_v2.sh -h 123.30.215.1 -s monitor -b 50 -i 436367360")
livetv_hcm_use_47 = commands.getoutput("sh get_bw_v2.sh -h 123.30.215.1 -s monitor -b 50 -i 436224000")
livetv_hcm_use = (float(livetv_hcm_use_65.split()[1]) + float(livetv_hcm_use_43.split()[1]) + float(livetv_hcm_use_47.split()[1]))/1000000
x.execute (" INSERT INTO result VALUES ('%s','%s','%s', '%s','%s','%s','%s')"%(datetime.datetime.utcnow(),'HCM','HCM_LIVETV', livetv_hcm_quota,livetv_hcm_use,livetv_hcm_quota - livetv_hcm_use, livetv_hcm_use/livetv_hcm_quota*100,))

# CDN NPS = 27.25 + 27.76 + 27.77 + 27.103 + 27.107 + 27.131
cdn_nps_use_25 = commands.getoutput("sh get_bw_v2.sh -h 172.31.1.223 -s monitor -b 50 -i 403832867")
cdn_nps_use_76 = commands.getoutput("sh get_bw_v2.sh -h 172.31.1.223 -s monitor -b 50 -i 404029481")
cdn_nps_use_77 = commands.getoutput("sh get_bw_v2.sh -h 172.31.1.223 -s monitor -b 50 -i 403996712")
cdn_nps_use_103 = commands.getoutput("sh get_bw_v2.sh -h 172.31.1.223 -s monitor -b 50 -i 404062250")
cdn_nps_use_107 = commands.getoutput("sh get_bw_v2.sh -h 172.31.1.223 -s monitor -b 50 -i 403570715")
cdn_nps_use_131 = commands.getoutput("sh get_bw_v2.sh -h 172.31.1.223 -s monitor -b 50 -i 403144718")
cdn_nps_use = (float(cdn_nps_use_25.split()[1]) + float(cdn_nps_use_76.split()[1]) + float(cdn_nps_use_77.split()[1]) + float(cdn_nps_use_103.split()[1]) + float(cdn_nps_use_107.split()[1]) + float(cdn_nps_use_131.split()[1]))/1000000
x.execute (" INSERT INTO result VALUES ('%s','%s','%s', '%s','%s','%s','%s')"%(datetime.datetime.utcnow(),'NPS','NPS_CDN', cdn_nps_quota,cdn_nps_use,cdn_nps_quota - cdn_nps_use, cdn_nps_use/cdn_nps_quota*100,))

# CDN FPT =  37.51 + 37.48 + 37.52 + 37.22
cdn_fpt_use_51 = commands.getoutput("sh get_bw_v2.sh -h 42.112.37.1 -s monitor -b 50 -i 3")
cdn_fpt_use_48 = commands.getoutput("sh get_bw_v2.sh -h 42.112.37.1 -s monitor -b 50 -i 6")
cdn_fpt_use_52 = commands.getoutput("sh get_bw_v2.sh -h 42.112.37.1 -s monitor -b 50 -i 34")
cdn_fpt_use_22 = commands.getoutput("sh get_bw_v2.sh -h 42.112.37.1 -s monitor -b 50 -i 5")
cdn_fpt_use = (float(cdn_fpt_use_51.split()[1]) + float(cdn_fpt_use_48.split()[1]) + float(cdn_fpt_use_52.split()[1]) + float(cdn_fpt_use_22.split()[1]))/1000000
x.execute (" INSERT INTO result VALUES ('%s','%s','%s', '%s','%s','%s','%s')"%(datetime.datetime.utcnow(),'FPT','FPT_CDN', cdn_fpt_quota,cdn_fpt_use,cdn_fpt_quota - cdn_fpt_use, cdn_fpt_use/cdn_fpt_quota*100,))


# CDN NTL = 32.19 + 32.25 + 32.15 + 32.26 + 32.17 + 32.18
cdn_ntl_use_25 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.6 -s monitor -b 50 -i 436207616")
cdn_ntl_use_17 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.6 -s monitor -b 50 -i 436208640")
cdn_ntl_use_18 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.6 -s monitor -b 50 -i 436208128")
cdn_ntl_use_15 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.9 -s monitor -b 50 -i 436208640")
cdn_ntl_use_19 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.9 -s monitor -b 50 -i 436216832")
cdn_ntl_use_26 = commands.getoutput("sh get_bw_v2.sh -h 172.18.255.9 -s monitor -b 50 -i 436210176")
cdn_ntl_use = (float(cdn_ntl_use_25.split()[1]) + float(cdn_ntl_use_17.split()[1]) + float(cdn_ntl_use_18.split()[1]) + float(cdn_ntl_use_15.split()[1]) + float(cdn_ntl_use_19.split()[1]) + float(cdn_ntl_use_26.split()[1]))/1000000
x.execute (" INSERT INTO result VALUES ('%s','%s','%s', '%s','%s','%s','%s')"%(datetime.datetime.utcnow(),'NTL','NTL_CDN', cdn_ntl_quota,cdn_ntl_use,cdn_ntl_quota - cdn_ntl_use, cdn_ntl_use/cdn_ntl_quota*100,))

# CDN HCM = 215.11 + 215.41 + 215.42 + 215.51 + 215.40
cdn_hcm_use_11 = commands.getoutput("sh get_bw_v2.sh -h 123.30.215.1 -s monitor -b 50 -i 436215808")
cdn_hcm_use_41 = commands.getoutput("sh get_bw_v2.sh -h 123.30.215.1 -s monitor -b 50 -i 436400128")
cdn_hcm_use_42 = commands.getoutput("sh get_bw_v2.sh -h 123.30.215.1 -s monitor -b 50 -i 436207616")
cdn_hcm_use_51 = commands.getoutput("sh get_bw_v2.sh -h 123.30.215.1 -s monitor -b 50 -i 436211712")
cdn_hcm_use_40 = commands.getoutput("sh get_bw_v2.sh -h 123.30.215.1 -s monitor -b 50 -i 436383744")
cdn_hcm_use = (float(cdn_hcm_use_11.split()[1]) + float(cdn_hcm_use_41.split()[1]) + float(cdn_hcm_use_42.split()[1]) + float(cdn_hcm_use_51.split()[1]) + float(cdn_hcm_use_40.split()[1]))/1000000
x.execute (" INSERT INTO result VALUES ('%s','%s','%s', '%s','%s','%s','%s')"%(datetime.datetime.utcnow(),'HCM','HCM_CDN', cdn_hcm_quota,cdn_hcm_use,cdn_hcm_quota - cdn_hcm_use, cdn_hcm_use/cdn_hcm_quota*100,))

x.close()
