# ✋ Blacklist
Simple Python CLI to block distracting domains by redirecting all access to localhost using `/etc/hosts`.
Note that this is intentionally not a tool for tracking focus time or to do time-based tracking. It just blocks all access to a domain until you decide to unblock it again.

## Installation
```
pip install -U blacklist-cli
```

## Usage
```
sudo blacklist block reddit.com
```

```
sudo blacklist unblock reddit.com
```

```
blacklist show
```
