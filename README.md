# GameZone Blog

👉 **[Live Site Here](https://gamezone-blog.onrender.com)**

This repository contains a functional Django gaming blog deployed using a decoupled production architecture. Built as a technical project, the application supports article publishing and embedded media via a secure administrative dashboard.

## Technical Milestones Achieved

* **Database Migration:** Transitioned the application backend from a local file-based SQLite database to a live, managed **PostgreSQL** database hosted on **Aiven Cloud** to ensure permanent data persistence.
* **Cloud Deployment:** Configured, optimized, and hosted the application infrastructure on **Render**.
* **Environment Separation & Security:** Utilized `dj-database-url` to handle environment configurations. Production database credentials are completely abstracted into Render environment variables, keeping the GitHub repository secure.
* **Static File Management:** Integrated **WhiteNoise** middleware into the Django pipeline to handle collection and delivery of CSS/JS assets, ensuring proper rendering of production administrative interfaces.
* **Production Security Alignment:** Resolved routing layer obstacles by explicitly configuring `CSRF_TRUSTED_ORIGINS` to authorize secure administrative actions on the live domain.

## Tech Stack
* **Framework:** Python / Django
* **Database:** PostgreSQL (Production) / SQLite (Local Fallback)
* **Hosting Platforms:** Render & Aiven Cloud
* **Asset Pipeline:** WhiteNoise