import click

from app.services.specification_seed import seed_specifications

from app.extensions import db

from app.services.document_seed import seed_documents


def register_commands(app):

    @app.cli.command("create-admin")
    @click.option("--username", prompt=True)
    @click.option("--email", prompt=True)
    @click.option("--full-name", prompt=True)
    @click.option(
        "--password",
        prompt=True,
        hide_input=True,
        confirmation_prompt=True,
    )
    def create_admin(username, email, full_name, password):

        from app.models import Admin

        existing = Admin.query.filter_by(username=username).first()

        if existing:
            click.echo("❌ Admin already exists.")
            return

        admin = Admin(
            username=username,
            email=email,
            full_name=full_name,
        )

        admin.set_password(password)

        db.session.add(admin)
        db.session.commit()

        click.echo("✅ Admin created successfully.")


    @app.cli.command("seed-specifications")
    def seed_specifications_command():

        seed_specifications()

        click.echo("✅ Specification Library seeded successfully.")

    @app.cli.command("seed-documents")
    def seed_documents_command():

        seed_documents()

        click.echo("✅ Document Library seeded successfully.")