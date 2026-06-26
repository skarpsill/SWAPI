---
title: "CustomSymbol::Scale2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__Scale2.htm"
---

# CustomSymbol::Scale2

This property is obsolete and has been superseded
by[BlockInstance::Scale2](../BlockInstance/BlockInstance__Scale2.htm).

Description

This property gets or sets the scale of this
custom symbol.

Syntax (OLE Automation)

scaleValue
= CustomSymbol.Scale2 (VB Get property)

CustomSymbol.Scale2
= scaleValue (VB Set property)

scaleValue
= CustomSymbol.Scale2 ( ) (C++ Get property)

CustomSymbol.Scale2
( scaleValue ) (C++ Set property)

(Table)=========================================================

| Property: | (long) scaleValue | Scale of this custom symbol |
| --- | --- | --- |

Syntax (COM)

status
= CustomSymbol->get_Scale2 ( &scaleValue)

status
= CustomSymbol->put_Scale2 ( scaleValue )

(Table)=========================================================

| Property: | (long) scaleValue | Scale of this custom symbol |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The scale of a custom symbol must be between 0.1
to 10.0. If you specify a value outside of the range, SolidWorks sets
the scale so that it does not exceed the range minimum or maximum. For
example, if you set this property to 12.5, SolidWorks set the scale to
10.0.

To display changes to the custom symbol when you
change this property, you must use ModelDoc2::GraphicsRedraw2 or ModelDoc2::WindowRedraw
to redraw the window.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CustomSymbol\CustomSymbol__Scale2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
