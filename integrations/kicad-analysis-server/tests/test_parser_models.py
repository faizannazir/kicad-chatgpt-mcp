from kicad_mcp_server.parsers.pcb_parser import PCBFootprint
from kicad_mcp_server.parsers.schematic_parser import SchematicComponent


def test_schematic_component_conversion_preserves_identity_and_properties():
    component = SchematicComponent.from_kicad_skip(
        {
            "reference": "U1",
            "lib_id": "MCU_ST_STM32F4:STM32F407VG",
            "properties": [
                {"key": "Value", "value": "STM32F407VGT6"},
                {"key": "Footprint", "value": "Package_QFP:LQFP-100"},
            ],
            "at": {"x": 42.5, "y": 18.0},
            "pins": [{"number": "1", "name": "VBAT"}],
        }
    )
    assert component.reference == "U1"
    assert component.value == "STM32F407VGT6"
    assert component.library_id == "MCU_ST_STM32F4:STM32F407VG"
    assert component.footprint == "Package_QFP:LQFP-100"
    assert component.position == (42.5, 18.0)
    assert component.pins == [{"number": "1", "name": "VBAT"}]


def test_pcb_footprint_conversion_preserves_layer_and_geometry():
    footprint = PCBFootprint.from_dict(
        {
            "reference": "J1",
            "footprint_id": "Connector_USB:USB_C_Receptacle",
            "value": "USB-C",
            "layer": "B.Cu",
            "at": {"x": 12.3, "y": 45.6, "rotation": 90},
            "pads": [{"number": "A1"}, {"number": "A2"}],
        }
    )
    assert footprint.reference == "J1"
    assert footprint.footprint_id == "Connector_USB:USB_C_Receptacle"
    assert footprint.layer == "B.Cu"
    assert footprint.position == (12.3, 45.6)
    assert footprint.rotation == 90
    assert footprint.pad_count == 2
