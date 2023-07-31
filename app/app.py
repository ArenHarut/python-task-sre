from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch, NotFoundError

app = Flask(__name__)
es = Elasticsearch([{'host': 'elasticsearch-master', 'port': 9200, 'scheme': 'http'}])

@app.route('/')
def health_check():
    return "OK"

@app.route('/city', methods=['POST'])
def create_city():
    data = request.get_json()
    city_name = data.get('name')
    population = data.get('population')
    try:
        city = es.get(index='cities', id=city_name)['_source']
        city['population'] = population
    except NotFoundError:
        city = {'name': city_name, 'population': population}
    res = es.index(index='cities', id=city_name, body=city)
    return jsonify({'message': f'City {city_name} has been updated/added'}), 200

@app.route('/city/<name>', methods=['GET'])
def get_city(name):
    try:
        city = es.get(index='cities', id=name)['_source']
        return jsonify({'name': city['name'], 'population': city['population']}), 200
    except NotFoundError:
        return jsonify({'message': 'City not found'}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
