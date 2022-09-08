[![Tests](https://github.com/netascode/iac-validate/actions/workflows/test.yml/badge.svg)](https://github.com/netascode/iac-validate/actions/workflows/test.yml)

# Validation of Terraform NX-OS Configuration Module

This repository contains [Yamale](https://github.com/23andMe/Yamale) schema and [iac-validate](https://github.com/netascode/iac-validate) rules to perform syntactic and semantic validation of YAML model for [Terraform NX-OS Configuration Module](https://github.com/netascode/terraform-nxos-config).

Example usage:
```
$ yamale -s schema.yaml example_nxos_model.yaml          
Validating /Users/ivan/job/tf/terraform-nxos/terraform-nxos-config-validation/example_nxos_model.yaml...
Validation success! 👍
```

```shell
$ iac-validate -r rules example_nxos_model.yaml
ERROR - Rule 103.001: BGP peer template is not configured under root.bgp.template_peers (['root.bgp.vrfs.0.neighbors.0 - SPINE-PEERS2', 'root.bgp.vrfs.0.neighbors.1 - SPINE-PEERS3'])
ERROR - Rule 100.001: VRF for ethernet interface is not configured under root.vrfs (['root.interfaces_ethernet.1/52.vrf - foo'])
ERROR - Rule 100.002: VRF for loopback interface is not configured under root.vrfs (['root.interfaces_loopback.1.vrf - foo'])
ERROR - Rule 101.001: Feature BGP is not enabled, but BGP configuraion is present. (['add `bgp` to root.features'])
```

## Installation

Python 3.6+ is required to install `iac-validate`. This is the package that needs to be installed.

`iac-validate` can be installed in a virtual environment using `pip`:

```shell
pip install iac-validate
```

Reference: https://github.com/netascode/iac-validate#installation
