# aa-decode

> Decode AppArmor audit logs into a human-readable format.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-decode.8>.

- Decode a hex string:

`aa-decode {{hexstring}}`

- Decode a log file:

`sudo aa-decode {{logfile}}`

- Decode logs from `stdin` (e.g., redirected file):

`sudo aa-decode - < {{logfile}}`

- Display help:

`aa-decode {{[-h|--help]}}`

----------------------------------------------------------------------
--- PARSED --------

[
    {
        "command": "aa-decode",
        "page_desc": "Decode AppArmor audit logs into a human-readable format.",
        "ex_desc": "Decode a hex string",
        "ex_cmd": "aa-decode {{hexstring}}",
    },
    {
        "command": "aa-decode",
        "page_desc": "Decode AppArmor audit logs into a human-readable format.",
        "ex_desc": "Decode a log file",
        "ex_cmd": "sudo aa-decode {{logfile}}",
    },
    {
        "command": "aa-decode",
        "page_desc": "Decode AppArmor audit logs into a human-readable format.",
        "ex_desc": "Decode logs from `stdin` (e.g., redirected file)",
        "ex_cmd": "sudo aa-decode - < {{logfile}}",
    },
    {
        "command": "aa-decode",
        "page_desc": "Decode AppArmor audit logs into a human-readable format.",
        "ex_desc": "Display help",
        "ex_cmd": "aa-decode {{[-h|--help]}}",
    },
]