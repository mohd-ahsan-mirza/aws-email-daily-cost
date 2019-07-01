# Background
This lambda currently get triggered every night at 1am in my aws account to send me an email about the daily usage costs. I built this tool so I don't have to login the root account to view billing. It also helps me in cases where if I provision a resource but forget to bring it down and I would start incurring inadvertent charges. Optionally, a CloudWatch alarm can also be configured to trigger the lambda function in case costs or usage exceeds a certain threshold

# Setup
* Login the root account of AWS
* Click on your username and then click ```My Account```
* Scroll to ```IAM User and Role Access to Billing Information``` section 
* Check ```Activate IAM Access``` and then click ```Update```
