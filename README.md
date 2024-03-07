# Build Circle Superheroes tech test

Superheroes and villains are always battling it out, but how do we know who wins? In this test, we will deploy a simple function to find out.

The superhero and villain characters along with their stats are stored in a public json file in AWS S3 - https://s3.eu-west-2.amazonaws.com/build-circle/characters.json. When the function is deployed you can run it with a query like https://my-azure-function.azurewebsites.net/api/?hero=Superman&villain=Joker and the returned result should be some information about the winner.

During a battle, the character with the highest score wins.

We expect the solution to be simple, readable, and secure.

For this exercise, we need to deploy an Azure Function with:

* A publicly accessible function URL.
* The data source URL as an environment variable 'data_url'.
* Some Azure Monitor alert for when the function throws an exception.

The function code for deployment can be found in `main.py` and it shouldn't require modification. You can use any framework for deploying infrastructure such as bicep, or Terraform.
