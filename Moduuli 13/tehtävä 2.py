from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)



def create_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="salasana",
        database="flight_game",  # Tietokannan nimi
        autocommit=True
    )


def get_airports():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """SELECT iso_country, ident, name, type, latitude_deg, longitude_deg
             FROM airport
             
             ;"""

    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result


@app.route('/kenttä/<icao_koodi>', methods=['GET'])
def hae_lentokentta_info(icao_koodi):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """SELECT iso_country, ident, name, municipality
             FROM airport
             WHERE ident = %s;"""

    cursor.execute(sql, (icao_koodi.upper(),))
    kentta = cursor.fetchone()
    conn.close()

    if kentta:
        return jsonify(kentta)
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)
