class EmailService:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.smtp_server = 'smtp.naver.com'
        self.smtp_port = 587

    def send_email(self, recipient, subject, body):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        # Validate inputs
        if not all([self.username, self.password, recipient, subject, body]):
            print(self.username, self.password, recipient, subject, body)
            raise ValueError("Missing required email parameters")

        # Ensure body is a string
        body = str(body) if body is not None else ""
        
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body with proper encoding
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            
            # Login with error handling
            try:
                server.login(self.username, self.password)
            except smtplib.SMTPAuthenticationError:
                raise Exception("Failed to authenticate with SMTP server")
            
            # Send the email
            server.send_message(msg)
            print(f"Email sent successfully to {recipient}")
            return True
            
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False
            
        finally:
            try:
                server.quit()
            except:
                pass