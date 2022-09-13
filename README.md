[![Tests](https://github.com/netascode/terraform-nxos-config-validation/actions/workflows/test.yml/badge.svg)](https://github.com/netascode/terraform-nxos-config-validation/actions/workflows/test.yml)

# Validation of Terraform NX-OS Configuration Module

This repository contains [Yamale](https://github.com/23andMe/Yamale) schema and [iac-validate](https://github.com/netascode/iac-validate) rules to perform syntactic and semantic validation of YAML model for [Terraform NX-OS Configuration Module](https://github.com/netascode/terraform-nxos-config).

Example usage for correct YAML model file:
```shell
$ iac-validate -s schema.yaml -r rules nxos_model_example.yaml
$
```

Example usage for incorrect YAML model file:
```shell
$ iac-validate -s schema.yaml -r rules nxos_model_example_with_errors.yaml
ERROR - Syntax error 'nxos_model_example_with_errors.yaml': vrfs.1.rd: Unexpected element
ERROR - Syntax error 'nxos_model_example_with_errors.yaml': vlans.3.vrf: Unexpected element
ERROR - Semantic error, rule 103.001: BGP peer template is not configured under root.bgp.template_peers (['root.bgp.vrfs.0.neighbors.0 - SPINE-PEERS2', 'root.bgp.vrfs.0.neighbors.1 - SPINE-PEERS3'])
ERROR - Semantic error, rule 100.001: VRF for ethernet interface is not configured under root.vrfs (['root.interfaces_ethernet.1/52.vrf - foo'])
ERROR - Semantic error, rule 100.002: VRF for loopback interface is not configured under root.vrfs (['root.interfaces_loopback.1.vrf - foo'])
ERROR - Semantic error, rule 101.001: Feature BGP is not enabled, but BGP configuraion is present. (['add `bgp` to root.features'])
$
```

## Installation

This is the only package that needs to be installed is `iac-validate`. Python 3.6+ is required to install it.

`iac-validate` can be installed in a virtual environment using `pip`:

```shell
pip install iac-validate
```

Reference: https://github.com/netascode/iac-validate#installation
