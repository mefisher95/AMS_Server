sudo apt clean  
sudo apt update -y
sudo apt upgrade -y

sudo apt install -y g++
g++ server.cpp -o Server.out
g++ client.cpp -o Client.out
