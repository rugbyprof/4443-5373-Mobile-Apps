## Q

Can you help me with using token based authentication via react native and fast api? Assume I have a registration and login page and was authenticating passwords using `passlib`. What logic would I need to add to my api and the login process too make token based authentication possible?

## A

Absolutely, Terry! Implementing token-based authentication in a FastAPI application, with React Native as the client, involves a few steps on both the backend and the frontend. We'll use JWT (JSON Web Tokens) for this purpose, as it's a popular choice for token-based authentication due to its compact and self-contained way for securely transmitting information between parties.

### Backend (FastAPI)

1. **Dependencies**: First, ensure you have the necessary dependencies, like `fastapi`, `pydantic`, `passlib`, and `python-jose` for JWT.

2. **User Model and Password Hashing**: Continue using `passlib` for hashing and verifying passwords. No changes needed here from your existing setup.

3. **Token Generation**: Use JWT to generate a token upon successful authentication.

4. **Authentication Endpoint**: Implement login endpoint that authenticates the user and returns a JWT.

5. **Token Verification Middleware**: Create middleware or a dependency to verify the JWT on protected routes.

#### Example Code Snippets

**JWT Token Generation and Verification**:

```python
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)
```

**Login Endpoint**:

```python
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from yourapp import models  # Import your user models
from yourapp.token import create_access_token, verify_password  # Assuming the above functions are in token.py

router = APIRouter()

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

def authenticate_user(username: str, password: str):
    user = models.User.get(username=username)  # Adjust based on your user retrieval logic
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
```

### Frontend (React Native)

1. **Login Page**: Create a login form that captures the username and password.

2. **Token Storage**: Upon successful login, store the JWT returned by the server, typically in AsyncStorage.

3. **Sending Token in Requests**: For subsequent API requests, retrieve the token from storage and include it in the request headers.

#### Example Code Snippets

**Login and Store Token**:

```javascript
import AsyncStorage from '@react-native-async-storage/async-storage';

const loginUser = async ({username, password}) => {
  try {
    const response = await fetch('http://yourapi.com/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `username=${username}&password=${password}`
    });

    const data = await response.json();
    if (data.access_token) {
      await AsyncStorage.setItem('userToken', data.access_token);
    }
  } catch (error) {
    console.error(error);
  }
};
```

**Use Token for Authenticated Requests**:

```javascript
const fetchProtectedData = async () => {
  const token = await AsyncStorage.getItem('userToken');
  try {
    const response = await fetch('http://yourapi.com/protected-route', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};
```

### Summary

On the **backend**, you authenticate the user, generate a JWT if successful, and verify this token on subsequent requests to protected endpoints. On the **frontend** (React Native), you manage the login process, store the received token, and use it for authenticated requests. This setup provides a secure and flexible authentication system for your application.