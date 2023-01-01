# Deploy our app

## Multipass

First, I choose to work with Multipass (k3s not support macOS)

Install k3s in your laptop:

```
brew install --cask multipass
```

## K3S

Second, launch our enviorment:

```
multipass launch --name k3s-master --mem 4G --disk 40G

```
SSH to the master node:

```
multipass shell k3s-master

```
Install k3s on master node:
```
curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644 --node-name k3s-master-01
```
Get token (for connect worker node):
```
sudo cat /var/lib/rancher/k3s/server/node-token
```
Launch the worker node:
```
multipass launch --name k3s-worker --mem 3G --disk 30G
```
Install k3s on worker node with master's token and ip:
```
curl -sfL https://get.k3s.io | K3S_NODE_NAME=k3s-worker-01 K3S_URL=https://<IP>:6443 K3S_TOKEN=<TOKEN> sh –
```


## Certificates

Third, we need to create certificate for our application.

Installing cert-manager:
```
curl -sL \
https://github.com/jetstack/cert-manager/releases/latest/download/cert-manager.yaml |\
sed -r 's/(image:.*):(v.*)$/\1-arm:\2/g' > cert-manager-arm.yaml
```
```
kubectl apply -f cert-manager-arm.yaml
```

Configuring cert-manager to use Lets Encrypt:
```
kubectl apply -f letsencrypt-issuer.yaml
```

Request a certificate for our website:
```
kubectl apply -f cert-manager-arm.yaml
```

## App
Deploy our app:

```
kubectl apply -f mysite.yaml
```












