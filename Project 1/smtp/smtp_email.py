from socket import *
import base64
import time
import ssl


msg = "\r\n Mitra Sasanka Darbha Computer Networks!"
endmsg = "\r\n.\r\n"
mailserver = ("smtp.gmail.com",465) #Fill in start #Fill in end
#def getSSLSocket():
#    return ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), ssl_version=ssl.PROTOCOL_SSLv23)
clientSocket = socket(AF_INET, SOCK_STREAM)
#ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_TLSv1)
clientSocketSSL = ssl.wrap_socket(clientSocket)
clientSocketSSL.connect(mailserver)
recv = clientSocketSSL.recv(1024)
recv = recv.decode()
print("Message after connection request:" + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
    ## Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocketSSL.send(heloCommand.encode())
recv1 = clientSocketSSL.recv(1024)
recv1 = recv1.decode()
print("Message after EHLO command:" + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

#Info for username and password
username = "sasanka.msd97@gmail.com"
password = "Sasanka1997"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocketSSL.send(authMsg)
recv_auth = clientSocketSSL.recv(1024)
print(recv_auth.decode())

mailFrom = "MAIL FROM:<sasanka.msd97@gmail.com>\r\n"
clientSocketSSL.send(mailFrom.encode())
recv2 = clientSocketSSL.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: "+recv2)
rcptTo = "RCPT TO:<sasanka.msd97@gmail.com>\r\n"
clientSocketSSL.send(rcptTo.encode())
recv3 = clientSocketSSL.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: "+recv3)
data = "DATA\r\n"
clientSocketSSL.send(data.encode())
recv4 = clientSocketSSL.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)
subject = "Subject: testing my client\r\n\r\n"
clientSocketSSL.send(subject.encode())
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
date = date + "\r\n\r\n"
clientSocketSSL.send(date.encode())
clientSocketSSL.send(msg.encode())
clientSocketSSL.send(endmsg.encode())
recv_msg = clientSocketSSL.recv(1024)
print("Response after sending message body:"+recv_msg.decode())
quit = "QUIT\r\n"
clientSocketSSL.send(quit.encode())
recv5 = clientSocketSSL.recv(1024)
print(recv5.decode())
clientSocketSSL.close()

clientSocket.close()
