from my_settings import EMAIL

import smtplib
from email.mime.text import MIMEText


def google_mail(send_to: str):
    s = smtplib.SMTP(EMAIL['HOST'], EMAIL['PORT'])
    s.starttls()
    s.login(EMAIL['HOST_USER'], EMAIL['HOST_PW'])

    msg            = MIMEText('내용 : 본문내용 테스트입니다.')
    msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'
    msg['To']      = send_to

    s.sendmail(EMAIL['HOST_USER'], send_to, msg.as_string())
    s.quit()

    return


# import smtplib
# from email.mime.text      import MIMEText
# from email.mime.multipart import MIMEMultipart
# 
# username = "conpages@naver.com"
# password = "ekfhal251714!"
# mail_from = username
# mail_to = "yangdaz3@gmail.com"
# mail_subject = "Test Subject"
# mail_body = "This is a test message"
# 
# def mail_test():
#     mimemsg = MIMEMultipart()
#     mimemsg['From'] = mail_from
#     mimemsg['To'] = mail_to
#     mimemsg['Subject'] = mail_subject
#     mimemsg.attach(MIMEText(mail_body, 'plain'))
# 
#     connection = smtplib.SMTP(host='smtp.office365.com', port=587)
#     connection.starttls()
#     connection.login(username, password)
#     connection.send_message(mimemsg)
#     connection.quit()
# 
#     return "okay"
 
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# 
# username = "vegeto@office365.com"
# password = "password123qwe"
# mail_from = "vegeto@office365.com"
# mail_to = "goku@dbz.com"
# mail_subject = "Test Subject"
# mail_body = "This is a test message"
# mail_attachment="/tmp/test.txt"
# mail_attachment_name="test.txt"
# 
# mimemsg = MIMEMultipart()
# mimemsg['From']=mail_from
# mimemsg['To']=mail_to
# mimemsg['Subject']=mail_subject
# mimemsg.attach(MIMEText(mail_body, 'plain'))
# 
# with open(mail_attachment, "rb") as attachment:
#     mimefile = MIMEBase('application', 'octet-stream')
#     mimefile.set_payload((attachment).read())
#     encoders.encode_base64(mimefile)
#     mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
#     mimemsg.attach(mimefile)
#     connection = smtplib.SMTP(host='smtp.office365.com', port=587)
#     connection.starttls()
#     connection.login(username,password)
#     connection.send_message(mimemsg)
#     connection.quit()

