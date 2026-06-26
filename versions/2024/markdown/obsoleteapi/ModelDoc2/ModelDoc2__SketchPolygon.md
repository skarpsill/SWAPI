---
title: "ModelDoc2::SketchPolygon"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchPolygon.htm"
---

# ModelDoc2::SketchPolygon

This method is obsolete and has been superseded
by[SketchManager::CreatePolygon](sldworksAPI.chm::/SketchManager/SketchManager__CreatePolygon.htm).

Description

This method creates a polygon in the active
sketch.

Syntax (OLE Automation)

retval = ModelDoc2.SketchPolygon (xCenter, yCenter, xEdge, yEdge, nSides, bInscribed)

(Table)=========================================================

| Input: | (double) xCenter | X component of the polygon's center |
| --- | --- | --- |
| Input: | (double) yCenter | Y component of the polygon's center |
| Input: | (double) xEdge | X component of the first vertex on the polygon |
| Input: | (double) yEdge | Y component of the first vertex on the polygon |
| Input: | (int) nSides | Number of sides for the polygon |
| Input: | (BOOL) bInscribed | TRUE to show an inscribed construction circle,
FALSE to show a circumscribed construction circle |
| Return: | (BOOL) retval | TRUE if polygon created, FALSE if not |

Syntax (COM)

status = ModelDoc2->SketchPolygon ( double xCenter,
double yCenter, double xEdge, double yEdge, int nSides, VARIANT_BOOL*
retval )

(Table)=========================================================

| Input: | (double) xCenter | X component of the polygon's center |
| --- | --- | --- |
| Input: | (double) yCenter | Y component of the polygon's center |
| Input: | (double) xEdge | X component of the first vertex on the polygon |
| Input: | (double) yEdge | Y component of the first vertex on the polygon |
| Input: | (int) nSides | Number of sides for the polygon |
| Input: | (BOOL) bInscribed | TRUE to show an inscribed construction circle,
FALSE to show a circumscribed construction circle. |
| Output: | (VARIANT_BOOL) retval | TRUE if polygon created, FALSE
if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

After using this method, the PropertyManager page
is in edit mode for the polygon. To exit this PropertyManager page and
complete the operation, use ModelDoc2::SetPickMode, ModelDoc2::ClearSelection2,
or exit the sketch.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SketchPolygon.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SketchPolygon.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
