from flask import Flask, request, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<numba>')
def alkuluku(numba):



    try:

        alkis = int(numba)
        if alkis <= 1:
            print(f"{alkis} is not a prime number.")
            is_prime = False
        elif alkis <= 3:
            print(f"{alkis} is a prime number.")
            is_prime = True
        elif alkis % 2 == 0 or alkis % 3 == 0:
            print(f"{alkis} is not a prime number.")
            is_prime = False
        else:
            tru = True
            i = 5
            is_prime = True
            for i in range(2, alkis):

                if (alkis % i == 0):
                    print(f"{alkis} is not a prime number.")
                    tru = False
                    break
            if tru == True:
                print(f"{alkis} is a prime number.")

        answa = {
            "this is thy number" : alkis,
            "this number is a prime" : is_prime,
        }
        statsucode = 200
    except ValueError:
        statsucode = 400
        answa = {
            "status": statsucode,
            "teksti": "Virheellinen yhteenlaskettava"
        }
    answa = json.dumps(answa)
    return Response(response=answa, status=statsucode, mimetype="application/json")



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
    #