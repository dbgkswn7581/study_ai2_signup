from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == "POST":
        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import db

        cred = credentials.Certificate({
            "type": "service_account",
            "project_id": "study-user-data",
            "private_key_id": "78a52a520881c12611be38ae693ef299512008f9",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC4SqCi1ZhQwXcG\n1qTOxXauTNmK+aJC2wd8rhN/9wwI3wVDSUlKOJDSC61pTNGEodP23BqK1yEEKgLn\nGJBlNIdJdjQNO4m5d8sFLT2LOWQVfOl0R2y5SdH6Gu8APmH1VnDaxJdvpqRVqAVY\nbHSmxfDhAlnKUM5M6TM4SZBDqqCLeME2M1YC3gAJHKUETfcU8XHl2s5bq9OSXDmG\ncv5yw6yionMaJpRcBCC2v+tTu1FVyRLxnZA3qOxieKE2dwIjpv2zQAP17hBQUmoP\n/IEFt7VDEufvDGiO+hEbbHXwsWRBqzqkEGCVUoyZgG2Pv2HsTyx7HBCIi1az1SCZ\nBPl1AWsLAgMBAAECggEALbtfJ2lHtep8ZfcHyMPZkqFBbqpJ6Ls/nWH5Ns0QcHcf\ncDYUeNWWonkBXFsStw4NcnnmIEQITmc6dyxyUJr7Y3BwtEPtBlhCyhMS7aSdQHPR\n3ugGg+hcserTGkVgu6fqs28LgUpiB1t9kBbBz8zY3I1fyMPKne1Up4ghw5jo5BLz\n2CqGcprkVeobkBMCBu/fOoE8OpR8ElLSFvc1+6Mw+zhmCkAmTS3Zzstozd+cIRu8\nCDCdj5LqmFDkbi7N2L9uZcTrP4T2VKQOl9RhCZ2uANkWdFTg5OkzgM+GKEHgwGLb\n5TYxw4ZTkraeDbbCTYCMTTPvKmHpIfzhd8wGxXMCEQKBgQDvVqtjExqqvTbDfAKe\nIxcaUds4Ni1Gfake9FCUo18cEc6WDTytBgpOOpxL9RipSJRq6vap/3b0ENsGrz9b\ndNBsfaL5SlqmD07v/ma54AmdkUA8JJAa+Jd2ulSxlpQApKYrVGcdPKRHRqOKMF45\nliGANA+vvPV8SaUzHBkne6J/YwKBgQDFHvJdrQvWnSm/8A07GaX77TZm2M62BuFo\ndkB+49qNKL2N1IqQ4TRxXfGqhpiM7xA2kHDQ90FImHWX5fHOg/BZXz5708KL9lS6\nwFRD0WfkfuoOy/3RjLfyEte3YnkM3/kzxE1t0ht7aPXnmgzU10ZXtCWzMhtgzKoO\nkL9TlIEaOQKBgFbuZ/noansxlr6SQHEn1bBdov5bzz4XTmJL4yjZ3iXX4e1miW9f\nDkczyqlcMMTr89yR014TyCUGKkfXR2/0ke+WAqgBdcNzM/y/rpg848EzjN1LenwR\nZxJcw35tbvx80U5TrdBUwmaRJb1/q/nGqgxi3H+8Zn3qUfKqdgh9Q5x5AoGBAIA2\nb8hUXOXb1aL9PW3acebZ1M+yZ0loUkbC25JtG+NCw4Az5Wj0wkqWozCaWTEZ8b67\n1lVk7XaNi7cgHlaH5NYMqDSceObWcygBHw35b4zkq9KyBka9M4vli5/BEiE4sPtl\nzEMJLUzo6UEaJwxtdVhoWTkj90DP/jB5H6j6Z7qpAoGBALymKFDv0bEgeZW5LbK8\nOagOnrGKMEZYsFjIJtDhH0V2gEwQ5V1VAvVIhbcfrFlUFClg4F3d6xRzjSHC3Djz\nmNg+8ShknqQ3rXJZQSUmTugLJ4r6hhxvzC3hEExocZPH1PW/V3kLBpfxCjNYswsQ\n0xLMSetZv4OdC8mjetmpRJWV\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-w8caj@study-user-data.iam.gserviceaccount.com",
            "client_id": "100809425446768980112",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-w8caj%40study-user-data.iam.gserviceaccount.com"
        })

        firebase_admin.initialize_app(cred,{
            'databaseURL' : 'https://study-user-data-default-rtdb.firebaseio.com/'
        }) 

        result = request.form
        re_dict = request.form.to_dict()
        dir = db.reference('user')
        dir.child(re_dict['nick']).update(re_dict)
        print(request.form.to_dict())
        return render_template('result.html', result = result)

if __name__ == "__main__":
    app.run(debug=True)