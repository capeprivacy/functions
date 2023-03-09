# Password manager

Password manager takes an existing cape encrypted input and returns the specified account and password. 

## Using the password manager
To keep track of a list of passwords the best way is to use your own auth token. 
Encryption of sensitive data is reliant on Cape encrypt. 


## Local format
The local format for your password store is: 

Account|Label|encrypted output|


## App
We can just use a simple echo app to return the password in plaintext. 

### Commands

There are a couple of commands that we can use to interact with the password manager app.
The syntax for interacting with the app is `<identifier>:<keyword>`.

**name**
Specify the name of the account and password.

**tag**
Returns all the secrets with the corresponding tag. 

**all**
Returns all the secrets stored in the password vault.


## Alternative design
We can encrypt the entire password store and pass two separate values one after the other.
In the form of password vault + tag/account and it will return a password. 

If we do this then one deployed webapp can work for everyone. 

However, if you want to add a new account you will have to decode everything and modify
the output. The first one design makes it easy to add an account. However, it requires
more code to run on the client side and doesn't offer storage on Cape. 

## Alternative design 2
Embed the data in the function. Require a custom app to run this, lots more work on the user. 

