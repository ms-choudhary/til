# Slack

Slack is a maze of endpoints, and I always get confused, how to configure a new app or change some aspect of existing custom apps. There're so many pages titled "Your apps configuration", I've lost my way many a time, hence, this documentation. 

### Manage custom slack apps
Manage your custom slack apps at URL: https://api.slack.com/apps/

### Post to a channel

- Create a new slack app at above endpoint
- Add oauth scopes `chat:write` for posting new messages to channel
- Generate bot token, export that as env `SLACK_TOKEN`
- `C0AUQ88NCAZ` is channel id
```
func postSlackMessage(message string) error {
	token := envOrFatal("SLACK_TOKEN")
	client := slack.New(token)
	_, _, err := client.PostMessage("C0AUQ88NCAZ", slack.MsgOptionText(message, false))
	if err != nil {
		return err
	}
	return nil
}

func envOrFatal(key string) string {
	v := os.Getenv(key)
	if v == "" {
		log.Fatal("missing %s", key)
	}
	return v
}
```
## Sources
- 
## Related
- [[]]
