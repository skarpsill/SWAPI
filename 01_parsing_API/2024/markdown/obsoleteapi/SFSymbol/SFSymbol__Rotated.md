---
title: "SFSymbol::Rotated"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SFSymbol/SFSymbol__Rotated.htm"
---

# SFSymbol::Rotated

This property is obsolete and has been superseded
by[SFSymbol::Orientation](sldworksAPI.chm::/SFSymbol/SFSymbol__Orientation.htm).

Description

This property indicates whether this surface-finish symbol is horizontal
or vertical (rotated 90° ).

Syntax (OLE Automation)

rotated = SFSymbol::Rotated (VB Get property)

SFSymbol::Rotated = rotated (VB Set property)

rotated = SFSymbol::GetRotated ( ) (C++ Get
property)

SFSymbol::SetRotated ( rotated ) (C++ Set property)

(Table)=========================================================

| Property: | (BOOL) rotated | TRUE if symbol is rotated 90 ° (vertical), FALSE if symbol
is not rotated (horizontal) |
| --- | --- | --- |

Syntax (COM)

status = SFSymbol->Rotated ( VARIANT_BOOL rotated
)

(Table)=========================================================

| Property: | (VARIANT_BOOL)
rotated | TRUE if symbol is rotated 90 ° (vertical), FALSE if symbol
is not rotated (horizontal) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To see the model or drawing changes caused by setting this property,
you must redraw your window. See ModelDoc2::GraphicsRedraw2 for details.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SFSymbol_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SFSymbol\SFSymbol__Rotated.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
