---
title: "CustomSymbol::GetArrowHeadInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetArrowHeadInfo.htm"
---

# CustomSymbol::GetArrowHeadInfo

This method is obsolete and has been superseded
by[Note::GetArrowHeadInfo](sldworksAPI.chm::/Note/Note__GetArrowHeadInfo.htm).

Description

This
method gets the arrow head information for this symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetArrowHeadInfo ( )

(Table)=========================================================

| Return: | (VARIANT)
retval | VARIANT
of type SafeArray of doubles (see below) |
| --- | --- | --- |

Syntax (COM)

status
= CustomSymbol->IGetArrowHeadInfo ( &retval )

(Table)=========================================================

| Output: | (double*)retval | Pointer
to array of doubles (see below) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if Successful |

Remarks

This method returns an array of doubles that describe the geometry of
the arrowhead on the far end of the leader line. Note that this information
is independent of whether this SFSymbol has an arrowhead.

Format of return information is the following array of doubles:

retval[0]
= Arrow length (leader into arrowhead)

retval[1]
= Arrowhead length

retval[2]
= Arrowhead width

retval[3]
= Arrowhead style as defined in swArrowStyle_e

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
<param name="Items" value="CustomSymbol_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\CustomSymbol\CustomSymbol__GetArrowHeadInfo.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
