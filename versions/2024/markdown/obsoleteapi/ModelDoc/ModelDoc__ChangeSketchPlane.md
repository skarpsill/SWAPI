---
title: "ModelDoc::ChangeSketchPlane"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ChangeSketchPlane.htm"
---

# ModelDoc::ChangeSketchPlane

This method is obsolete and has been superseded by[ModelDoc2::ChangeSketchPlane](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ChangeSketchPlane.htm).

Description

Every sketch is associated with a plane (that is, a reference plane
or a planar face). This method changes the plane used by a sketch by moving
the selected sketch to a selected plane.

Syntax (OLE Automation)

retval = ModelDoc.ChangeSketchPlane
()

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if the change was successful, FALSE otherwise |
| --- | --- | --- |

Syntax
(COM)

status = ModelDoc->ChangeSketchPlane
( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if the change was successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires that the sketch and the new
plane or face are selected when it is called.

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifySketch$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__ChangeSketchPlane.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ChangeSketchPlane_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__ChangeSketchPlane.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
