---
title: "PartDoc::EnumRelatedBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__EnumRelatedBodies.htm"
---

# PartDoc::EnumRelatedBodies

This
method is obsolete and has been superseded by[PartDoc::EnumRelatedBodies2](sldworksAPI.chm::/PartDoc/PartDoc__EnumRelatedBodies2.htm).

Description

This method creates an enumerated list of bodies. The list contains
only those bodies associated with reference surfaces. What results is
a list of bodies that is related to the model, but it does not include
the part body itself.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = PartDoc->EnumRelatedBodies
( &retval )

(Table)=========================================================

| Output: | (LPENUMBODIES) retval | Pointer to the enumerated list of bodies |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A Reference surface feature can consist of one or more surfaces knitted
together.

Each reference surface feature has two Body objects:

- One to represent the front faces
- one to represent the back faces

Each Body object has one or more faces depending on whether the reference
surface feature is a set of knitted surfaces or a single underlying surface.
The corresponding faces for each body pair should have normal vectors
that are opposite.

To use the enumerated list, see the EnumBodies object.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\PartDoc\PartDoc__EnumRelatedBodies.htm" >
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
<param name="Items" value="Enumerate_Bodies_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\PartDoc\PartDoc__EnumRelatedBodies.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
