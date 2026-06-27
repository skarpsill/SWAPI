---
title: "swMouse_e Enumeration"
project: "SOLIDWORKS API Commands Enumeration"
interface: "swMouse_e"
member: ""
kind: "enum"
source: "swcommands/SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swMouse_e.html"
---

# swMouse_e Enumeration

Mouse commands.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMouse_e
   Inherits System.Enum
```

### C#

```csharp
public enum swMouse_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMouse_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMouse_Absolute | 256 or 0x100 |
| swMouse_Click | 512 or 0x200 |
| swMouse_DoubleClick | 1024 or 0x400 |
| swMouse_LeftDown | 2 or 0x2 |
| swMouse_LeftUp | 4 or 0x4 |
| swMouse_MiddleDoubleClick | 8192 or 0x2000; Zoom to fit |
| swMouse_MiddleDown | 32 or 0x20 |
| swMouse_MiddleUp | 64 or 0x40 |
| swMouse_MouseMove | 1 or 0x1 |
| swMouse_RightClick | 2048 or 0x800 |
| swMouse_RightDoubleClick | 4096 or 0x1000 |
| swMouse_RightDown | 8 or 0x8 |
| swMouse_RightUp | 16 or 0x10 |
| swMouse_SelectANNOTATIONTABLES | 0x620000; filters mouse selections to annotation tables |
| swMouse_SelectANNOTATIONVIEW | 0x8b0000; filters mouse selections to annotation views |
| swMouse_SelectARROWS | 0x310000; filters mouse selections to arrows |
| swMouse_SelectATTRIBUTES | 0x80000; filters mouse selections to attributes |
| swMouse_SelectBLOCKDEF | 0x630000; filters mouse selections to block definitions |
| swMouse_SelectBLOCKINST | 0x5d0000; filters mouse selections to block instances |
| swMouse_SelectBODYFEATURES | 0x160000; filters mouse selections to body features |
| swMouse_SelectBODYFOLDER | 0x760000; filters mouse selections to body folders |
| swMouse_SelectBOMFEATURES | 0x610000; filters mouse selections to BOM features |
| swMouse_SelectBOMS | 0x360000; filters mouse selections to BOMs |
| swMouse_SelectBOMTEMPS | 0x400000; filters mouse selections to BOM templates |
| swMouse_SelectBorder | 0xfe0000; filters mouse selections to borders |
| swMouse_SelectBREAKLINES | 0x1f0000; filters mouse selections to breaklines |
| swMouse_SelectBROWSERITEM | 0x450000; filters mouse selections to browser items |
| swMouse_SelectCAMERAS | 0x880000; filters mouse selections to cameras |
| swMouse_SelectCENTERLINES | 0x670000; filters mouse selections to centerlines |
| swMouse_SelectCENTERMARKS | 0x1c0000; filters mouse selections to centermarks |
| swMouse_SelectCENTERMARKSYMS | 0x640000; filters mouse selections to centermark symbols only |
| swMouse_SelectCOMMENT | 0x7f0000; filters mouse selections to comments |
| swMouse_SelectCOMMENTSFOLDER | 0x7e0000; filters mouse selections to comment folders |
| swMouse_SelectCOMPONENTS | 0x140000; filters mouse selections to components |
| swMouse_SelectCOMPPATTERN | 0x250000; filters mouse selections to component patterns |
| swMouse_SelectCOMPSDONTOVERRIDE | 0x480000; filters mouse selections to specified selection types (e.g., edges, vertices, or faces) over the competing component selection type in an assembly |
| swMouse_SelectCONFIGURATIONS | 0x2f0000; filters mouse selections to configurations |
| swMouse_SelectCONNECTIONPOINTS | 0x420000; filters mouse selections to connection points |
| swMouse_SelectCOORDSYS | 0x3d0000; filters mouse selections to coordinate systems |
| swMouse_SelectCOSMETICWELDS | 0xdc0000; filters mouse selections to cosmetic welds |
| swMouse_SelectCTHREADS | 0x270000; filters mouse selections to cosmetic threads |
| swMouse_SelectCUSTOMSYMBOLS | 0x3c0000; filters mouse selections to custom symbols |
| swMouse_SelectDATUMAXES | 0x50000; filters mouse selections to datum axes |
| swMouse_SelectDATUMLINES | 0x3e0000; filters mouse selections to datum lines |
| swMouse_SelectDATUMPLANES | 0x40000; filters mouse selections to datum planes |
| swMouse_SelectDATUMPOINTS | 0x60000; filters mouse selections to datum points |
| swMouse_SelectDATUMTAGS | 0x240000; filters mouse selections to datum tags |
| swMouse_SelectDCABINETS | 0x2a0000; filters mouse selections to D cabinets |
| swMouse_SelectDETAILCIRCLES | 0x110000; filters mouse selections to detail circles |
| swMouse_SelectDIMENSIONS | 0xe0000; filters mouse selections to dimensions |
| swMouse_SelectDISPLAYSTATE | 0x940000; filters mouse selections to display states |
| swMouse_SelectDOCSFOLDER | 0x7d0000; filters mouse selections to document folders |
| swMouse_SelectDOWELSYMS | 0x560000; filters mouse selections to dowel symbols |
| swMouse_SelectDRAWINGVIEWS | 0xc0000; filters mouse selections to drawing views |
| swMouse_SelectDTMTARGS | 0x280000; filters mouse selections to datum targets |
| swMouse_SelectEDGES | 65536 or 0x10000; filters mouse selections to edges |
| swMouse_SelectEMBEDLINKDOC | 0x7b0000; filters mouse selections to embedded document links |
| swMouse_SelectEMPTYSPACE | 0x480000; filters mouse selections to empty spaces |
| swMouse_SelectEQNFOLDER | 0x370000; filters mouse selections to equations folders |
| swMouse_SelectEXCLUDEMANIPULATORS | 0x6f0000; filters mouse selections to exclude manipulators |
| swMouse_SelectEXPLLINES | 0x2d0000; filters mouse selections to explode lines |
| swMouse_SelectEXPLSTEPS | 0x2c0000; filters mouse selections to explode steps |
| swMouse_SelectEXPLVIEWS | 0x2b0000; filters mouse selections to explode views |
| swMouse_SelectEXTSKETCHPOINTS | 0x190000; filters mouse selections to sketch points |
| swMouse_SelectEXTSKETCHSEGS | 0x180000; filters mouse selections to sketch segments |
| swMouse_SelectEXTSKETCHTEXT | 0x580000; filters mouse selections to sketch text |
| swMouse_SelectFABRICATEDROUTE | 0x460000; filters mouse selections to a fabricated routes |
| swMouse_SelectFACES | 131072 or 0x20000; filters mouse selections to faces |
| swMouse_SelectFRAMEPOINT | 0x4d0000; filters mouse selections to frame points |
| swMouse_SelectFTRFOLDER | 0x5e0000; filters mouse selections to feature folders |
| swMouse_SelectGENERALTABLEFEAT | 0x8e0000; filters mouse selections to general table features |
| swMouse_SelectGTOLS | 0xd0000; filters mouse selections to Gtols |
| swMouse_SelectHELIX | 0x1a0000; filters mouse selections to helixes |
| swMouse_SelectHOLESERIES | 0x530000; filters mouse selections to hole series |
| swMouse_SelectHOLETABLEAXES | 0x690000; filters mouse selections to hole table axes |
| swMouse_SelectHOLETABLEFEATS | 0x680000; filters mouse selections to hole table features |
| swMouse_SelectIMPORTFOLDER | 0x390000; filters mouse selections to import folders |
| swMouse_SelectINCONTEXTFEAT | 0x1d0000; filters mouse selections to in-context features |
| swMouse_SelectINCONTEXTFEATS | 0x200000; filters mouse selections to in-context features |
| swMouse_SelectJOURNAL | 0x7c0000; filters mouse selections to journals |
| swMouse_SelectLEADERS | 0x540000; filters mouse selections to leaders |
| swMouse_SelectLIGHTS | 0x490000; filters mouse selections to lights |
| swMouse_SelectMAGNETICLINES | 0xe10000; filters mouse selections to magnetic lines |
| swMouse_SelectMANIPULATORS | 0x4f0000; filters mouse selections to manipulators |
| swMouse_SelectMATEGROUP | 0x1e0000; filters mouse selections to mate groups |
| swMouse_SelectMATEGROUPS | 0x210000; filters mouse selections to multiple mate groups |
| swMouse_SelectMATES | 0x150000; filters mouse selections to mates |
| swMouse_SelectMATESUPPLEMENT | 0x8a0000; filters mouse selections to mate supplemental faces |
| swMouse_SelectMIDPOINTS | 0x3b0000; filters mouse selections to midpoints |
| swMouse_SelectNOTES | 0xf0000; filters mouse selections to notes |
| swMouse_SelectOBJGROUP | 0xcf0000; filters mouse selections to object groups |
| swMouse_SelectOBJHANDLES | 0x300000; filters mouse selections to object handles |
| swMouse_SelectOLEITEMS | 0x70000; filters mouse seletions to OLE items |
| swMouse_SelectPICTUREBODIES | 0x500000; filters mouse selections to picture bodies |
| swMouse_SelectPLANESECTIONS | 0xdb0000; filters mouse selections to plane sections |
| swMouse_SelectPOINTREFS | 0x290000; filters mouse selections to point references |
| swMouse_SelectPOSGROUP | 0x440000; filters mouse selections to mate reference folders |
| swMouse_SelectPUNCHTABLEFEATS | 0xea0000; filters mouse selections to punch table features |
| swMouse_SelectREFCURVES | 0x170000; filters mouse selections to reference curves |
| swMouse_SelectREFEDGES | 0x330000; filters mouse selections to reference edges |
| swMouse_SelectREFERENCECURVES | 0x1a0000; filters mouse selections to reference curves |
| swMouse_SelectREFFACES | 0x340000; filters mouse selections to reference faces |
| swMouse_SelectREFSILHOUETTE | 0x350000; filters mouse selections to reference silouettes |
| swMouse_SelectREFSURFACES | 0x1b0000; filters mouse selections to reference surfaces |
| swMouse_SelectREVISIONCLOUDS | 0xf00000; filters mouse selections to revision clouds |
| swMouse_SelectREVISIONTABLE | 0x710000; filters mouse selections to revision tables |
| swMouse_SelectREVISIONTABLEFEAT | 0x770000; filters mouse selections to revision table features |
| swMouse_SelectROUTECURVES | 0x3f0000; filters mouse selections to route curves |
| swMouse_SelectROUTEPOINTS | 0x410000; filters mouse selections to route points |
| swMouse_SelectROUTESWEEPS | 0x430000; filters mouse selections to route sweeps |
| swMouse_SelectSECTIONLINES | 0x100000; filters mouse selections to section lines |
| swMouse_SelectSECTIONTEXT | 0x120000; filters mouse selections to section text |
| swMouse_SelectSELECTIONSETFOLDER | 0x1020000; filters mouse selections to selection set folders |
| swMouse_SelectSELECTIONSETNODE | 0x1030000; filters mouse selections to selection set nodes |
| swMouse_SelectSFSYMBOLS | 0x230000; filters mouse selections to SF symbols |
| swMouse_SelectSHEETS | 0x130000; filters mouse selections to sheets |
| swMouse_SelectSILHOUETTES | 0x2e0000; filters mouse selections to silhouettes |
| swMouse_SelectSIMELEMENT | 0x660000; filters mouse selections to simulation elements |
| swMouse_SelectSIMULATION | 0x650000; filters mouse selections to simulation studies |
| swMouse_SelectSKETCHBITMAP | 0x550000; filters mouse selections to sketch bitmaps |
| swMouse_SelectSKETCHCONTOUR | 0x600000; filters mouse selections to sketch contours |
| swMouse_SelectSKETCHES | 0x90000; filters mouse selections to sketches |
| swMouse_SelectSKETCHHATCH | 0x380000; filters mouse selections to sketch hatches |
| swMouse_SelectSKETCHPOINTFEAT | 0x470000; filters mouse selections to sketch point features |
| swMouse_SelectSKETCHPOINTS | 0xb0000; filters mouse selections to sketch points |
| swMouse_SelectSKETCHREGION | 0x5f0000; filters mouse selections to sketch regions |
| swMouse_SelectSKETCHSEGS | 0xa0000; filters mouse selections to sketch segments |
| swMouse_SelectSKETCHTEXT | 0x220000; filters mouse selections to sketch text |
| swMouse_SelectSOLIDBODIES | 0x4c0000; filters mouse selections to solid bodies |
| swMouse_SelectSOLIDBODIESFIRST | 0x510000; filters mouse selections to solid bodies over competing selection types (e.g., face, component) |
| swMouse_SelectSUBATOMFOLDER | 0x790000; filters mouse selections to body folders |
| swMouse_SelectSUBSKETCHDEF | 0x9a0000; filters mouse selections to sketch block definitions |
| swMouse_SelectSUBSKETCHINST | 0x720000; filters mouse selections to sketch block instances |
| swMouse_SelectSUBWELDFOLDER | 0x6b0000; filters mouse selections to sub-weldment folders |
| swMouse_SelectSURFACEBODIES | 0x4b0000; filters mouse selections to surface bodies |
| swMouse_SelectSURFBODIESFIRST | 0x4e0000; filters mouse selections to surface bodies over competing selection types (e.g., face, component) |
| swMouse_SelectSWIFTANNOTATIONS | 0x820000; filters mouse selections to Swift annotations |
| swMouse_SelectSWIFTFEATURES | 0x840000; filters mouse selections to Swift features |
| swMouse_SelectSWIFTSCHEMA | 0x9f0000; filters mouse selections to Swift schemas |
| swMouse_SelectTITLEBLOCK | 0xc00000; filters mouse selections to title blocks |
| swMouse_SelectTITLEBLOCKTABLEFEAT | 0xce0000; filters mouse selections to title block table features |
| swMouse_SelectVERTICES | 196608 or 0x30000; filters mouse selections to vertexes |
| swMouse_SelectVIEWERHYPERLINK | 0x3a0000; filters mouse selections to viewer hyperlinks |
| swMouse_SelectWELDBEADS | 0x7a0000; filters mouse selections to weld beads |
| swMouse_SelectWELDMENT | 0x6a0000; filters mouse selections to weldments |
| swMouse_SelectWELDMENTTABLEFEATS | 0x740000; filters mouse selections to weldment table features |
| swMouse_SelectWELDS | 0x260000; filters mouse selections to welds |
| swMouse_SelectWIREBODIES | 0x4a0000; filters mouse selections to wire bodies |
| swMouse_SelectZONES | 0x320000; filters mouse selections to zones |
| swMouse_Wheel | 128 or 0x80 |

## See Also

[SolidWorks.Interop.swcommands Namespace](SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands_namespace.html)
