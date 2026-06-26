---
title: "ModelDocExtension::GetSectionProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__GetSectionProperties.htm"
---

# ModelDocExtension::GetSectionProperties

This method is obsolete and has been superseded
by[ModelDocExtension::GetSectionProperties2](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetSectionProperties2.htm).

Description

This method gets the section properties for
the following types of selected items:

- Planar
  model face in any document
- Face
  on a section plane
- Crosshatch
  section face in a section view in a drawing a sketch
- Sketch

Syntax (OLE Automation)

retval = ModelDocExtension.GetSectionProperties (
sections )

(Table)=========================================================

| Input: | (VARIANT) sections | Array of sections |
| --- | --- | --- |
| Output: | (VARIANT) * retval | SafeArray of section properties for the selected items |

Syntax (COM)

status = ModelDocExtension->IGetSectionProperties
( count, sections, retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) count | Number of sections |
| --- | --- | --- |
| Input: | (LPUNKNOWN) *sections | Array of sections of size count |
| Output: | (double) * retval | Array of size 15 of the section properties for
the selected items (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method clears the selection set.

(Table)=========================================================

| If... | Then... |
| --- | --- |
| The user selected a set of either parallel planes or parallel faces | You can pass an empty sections array |
| The user selected any items and you pass a sections array | The properties of the user-selected items and the sections array are
combined in retval |
| You pass a sections array and you do not want this array combined with
the properties of any user-selected items | Clear any user-selected items |

The objects in the sections parameter are added
to the current selection set. If the objects are already in the current
selection set, an error is generated; that is, status code will be equal
to 1, which means invalid input.

The format of retval is an
array of size 15:

(Table)=========================================================

| retval[0] | status of request: 0
= success 1
= invalid input 2
= selected faces are not in the same or parallel planes 3
= unable to compute section properties |
| --- | --- |
| retval[1] | area |
| retval[2] | centroid x |
| retval[3] | centroid y |
| retval[4] | centroid z |
| retval[5] | moment of inertia XX |
| reval[6] | moment of inertia YY |
| retval[7] | moment of inertia ZZ |
| retval[8] | moment of inertia -XY |
| retval[9] | moment of inertia -ZX |
| retval[10] | moment of inertia -YZ |
| retval[11] | polar moment of inertia of an area at the centroid |
| retval[12] | angle between principal axis and part axis |
| retval[13] | principal moment of inertia of an area at the centroid, 1x |
| retval[14] | principal moment of inertia of an area at the centroid, 1y |

This method returns metric
units unless explicitly specified otherwise.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDocExtension\ModelDocExtension__GetSectionProperties.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDocExtension_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDocExtension\ModelDocExtension__GetSectionProperties.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
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
<param name="Items" value="SectionProperties_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDocExtension\ModelDocExtension__GetSectionProperties.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
