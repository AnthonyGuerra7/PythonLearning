"""
This program demonstrates basic string operations to format
and display customer data properly.
"""

#Customer information
first_name = "anthony"
last_name = "guerra"
email = "anthony.guerra@coolemail.com"

#Captilize the first letter of firstname and lastnames and domain name
formatted_first_name = first_name.capitalize()
formatted_last_name = last_name.capitalize()

# Finding the index position of the @ symbol
at_index = email.find("@")

# Extract the domain based on everything after @ symbol
domain = email[at_index + 1:]

#Create formatted customer ID
# - First 3 letters of lastname
# - Length  of firstname
# - First 3 letters of the domain

customer_id = (
    last_name[:3].upper()
    + str(len(first_name))
    + domain[:3]
)

print("\nCustomer Information")
print("--------------------")
print(f"Name: {formatted_first_name} {formatted_last_name}")
print(f"Email: {email}")
print(f"Email Domain: {domain}")
print(f"Customer ID: {customer_id}")



