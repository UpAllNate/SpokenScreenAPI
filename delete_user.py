import postgres
import click

@click.command()
@click.option('--username', help='Username')

def delete_user(username):
    connection=postgres.get_connection()
    cur=connection.cursor()
    cur.execute("DELETE FROM users WHERE username=%s",(username,))
    connection.commit()


if __name__ == '__main__':
    delete_user()