# Minecraft Server Update

Downloads minecraft server releases

## Example Usage

### Help

```
$ ./run.sh -h

positional arguments:
  version               desired version number, latest if not provided

optional arguments:
  -h, --help            show this help message and exit
  --release             latest release version of minecraft
  --snapshot            latest snapshot version of minecraft, overrides
                        --release if both are provided
  -n NAME, --name NAME  filename of the jar file
  -d DESTINATION, --destination DESTINATION
                        destination path to save the server.jar
```

### Download latest release to current directory
```
$ ./run.sh

Found blob for release version 1.17.1
Downloading server.jar for 1.17.1...
Replacing /home/tony/repos/mc-server-update/server.jar
Done!
```

### Download latest snapshot to current directory
```
$ ./run.sh --snapshot

Found blob for snapshot version 1.18-rc3
Downloading server.jar for 1.18-rc3...
Replacing /home/tony/repos/mc-server-update/server.jar
Done!
```

### Download latest snapshot to current directory
```
$ ./run.sh --snapshot

Found blob for snapshot version 1.18-rc3
Downloading server.jar for 1.18-rc3...
Replacing /home/tony/repos/mc-server-update/server.jar
Done!
```

### Download snapshot 21w44a to current directory
```
$ ./run.sh --snapshot 21w44a

Found blob for snapshot version 21w44a
Downloading server.jar for 21w44a...
Replacing /home/tony/repos/mc-server-update/server.jar
Done!
```


## Example Usage in Script

```bash
# update-minecraft-server.sh
#!/bin/bash
minecraftd stop
minecraftd backup
PWD=`pwd`
cd ~/repos/mc-server-update
sudo ~/repos/mc-server-update/run.sh -d /srv/minecraft -n minecraft_server.jar "$@"
cd "$PWD"
minecraftd start
```