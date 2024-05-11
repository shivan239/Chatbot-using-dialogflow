from  flask import Flask,request,jsonify
#get,post,uddate,delete
app = Flask(__name__)
upi_currency = {'INR': {'USD': 0.012, 'CND': 0.016, 'AUD': 0.018},
                'USD': {'INR': 82.91, 'CND': 1.34, 'AUD': 1.49},
                'CAD': {'INR': 62.09, 'USD': 0.75, 'AUD': 1.12},
                'AUD': {'INR': 55.57, 'USD': 0.67, 'CND': 0.90}}

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']#usd
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    print(data)
    print(source_currency)
    print(amount)
    print(target_currency)
#5000 inr to usd
    to_curDict = upi_currency[source_currency]
    if to_curDict:
        con_value = to_curDict[target_currency]
        con_amount = amount * con_value
    else:
        pass

    print(con_amount)


    response = {
        'fulfillmentText': "{}  {} is {} {}".format(amount,source_currency,con_amount,target_currency)
    }
    print(response['fulfillmentText'])
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

