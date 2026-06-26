---
title: "CustomSymbol::Angle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__Angle.htm"
---

# CustomSymbol::Angle

This
property is obsolete and has been superseded byBlockInstance::Angle.

Description

This property gets or sets the rotation angle
of this custom symbol.

Syntax (OLE Automation)

angleValue
= CustomSymbol.Angle (VB Get property)

CustomSymbol.Angle
= angleValue (VB Set property)

angleValue
= CustomSymbol.Angle ( ) (C++ Get property)

CustomSymbol.Angle
( angleValue ) (C++ Set property)

(Table)=========================================================

| Property: | (long) angle | Rotation angle in radians |
| --- | --- | --- |

Syntax (COM)

status
= CustomSymbol->get_Angle ( &angleValue)

status
= CustomSymbol->put_Angle ( angleValue )

(Table)=========================================================

| Property: | (long) angle | Rotation angle in radians |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The rotation angle of a CustomSymbol must be between
-360 to +360. If a value is specified that is outside of that range, the
angle wraps around in order to map back into range. For example, if you
set the Angle property to a value of 365 degrees, SolidWorks set the angle
to 5 degrees.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="CustomSymbol_Object$$**$$ZGetInfoCustomSymbol$$**$$ZModifyCustomSymbol$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CustomSymbol\CustomSymbol__Angle.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
