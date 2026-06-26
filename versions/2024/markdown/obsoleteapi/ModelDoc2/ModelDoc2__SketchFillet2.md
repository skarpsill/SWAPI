---
title: "ModelDoc2::SketchFillet2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchFillet2.htm"
---

# ModelDoc2::SketchFillet2

This method is obsolete and has been superseded
by[SketchManager::CreateFillet](sldworksAPI.chm::/SketchManager/SketchManager__CreateFillet.htm).

Description

This method creates a sketch fillet between
the two sketch selected entities.

Syntax (OLE Automation)

retval = ModelDoc2.SketchFillet2 (radius, constrainedCorners)

(Table)=========================================================

| Input: | (double) radius | Radius of the fillet in meters |
| --- | --- | --- |
| Input: | (short) constrainedCorners | Action to take if the corner to be filleted is
constrained or has a dimension (see Remarks ) |
| Return: | (BOOL) retval | TRUE if the fillet is created, FALSE if not |

Syntax (COM)

status = ModelDoc2->SketchFillet2 (radius, constrainedCorners, &retval)

(Table)=========================================================

| Input: | (double) radius | Radius of the fillet in meters |
| --- | --- | --- |
| Input: | (short) constrainedCorners | Action to take if the corner to be filleted is
constrained or has a dimension (see Remarks ) |
| Output: | (VARIANT_BOOL) retval | TRUE if the fillet s created, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The constrainedCorners argument:

- Indicates
  what action to take if the corner to be filleted is constrained in some
  manner or has a dimension related to it. In this case, adding a fillet
  to the corner cannot be done without certain consequences. If the corner
  is not involved with any constraints, this argument is ignored.
- Can take
  one of the values found in swConstrainedCornerAction_e.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SketchFillet2.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SketchFillet2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
