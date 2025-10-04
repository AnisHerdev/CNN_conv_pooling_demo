from flask import Flask, render_template, request
from max_pooling import convert_to_numpy, max_pooling_colored, max_pooling_black_and_white, save_image
import os
app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/convolution",methods=["GET"])
def convolution():
    return render_template("convolution.html")

@app.route("/max_pooling",methods=["GET","POST"])
def max_pooling():
    if request.method == 'POST':
        print("request.files:", request.files)
        print("request.form:", request.form)
        # Check if file part is in request
        if 'image' not in request.files:
            return "No file part in request", 400

        uploaded_file = request.files['image']

        if uploaded_file.filename == '':
            return "No file selected", 400

        # Create uploads directory if it doesn't exist
        uploads_dir = os.path.join("static", "uploads")
        os.makedirs(uploads_dir, exist_ok=True)
        
        # Save the file (you can use a proper path here)
        image_path = os.path.join(uploads_dir, uploaded_file.filename)
        uploaded_file.save(image_path)

        # Get number of iterations from form
        iterations = int(request.form.get('iterations', 1))
        iterations = max(1, min(5, iterations))  # Ensure it's between 1 and 5
        
        # Now process the uploaded image with multiple iterations
        img_array = convert_to_numpy(image_path)
        processed_images = []
        
        current_array = img_array
        for i in range(iterations):
            current_array = max_pooling_colored(current_array)
            # Save each iteration result
            iteration_filename = f"max_pooled_iteration_{i+1}.png"
            save_image(current_array, f"static/images/{iteration_filename}")
            processed_images.append(f"images/{iteration_filename}")
        
        # Create proper URLs for the images
        original_image_url = f"uploads/{uploaded_file.filename}"
        
        return render_template("max_pooling.html", uploaded=True, original_image=original_image_url, 
                             processed_images=processed_images, iterations=iterations)
    return render_template("max_pooling.html",uploaded=False)

@app.route("/min_pooling",methods=["GET"])
def min_pooling():
    return render_template("min_pooling.html")

if __name__ == "__main__":
    app.run()