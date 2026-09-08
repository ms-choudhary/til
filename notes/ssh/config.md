# Config

### RemoteCommand

```sh
Host homelab
  HostName homelab
  # If the remote command requires a TTY
  RequestTTY yes
  # -A attaches to an existing session, if no session it creates one
  # -s specifies the session name 'work'
  RemoteCommand tmux new-session -A -s work
```

Gotcha, you cannot run other command while specifying RemoteCommand. For eg `ssh homelab ls` fails with `Cannot execute command-line and remote command`. Can also affect other tools using ssh, like rsync, scp etc. 