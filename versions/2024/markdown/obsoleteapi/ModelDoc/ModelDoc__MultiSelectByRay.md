---
title: "ModelDoc::MultiSelectByRay"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__MultiSelectByRay.htm"
---

# ModelDoc::MultiSelectByRay

This
method is obsolete and has been superseded by[ModelDoc2::MultiSelectByRay](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IMultiSelectByRay.htm).

Description

This method selects multiple objects of the specified type that are
intersected by a ray from point (x,y,z in meters) in direction vector
(x,y,z) within a distance radius.

Syntax (OLE Automation)

retval = ModelDoc.MultiSelectByRay
( doubleInfoIn, typeWanted, append )

(Table)=========================================================

| Input: | (VARIANT) doubleInfoIn | VARIANT of type SafeArray of 7 doubles: 3 for the start point of the
ray, 3 for the direction of the ray, and 1 for the radius. |
| --- | --- | --- |
| Input: | (long) typeWanted | Type of objects to select as defined in swSelectType_e |
| Input: | (BOOL) append | TRUE if a you wish to append the selections to the current selection
list, FALSE otherwise |
| Return: | (BOOL) retval | TRUE if a selection was made |

Syntax (COM)

status = ModelDoc->IMultiSelectByRay
( pointIn, vectorIn, radiusIn, typeWanted, append, &retval )

(Table)=========================================================

| Input: | (double*) pointIn | Pointer to an array containing 3 doubles that define the start point
of the ray |
| --- | --- | --- |
| Input: | (double*) vectorIn | Pointer to an array containing 3 doubles that define the direction of
the ray |
| Input: | (double) radiusIn | Radius of the ray in meters |
| Input: | (long) typeWanted | Type of objects to select as defined in swSelectType_e |
| Input: | (VARIANT_BOOL) append | TRUE if a you wish to append the selections to the current selection
list, FALSE otherwise |
| Output: | (VARIANT_BOOL) retval | TRUE if an object was selected, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method defines a cylindrical region of infinite
length that begins at pointIn, runs parallel to vectorIn, and has a radius
of radiusIn. If edge or vertex entities have been specified, then any
edge or vertex found within the selection cylinder is selected.

This method selects only entity objects, which
include faces, edges, and vertices. You cannot use this method to select
Sketch objects.

For selecting face entities, the radiusIn value
is ignored and a cylinder of infinitely small radius is used.

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetSelection$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__MultiSelectByRay.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
