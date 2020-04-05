# Dev Tools
A collections of helper utilities to assist with common tasks. These tools run `docker exec` commands, which require a container to be up and running to attach to (as a result of the `docker-compose up` command). 

The `docker-compose run` version is also available in the script (but commented out). This version would spin up it's own container even if one is already running.

## mac
### `manage_py.sh <args>`
* Can be run from within the `/dev/mac` folder directly or from the top level repo with `dev/mac/manage_py.sh`
* Runs `manage.py` within the `pandaid-api_web_1` container, passing through `args`. 
    * `manage_py.sh -h`
        * Brings up the help for `manage.py`.
    * `manage_py.sh shell`
        * Opens Django's pre-configured IPython console within the `pandaid-api_web_1` container. 

### `run_psql.sh <args>`
* Can be run from within the `/dev/mac` folder directly or from the top level repo with `dev/mac/run_psql.sh`
* Runs `psql` within the `pandaid-api_postgres_1` container, passing through `args`. "`-U postgres`" is passed within the script to have the correct username.
    * `run_psql.sh --help`
        * Brings up the help for `psql` to see additional options available.

## win
### `manage_py.bat <args>`
* Can be run from within the `\dev\win` folder directly or from the top level repo with `dev\win\manage_py.bat`
* Runs `manage.py` within the `pandaid-api_web_1` container, passing through `args`. 
    * `manage_py.bat -h`
        * Brings up the help for `manage.py`.
    * `manage_py.bat shell`
        * Opens Django's pre-configured IPython console within the `pandaid-api_web_1` container. 

### `run_psql.bat <args>`
* Can be run from within the `/dev/win` folder directly or from the top level repo with `dev/win/run_psql.bat`
* Runs `psql` within the `pandaid-api_postgres_1` container, passing through `args`. "`-U postgres`" is passed within the script to have the correct username.
    * `run_psql.bat --help`
        * Brings up the help for `psql` to see additional options available.

## VSCode Tools
Visual Studio Code has some pretty helpful extensions that provide a bit more visual interaction with Docker containers. 
1. Install VSCode for your platform [here](https://code.visualstudio.com/download).
2. Install the 'Docker' and 'Remote - Containers' Extensions (both authored by Microsoft)
![image](imgs/Extensions.png)
3. Open VSCode and load the root repository folder with "Open folder" --> `pandaid-api`. Click on the "Docker" Extension.
![image](./imgs/RootFolder.png)
4. If you haven't done so before, run `docker-compose build` from the terminal to build your `docker` containers. If the terminal screen isn't up, press "control + ~" to bring it up, or "Terminal" -> "New" from the menu bar. This command will take a good bit of time the first time as images are downloaded and built. You'll see them under "Images" on the sidebar.
![image](imgs/postBuild.png)
5. Now running `docker-compose up` will start the images creating containers (or pull down an hosted image like `postgres` and start it). The containers will appear under "Containers" on the sidebar. The green triangles indicates the containers are running, red squares will indicate they've stopped.
![image](imgs/runningContainers.png)
6. If you right click on a container, you'll see additional options that are helpful. The first I want to highlight is "Attach Shell". This is actually running a `docker` command to get the shell in the container. By attaching a shell, you can open up a terminal inside one of your containers. In this case, I've opened a terminal in the `web` container, where the Django backend is running. This is another way to run `manage.py` or just explore what the working container actually has access to.
![image](imgs/attachShell.png)
7. Another helpful option is "Attach Visual Studio Code". This option will allow you to have a full instance of VSCode inside of your container, for more options than just attaching a shell. It takes a second for the remote development container to install, but eventually it will bring up a new VSCode window inside of your container. Make sure to press the "Files" button on the tab-bar. 
![image](imgs/attachVSCode.png)
8. Now click "Open Folder" and replace "/root/" with "/" or "." and press "OK".
![image](imgs/selectFolder.png)
9. I've expanded the "code" folder in the sidebar, as well as brought up a terminal. This terminal also is within the container itself. Now you can explore everything that's happening inside the container! It's good to note that files that are mounted as a volume will persist across the OS and container. Otherwise, changes to the container will only remain as long as the container exists (I think you can start/stop all you want, but if you re-build the changes disappear).
![image](./imgs/codeInContainer.png)
10. There are more options within the Docker tab that are worth exploring: Starting, Stopping, Removing, Logs, etc. A lot of the commands are visually ways to execute `docker` CLI commands, but I find them helpful to better understand how Docker works!
