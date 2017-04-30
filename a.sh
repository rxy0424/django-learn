# example location - can be customized
export TORCH_ROOT=~/torch

git clone https://github.com/torch/distro.git $TORCH_ROOT --recursive
cd $TORCH_ROOT
./install-deps
./install.sh -b
source ~/.bashrc
