# Docker container for Minecraft server status checker

This is Minecraft status check container.

## How to use

```bash
docker run ornew/minecraft-status <ip> <port>
```

### Another host container server

If you run Minecraft server on host container.

```bash
docker run --link <container> ornew/minecraft-status <container> <port>
```

