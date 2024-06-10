brugere = ["Alice", "Bob", "Charlie", "David", "Erika"]
brugere_data = {user: "kodeord" for user in brugere}  
kode = []

def login(username, password):
    if username in brugere_data:
        if brugere_data[username] == password:
            print(f"{username} er logget ind")
            return username, password
        else:
            print("Forkert kode, prøv igen")
    else:
        print("Bruger findes ikke")
    return None, None

def logout(username, session):
    if session.get("username") == username:
        session.pop("username")
        print(f"{username} er logget ud")
    else:
        print(f"{username} er ikke logget ind")

def check_session(session):
    if "username" in session:
        print(f"{session['username']} er logget ind")
    else:
        print("Ingen bruger er logget ind")

if __name__ == "__main__":

    session = {}
    username, password = login("Alice", "password")
    if username:
        session["username"] = username
    
    check_session(session)
    logout(username, session)
    check_session(session)
