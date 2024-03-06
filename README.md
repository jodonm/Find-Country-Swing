# Find-Country-Swing

Welcome to the GitHub repository for my Find Country Swing project! This Django-based application is designed to help users discover places to enjoy country swing dancing. Whether you're a seasoned dancer or new to the scene, Find Country Swing aims to connect you with venues, events, and communities dedicated to country swing.

I created this website as a way to for me to learn the Django platform and develop my skills in web design, database managment, and python logic. This was primarily a hobby project but I hope that it is useful for others who enjoy country swing dance.

<img width="1117" alt="Screenshot 2024-03-05 at 11 47 49 PM" src="https://github.com/jodonm/Find-Country-Swing/assets/155393989/40cde9a7-8c41-4b23-bbd5-925df8c51fba">

## Features

- **Venue Discovery**: Users can explore a curated list of places offering country swing dancing, including bars, clubs, and community centers.
- **Interactive Map**: A dynamic map view that allows users to visually browse country swing venues in their vicinity or specific areas.
- **User Input**: Accepts user input for new locations that can later be added.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:

- Python (3.8 or newer)
- Virtualenv (optional, but recommended for creating isolated Python environments, this also simplifies the deploying process)

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/find-country-swing.git
cd find-country-swing
```

2. **Set Up a Virtual Environment** (Optional)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Environment Variables**

Create a `.env` file in the root directory and populate it with the necessary environment variables:

```plaintext
SECRET_KEY=your_secret_key_here
DEBUG=True  # Set to False in production
DJANGO_SETTINGS_MODULE=swing_dance_directory.settings
```

5. **Database Migrations**

```bash
python manage.py migrate
```

6. **Run the Development Server**

```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/dancing_places/map` in your browser to view the app.

## Deployment

Refer to the platform-specific documentation for deploying Django applications. For example, when deploying to Railway, ensure you set the required environment variables in the Railway app settings dashboard, including `DJANGO_SETTINGS_MODULE`, `SECRET_KEY`, and `DATABASE_URL`.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


---

 
