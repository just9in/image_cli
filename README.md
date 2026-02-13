# Image CLI

WORKFLOW : https://drive.google.com/file/d/1bSwP8cmH3u0BYPETnlOY-jRjBbaAfOCM/view?usp=sharing

A Command Line Interface (CLI) application to:
- register images,
- search for a matching image,
- de-register (delete) registered images.

The project uses a relational database (SQLite) to store image metadata and perceptual hashes.

## What this project demonstrates

- Python CLI development with `argparse`
- Relational database usage with SQLite
- Image similarity matching using perceptual hashing (`pHash`)
- Basic error handling and modular project structure

## Features

- **Image Registration**
  - Save image name, path, and hash in DB
  - Prevent duplicate names
- **Image Search**
  - Accept an input image
  - Compare with stored hashes
  - Return matched image name
- **Image De-registration**
  - Delete a registered image record by name

## Tech Stack

- Python 3
- SQLite (built into Python)
- Pillow
- ImageHash

## Project Structure

```
imageCLI/
├── app.py             # CLI entry point
├── db.py              # Database setup + CRUD operations
├── image_utils.py     # Image hashing helper
├── images/            # Place your input images here
├── requirements.txt
└── README.md
```

> `database.db` is auto-created at runtime and intentionally not committed to GitHub.

## Database Schema

Table: `images`

| Column     | Type      | Description                      |
|------------|-----------|----------------------------------|
| id         | INTEGER   | Primary key (auto increment)     |
| name       | TEXT      | Unique image name                |
| path       | TEXT      | Absolute image file path         |
| hash       | TEXT      | Perceptual hash (pHash)          |
| created_at | TIMESTAMP | Record creation timestamp        |

## Setup

From the `imageCLI` folder:

```bash
pip install -r requirements.txt
```

## Usage

You can run from project root (`CLI interfacing`) or from inside `imageCLI`.

### 1) Show help

```bash
python imageCLI/app.py --help
```

### 2) Register an image

```bash
python imageCLI/app.py register --path dog.jpg --name MyDog
```

### 3) Search for a match

```bash
python imageCLI/app.py search --path dog.jpg
```

### 4) De-register an image

```bash
python imageCLI/app.py delete --name MyDog
```

## Path behavior

- If `--path` is a full/relative valid path, that file is used.
- If only a filename is provided (example: `dog.jpg`), the app looks inside `imageCLI/images/`.

## Matching logic

- Each image is converted into a perceptual hash (`pHash`).
- During search, hash distance is measured using Hamming distance.
- Current threshold: `<= 5` is treated as a match.

## Common errors and fixes

- **"Image file does not exist"**
  - Ensure the file exists in `imageCLI/images/` or provide full path.
- **Duplicate name error**
  - Use a different `--name`.
- **"Image not found" on delete**
  - The provided name is not registered.

## Quick demo commands

```bash
python imageCLI/app.py register --path cat.jpg --name Cat1
python imageCLI/app.py search --path cat.jpg
python imageCLI/app.py delete --name Cat1
```

## Future improvements

- Add a `list` command to show all registered images
- Make similarity threshold configurable
- Add unit tests
- Add Docker support


