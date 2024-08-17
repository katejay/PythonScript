import paramiko
import pymysql

# SSH Configuration
ssh_host = '127.0 0.1'
ssh_port = 22
ssh_username = 'Username'
ssh_password = 'Password'

# Database Configuration
db_host = '127.0.0.1'
db_port = 3310
db_username = 'DBUserName'
db_password = 'DBPassword'
db_name = 'DBName'

# User ID List
user_ids = {
    1: ("Jay", 1234),
    2: ("Test", 1235),
    3: ("User", 1236),
}

# Display the list of users
def display_user_list():
    print("Select a user by number (1-3):")
    for key, (name, _) in user_ids.items():
        print(f"{key}. {name}")

# Get user choice and confirmation
def get_user_selection():
    while True:
        display_user_list()
        try:
            choice = int(input("Enter the number corresponding to the user: "))
            if choice not in user_ids:
                print("Invalid choice. Please select a number between 1 and 16.")
                continue
            
            selected_name, selected_user_id = user_ids[choice]
            print(f"You selected: {selected_name}'s User ID: {selected_user_id}")
            
            confirmation = input("Do you want to proceed with this user ID? (Y/N): ").strip().upper()
            if confirmation == 'Y':
                return selected_user_id
            elif confirmation == 'N':
                print("Reselecting user...")
                continue
            else:
                print("Invalid input. Please enter Y or N.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get prod_code choice
def get_prod_code_selection():
    while True:
        print("\nSelect a product code:")
        print("1. DS")
        print("2. MS")
        print("3. Both")
        
        try:
            choice = int(input("Enter the number corresponding to the product code: "))
            if choice == 1:
                return 'DS'
            elif choice == 2:
                return 'MS'
            elif choice == 3:
                return 'Both'
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Set up SSH tunnel
def setup_ssh_tunnel():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        print("Connecting to SSH server...")
        ssh_client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)
        print("SSH connection established.")
        
        print("Setting up port forwarding...")
        transport = ssh_client.get_transport()
        transport.request_port_forward('127.0.0.1', 3310)
        print("Port forwarding set up.")
        
        return ssh_client
    except paramiko.AuthenticationException as e:
        print(f"Authentication failed: {e}")
        raise
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
        raise

# Execute DELETE queries based on prod_code
def delete_user_data(user_id, prod_code):
    try:
        connection = pymysql.connect(
            host=db_host,
            port=db_port,
            user=db_username,
            password=db_password,
            database=db_name
        )

        # Replace db.tablename with actual db name table name
        with connection.cursor() as cursor:
            if prod_code == 'Both':
                delete_queries = [
                    f"DELETE FROM db.tablename WHERE usr_id={user_id};",
                    f"DELETE FROM db.tablename WHERE usr_id={user_id};",
                    f"DELETE FROM db.tablename WHERE usr_id={user_id};"
                ]
            else:
                delete_queries = [
                    f"DELETE FROM db.tablename WHERE usr_id={user_id} AND prod_code='{prod_code}';",
                    f"DELETE FROM db.tablename WHERE usr_id={user_id} AND prod_code='{prod_code}';",
                    f"DELETE FROM db.tablename WHERE usr_id={user_id} AND prod_code='{prod_code}';"
                ]
            
            # Execute all DELETE queries
            for query in delete_queries:
                print(f"Executing query: {query}")
                cursor.execute(query)
                connection.commit()
                print(f"{user_id} user's data deleted successfully.")
            
    except pymysql.MySQLError as e:
        print(f"MySQL error: {e}")
        raise
    finally:
        connection.close()

# Main script execution
def main():
    ssh_client = None
    try:
        ssh_client = setup_ssh_tunnel()
        user_id = get_user_selection()
        prod_code = get_prod_code_selection()
        delete_user_data(user_id, prod_code)
    finally:
        if ssh_client:
            ssh_client.close()
            print("SSH connection closed.")

if __name__ == "__main__":
    main()