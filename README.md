# Photo-Management-Web-App
# Photo Gallery Site - Munteanu Irina Daniela

This Flask application is a photo gallery site where an authenticated user (the admin) can upload, view, and delete images. It includes routes for authentication and logout, image uploading, gallery viewing, and an "About Me" page.

## Overview

### `app.py`
This is the main file that configures and runs your Flask web application.

- **Index Route**: Manages the main page where all images are displayed, organized by categories. It reads the directory structure and sends the images to the `index.html` template.

### `index.html`
Displays all categories of images and the corresponding images for each category. For each image, a link to the full-size image is created, and its name is displayed. If the user is authenticated as an admin, a button to delete the image appears.

### Login Route
Handles authentication. If the credentials are correct, the user is redirected to the upload page; otherwise, an error message is displayed.

#### `login.html`
Includes a login form with fields for username and password. (Hints for admin credentials are provided.)
- **Admin Username**: `tema`
- **Password**: `tema`

### Logout Route
Manages logging out by removing the admin session and redirecting the user to the main page.

### Upload Route
Handles both the display of the upload form and the processing of the uploaded image. If the user is not authenticated as an admin, they are redirected to the login page. The uploaded image is renamed if a new name is specified, saved in the specified category, and a success message is displayed.

#### `upload.html`
Includes fields for selecting the image file, an optional rename for the image, and a dropdown for selecting the category. The form is configured to send data via POST to the upload route.

### Delete Route
Handles image deletion. Only an authenticated admin can delete images. If the image exists, it is deleted, and a success message is displayed.

### About Route
Displays the "About Me" page, including information about me (my name is Anastasia! 😊), my photography career, and the purpose of this site. It features a customized style for the "About Me" section to enhance visual appeal.

### `base.html`
Serves as the base for all your pages. It contains navigation and a section for displaying flash messages and page-specific content. Each of these templates extends from `base.html`, adding content specific to each page. It includes a navigation menu with links to different sections of the site (Home, About, Gallery, Upload, Login/Logout). It uses Bootstrap for styling and responsive design.

### `utils.py`
A helper module containing useful functions for file processing. The program checks if a file has a permitted extension and saves the uploaded image in the specified directory. If the category directory does not exist, it creates it.

## Directory Structure
Here's an overview of the project directory structure:
/photo-gallery-site │ ├── app.py ├── utils.py │ ├── templates │ ├── base.html │ ├── index.html │ ├── login.html │ ├── upload.html │ └── about.html │ ├── static │ ├── css │ │ └── styles.css │ └── uploads │ └── [uploaded images] │ └── requirements.txt

## Acknowledgments
Thank you for your attention! I hope you enjoy this project. It has been a labor of love, and I truly enjoyed creating it. This was my first assignment where I was allowed to unleash my creativity, and it didn't feel like a chore at all.


