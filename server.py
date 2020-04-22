from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
 
non_ppc_people = [
    "Phyllis",
    "Dwight",
    "Oscar",
    "Creed",
    "Pam",
    "Jim",
    "Stanley",
    "Michael",
    "Kevin",
    "Kelly"
]

ppc_people = [ 
    "Angela"
]

@app.route('/')
def ppc(name=None):
   return render_template('ppc.html', non_ppc=non_ppc_people, ppc=ppc_people)

@app.route('/move_to_ppc', methods=['GET', 'POST'])
def move_to_ppc():
    global non_ppc_people
    global ppc_people

    json_data = request.get_json()   
    person_to_move = json_data["name"]

    ppc_people.append(person_to_move)
    non_ppc_people.remove(person_to_move)

    return jsonify(non_ppc_people = non_ppc_people, ppc_people=ppc_people)

@app.route('/move_to_non_ppc', methods=['GET', 'POST'])
def move_to_non_ppc():
    global non_ppc_people
    global ppc_people

    json_data = request.get_json()
    person_to_move = json_data["name"]

    non_ppc_people.append(person_to_move)
    ppc_people.remove(person_to_move)

    return jsonify(non_ppc_people = non_ppc_people, ppc_people=ppc_people)

if __name__ == '__main__':
   app.run(debug = True)




