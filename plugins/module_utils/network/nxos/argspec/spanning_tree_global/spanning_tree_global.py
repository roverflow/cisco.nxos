# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# ansible.content_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the documentation in the module file and re-run
# ansible.content_builder commenting out
# the path to external 'docstring' in build.yaml.
#
##############################################

"""
The arg spec for the nxos_spanning_tree_global module
"""


class Spanning_tree_globalArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_spanning_tree_global module"""

    argument_spec = {
        "config": {
            "type": "dict",
            "options": {
                "bridge": {
                    "type": "dict",
                    "options": {
                        "bridge_assurance": {"type": "bool"},
                        "bridge_domain": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "bd_list_range": {"type": "str"},
                                "forward_time": {"type": "int"},
                                "hello_time": {"type": "int"},
                                "max_age": {"type": "int"},
                                "priority": {"type": "int"},
                                "root": {
                                    "type": "dict",
                                    "mutually_exclusive": [
                                        ["primary", "secondary"],
                                    ],
                                    "options": {
                                        "primary": {
                                            "type": "dict",
                                            "options": {
                                                "enable": {"type": "bool"},
                                                "diameter": {"type": "int"},
                                                "hello_time": {"type": "int"},
                                            },
                                        },
                                        "secondary": {
                                            "type": "dict",
                                            "options": {
                                                "enable": {"type": "bool"},
                                                "diameter": {"type": "int"},
                                                "hello_time": {"type": "int"},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                "domain": {
                    "type": "dict",
                    "mutually_exclusive": [["identifier", "disable", "enable"]],
                    "options": {
                        "identifier": {"type": "int"},
                        "disable": {"type": "bool"},
                        "enable": {"type": "bool"},
                        "clear_stats": {"type": "bool"},
                    },
                },
                "fcoe": {"type": "bool"},
                "lc_issu": {
                    "type": "str",
                    "choices": ["auto", "disruptive", "non-disruptive"],
                },
                "loopguard_default": {"type": "bool"},
                "mode": {"type": "str", "choices": ["mst", "rapid-pvst"]},
                "mst": {
                    "type": "dict",
                    "options": {
                        "forward-time": {"type": "int"},
                        "hello-time": {"type": "int"},
                        "max_age": {"type": "int"},
                        "max_hops": {"type": "int"},
                        "simulate_pvst_global": {"type": "bool"},
                        "configure_mst": {
                            "type": "dict",
                            "options": {
                                "name": {"type": "str"},
                                "revision": {"type": "int"},
                                "private_vlan_sync": {"type": "bool"},
                                "instance_vlan": {
                                    "type": "dict",
                                    "options": {
                                        "instance_id": {"type": "int"},
                                        "vlan_range": {"type": "str"},
                                    },
                                },
                            },
                        },
                    },
                },
                "pathcost_method": {"type": "str", "choices": ["long", "short"]},
                "port_type": {
                    "type": "dict",
                    "mutually_exclusive": [["edge", "network", "default"]],
                    "options": {
                        "edge": {
                            "type": "str",
                            "choices": ["bpdufilter", "bpduguard", "default"],
                        },
                        "network": {"type": "bool"},
                        "default": {"type": "bool"},
                    },
                },
                "pseudo_info": {
                    "type": "dict",
                    "options": {
                        "bridge_domain_info": {
                            "type": "dict",
                            "mutually_exclusive": [["designated", "root"]],
                            "options": {
                                "range": {"type": "str"},
                                "designated_priority": {"type": "int"},
                                "root_priority": {"type": "int\\"},
                            },
                        },
                        "mst_info": {
                            "type": "dict",
                            "mutually_exclusive": [["designated", "root"]],
                            "options": {
                                "range": {"type": "str"},
                                "designated_priority": {"type": "int"},
                                "root_priority": {"type": "int"},
                            },
                        },
                        "vlan_info": {
                            "type": "dict",
                            "mutually_exclusive": [["designated", "root"]],
                            "options": {
                                "range": {"type": "str"},
                                "designated_priority": {"type": "int"},
                                "root_priority": {"type": "int"},
                            },
                        },
                    },
                },
                "vlan": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "vlan_range": {"type": "str"},
                        "forward_time": {"type": "int"},
                        "hello_time": {"type": "int"},
                        "max_age": {"type": "int"},
                        "priority": {"type": "int"},
                        "root": {
                            "type": "dict",
                            "mutually_exclusive": [["primary", "secondary"]],
                            "options": {
                                "primary": {
                                    "type": "dict",
                                    "options": {
                                        "enable": {"type": "bool"},
                                        "diameter": {"type": "int"},
                                        "hello_time": {"type": "int"},
                                    },
                                },
                                "secondary": {
                                    "type": "dict",
                                    "options": {
                                        "enable": {"type": "bool"},
                                        "diameter": {"type": "int"},
                                        "hello_time": {"type": "int"},
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "rendered",
                "gathered",
                "purged",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
