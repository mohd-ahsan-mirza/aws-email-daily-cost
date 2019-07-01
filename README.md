# Background
This lambda currently get triggered every night at 1am in my aws account to send me an email about the daily usage costs. I built this tool so I don't have to login the root account to view billing. It also helps me in cases where if I provision a resource but forget to bring it down and I would start incurring inadvertent charges. Optionally, a CloudWatch alarm can also be configured to trigger the lambda function in case costs or usage exceeds a certain threshold

# Setup
* Login the root account of AWS
* Click on your username and then click ```My Account```
* Scroll to ```IAM User and Role Access to Billing Information``` section 
* Check ```Activate IAM Access``` and then click ```Update```
* Go to the IAM service
* Create a new policy with the following JSON statement
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ce:*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```
* Create a new Lamdbda function
* Attach the above policy and ```AmazonSESFullAccess``` policy to the function
* Remove the default code and copy paste the code from ```lambda_function.py``` from this repository in the editor of the AWS Lambda function console
* Add an environment variable ```destination_email```. It's value is going to be your email
* Save the function
