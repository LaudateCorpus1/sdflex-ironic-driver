# Copyright 2016 Intel Corporation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from ironic.drivers import redfish

from sdflex_ironic_driver.sdflex_redfish import management as sdflex_mgmt
from sdflex_ironic_driver.sdflex_redfish import power as sdflex_power


class SdflexRedfishHardware(redfish.RedfishHardware):
    """Sdflex Redfish hardware type."""

    @property
    def supported_management_interfaces(self):
        """List of supported management interfaces."""
        return [sdflex_mgmt.SdflexRedfishManagement]

    @property
    def supported_power_interfaces(self):
        """List of supported power interfaces."""
        return [sdflex_power.SdflexRedfishPower]