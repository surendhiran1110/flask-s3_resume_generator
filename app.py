from flask import Flask, render_template, request, send_file
import boto3
from datetime import datetime

app = Flask(__name__)

# AWS S3 configuration
S3_BUCKET = 'bucket name'
S3_ACCESS_KEY = 'your access key'
S3_SECRET_KEY = 'your secret key'

# Configure boto3 to interact with S3
s3 = boto3.client(
    's3',
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY
)

uploaded_file_key = None  # Global variable to store the S3 key of the uploaded file

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        objective = request.form['objective']
        education_10th_percentage = request.form['10th_percentage']
        education_12th_percentage = request.form['12th_percentage']
        education_cgpa = request.form['cgpa']
        work_experience = request.form['work_experience']
        skills = request.form['skills']
        
        # Create content for the resume
        resume_content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}\n\n"
        resume_content += f"Objective:\n{objective}\n\n"
        resume_content += f"Education:\n10th Percentage: {education_10th_percentage}%\n12th Percentage: {education_12th_percentage}%\nCGPA: {education_cgpa}\n\n"
        resume_content += f"Work Experience:\n{work_experience}\n\n"
        resume_content += f"Skills:\n{skills}"
        
        # Upload file to S3
        global uploaded_file_key
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{name}_{timestamp}_resume.txt"
        s3.put_object(Body=resume_content, Bucket=S3_BUCKET, Key=filename)
        uploaded_file_key = filename
        
        return render_template('success.html', filename=filename)
    return render_template('resume_upload.html')


@app.route('/download', methods=['GET'])
def download():
    global uploaded_file_key
    if uploaded_file_key:
        obj = s3.get_object(Bucket=S3_BUCKET, Key=uploaded_file_key)
        return send_file(obj['Body'], as_attachment=True, attachment_filename=uploaded_file_key)
    return "No file uploaded yet."



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
