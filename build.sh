echo "Cloning rpi-rgb-led-matrix submodule"
git submodule init
git submodule update
echo "Done"

cd rpi_rgb_led_matrix

echo "Running make build-python"
make build-python
echo "Done"

echo "Running make install-python"
make install-python
echo "Done"