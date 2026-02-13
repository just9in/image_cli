📌 Image CLI – Image Registration, Search & De-registration System
📖 Overview

This is a Command Line Interface (CLI) based Image Management Application built using Python and SQLite (Relational Database).

The system allows users to:

✅ Register an image

🔍 Search for a matching image

❌ De-register (delete) an image

The application uses perceptual image hashing to compare image similarity efficiently.

🏗️ System Architecture
User (CLI Command)
        ↓
Argument Parser (argparse)
        ↓
Image Processing (Pillow + imagehash)
        ↓
SQLite Database
        ↓
Result Output


The application stores only metadata and image hash in the database (not the full image).

🛠️ Technologies Used

Python 3

SQLite (Relational Database)

Pillow (Image Processing)

imagehash (Perceptual Hashing)

argparse (CLI handling)

📂 Project Structure
image_cli/
│
├── app.py           # Main CLI controller
├── db.py            # Database operations
├── image_utils.py   # Image hashing logic
├── database.db      # SQLite database (auto-created)
└── README.md

🗄️ Database Design

Table Name: images

Column	Type	Description
id	INTEGER	Primary Key
name	TEXT	Unique image name
path	TEXT	Image file path
hash	TEXT	Perceptual hash
created_at	TIMESTAMP	Registration time
SQL Schema
CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    path TEXT NOT NULL,
    hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

🖼️ How Image Matching Works

The system uses Perceptual Hashing (pHash).

What is Perceptual Hashing?

Instead of comparing full images pixel by pixel:

The image is converted into a small fingerprint (hash).

The hash represents image structure.

During search, hashes are compared using Hamming Distance.

Hamming Distance

Measures difference between two hashes.

Smaller value = more similar images.

Threshold used: <= 5

⚙️ Installation & Setup
1️⃣ Clone or Download Project
git clone <repository_url>
cd image_cli

2️⃣ Install Dependencies
pip install pillow imagehash


SQLite is included with Python.

🚀 Usage

Run commands from terminal:

📌 Register an Image
python app.py register --path image.jpg --name MyImage


This will:

Generate perceptual hash

Store metadata in database

🔍 Search for an Image
python app.py search --path image.jpg


This will:

Generate hash of input image

Compare with stored hashes

Return matching image name (if found)

❌ Delete an Image
python app.py delete --name MyImage


This removes the image record from the database.

🧠 Key Features

CLI-based interaction

Relational database storage

Efficient similarity search

Unique name constraint

Parameterized SQL queries (prevents SQL injection)

Lightweight & portable system

⚠️ Error Handling

The system handles:

File not found

Duplicate image name

Empty database search

Invalid CLI arguments

Non-existent delete requests

🔧 Possible Improvements

Add indexing on hash column

Store image size & format metadata

Add fuzzy threshold parameter

Upgrade to PostgreSQL for large-scale systems

Add logging support

Store images as BLOB (alternative design)

📊 Scalability Considerations

For large datasets:

Add database indexing

Use binary hash storage

Use Approximate Nearest Neighbor (ANN) search

Move to a more scalable database (PostgreSQL)

🎯 Design Decisions
Why SQLite?

Lightweight

No server required

ACID compliant

Good for small-medium applications

Why Not Store Images in Database?

Increases database size

Slows down queries

File system storage is more efficient for large binary files

Why Use Hashing?

Faster comparison

Memory efficient

Allows similarity matching

🏁 Conclusion

This project demonstrates:

CLI application development

Relational database usage

Image processing fundamentals

Efficient similarity search techniques

Clean modular Python architecture

The system provides a simple but scalable approach to image registration and search using perceptual hashing.