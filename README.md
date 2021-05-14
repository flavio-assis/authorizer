---
Project: Authorizer
languages:
  - python 3.9
  
Products:
  - Python 3.9
  - Docker 20.10.5
---

## Description
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

### Using Docker
To use the application using docker you must build the image. To do that, you can use the make command:
```
make docker-build IMAGE_NAME=<my_image_name> VERSION=<my_image_tag>
```
_Note: The default values for IMAGE_NAME and VERSION are respectively `authorizer` and `0.0.1`_

After the image is built you can use it by using the make command:
```
make authorize INPUT_PATH=<full_path_of_operations_file>
```
This command will load the input file inside a docker volume, and it will use it to pass the file for stdin.

### Using virtual environment
Another approach to use the application is to run it inside a virtual environment. To do that, you can use another make command:
```
make virtualenv
```

Then 
```
source venv/bin/activate
```
Finally
```
authorize < <input_file_path>
```

## Running the tests 
To run the tests you can use the make command:
```
make test
```
They are unit and integration tests built with the python package `unittest`

## Project structure
```
.                                                                                   
├── CHAGELOG.md                                                      # Keep track of the modifications
├── Dockerfile                                                       # Dockerfile definition
├── LICENSE                                                          # MIT License
├── Makefile                                                         # Makefile with the most used actions
├── README.md                                                        # This README
├── THEROADSOFAR.md                                                  # Explains a little about how I get to this solution
├── pyproject.toml                                                   # Python project constraints
├── setup.py                                                         # Python setup configuration
├── src                                                              # Main logic folder
│   ├── __init__.py                                                  
│   ├── authorizer.py                                                # The authorizer itself
│   ├── models                                                       # Some defined modules
│   │   ├── __init__.py                                              
│   │   ├── account.py                                               
│   │   ├── context.py                                               
│   │   ├── transaction.py                                           
│   │   └── validator.py                                             
│   ├── utils                                                        # Common utils for the source code
│   │   ├── __init__.py                                              
│   │   ├── datetime_utils.py                                        
│   │   ├── event.py                                                 
│   │   └── logger.py                                                
│   └── validators                                                   # Validators' logic
│       ├── __init__.py                                              
│       ├── account_validators.py                                    
│       └── transactions_validators.py                               
└── tests                                                            # Tests folder
    ├── __init__.py                                                  
    ├── integration                                                  # Integration tests
    │   ├── __init__.py                                              
    │   ├── files                                                    
    │   │   ├── inputs                                               
    │   │   │   ├── operations_account_already_initialized           
    │   │   │   ├── operations_account_not_initialized               
    │   │   │   ├── operations_card_not_active                       
    │   │   │   ├── operations_double_transaction                    
    │   │   │   ├── operations_high_frequency_small_interval         
    │   │   │   ├── operations_insufficient_limit                    
    │   │   │   └── operations_no_violations                         
    │   │   └── outputs                                              
    │   │       ├── operations_account_already_initialized           
    │   │       ├── operations_account_not_initialized               
    │   │       ├── operations_card_not_active                       
    │   │       ├── operations_double_transaction                    
    │   │       ├── operations_high_frequency_small_interval         
    │   │       ├── operations_insufficient_limit                    
    │   │       └── operations_no_violations                         
    │   └── test_integrations.py                                     
    └── unit                                                         # Unittests
        ├── __init__.py                                              
        ├── models                                                   
        │   ├── __init__.py                                          
        │   ├── test_account_model.py                                
        │   ├── test_context_model.py                                
        │   ├── test_transaction_model.py                            
        │   └── test_validator_model.py                              
        ├── utils                                                    
        │   ├── __init__.py                                          
        │   ├── test_datetime_utils.py                               
        │   ├── test_event.py                                        
        │   └── test_logger.py                                       
        └── validators                                               
            ├── __init__.py                                          
            ├── test_account_already_initialized.py                  
            ├── test_account_not_initialized.py                      
            ├── test_card_not_active.py                              
            ├── test_double_transaction.py                           
            ├── test_get_violations.py                               
            ├── test_high_frequency_small_interval.py                
            └── test_insufficient_limit.py                           
```