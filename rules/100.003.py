class Rule:
    id = "100.003"
    description = "VRF for vlan interface is not configured under root.vrfs"
    severity = "HIGH"

    @classmethod
    def match(cls, data):
        results = []
        vrfs = [vrf["name"] for vrf in data["vrfs"]]
        key = "interfaces_vlan"
        try:
            for interface in data[key]:
                if "vrf" in interface:
                    if interface["vrf"] not in vrfs:
                        results.append(f"root.{key}.{interface['id']}.vrf - {interface['vrf']}")
        except KeyError:
            pass

        return results
