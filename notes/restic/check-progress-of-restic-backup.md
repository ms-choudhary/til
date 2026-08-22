# Check progress of restic backup

**Source**: https://restic.readthedocs.io/en/latest/manual_rest.html

If you're running restic in a non interactive setup (like in cron/systemd timer etc), there are two ways to show current backup progress:

- set env `RESTIC_PROGRESS_FPS`  to 1 for printing progress every second,  `1/60 = 0.016667` for every min
- invoking `SIGUSR1` signal to running restic process should shows current progress in stdout logs

```
kill -SIGUSR1 $(pgrep restic)
```

## Questions
- 
## Related
- [[]]
