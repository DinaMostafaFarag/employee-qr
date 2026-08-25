"""
Generate a permanent QR code for each employee in data/employees.json.

Each QR code points to:
    {BASE_URL}/?id={employee_id}

Usage:
    pip install qrcode[pil]
    python generate_qr.py
"""

import json
import os
import qrcode

# ---------------------------------------------------------------------------
# EDIT THIS after you publish the repo on GitHub Pages.
# Format: https://<your-github-username>.github.io/<repo-name>
# Example: https://nawal-ebc.github.io/employee-qr
# ---------------------------------------------------------------------------
BASE_URL = "https://YOUR-USERNAME.github.io/employee-qr"

DATA_FILE = os.path.join("data", "employees.json")
OUTPUT_DIR = "qrcodes"


def main():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        employees = json.load(f)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for emp_id, emp in employees.items():
        url = f"{BASE_URL}/?id={emp_id}"

        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=12,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="#14213B", back_color="white")

        safe_name = emp.get("name", emp_id).replace(" ", "_")
        out_path = os.path.join(OUTPUT_DIR, f"{emp_id}_{safe_name}.png")
        img.save(out_path)

        print(f"Generated: {out_path}  ->  {url}")

    print("\nDone. If BASE_URL still contains 'YOUR-USERNAME', "
          "edit this file with your real GitHub Pages link and re-run.")


if __name__ == "__main__":
    main()
