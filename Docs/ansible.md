# Ansible — Notes

Configuration management and automation with Ansible.

## Core ideas
- **Agentless** — connects over SSH; no agent needed on managed hosts.
- **Idempotent** — running a playbook repeatedly produces the same end state.
- **Push-based** — control node pushes config to managed nodes.

## Building blocks
- **Inventory** — defines managed hosts and groups (static .ini or dynamic).
- **Modules** — units of work (apt, service, copy, template, etc.).
- **Ad-hoc commands** — one-off tasks: `ansible web -m ping`.
- **Playbooks** — YAML files describing desired state across plays and tasks.
- **Variables** — group_vars, host_vars, facts; inspected with the debug module.
- **Control flow** — `when` conditionals, `loop`, and handlers via `notify`.
- **Templates** — Jinja2 (`.j2`) for dynamic config files.
- **Roles** — reusable, structured automation (tasks, handlers, templates, vars).

## Cloud
- **Ansible for AWS** — provisioning and configuring EC2 instances via Ansible modules.

## Useful commands
- `ansible all -m ping` — connectivity check
- `ansible-playbook site.yml -i inventory.ini` — run a playbook
- `ansible-playbook site.yml --check` — dry run
- `ansible-inventory --list` — view parsed inventory

## Security note
Inventory with real IPs, SSH keys, and AWS credentials are kept out of git.