from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer(app.config['*67@hjyjhk'],seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
