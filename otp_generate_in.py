# There are several ways to generate a One-Time Password (OTP) in Python. Below are three different methods:
# 1 using the random module for a simple numeric OTP,
# 2 using the secrets module for a more secure alphanumeric OTP,


# Generate a 6-digit OTP using

import random

def generate_otp():
    return random.randint(100000, 999999)

otp = generate_otp()
print("Your OTP is:", otp)

# # Generate an alphanumeric OTP using 

import secrets
import string

def generate_alphanumeric_otp(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

otp = generate_alphanumeric_otp()
print("Your OTP is:", otp)



