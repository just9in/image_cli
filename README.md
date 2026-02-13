# Image CLI – Image Registration, Search & De-registration

CLI-based image management app using Python and SQLite.

## Features
- Register an image with a name
- Search a matching image by perceptual hash
- De-register (delete) an image by name

## Tech Stack
- Python 3
- SQLite
- Pillow
- imagehash
- argparse

## Project Structure
- `app.py` – CLI entry point
- `db.py` – DB create/read/delete logic
- `image_utils.py` – image hashing logic
- `images/` – input images folder
- `database.db` – SQLite DB (auto-created)

## Setup
```bash
pip install -r requirements.txt
```

## Run (from workspace root)
```bash
python imageCLI/app.py --help
python imageCLI/app.py register --path dog.jpg --name MyDog
python imageCLI/app.py search --path dog.jpg
python imageCLI/app.py delete --name MyDog
```

## Notes
- If you pass only file name (like `dog.jpg`), app checks `imageCLI/images/` automatically.
- Matching uses pHash + Hamming distance threshold (`<= 5`).
