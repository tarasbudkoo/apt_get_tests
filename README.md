# Running tests using Docker and docker-compose

Build and start tests:

```
docker-compose up --build
```

Stop environment:

```
docker-compose stop
```

Restart/Update code:

```
docker-compose restart
```

Recreate environment

```
docker-compose up --build --force-recreate
```

Remove environment:

```
docker-compose down
```

# Test description

In pkg_manager_tests.py you can see base tests for 'install' operation of Ubuntu apt-get pkg-manager. 
Tests contain scenarios with a simple install of pkg, install pkg with specific versions, reinstall and update pkg, removing pkg, pkg installation interrupt, installation list of pkgs.