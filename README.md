# k8s Fibonacci Software

Using k8s to manage fibonacci piece of software and routing.

Inside `.k8s/` directory you will find all the .yaml files used to configure
kubernetes. For this example I'm using cluster-ip to manage the connection
between pods and the ingress to expose the application to the outside world.

## Troubleshooting

Below you will find some troubles I found during the build of the repo and the
answers I got.

* __I really need to push the containers to a repository?__ No, just follow
[this](https://medium.com/swlh/how-to-run-locally-built-docker-images-in-kubernetes-b28fbc32cc1d)
tutorial.

* __How to access externally the k8s network on the clusters?__ Using ingress
or load balance. This project I used ingress. More
[here](https://kubernetes.github.io/ingress-nginx/deploy/#minikube)
