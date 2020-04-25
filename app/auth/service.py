import bcrypt, uuid

from app import db

from ..user import User

class AuthService:
    def hashPassword(self, password):
        try:
            hashedPassword = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
            decodedHashedPassword = hashedPassword.decode('utf8')
            return decodedHashedPassword
        except:
            raise Exception('Error hashing password')

    def checkPassword(self, password, passwordHash):
        try:
            isSamePassword = bcrypt.checkpw(password.encode('utf8'), passwordHash.encode('utf8'))
            return isSamePassword
        except:
            raise Exception('Error checking password')
    
    @staticmethod
    def generateRandomSessionId():
        return uuid.uuid4()
    
    def loginUser(self, email, password):
        try:
            foundUser = User.query.filter_by(email=email).first()
            if foundUser is None:
                raise Exception('No user with those credentials')
        
            userPassword = foundUser.password
            passwordHash = self.hashPassword(userPassword)
            isSamePassword = self.checkPassword(password, passwordHash)

            if isSamePassword is False:
                raise Exception('Wrong password for user')
            
            return
        except Exception as error:
            raise Exception('Error logging in user', error) 

    def registerUser(self, email, username, password):
        try:
            password = self.hashPassword(password)
            newUser = User(email, username, password)

            db.session.add(newUser)
            db.session.commit()

        except Exception as error:
            raise Exception('Error registering user', error)