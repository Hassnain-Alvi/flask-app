# flask-app
A simple flask app with one post endpoint to write data in file
This application is already packages as a helm chart for easy deployment in Kubernetes cluster
Docker container is already pushed on DOcker hub and can be pulled as follows:
```
docker pull hassnainalvi021/flask-app
```
A groovy script is written with all deployment commands for build and deploy stages. As i don't have any local Jenkins installation because use Circle CI and GitLab CI for my deployments, please ignore any syntax errors in that script. All shell commands will work fine for building Docker and deployment helm release

Helm chart can be deployed with default values in your local or remote Kubernetes cluster using helm as follows
```
helm install flask-app chart/
```
Note: Make sure kubectl is pointing to correct cluster context.
For Jenkins deployment i have assumed that the agent running build has necessary binary files installed and Kubernetes context set properly 
