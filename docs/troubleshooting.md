# Troubleshooting

## Common Issues

### Plugins not loading after install

1. Restart Claude Code
2. Check `claude plugins list` to verify installation
3. Ensure `~/.claude/settings.json` has the plugins in `enabledPlugins`

### "jq not found" during install

```bash
# Ubuntu/Debian
sudo apt install jq

# macOS
brew install jq

# Arch
sudo pacman -S jq
```

### MCP server authentication fails

Delete the cached credentials and re-authenticate:
```bash
# Edit ~/.claude/.credentials.json and remove the relevant entry
# Then restart Claude Code and trigger the auth flow again
```

### Plugin conflicts

If plugins conflict, disable the conflicting one:
```bash
claude plugins disable plugin-name
```

Or edit `~/.claude/settings.json` directly:
```json
{
  "enabledPlugins": {
    "conflicting-plugin@claude-plugins-official": false
  }
}
```

### Hooks not firing

1. Check that the hook event matches what you expect
2. Verify the script is executable: `chmod +x hooks/scripts/my-hook.sh`
3. Test the script manually with sample input

### Install script fails on existing settings

The installer backs up your settings before making changes. Find backups at:
```
~/.claude/backups/divan-YYYYMMDD-HHMMSS/settings.json
```

To restore:
```bash
cp ~/.claude/backups/divan-*/settings.json ~/.claude/settings.json
```

### Performance issues with many plugins

Try the minimal profile:
```bash
./install.sh --user --minimal
```

Then add plugins individually as needed.
