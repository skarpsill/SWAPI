---
title: "PartDoc::Body"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__Body.htm"
---

# PartDoc::Body

The
OLE version of this method is obsolete and has been superseded by[PartDoc::GetBodies2](sldworksAPI.chm::/PartDoc/PartDoc__GetBodies2.htm)and[PartDoc::EnumBodies 3](sldworksAPI.chm::/PartDoc/PartDoc__EnumBodies3.htm).

The COM version of this method is also obsolete
and has been superseded by[PartDoc::IBodyObject2](PartDoc__IBodyObject2.htm).

Description

This method returns a pointer or Dispatch pointer to the Body object
for this part. You can object surfaces and edges by referencing this object.

Syntax (OLE Automation)

retval = PartDoc.Body ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Dispatch pointer to Dispatch object, the geometry of the part |
| --- | --- | --- |

Syntax (COM)

status = PartDoc->IBodyObject (
&retval )

(Table)=========================================================

| Output: | (LPBODY) retval | Pointer to the geometry of the part |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

When working with assemblies, you may want to obtain the Body object
using Component::GetBody. Obtaining the Body object from the actual Component
object recognizes any assembly-level changes made to this body.

For example, if an assembly-level hole is drilled through an assembly
component, then the Body object returned from Component::GetBody contains
that hole; whereas, the Body object returned from PartDoc::Body does not
contain the hole. This is because this type of assembly-level change is
kept with the assembly component and is not propagated to the underlying
part document.

If the PartDoc contains more than one body, this method returns NULL
or Nothing in Visual Basic. See Partdoc::EnumBodies3 and PartDoc::GetBodies2.

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
<param name="Items" value="PartDoc_Object$$**$$Body$$**$$ZGetBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\PartDoc\PartDoc__Body.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="Get_All_Edges_and_Vertices_Example$$**$$Entity_Select_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\PartDoc\PartDoc__Body.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
