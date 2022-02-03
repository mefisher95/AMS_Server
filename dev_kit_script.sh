sudo apt clean  
sudo apt update -y
sudo apt upgrade -y

sudo apt install -y g++
g++ server.cpp -o Server.out
g++ client.cpp -o Client.out

cd ~
git clone https://github.com/data61/MP-SPDZ.git
apt-get install -Y automake build-essential git libboost-dev libboost-thread-dev libntl-dev libsodium-dev libssl-dev libtool m4 python3 texinfo yasm 
cd AMS_Server
