hosts = open('hosts','r')
text = hosts.read()
if "#127" not in text:
    text = text.replace("127", "#127")
else:
    text = text.replace("#127", "127")
hosts.close()
hosts = open('hosts','w')
hosts.write(text)