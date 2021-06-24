import smtplib
from email.mime.text import MIMEText

from util            import aes256, hashing
from models          import User
from my_settings     import EMAIL, SECRET


def google_mail(user: User):
    s = smtplib.SMTP(EMAIL['HOST'], EMAIL['PORT'])
    s.starttls()
    s.login(EMAIL['HOST_USER'], EMAIL['HOST_PW'])

    uid    = aes256.AESCipher(bytes(SECRET['AES_KEY'])).encrypt(str(user.id))
    hashed = hashing.create_hash(str(user.id), user.email)

    auth_url = EMAIL['AUTH_URL'] + f'/{uid.decode()}/{hashed.decode()}'

    msg            = MIMEText(auth_url)
    msg['Subject'] = 'Prism39 신규 회원 메일 인증'
    msg['To']      = user.email

    s.sendmail(EMAIL['HOST_USER'], user.email, msg.as_string())
    s.quit()

    return
