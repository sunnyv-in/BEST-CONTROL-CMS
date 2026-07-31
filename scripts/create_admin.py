import getpass

from app import create_app
from app.extensions import db
from app.models import Admin


def main():
    app = create_app()

    with app.app_context():

        print("=" * 50)
        print("BEST CONTROL CMS - Create Admin User")
        print("=" * 50)

        username = input("Username: ").strip()
        email = input("Email: ").strip()
        full_name = input("Full Name: ").strip()

        while True:
            password = getpass.getpass("Password: ")
            confirm_password = getpass.getpass("Confirm Password: ")

            if password != confirm_password:
                print("\n❌ Passwords do not match. Try again.\n")
                continue

            if len(password) < 8:
                print("\n❌ Password must be at least 8 characters.\n")
                continue

            break

        if Admin.query.filter_by(username=username).first():
            print("\n❌ Username already exists.")
            return

        if Admin.query.filter_by(email=email).first():
            print("\n❌ Email already exists.")
            return

        admin = Admin(
            username=username,
            email=email,
            full_name=full_name,
        )

        admin.set_password(password)

        db.session.add(admin)
        db.session.commit()

        print("\n✅ Admin user created successfully!")
        print(f"Username: {username}")


if __name__ == "__main__":
    main()