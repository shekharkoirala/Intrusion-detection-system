import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["0", "udp", "private", "SF", "105", "146", "0 (2)", "0 (3)", "0 (4)", "0 (5)", "0 (6)", "0 (7)", "0 (8)", "0 (9)", "0 (10)", "0 (11)", "0 (12)", "0 (13)", "0 (14)", "0 (15)", "0 (16)", "0 (17)", "1", "1 (2)", "0.00", "0.00 (2)", "0.00 (3)", "0.00 (4)", "1.00", "0.00 (5)", "0.00 (6)", "255", "254", "1.00 (2)", "0.01", "0.00 (7)", "0.00 (8)", "0.00 (9)", "0.00 (10)", "0.00 (11)", "0.00 (12)", "normal."],
                    "Values": [ [ "0", "value", "value", "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "value" ], [ "0", "value", "value", "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "value" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/fccd3f284e94482c867ec9f2b4610cc0/services/06bb6591f6664f5c9e3b3a6a5e9d1144/execute?api-version=2.0&details=true'
api_key = 'unZZEGZn7h1v9KmeIjr6gRsMYXyV8klqeFR5+MOrBugNXRKWR1LDCZro61YtTMmTEHAULigNcTR57frUcdgQlw==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 
