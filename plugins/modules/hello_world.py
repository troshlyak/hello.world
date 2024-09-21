#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.0",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: hello_world
short_description: 'Example Hello World Ansible Module'
description: "Example Hello World Ansible Module"
version_added: '2.9'
author: 'Todor Tsankov'
options:
    greet_name:
        description: 'Whom should be greeted'
        required: true
        type: str
"""

EXAMPLES = """
- name: Hello World
  hello.world.hello_world:
    greet_name: "Cooper"
"""

RETURN = """# """

from ansible.module_utils._text import to_native  # type: ignore
from ansible.module_utils.basic import AnsibleModule  # type: ignore


def main():
    GREET_STRING_SPEC = "Hello World, {greet_name}!"
    argument_spec = dict(
        greet_name=dict(type="str", required=True),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    greet_name = module.params["greet_name"].capitalize()
    greeting = GREET_STRING_SPEC.format(greet_name=greet_name)

    if module.check_mode:
        module.exit_json(changed=False, result=f"Will greet with '{greeting}'")

    try:
        module.exit_json(changed=True, result=greeting)
    except Exception as err:
        module.fail_json(
            msg="Failed to greet with [{greeting}]. Error: [{error}].".format(
                greeting=greeting, error=to_native(err)
            )
        )


if __name__ == "__main__":
    main()
