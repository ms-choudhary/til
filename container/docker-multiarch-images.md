# Docker Multiarch Images

Docker image is specific for os + host architecture (eg linux + arm64 or linux + amd64). 
```
 $ docker image inspect miniflux/miniflux | jq '.[] | "\(.Os)\/\(.Architecture)"'
"linux/arm64"
```

Same image can be built for different architectures. Running non multi arch image on incorrect platform will fail. Docker pulls correct image from registry based on os/arch set in docker engine.

```
$ docker version
  OS/Arch:          linux/arm64
```


Image listing on dockerhub generally shows if it's a multiarch image (os/arch) for each tag. 

Image manifests files contains all individual multi arch images links. This is part of docker/OCI  registry spec. 

```
$ docker manifest inspect alpine:latest
{
   "schemaVersion": 2,
   "mediaType": "application/vnd.oci.image.index.v1+json",
   "manifests": [
      {
         "mediaType": "application/vnd.oci.image.manifest.v1+json",
         "size": 1022,
         "digest": "sha256:59855d3dceb3ae53991193bd03301e082b2a7faa56a514b03527ae0ec2ce3a95",
         "platform": {
            "architecture": "amd64",
            "os": "linux"
         }
      },

```

Pulling `alpine:latest` in this case will fetch the image mainfest file, it then matches the local os/arch and pulls the corresponding image sha. Image spec contains individual layers, which are pulled next. 

```
$ docker image inspect alpine:latest

        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:0b83d017db6efafadf6b3f18d087d2ce1d67d8f0e927dc7254b0ad088074cd3a",
                "sha256:1c2824e33c7138199cf5b48c29289ceb30179b427bf1cee68cf2f502b537ae82",
                "sha256:f19172968839067b8298f671f9d192997f1e8cc7b79604b4df72793197668477"
            ]
        },
```

Non multiarch images manifest just link a single image. 

### Build

To build a multi arch image, you can build and push the image separately for each arch on a build farm (set of machines with different arch). Each of these image exists as a separate manifest. Finally create a common manifest file linking all previous images, and push that to registry. 

```
$ docker manifest create alpine:latest alpine:arm64-latest alpine:amd64-latest
$ docker manifest push alpine:latest
```

In dockerfile, if base image is multi arch, you don't need to do anything else. It should pull correct image and build your app for correct platform. If, however, base is not multi arch, you need to create and maintain separate dockerfile for each architecture. 

In recent docker (with buildx), you can run:

```
$ docker build --platform linux/amd64, linux/arm64 image .
```

to automate all these separate steps, i.e, building and pushing individual images and creating manifest. 

It requires emulation via qemu, that must be separately configured. 

## Sources
- https://www.youtube.com/watch?v=cDJrQ4IzZ_M
## Questions
- Explore qemu emulation and binfmt_misc #question 
## Related
- [containers#Image](/container/containers.md#Image)
