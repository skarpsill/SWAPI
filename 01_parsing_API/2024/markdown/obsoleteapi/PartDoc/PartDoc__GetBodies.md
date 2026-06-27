---
title: "PartDoc::GetBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__GetBodies.htm"
---

# PartDoc::GetBodies

This method is obsolete and has been superseded
by[PartDoc::GetBodies2](sldworksAPI.chm::/PartDoc/PartDoc__GetBodies2.htm).

Description

This method gets all of the bodies in a part.

Syntax (OLE Automation)

bodies = PartDoc.GetBodies (bodyType)

(Table)=========================================================

| Input: | ( long ) bodyType | Type of bodies to obtain as defined in swBodyType_e |
| --- | --- | --- |
| Return: | (VARIANT) bodies | VARIANT of type SafeArray of Dispatch pointers
to the bodies |

Syntax (COM)

status = PartDoc->GetBodies (bodyType,
&bodies )

(Table)=========================================================

| Input: | ( long ) bodyType | Type of bodies to obtain as defined in swBodyType_e |
| --- | --- | --- |
| Output: | (VARIANT) bodies | VARIANT of type SafeArray of Dispatch pointers
to the bodies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Only solid and sheet body types are supported.
If swSolidBody is used, only one solid is returned for this part; if swSheetBody
is used, all the sheet bodies for the part are returned.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="PartDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PartDoc\PartDoc__GetBodies.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
