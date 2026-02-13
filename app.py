import argparse
import os
import sqlite3
from db import init_db, insert_image, get_all_images, delete_image
from image_utils import generate_hash
import imagehash

BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "images")


def resolve_image_path(path_value):
    if os.path.exists(path_value):
        return path_value

    candidate = os.path.join(IMAGES_DIR, path_value)
    if os.path.exists(candidate):
        return candidate

    return None

def register_image(args):
    image_path = resolve_image_path(args.path)
    if not image_path:  #checking if file exists or no?
        print("Image file does not exist.")
        print(f"Put your image in: {IMAGES_DIR}")
        return

    hash_value = generate_hash(image_path)

    try:
        insert_image(args.name, os.path.abspath(image_path), hash_value)
        print(f"Image '{args.name}' image ADDED :) ")
    except sqlite3.IntegrityError:
        print("sorry but image already exists")
    except Exception as e:
        print("error:", e)


def search_image(args):                 #to check if image is there or no
    image_path = resolve_image_path(args.path)
    if not image_path:
        print("image doesnt exists")
        print(f"Put your image in: {IMAGES_DIR}")
        return

    search_hash = generate_hash(image_path)
    images = get_all_images()

    if not images:                              #case 2 db is empty
        print("no images in DB right now")
        return

    for img in images:
        db_hash = img[3]
        distance = imagehash.hex_to_hash(search_hash) - imagehash.hex_to_hash(db_hash)

        if distance <= 5:  # threshold
            print(f"match found! Image name: {img[1]}")
            return

    print("no matching image found")


def remove_image(args):
    deleted = delete_image(args.name)
    if deleted:
        print("Image deleted successfully.")
    else:
        print("Image not found.")


def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    init_db()

    parser = argparse.ArgumentParser(description="Image CLI Application")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Register
    register_parser = subparsers.add_parser("register")
    register_parser.add_argument("--path", required=True)
    register_parser.add_argument("--name", required=True)

    # Search
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("--path", required=True)

    # Delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--name", required=True)

    args = parser.parse_args()

    if args.command == "register":
        register_image(args)
    elif args.command == "search":
        search_image(args)
    elif args.command == "delete":
        remove_image(args)


if __name__ == "__main__":
    main()