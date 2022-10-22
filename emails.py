import smtplib
import emails_config

"""config_email = "macoumbaguedelmbodj@gmail.com"
config_password ="mkbhmtwfofjtajlf"
config_server = "smtp.gmail.com"
config_server_port = 587"""


def envoyer_email(email_destinataire, message):
    serveur_mail = smtplib.SMTP(emails_config.config_server, emails_config.config_server_port)
    serveur_mail.starttls()
    serveur_mail.login(emails_config.config_email, emails_config.config_password)
    serveur_mail.sendmail(emails_config.config_email, email_destinataire, message)
    serveur_mail.quit()


envoyer_email("macoumbaguedelmbodj@outlook.com", "Salut")
