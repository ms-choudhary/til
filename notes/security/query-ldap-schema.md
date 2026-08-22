
# Query LDAP schema

**Source**: https://dexidp.io/docs/connectors/ldap/#getting-started

Generally when you're configuring LDAP authentication for an application, you've to discover/map certain fields to application configuration. Following tools are helpful in that. 

### Install ldapsearch

```
dnf install openldap-clients
<or>
apt-get install ldap-utils
```
### User/group schema mapping
If directory is small, you can dump all entries by:
```
ldapsearch -x -H ldap://ldap.example.org -b 'dc=example,dc=org'
```

First find user entry 
```
dn: uid=jdoe,cn=users,cn=compat,dc=example,dc=org
cn: Jane Doe
objectClass: posixAccount
objectClass: ipaOverrideTarget
objectClass: top
gidNumber: 200015
gecos: Jane Doe
uidNumber: 200015
loginShell: /bin/bash
homeDirectory: /home/jdoe
mail: jane.doe@example.com
uid: janedoe
```
Which can be mapped like:
```
userSearch:
  # The directory directly above the user entry.
  baseDN: cn=users,cn=compat,dc=example,dc=org
  filter: "(objectClass=posixAccount)"

  # Expect user to enter "janedoe" when logging in.
  username: uid

  # Use the full DN as an ID.
  idAttr: DN

  # When an email address is not available, use another value unique to the user, like uid.
  emailAttr: mail
  nameAttr: gecos
```

Then find group entry:
```
dn: cn=developers,cn=groups,cn=compat,dc=example,dc=org
memberUid: janedoe
memberUid: johndoe
gidNumber: 200115
objectClass: posixGroup
objectClass: ipaOverrideTarget
objectClass: top
cn: developers
```
Group search must match a user attribute to group attribute. For eg, user's uid is matched to group's memberUid. 
```
groupSearch:
  # The directory directly above the group entry.
  baseDN: cn=groups,cn=compat,dc=example,dc=org
  filter: "(objectClass=posixGroup)"

  # The group search needs to match the "uid" attribute on
  # the user with the "memberUid" attribute on the group.
  userMatchers:
  - userAttr: uid
    groupAttr: memberUid

  # Unique name of the group.
  nameAttr: cn
```
## Questions
- 
## Related
- [oidc](/security/oidc.md)





