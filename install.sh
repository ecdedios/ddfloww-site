# Script used for deployment with cods (https://github.com/zgulde/cods)
set -e

cd $SITE_DIR

echo "[install.sh] (re-)creating the venv"
rm -rf env
python3 -m venv env
echo '[install.sh] Activating venv and installing dependencies'
source env/bin/activate
python3 -m pip install -r requirements.txt