import postgres
import click

# @click.command()
# @click.option('--username', help='Username')
# @click.option('--password', prompt='Your password that will be stored as text',
#               help='Any password you wish it is unsafe anyway')
def create_user(username:str,password:str,groupename:str):
    connection=postgres.get_connection()
    cur=connection.cursor()
    cur.execute("INSERT INTO users (username,password,groupid) VALUES (%s,%s, (SELECT groupid FROM usergroups WHERE groupname=%s))",(username,password,groupename))
    success=connection.commit()
    print(success)
    connection.close()
    return True

def delete_user(username):
    connection=postgres.get_connection()
    cur=connection.cursor()
    cur.execute("DELETE FROM users WHERE username=%s",(username,))
    connection.commit()
    connection.close()
    return True


# if __name__ == '__main__':
#     create_user()