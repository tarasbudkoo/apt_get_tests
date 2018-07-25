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
Tests contain scenarios below:
 * test simple pkg install; 
 * test installation pkg with specific versions; 
 * test reinstall and update pkg, removing pkg; 
 * test pkg installation interrupt; 
 * test installation list of pkgs;
 
 To interact with apt-get and execute commands was implemented test framework(apt_get_wrapper.py) which contains all base operations of apt-get pkg-manager:
 * install
 * update
 * upgrade
 * remove