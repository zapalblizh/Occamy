# Occamy

Occamy is a magical and fantastic application made to compress your images.

[Link to my Video](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Origin of Occamy

At the start, I looked through the final projects that were submitted by CS50 students,
and I found that there were many similar things developed, such as a weather app or a simple
website for a restaurant or business etc. I wanted to do something different, and so I decided on
making an image compression application.

When I started working on the project, I started out on creating the skeleton of my project,
at first I was really lost as for the structure I should have, but thanks to other projects 
I've explored and the AI assistant in Webstorm, I was able to create the structure.

Next, I created a basic rough design of the index.html, borrowing the design of the header and footer from tailwindcss
and the main content was made with just a simple form to upload and a button to submit.

After that, I started working on the backend, via Flask on Python, however, 
this proved to be harder than expected as it was my first time using Flask.

Once my Flask local server was setup, I was able to experiment with how I would compress my images. 
I found a library called Pillow for Python, which compresses the image, seems pretty simple enough, but the thing is 
I wanted the images to display on the template homepage.

Via AlpineJS, I was able to create many functions, such as fileInputChanged and handleDrop 
(implemented later to allow drag and drop image) to store the image submitted.

Said functions also required many variables, all to display what is needed at each stage. 
Since I have experience with AlpineJS, this was pretty simple.

The biggest challenge for me, was to create the submit function, rather not the function itself, 
but the backend for the post request using axios that I setup to retrieve the compressed image.

After a lot of tinkering, trial and error, I was able to send the user's image to the backend via `/api/upload` 
and retrieve a json object with the data required for the displaying of both user's image and compressed image 
while compressing the image perfectly.

I then made a simple download AlpineJS function for the download button, since the compressed image is already stored on the browser's side to download the image.

Then I realised I did not really have that much security set up for the uploading of the image. 
So I used the secure_filename function along with a name randomiser for the uploaded image's name.

Lastly, I cleaned up my code, and implemented loading for my submit button so that the user won't panic when the compressing occurs too fast

The final result ended up being an Image compressor that 
accepts up to 10MB for file size, and accepts only PNG, JPG and JPEG image file extensions.

This can always be edited to accept other file types and sizes, but the purpose of this project 
was to make it simple and easy to use.

After working hard on this project, I'm very satisfied with the result, and I hope you
will feel inspired to create a CS50 final project that is just as unique or better than this.


Fun fact: The name Occamy is inspired by the magical creature from Fantastic Beasts and where to find them.
The snake could shrink and grow to fit the available space.

## Setup

1) Clone the repo and CD into it
2) Install all required python libraries via `pip3 install -r requirements.txt`
3) For local development, run `start:serve` or `python3 -m flask run` to start the server

## Tech Stack (ATF: AlpineJS, TailwindCSS, Flask)
- [AlpineJS](https://alpinejs.dev/): Alpine is a rugged, minimal tool for composing behavior directly in your markup. Think of it like jQuery for the modern web.
- [TailwindCSS](https://tailwindcss.com/): A utility-first CSS framework.
- [Flask](https://flask.palletsprojects.com/en/3.0.x/): Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

## Site Structure
- **_app_**: contains all the application's templating and backend REST API logic
  - **_app/static_**: includes the images directory (where all uploaded and compressed images reside), css and javascript.
    - **_app/static/images_**: includes all images uploaded and downloaded by the user along with header image.
      - **_app/static/images/uploads_**: where uploaded images are stored.
      - **_app/static/images/compressed_**: where compressed images are stored.
  - **_app/templates_**: includes all the HTML templates for the application. In this case, just the index.html template.
  - **_app/\_\_init\_\_.py_**: initializes the Flask application and sets up the routes, such as uploading and returning compressed image.

## Dotenv

1) Create `.env` file in the root of the project
2) Add `FLASK_ENV=development` variable into your `.env` file