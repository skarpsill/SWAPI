---
title: "PartDoc::EnumBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__EnumBodies.htm"
---

# PartDoc::EnumBodies

This
method is obsolete and has been superseded by[PartDoc::IEnumBodies2](PartDoc__EnumBodies2.htm).

Description

This method enumerates the
bodies in a part

Syntax (OLE Automation)

Not Available.

Syntax (COM)

status = PartDoc->EnumBodies ( bodyType, &retval
)

(Table)=========================================================

| Input: | (long) bodyType | Type of body to obtain as defined in swBodyType_e |
| --- | --- | --- |
| Output: | (LPENUMBODIES) retval | Pointer to the EnumBodies object containing the
list of bodies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Only solid and sheet body types are supported.
If swSolidBody is used, only one solid is returned for this part; if swSheetBody
is used, all the sheet bodies for the part are returned.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="PartDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\PartDoc\PartDoc__EnumBodies.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
