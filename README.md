Reference API server of SMART Genomics

## How to use it
* Change the application settings in `config.py`, including what SQL database you would like to use.
* Optional: load FHIR's spec with the script `load_spec.py`.
You don't need to do this unless you have your own FHIR spec.
* Setup database and load sample data with
```
# note that this will also clear the database
$ python fhir_genomics.py reload
```
* Run the server locally with
```
$ python fhir_genomics.py
```
* The WSGI objct is located in server.py, which you can use like this
```
$ gunicorn server:app 
```
