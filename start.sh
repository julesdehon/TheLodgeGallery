export PATH="/home/pi/miniconda3/bin/:$PATH"
export PYTHONPATH=$PWD
source activate TheLodgeGallery
python matrixserver/main.py -c matrixserver/config.json