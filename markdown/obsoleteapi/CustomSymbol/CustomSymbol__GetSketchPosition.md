---
title: "CustomSymbol::GetSketchPosition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetSketchPosition.htm"
---

# CustomSymbol::GetSketchPosition

This method is obsolete and was not superseded
.

Description

This
method gets the position of the custom symbol sketch.

Syntax (OLE Automation)

retval
= CustomSymbol.GetSketchPosition ()

(Table)=========================================================

| Return: | (VARIANT)
retval | VARIANT
of type SafeArray of doubles (see below) |
| --- | --- | --- |

Syntax (COM)

status
= CustomSymbol->IGetSketchPosition ( &retval )

(Table)=========================================================

| Output: | (double*)
retval | Pointer
to an array of doubles (see below) |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

The return value is the following array of doubles:

[textPtX,
textPtY, textPtZ]

where these sketch position values are actually
offset values from the origin of this custom symbol object.

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
<param name="Items" value="CustomSymbol_Object$$**$$ZGetInfoCustomSymbol$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CustomSymbol\CustomSymbol__GetSketchPosition.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
