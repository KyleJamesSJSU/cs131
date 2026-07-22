import socket, platform, cowsay

# construct string
text = "hostname=" + socket.gethostname() + "\npython=" + platform.python_version() + "\ncowsay=" + cowsay.__version__

# say the line
cowsay.cow(text)
