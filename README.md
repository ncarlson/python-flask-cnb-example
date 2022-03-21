## To Build

```bash
pack build pf-test --buildpack paketo-buildpacks/python

```

## To Run
```bash
docker run --rm -it --publish 5000:5000 pf-test
curl -v localhost:5000/hello
```

## To Run Unit Tests
```bash
docker run -it --entrypoint /cnb/process/unit pf-test
```
