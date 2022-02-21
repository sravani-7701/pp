# Package import
import datetime
import os
from copy_service.outputfile import outputfile

from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request,send_from_directory
# initialise app

app = Flask(__name__,template_folder='copy_service/templates')
# decorator for homepage
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html',PageTitle="Landing page")
# route for form submission
@app.route('/',methods=['POST'])
def merge():
    #retrieving the form data
    uploaded_file1 = request.files['file1']
    uploaded_file2 = request.files['file2']
    uploaded_file3 = request.files['file3']
    if uploaded_file1.filename != '' and uploaded_file2.filename != '' and uploaded_file3.filename != '':
        tag=request.form['tag']
        # calling the outputfile function which merges the input files
        csv = outputfile(uploaded_file1, uploaded_file2, uploaded_file3,tag)
        # if a value error occurs csv type would be string, so we return the response status as 400
        if type(csv)==str:
            response=make_response();
            response.status=400;
            return response;
        # if type of csv is not a string return csv file
        csvfile = csv.to_csv()
        return Response(csvfile,200,content_type="text/csv");  
    # if user does'nt select a file
    else:
        response=make_response();
        response.status=400;
        return response;
if __name__ == '__main__':
    app.run(debug=True, port=5000)
 