import argparse
import datetime
import os
import shutil
import time

import img2pdf
import pyautogui
from PIL import Image


class PDFCreator:
    def __init__(
        self, output_dir="output", pdf_name="output.pdf", page=5, direction="right"
    ):
        self.output_dir = output_dir
        self.pdf_name = pdf_name
        self.page = page
        self.direction = direction
        self.tmp_dir = "tmp"
        self.screenshot_interval = 0.1
        self.image_paths = []

        self.validate_direction()

    def validate_direction(self):
        if self.direction not in ["left", "right"]:
            raise ValueError("Invalid direction. Choose 'left' or 'right'.")

    def create_temp_dir(self):
        os.makedirs(self.tmp_dir, exist_ok=True)

    def remove_temp_dir(self):
        shutil.rmtree(self.tmp_dir)

    def take_screenshots(self):
        time.sleep(10)
        for p in range(self.page):
            image_path = os.path.join(self.tmp_dir, f"picture_{p+1:04d}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(image_path)
            self.image_paths.append(image_path)
            pyautogui.keyDown(self.direction)
            pyautogui.keyUp(self.direction)
            time.sleep(self.screenshot_interval)

    def convert_images_to_jpg(self):
        image_list = []
        for image_path in self.image_paths:
            image = Image.open(image_path)
            jpg_image_path = image_path[:-3] + "jpg"
            image.convert("RGB").save(jpg_image_path)
            image_list.append(jpg_image_path)
        return image_list

    def create_pdf(self, image_list):
        os.makedirs(self.output_dir, exist_ok=True)
        pdf_path = os.path.join(self.output_dir, self.pdf_name)
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_list))
        print(f"Finish! PDF saved at: {pdf_path}")

    def run(self):
        self.create_temp_dir()
        self.take_screenshots()
        image_list = self.convert_images_to_jpg()
        self.create_pdf(image_list)
        self.remove_temp_dir()


if __name__ == "__main__":
    default_pdf_name = f"output_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--pdf_name", type=str, default=default_pdf_name, help="Name of PDF file"
    )
    parser.add_argument("-p", "--page", type=int, default=5, help="Number of pages")
    parser.add_argument(
        "-d",
        "--direction",
        type=str,
        default="right",
        help="Direction of page ('left' or 'right')",
    )
    args = parser.parse_args()

    pdf_creator = PDFCreator(
        pdf_name=args.pdf_name, page=args.page, direction=args.direction
    )
    pdf_creator.run()
