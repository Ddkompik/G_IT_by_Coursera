import logging
from email.message import EmailMessage
import os
import mimetypes
import smtplib
import ssl

def loggin_check() -> None:
    logging.basicConfig(filename="C:\\Users\\dasha\\Documents\\CODE\\GitHub\\G_IT_by_Coursera\\AutoPython\\basic.log",
                        level=logging.DEBUG,
                        encoding="utf-8",
                        format = '%(asctime)s %(levelname)s - %(funcName)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    logging.debug("This is a DEBUG message.")
    logging.info("This is an INFO message.")
    logging.warning("This is a WARNING message.")
    logging.error("This is an ERROR message.")
    logging.critical("This is a CRITICAL message.")

def handlers() -> None:
    stream_log = logging.getLogger("stream_log")
    stream_log.setLevel(logging.DEBUG)
    stream_log.handlers = []
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_log.addHandler(stream_handler)
    stream_log.info("This is Info")
    log = logging.getLogger(__name__)

def email_check():
    '''Use EmailMessage Class to Use for Sender and Receiver With Etc Info And Put in a Body For Email'''
    message = EmailMessage()
    sender = "user_0@gmail.com"
    #not a good style to do like this
    login = ""
    recepient = "user_1@gmail.com"

    message["From"] = sender
    message["To"] = recepient
    message["Subject"] = "Greetings from {} to {}".format(sender, recepient)
    body = """Hello, dear Friend! Is that your mail, correct? {}""".format(recepient)
    message.set_content(body)

    '''Here We Use Mime lib to recognize the type of file'''
    attachment_path = "C:\\Users\\dasha\\Documents\\CODE\\GitHub\\G_IT_by_Coursera\\AutoPython\\owl.png"
    attachment_filename = os.path.basename(attachment_path)
    mime_types, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_types.split("/", 1)
    print(mime_type, mime_subtype)

    '''Use The PNG File To Next Sending Level, But Befor This We need to Convert it With Mimmom in Text'''
    with open(attachment_path, "rb") as file:
        message.add_attachment(file.read(), 
                               maintype = mime_type,
                               subtype = mime_subtype, 
                               filename = os.path.basename(attachment_path))
        
    '''Use the txt file and put all Message Info to TXT'''
    with open("C:\\Users\\dasha\\Documents\\CODE\\GitHub\\G_IT_by_Coursera\\AutoPython\\text_for_file_check.txt", "w+", buffering=16_384) as file:
        for line in str(message):
            file.write(line)

    '''Trying to Send this message to sender with SMTP lib & localhost'''
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp_server:
        smtp_server.login(sender, login) #use env?
        smtp_server.send_message(message)
        
if __name__ == "__main__":
    # loggin_check()
    # handlers()
    '''works if you have the Admin Console Google Account'''
    # email_check()