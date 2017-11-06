Kubeless is more!
The hottest topic now in the cloud industry is Serverless-Computing.
In the past few years, cloud industry became more and more popular and brought to us new approaches and technologies to use. In this post I will talk about Serverless implemented in kubernetes cluster.
What is Serverless?
Actually, there is no such thing as “serverless”, I know this name suggest that you can write a piece of code and let it “float” somewhere and automagically the app will work, No It’s just mean that someone else is doing this job for you. When using serveless computing no need to worry about  server creation, maintenance, hardware, blackout ,support, and staffing resources. Simply take advantage of the cloud platform and resources and let it manage those topics. Serverless computing takes it to next level by letting the developer focus on their code only.
There are a lot of frameworks around serverless. I will be talking about a Kubernetes-native serverless framework — kubeless.
What is kubeless?
It is an open source serverless framework running on top of Kubernetes. It allows you to deploy a small bit of code without having to worry about underlying infrastructure. It uses Kubernetes resources to provide auto-scaling, routing, monitoring, and troubleshooting.
All you need to do is to create and deploy a function that will be exposed via event/trigger mechanism.
Functions have three possible types:
pubsub triggered.
http triggered.
schedule triggered.

Pubsub events are managed with Kafka cluster, which is built-in component in kubeless installation package while HTTP triggers are exposed with kubernetes services, schedule function will translate to a cron job.
Currently Python, NodeJS, Ruby and .Net Core are supported.
How does it works?
Kubeless will create a Custom Resource Definition, called Function, that way we can create function as a normal kubernetes resource, in the background a controller created, it will  watch over these custom resources and will launch runtimes on-demand.
Kubeless ArchitectureBefore we begin
some assomptions:
Basic knowledge in Kubernetes Concepts is required.
A working Kubernetes cluster, I will be using Minikube for this tutorial.
Kubectl cli installed.

Let’s get our hands dirty
First, we will create a namespace for kubeless components:
> kubectl create ns kubeless
Next, download and deploy kubeless into the cluster, I will be using the latest version (during the preparation of this guide):
> export RELEASE=v0.2.3
> kubectl create -f https://github.com/kubeless/kubeless/releases/download/$RELEASE/kubeless-$RELEASE.yaml
After a minute, let’s do some sanity checks: 
> kubectl get pods -n kubeless
NAME                                   READY  STATUS   RESTARTS  AGE
kafka-0                                1/1    Running   0        1m
kubeless-controller-1046320385-4dp09   1/1    Running   0        1m
zoo-0                                  1/1    Running   0        1m
> kubectl get customresourcedefinition
NAME           KIND
functions.k8s  CustomResourceDefinition.v1beta1.apiextensions.k8s
