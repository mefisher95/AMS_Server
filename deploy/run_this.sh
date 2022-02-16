sudo apt -y update
sudo apt -y upgrade
sudo apt -y install make g++
sudo apt -y install automake build-essential git libboost-dev libboost-thread-dev libntl-dev libsodium-dev libssl-dev libtool m4 python3 texinfo yasm
chmod +x Scripts/*.sh
if [ $# -gt 1 ]
then
    python3 input_randomization.py 100 $1
fi
make shamir_simple
Scripts/setup-online.sh 3 --ip-file-name hosts.txt
if [ $# -gt 1 ]
then
    python3 input_conversion.py 0 $1
fi
Scripts/shamir.sh secure_dna_comparison --ip-file-name hosts.txt
if [ $# -gt 1 ]
then
    python3 input_conversion.py 1 $1
fi
Scripts/shamir.sh secure_dna_comparison2 --ip-file-name hosts.txt
