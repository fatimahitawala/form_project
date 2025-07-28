# A Simple Form Developed using Python 
### I have created a simple form that will ask for name and email. Here are the steps:
#### Created a dockerfile to run python image, script and deployed image to docker hub using docker push  command   (personal registry).
#### Create a AKS cluster and using azure login, azure get credentials to esabilish config file.
#### Create a persistent volume claim and add 1GB storage
#### Called that volume in your deployment and create deployment.
#### From Azure portal enable ingress controller and create a cluster ingress
#### Implemented service with LB as type, declared this service in my ingress file.
#### Add IP address mapping with your custom DNS entry in etc/hosts file of linux and also in windows\system32\drivers\etc\hosts and add external IP of ingress as well as your   custom domain like formdetails.com
#### Check if domain is working using curl -v http://formdetails.com command.
