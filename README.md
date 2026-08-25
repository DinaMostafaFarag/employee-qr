[README (2).md](https://github.com/user-attachments/files/31435951/README.2.md)
# Employee QR — Digital Business Card

A free, permanent digital business card system. Each employee gets one QR
code. Scanning it opens a styled profile page showing their name, position,
company, and one-tap contact links (call, WhatsApp, email, website, save to
contacts).

## Project structure

```
employee-qr/
├── index.html          # The card page (reads ?id=... from the URL)
├── data/
│   └── employees.json  # Employee records — edit this to add/update people
├── generate_qr.py       # Generates a QR code per employee
├── qrcodes/              # Output folder for generated QR images
└── README.md
```

## 1. Add your employees

Open `data/employees.json` and add one entry per employee. Use any ID you like
(e.g. an employee number) as the key:

```json
{
  "10001": {
    "id": "10001",
    "name": "Nawal Al Abri",
    "position": "Training and Public Relation Consultant",
    "company": "European Business Center for Training & Development",
    "companyTagline": "Training, Human Resources Empower, Consultations",
    "mobile": "+968 96328989",
    "email": "social@ebctraining.net",
    "website": "www.ebctraining.net",
    "photo": ""
  }
}
```

## 2. Push this project to your `employee-qr` repository

From this folder:

```bash
git init
git add .
git commit -m "Initial employee QR project"
git branch -M main
git remote add origin https://github.com/<YOUR-USERNAME>/employee-qr.git
git push -u origin main
```

(Replace `<YOUR-USERNAME>` with your actual GitHub username. If you created
the repo on github.com already, use the remote URL it gave you instead.)

## 3. Turn on GitHub Pages

1. On GitHub, open your `employee-qr` repository.
2. Go to **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Branch: `main`, folder: `/ (root)`. Click **Save**.
5. Wait 1–2 minutes. GitHub will show your live URL, something like:

   ```
   https://<YOUR-USERNAME>.github.io/employee-qr/
   ```

## 4. Point the QR generator at your real link

Open `generate_qr.py` and edit this line with your real GitHub Pages URL from
step 3:

```python
BASE_URL = "https://YOUR-USERNAME.github.io/employee-qr"
```

## 5. Generate the final QR codes

```bash
pip install qrcode[pil]
python generate_qr.py
```

This creates one PNG per employee inside `qrcodes/`, e.g.
`10001_Nawal_Al_Abri.png`. Each QR code permanently points to:

```
https://<YOUR-USERNAME>.github.io/employee-qr/?id=10001
```

Print or share that image — scanning it will always open that employee's
card, and you can update their info anytime by editing
`data/employees.json` and pushing the change (no need to regenerate the QR).

## Notes

- The card page has no backend — it's pure HTML/CSS/JS, so hosting on GitHub
  Pages is completely free.
- To update someone's info later, just edit their entry in
  `data/employees.json` and push. The existing QR code keeps working.
- To remove an employee's access, delete their entry from `employees.json`
  (their old QR code will then show "No profile found").
