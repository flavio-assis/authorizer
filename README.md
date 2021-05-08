# Authorizer Project

This application implements a transaction authorizer.

## How does it works?

It works receiving a data file in `json` format from `stdin` and logging the new account balance for the account if 
the transaction was completed validated without any violations.

### The violations could be:

- `account-already-initilized`: If the application receive an event to create an account that is already created.
- `account-not-initialized`: If the transaction is made before an account creation.
- `card-not-active`: If the account does not have a card activated, the transaction will be blocked.
- `insufficient-limit`: If the card does not have the credit limit to complete the transaction.
- `high-frequency-small-interval`: If more than 3 transactions were made in an interval of 3 minutes, the next one will be blocked.
- `double-transaction`: If a transaction with the same amount for the same merchant is made within 2 minutes, only the first must be processed.

## Using the application
To use the application you must build the docker image. To do that you can use the make command:
```
make build IMAGE_NAME=<my_image_name> IMAGE_TAG=<my_image_tag>
```
_Note: The default values for IMAGE_NAME and IMAGE_TAG are respectively authorizer and latest_ 

After the image is built you can use it by using the make command:
```
make authorize INPUT_PATH=<full_path_of_operations_file>
```



