# Cluster API
### Cluster

Represents kubernetes cluster whose lifecycle is managed by CAPI. Provider specific custom resources are referenced by `infrastructureRef` or `controlPlanRef`

```
apiVersion: cluster.x-k8s.io/v1beta2
kind: Cluster
metadata:
  name: my-cluster
spec:
  clusterNetwork:
    pods:
      cidrBlocks:
      - 192.168.0.0/16
  infrastructureRef:
    apiGroup: infrastructure.cluster.x-k8s.io
    kind: VSphereCluster
    name: my-cluster-infrastructure
  controlPlaneRef:
    apiGroup: controlplane.cluster.x-k8s.io
    kind: KubeadmControlPlane
    name: my-control-plane
```

### ClusterClass

Allows managing multiple cluster objects. 

### Machine

Immutable objects representing kubernetes node. Never updated (other than labels, annotations & status) can only be deleted. Provider specific resources are referenced via `infrastructureRef`. Provider specific controller provisions a new host to register as new node matching the machine spec. If machine is deleted, underlying infrastructure and node is deleted. Imm

```
apiVersion: cluster.x-k8s.io/v1beta2
kind: Machine
metadata:
  name: my-machine
spec:
  clusterName: my-cluster
  version: v1.35.0
  infrastructureRef:
    apiGroup: infrastructure.cluster.x-k8s.io
    kind: VSphereMachineTemplate
    name: my-machine-infrastructure
  bootstrap:
    configRef:
      apiGroup: bootstrap.cluster.x-k8s.io
      kind: KubeadmConfigTemplate
      name: my-bootstrap-config
status:
  nodeRef:
    name: the-node-running-on-my-machine
```

#### Machine Deployment

Similar to pod deployment, creates machine set, which creates machines. 

#### Machine Pool

Infrastructure specific group of machines

#### Machine Set

Similar to pod replica set. 

#### Machine Healthcheck

Automatically initiate remediation for missing/unhealthy nodes, by replacing them. 

### Infrastructure Provider

Component responsible for provisioning compute machines required by cluster or machines. 

### Bootstrap Provider

Turn the server into kubernetes node using machine/node role specific init (using cloud-init) known as BootstrapData. BootStrapData is used by infrastructure provider to bootstrap machine into node. 
### Control Plane Provider

Can either be:
- Self provisioned, wholly managed by single Cluster-API deployment
- Pod based, require external hosting cluster, where control plane components are running as pod, exposed by service. 
- External or managed, controlled by service other than CAPI (eg GKE, AKS, EKS etc)

#### KubeAdmControlPlane

Manage set of machines as control plane nodes using kubeadm. 