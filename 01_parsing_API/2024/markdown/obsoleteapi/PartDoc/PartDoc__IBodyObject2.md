---
title: "PartDoc::IBodyObject2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__IBodyObject2.htm"
---

# PartDoc::IBodyObject2

This method is obsolete and has been superseded
by[PartDoc::GetBodies2](sldworksAPI.chm::/PartDoc/PartDoc__GetBodies2.htm)or[PartDoc::EnumBodies3](sldworksAPI.chm::/PartDoc/PartDoc__EnumBodies3.htm).

Description

This method returns a pointer to the Body2
object for this part. You can obtain surfaces and edges by referencing
this object.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = PartDoc->IBodyObject2 ( &retval )

Parameters Table Start

(Table)=========================================================

| Output: | (LPBODY2) retval | Pointer to the geometry of the part |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When working with assemblies,
you can obtain the Body2 object using Component2::IBody.

Obtaining the Body2 object
from the actual Component2 object recognizes any assembly-level changes
made to this body. For example, if an assembly-level hole was drilled
through an assembly component, then the Body2 object returned from Componen2t::IBody
contains that hole; whereas, the Body2 object returned from PartDoc::IBody
does not contain the hole. This is because this type of assembly-level
change is kept with the assembly component and is not propagated down
to the underlying part document.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\PartDoc\PartDoc__IBodyObject2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
