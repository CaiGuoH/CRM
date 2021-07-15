from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText


# ============定义发送邮件============
def send_mail(file_new, pic):
    smtpserver = "smtp.qq.com"  # 发件服务器
    port = 465  # 端口
    sender = "1509965844@qq.com"  # 发送端
    psw = "gkikyxikxpmphbbh"  # 密码/授权码
    # receiver = ['2469367871@qq.com', '1509965844@qq.com', '1183724987@qq.com', '2240531513@qq.com']  # 接收端
    # receiver = '1509965844@qq.com'
    receiver = ['2469367871@qq.com', '1509965844@qq.com']
    # =========编辑邮件内容=========
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    #图片
    # time.sleep(3)
    # print(pic)
    # f2 = open(pic, 'rb')
    # msgImage = MIMEImage(f2.read())
    # f2.close()
    # 定义发件人，收件人，和邮件标题
    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    for i in  receiver:
        msg["to"] = i
    # msg["to"] = receiver# 收件人
    msg["subject"] = "自动化测试报告"  # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)  # 挂起、固定？

    # 附件1
    att3 = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="report_test.html"'
    msg.attach(att3)
    # att = MIMEText(mail_body, "base64", "utf-8")
    # att["Content-Type"] = "application/octet-stream"
    # att["Content-Disposition"] = 'attachment; filename="测试报告附件_report.html"'  # 定义附件名称
    # msg.attach(att)  # 挂起

    #附件2
    # msgImage.add_header('Content-ID', 'photo')
    # msg.attach(msgImage)
    att2 = MIMEText(open(pic, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="123.jpg"'
    msg.attach(att2)
    # att2 = MIMEImage(msgImage,'base64','utf-8')
    # att2["Content-Type"] = "application/octet-stream"
    # att2["Content-Disposition"] = 'attachment; filename="测试报告附件_img.png"'  # 定义附件名称
    # msg.attach(att2)

    # =========发送邮件=========
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
    # 发送
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()  # 关闭