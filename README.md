This is a simple solution that deploys a python api microservice and elasticsearch via Helm.
Dockerfile is in root directory and k8s files can be found in it's own folder.

To deploy the solution to your k8s cluster here is what you need to do.
1. Navigate to helm folder.
2. Run `helm install python-app python-app-chart/`
3. After that run `helm install elasticsearch elasticsearch-chart/`

Once the solution is installed run this command to find the public ip of your service:
`kubectl get svc python-app-service`
The record that you will see in your external ip section is the one you can access the app.

`http://<external-ip>` should bring you OK as a healtcheck.
`http://<external-ip>/city` is a url where you can add records regarding cities and their populations.
Example you can run from Windows cmd:

`curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"London\", \"population\": 9000000}" http://<external-ip>/city`

`http://<external-ip>/city/London` will return the record that you inserted.
