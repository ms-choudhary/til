
# Windows

### Format the disk from power shell

- Run commands as admin

```
diskpart

list disk
select disk X
clean 
create partition primary

list volume
select volume X
format fs=fat32 quick
```