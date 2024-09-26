# GCE Runtime configuration

## Docker setup using Dockerfile

Build container (alternatively add --no-cache)

    docker build -t procureinsight .

Start container

Use content in '.entrypoint'




## GCE Artifact registry
Procedure for pushing new docker images to GCE:

    docker tag procureinsight:latest us-west2-docker.pkg.dev/randd-418508/procure/procureinsight:0.0.0
    docker push us-west2-docker.pkg.dev/randd-418508/procure/procureinsight:0.0.0


## GCE Cloud Run
^ Service used for running the docker image of django backend. Set to autoscale.