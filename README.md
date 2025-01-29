1.Create docker image "ip-tool" by running dockerfile using below command:
docker build -t ip-tool .

2. Push docker image to registry
    docker tag ip-tool registry.com/ip-tool:latest
    docker push registry.com/ip-tool:latest

3. Run deployment file using below command:
kubectl apply -f deployment.yaml
