# Terraform Workspaces

Each terraform config has a backend which defines how the terraform performs the operations and where the state is stored. #question this is not entirely clear how terraform works internally, explore more

Workspace allows creating different set of infra with same config, same plugins, same module cache & same backend. 

With workspace, you can switch between multiple instances of single config with single backend. 

Usecase: create a parallel distinct copy of set of infra to test before applying it for production. More like git feature branch. 



