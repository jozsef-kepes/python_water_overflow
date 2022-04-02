# Coding Challenge 2022
## python_water_overflow

These instructions have been written for OSX terminal users. I've listed the assumptions taken into account below:

- Assumption from the provided image: Glass increment is incorrect and should be j=0, j=1, j=2, j=3
- Assuming K litres can be a float.
- Assuming result will be in millilitres for row i, glass j.
- Assuming that if a glass is outside of the problem space a helpful error should be displayed. Otherwise the result should be assumed 0ml

### To run locally
To start you will need to install the dependencies. To do so run the following command:

    pip install -r requirements.txt

To run the supplied tests (inc. coverage) run the following command in the terminal:

    python -m pytest --cov=. tests/

To run the program use the following command structure:

    python overflow.py [-h] [-v] input row glass

Examples:

    python overflow.py 1.1 1 1

If would like to see verbose output for debugging purpose use the -v flag:

    python overflow.py 15.1 2 3 -v