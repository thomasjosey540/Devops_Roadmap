# Ansible — Configuration Management & Automation

Hands-on Ansible projects from my DevOps learning journey: inventory management, playbooks, roles, templating, and AWS provisioning.

## What this covers

| Area | Topics |
|------|--------|
| Setup & Inventory | Ansible install, infra setup, static inventory, ping module, grouping |
| Ad-Hoc & Modules | Ad-hoc commands, common modules, find/use/troubleshoot workflow |
| Playbooks | Playbook structure, modules, YAML syntax |
| Configuration | ansible.cfg, variables, debug, group/host/fact variables |
| Logic | Conditionals (when), loops, handlers |
| Files & Templates | file, copy, and template (Jinja2) modules |
| Roles | Role structure and reuse |
| Cloud | Ansible for AWS (EC2 provisioning) |

## Key concepts practiced

- **Inventory & grouping** — organizing managed hosts into groups for targeted automation
- **Idempotency** — playbooks that can run repeatedly with the same result
- **Variables** — group_vars, host_vars, facts, and debug output
- **Control flow** — conditional tasks (`when`), loops, and handlers triggered by `notify`
- **Templating** — dynamic config files with Jinja2 via the template module
- **Roles** — structured, reusable automation (tasks, handlers, templates, vars)
- **Cloud provisioning** — using Ansible to automate AWS EC2 resources

## Notes

All host IPs, SSH keys, and AWS credentials are kept out of version control (managed via inventory files and variables that are git-ignored).