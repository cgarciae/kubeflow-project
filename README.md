#

### Install kubernetes
```bash
minikube start \
    --cpus 5 \
    --memory 10288 \
    --disk-size 20gb \
    --kubernetes-version 1.14.10
```

### Install dashboard
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml
```
**Get token**
```bash
bash -c 'kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | awk \'/^deployment-controller-token-/{print $1}\') | awk \'$1=="token:"{print $2}\''
```
**start proxy**
```bash
kubectl proxy -p 8010
```
**open dashboard**
[http://localhost:8010/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy](http://localhost:8010/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy)


### Install kubeflow
```bash
set -e

KF_PATH="~/.kubeflow/v1.0"
mkdir -p $KF_PATH
cd $KF_PATH
wget https://github.com/kubeflow/kfctl/releases/download/v1.0/kfctl_v1.0-0-g94c35cf_linux.tar.gz

tar -xvf kfctl_v1.0-0-g94c35cf_linux.tar.gz			
export PATH=$PATH:$KF_PATH
export KF_NAME=my-kubeflow
export BASE_DIR=$KF_PATH
export KF_DIR=${BASE_DIR}/${KF_NAME}
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.2.yaml" 

mkdir -p ${KF_DIR}
cd ${KF_DIR}
kfctl apply -V -f ${CONFIG_URI}
```

### Open Central Dashboard
```
kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
```